"""Shared eval-harness helpers (paths, loaders, prompt building).

Lives outside conftest.py to avoid the name collision pytest creates when
multiple conftest files coexist along a directory path.
"""

from __future__ import annotations

import json
import os
import re
import shutil
from collections.abc import Callable
from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path

from pythainlp.tokenize import word_tokenize

ROOT = Path(__file__).parent.parent
KIEN_THAI_DIR = ROOT / "skills" / "kien-thai"
SKILL_PATH = KIEN_THAI_DIR / "SKILL.md"
EVALS_FILE = ROOT / "evals" / "evals.json"
WORKSPACE = ROOT / "workspace"


@dataclass(frozen=True)
class Output:
    text: str
    usage: dict


def _parse_claude(stdout: str) -> Output:
    """claude --output-format json: one JSON object with `result` + `usage`."""
    data = json.loads(stdout)
    return Output(data.get("result", ""), data.get("usage", {}))


def _parse_codex(stdout: str) -> Output:
    """codex --json: JSONL stream; agent_message carries text, turn.completed usage."""
    text = ""
    usage: dict = {}
    for line in stdout.splitlines():
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get("type") == "item.completed":
            item = event.get("item", {})
            if item.get("type") == "agent_message":
                text = item.get("text", text)
        elif event.get("type") == "turn.completed":
            usage = event.get("usage", {}) or usage
    return Output(text, usage)


@dataclass(frozen=True)
class Backend:
    name: str
    argv: tuple[str, ...]
    parse: Callable[[str], Output]

    @property
    def available(self) -> bool:
        return shutil.which(self.argv[0]) is not None


# Bare-mode invocations. Skills are injected via prompt prepend, never via
# the backend's own skill-loading machinery — so the only delta between
# `with_skill` and `baseline` is the prompt. Output-format flags emit usage
# stats (token counts + cache hit/miss) for per-pass instrumentation.
CLAUDE = Backend(
    "claude",
    ("claude", "--disable-slash-commands", "--output-format", "json", "-p"),
    _parse_claude,
)
CODEX = Backend("codex", ("codex", "exec", "--json"), _parse_codex)
BACKENDS: dict[str, Backend] = {b.name: b for b in (CLAUDE, CODEX)}


class Config(StrEnum):
    WITH_SKILL = "with_skill"
    BASELINE = "baseline"


class BundleMode(StrEnum):
    DRAFT = "draft"
    AUDIT = "audit"


class PassKind(StrEnum):
    INITIAL = "initial"
    AUDIT = "audit"
    FIX = "fix"


@dataclass(frozen=True)
class Eval:
    id: int
    name: str
    prompt: str
    register: str


def load_evals() -> list[Eval]:
    data = json.loads(EVALS_FILE.read_text(encoding="utf-8"))
    for raw in data["evals"]:
        if "register" not in raw:
            name = raw.get("name", raw.get("id"))
            raise ValueError(f"eval {name!r} missing required `register` field")
    return [Eval(**raw) for raw in data["evals"]]


def latest_iteration() -> Path | None:
    if not WORKSPACE.exists():
        return None
    iters = sorted(
        (p for p in WORKSPACE.iterdir() if p.is_dir() and p.name.startswith("iteration-")),
        key=lambda p: int(p.name.split("-")[1]),
    )
    return iters[-1] if iters else None


def next_iteration_dir() -> Path:
    last = latest_iteration()
    number = (int(last.name.split("-")[1]) + 1) if last else 1
    next_dir = WORKSPACE / f"iteration-{number}"
    next_dir.mkdir(parents=True, exist_ok=True)
    return next_dir


def enabled_backends() -> set[Backend]:
    """Backends opted in for this run. Default: claude only.

    Override via `EVAL_BACKENDS=claude,codex` (comma-separated). Empty/unset
    means claude only — codex is opt-in. Unknown names are rejected at this
    boundary rather than silently dropped.
    """
    raw = os.environ.get("EVAL_BACKENDS", "").strip()
    if not raw:
        return {CLAUDE}
    names = {n.strip() for n in raw.split(",") if n.strip()}
    unknown = names - BACKENDS.keys()
    if unknown:
        raise ValueError(f"unknown EVAL_BACKENDS: {sorted(unknown)}")
    return {BACKENDS[n] for n in names}


_FENCE_RE = re.compile(r"^(\s*)(```|~~~)")
_HEADER_RE = re.compile(r"^(#{1,6}\s+)")
_LIST_RE = re.compile(r"^(\s*(?:[-*+]|\d+\.)\s+)")
_BLOCKQUOTE_RE = re.compile(r"^(\s*>+\s*)")


def _wrap_paragraph(text: str, width: int, prefix: str = "", cont: str = "") -> list[str]:
    tokens = word_tokenize(text, keep_whitespace=True)
    if not tokens:
        return [prefix + text]
    lines: list[str] = []
    cur = prefix
    cur_prefix = prefix
    for tok in tokens:
        candidate = cur + tok
        if len(candidate.rstrip()) > width and cur.rstrip() != cur_prefix.rstrip():
            lines.append(cur.rstrip())
            cur = cont + tok.lstrip()
            cur_prefix = cont
        else:
            cur = candidate
    if cur.strip():
        lines.append(cur.rstrip())
    return lines


# (marker regex, continuation indent) per line type that wraps under a marker.
# Headers and lists indent the continuation to the marker width; blockquotes
# repeat the marker.
_WRAP_RULES: tuple[tuple[re.Pattern[str], Callable[[str], str]], ...] = (
    (_HEADER_RE, lambda marker: " " * len(marker)),
    (_LIST_RE, lambda marker: " " * len(marker)),
    (_BLOCKQUOTE_RE, lambda marker: marker),
)


def _block_prefix(line: str) -> tuple[str, str] | None:
    """Return (marker, continuation-indent) for a header/list/quote line, else None."""
    for regex, continuation in _WRAP_RULES:
        match = regex.match(line)
        if match:
            marker = match.group(1)
            return marker, continuation(marker)
    return None


def wrap_markdown(text: str, width: int = 90) -> str:
    """Wrap markdown for terminal readability. Thai-aware via pythainlp.

    Preserves fenced code blocks. Wraps paragraphs, headers, list items, and
    blockquotes while keeping their leading markers and continuation indent.
    """
    out: list[str] = []
    in_fence = False
    fence_marker: str | None = None
    for line in text.split("\n"):
        fence = _FENCE_RE.match(line)
        if fence:
            if in_fence and fence.group(2) == fence_marker:
                in_fence = False
                fence_marker = None
            elif not in_fence:
                in_fence = True
                fence_marker = fence.group(2)
            out.append(line)
            continue
        if in_fence or not line.strip():
            out.append(line)
            continue
        block = _block_prefix(line)
        if block:
            marker, cont = block
            out.extend(_wrap_paragraph(line[len(marker):], width, prefix=marker, cont=cont))
        else:
            out.extend(_wrap_paragraph(line, width))
    return "\n".join(out)


# --- Skill bundle preprocessor ----------------------------------------------
#
# kien_thai_bundle() builds the prompt-ready skill text. It does several
# runtime cuts so source files stay human-readable but the bundle stays lean:
#
# - drop YAML frontmatter (skill-discovery metadata, useless in prompt)
# - strip default meta `*(mechanical · all-registers · hard)*` etc. from rule headings
# - register-scope register.md, examples.md, exemplars.md when `register` is supplied
# - mode='audit' drops draft-time workflow sections from SKILL.md
# - pin exemplars.md last so native-Thai prose lands closest to the task prompt
#   (framing-investigation-2026-05-21.md, recommendations #1 and #2)
#
# Source files keep the verbose form (consistency test parses metadata).

REGISTER_HEADERS: dict[str, tuple[str, ...]] = {
    "explainer": ("Register 1",),
    "marketing-saas-sme": ("Register 2", "2.1"),
    "marketing-b2b-formal": ("Register 2", "2.2"),
    "marketing-fintech-warm": ("Register 2", "2.3"),
    "marketing-retail-tech": ("Register 2", "2.4"),
    "personal-blog": ("Register 3",),
    "news": ("Register 4",),
    "academic": ("Register 5",),
    "official": ("Register 6",),
}

_FRONTMATTER_RE = re.compile(r"\A---\n.*?\n---\n+", re.DOTALL)
_DEFAULT_META_RE = re.compile(
    r"^(### `[a-z0-9][a-z0-9/_-]*`)\s+\*\(([^)]+)\)\*\s*$",
    re.MULTILINE,
)
_WORKFLOW_HEADINGS = (
    "## Workflow when asked to write Thai prose",
    "## When asked to edit Thai prose",
    "## When asked to translate English to Thai",
)
_EXAMPLE_REGISTER_RE = re.compile(
    r"^<!--\s*register:\s*([a-z0-9-]+)\s*-->\s*$", re.MULTILINE
)
_DEFAULT_META_FIELDS = frozenset(
    {"mechanical", "all-registers", "hard", "craft", "style", "soft"}
)


def _strip_frontmatter(text: str) -> str:
    return _FRONTMATTER_RE.sub("", text, count=1)


def _strip_default_meta(text: str) -> str:
    r"""Drop default meta from rule headings.

    Matches `### \`slug\` *(type · scope · severity)*`. When all fields are
    default, collapses to `### \`slug\``. Non-default fields are preserved.
    """
    def repl(match: re.Match[str]) -> str:
        heading, meta_inner = match.group(1), match.group(2)
        fields = [f.strip() for f in meta_inner.split("·") if f.strip()]
        kept = [f for f in fields if f not in _DEFAULT_META_FIELDS]
        if not kept:
            return heading
        return f"{heading} *({' · '.join(kept)})*"
    return _DEFAULT_META_RE.sub(repl, text)


def _strip_workflow_sections(text: str) -> str:
    """Drop draft-time workflow sections (audit/fix passes don't need them)."""
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    skip = False
    for line in lines:
        stripped = line.rstrip("\n")
        if stripped in _WORKFLOW_HEADINGS:
            skip = True
            continue
        if skip and stripped.startswith("## ") and stripped not in _WORKFLOW_HEADINGS:
            skip = False
        if not skip:
            out.append(line)
    return "".join(out)


def _split_on_heading(text: str, prefix: str) -> list[str]:
    """Split into `[preamble, heading-led section, ...]` at lines starting with prefix."""
    sections = [""]
    for line in text.splitlines(keepends=True):
        if line.lstrip().startswith(prefix):
            sections.append(line)
        else:
            sections[-1] += line
    return sections


def _scope_register_md(text: str, register: str) -> str:
    """Keep only the active register's sections; drop the others.

    Always-keep `## ` sections: Quick register decision, Voice attributes,
    Person-arity, Cross-register: when to shift, Coherence, Default.
    Per-register `## Register N — ...` sections kept only if matching.
    Marketing sub-registers (`### 2.X`) under Marketing-family kept by match.
    """
    keys = REGISTER_HEADERS.get(register, ())
    if not keys:
        return text  # unknown register, ship full file

    preamble, *sections = _split_on_heading(text, "## ")
    kept = [preamble] + [_scope_register_section(s, keys) for s in sections]
    return "".join(kept)


def _scope_register_section(section: str, keys: tuple[str, ...]) -> str:
    """Keep a `## ` section; drop it only if it's a non-matching `## Register N`."""
    heading = section.splitlines()[0]
    if not heading.lstrip().startswith("## Register "):
        return section  # always-keep section (Voice, Coherence, ...)
    if not any(k in heading for k in keys):
        return ""  # a different register — drop it
    if keys[0] == "Register 2":
        return _filter_marketing_subregisters(section, keys)
    return section


def _filter_marketing_subregisters(section: str, keys: tuple[str, ...]) -> str:
    """Within the Marketing family, keep only the matching `### 2.X` sub-register."""
    sub_key = keys[1] if len(keys) > 1 else None
    preamble, *subsections = _split_on_heading(section, "### ")
    kept = [preamble]
    for sub in subsections:
        if sub_key and sub_key in sub.splitlines()[0]:
            kept.append(sub)
    return "".join(kept)


def _scope_examples_md(text: str, register: str) -> str:
    """Keep only the example tagged with the active register."""
    # Split on `<!-- register: xxx -->` markers. Header (text before first
    # marker) is always kept.
    chunks = _EXAMPLE_REGISTER_RE.split(text)
    # chunks: [header, reg1, body1, reg2, body2, ...]
    if len(chunks) < 3:
        return text
    out = [chunks[0]]
    for i in range(1, len(chunks), 2):
        if chunks[i] == register:
            out.append(f"<!-- register: {chunks[i]} -->\n")
            out.append(chunks[i + 1])
    return "".join(out)


def kien_thai_bundle(register: str | None = None, mode: BundleMode = BundleMode.DRAFT) -> str:
    """Build the prompt-ready skill bundle.

    register: optional register slug; when set, register.md, examples.md, and
        exemplars.md are scoped to the active register.
    mode: 'draft' (pass-0) keeps workflow sections; 'audit' drops them.

    exemplars.md is pinned last regardless of alphabetical order — proximity
    to the task prompt is the whole point of that file (see
    docs/notes/framing-investigation-2026-05-21.md).
    """
    skill = SKILL_PATH.read_text(encoding="utf-8")
    skill = _strip_frontmatter(skill)
    if mode == BundleMode.AUDIT:
        skill = _strip_workflow_sections(skill)
    skill = _strip_default_meta(skill)
    parts: list[str] = [skill]

    refs = sorted((KIEN_THAI_DIR / "references").glob("*.md"))
    refs = [r for r in refs if r.name != "exemplars.md"]
    exemplars = KIEN_THAI_DIR / "references" / "exemplars.md"
    if exemplars.exists():
        refs.append(exemplars)

    for ref in refs:
        body = ref.read_text(encoding="utf-8")
        body = _strip_default_meta(body)
        if register:
            if ref.name == "register.md":
                body = _scope_register_md(body, register)
            elif ref.name in ("examples.md", "exemplars.md"):
                body = _scope_examples_md(body, register)
        parts.append(f"\n\n## reference: {ref.name}\n\n{body}")
    return "".join(parts)


def wrap_skill(skill_text: str) -> str:
    """The `<skill>` envelope shared by every skill-injected prompt."""
    return f"ใช้แนวทางการเขียนต่อไปนี้:\n\n<skill>\n{skill_text}\n</skill>\n\n"


def skill_prompt(eval_case: Eval, bundle: str) -> str:
    return wrap_skill(bundle) + f"งานที่ต้องทำ:\n\n{eval_case.prompt}"


def audit_prompt(prose: str, bundle: str, register: str) -> str:
    """The audit-pass prompt. `bundle` must already be register-scoped."""
    return (
        wrap_skill(bundle)
        + f"prose นี้เป็น register `{register}`\n\n"
        "งาน: อ่าน prose ทั้งหมดให้จบก่อน แล้วค่อย flag issues — อย่าสแกนทีละบรรทัด. "
        "Pre-check: scan `forbidden-phrases.md` blocklist กับ prose "
        "(เฉพาะ occurrence ที่ไม่ได้อยู่ใน backtick — use/mention exemption). "
        "จากนั้น audit ตามกฎใน skill เต็มชุด. "
        "สำหรับทุก issue ให้ cite ด้วย slug ก่อน (เช่น `f4/targhak-closure`, "
        "`wrong-classifier`, `f6/ko-resumptive`); ยกข้อความที่ผิดมาประกอบทุกครั้ง. "
        "ถ้าผ่านทุกข้อ ให้ตอบบรรทัดเดียวว่า `CLEAN` ห้าม output prose\n\n"
        "<prose>\n" + prose + "\n</prose>"
    )


# --- Auditor-recall seed ----------------------------------------------------
#
# Each rule's own **Bad** example is a labeled known-bad item: fed to the audit
# pass, it should surface the rule's slug. This seeds the recall measure until
# the review loop's in-context misses expand it (see docs/spec/review-protocol.md and
# docs/decisions/2026-05-30-exemplar-first-pivot.md).

RULE_REF_FILES = ("ai-tells.md", "grammar.md", "register.md", "craft.md", "style-rules.md")

_RULE_HEADING_RE = re.compile(
    r"^###\s+`([a-z0-9][a-z0-9/_-]*)`\s+\*\(([^)]+)\)\*\s*$", re.MULTILINE
)
# Anchor on the colon so an inline-code token inside the **Bad (...)** descriptive
# label isn't mistaken for the example itself.
_BAD_EXAMPLE_RE = re.compile(r"\*\*Bad[^\n]*?:\s*`([^`]+)`")


@dataclass(frozen=True)
class KnownBad:
    slug: str
    bad: str
    register: str
    source: str


def _scope_to_register(scope: str) -> str:
    if scope in REGISTER_HEADERS:
        return scope
    if scope == "marketing":
        return "marketing-saas-sme"
    return "explainer"


# --- Model-route comparison (Typhoon vs Claude) -----------------------------
#
# Maps each eval's register slug to the corpus/curated/<path> used for few-shot
# conditioning of the Thai-native drafter (thai-native-draft.py -r). The drafter
# Path-joins the value under corpus/curated/, so a `family/sub` value resolves to
# the sub-register subdir. A register absent from this map has no corpus coverage —
# typhoon_pass skips it, since the drafter has no exemplars to condition on.

EVAL_REGISTER_TO_CORPUS: dict[str, str] = {
    "explainer": "tech-writing",
    "marketing-saas-sme": "marketing/saas-sme",
    "marketing-b2b-formal": "marketing/b2b-formal",
    "marketing-fintech-warm": "marketing/fintech-warm",
    "marketing-retail-tech": "marketing/retail-tech",
    "news": "newspaper-feature",
    "personal-blog": "personal-blog",  # 2 Vicharn Panich diary entries (2026-06-16 sweep)
    "academic": "scholarly",
}

_FORBIDDEN_BLOCKLIST = KIEN_THAI_DIR / "references" / "forbidden-phrases.md"
_FORBIDDEN_BULLET_RE = re.compile(r"^- (.+)$", re.MULTILINE)
_BACKTICK_TOKEN_RE = re.compile(r"`([^`]+)`")
# Parentheticals hold "use this instead" suggestions and rule-slug refs
# (`สำคัญ`, `cta-bang`), not forbidden phrases — drop them before extraction.
_PARENTHETICAL_RE = re.compile(r"\([^)]*\)")

# Formal connectives AI overuses; density per 1k chars (mirrors test_quant).
CONNECTIVES = ("ซึ่ง", "โดย", "ทั้งนี้", "อีกทั้ง", "นอกจากนี้", "อย่างไรก็ตาม")


def load_forbidden_phrases() -> list[str]:
    """Literal forbidden phrases from forbidden-phrases.md (Blocklist section).

    Pulls every backticked token on a `- ` bullet line; drops pattern entries
    (those with `...`/`…` ellipsis), which aren't plain substrings.
    """
    if not _FORBIDDEN_BLOCKLIST.exists():
        return []
    text = _FORBIDDEN_BLOCKLIST.read_text(encoding="utf-8")
    after = text.split("## Blocklist", 1)
    body = after[1] if len(after) == 2 else text
    phrases: list[str] = []
    for bullet in _FORBIDDEN_BULLET_RE.findall(body):
        bullet = _PARENTHETICAL_RE.sub("", bullet)
        for tok in _BACKTICK_TOKEN_RE.findall(bullet):
            tok = tok.strip()
            if tok and "..." not in tok and "…" not in tok:
                phrases.append(tok)
    return phrases


@dataclass(frozen=True)
class Signals:
    """Length-agnostic AI-tell heuristics for arm-vs-arm comparison.

    Advisory only (same status as test_quant) — routes a human's attention,
    never a quality verdict.
    """

    chars: int
    paragraphs: int
    forbidden_hits: tuple[str, ...]
    connective_density: float
    exclamations: int


def mechanical_signals(text: str) -> Signals:
    chars = len(text)
    connectives = sum(len(re.findall(c, text)) for c in CONNECTIVES)
    blocks = [b for b in re.split(r"\n\s*\n", text.strip()) if b.strip()]
    return Signals(
        chars=chars,
        paragraphs=len(blocks),
        forbidden_hits=tuple(p for p in load_forbidden_phrases() if p in text),
        connective_density=round(connectives / max(chars, 1) * 1000, 1),
        exclamations=text.count("!") + text.count("！"),
    )


def extract_known_bad() -> list[KnownBad]:
    """Labeled known-bad seed: (slug, the rule's own Bad example, register)."""
    items: list[KnownBad] = []
    refs = KIEN_THAI_DIR / "references"
    for name in RULE_REF_FILES:
        path = refs / name
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        headings = list(_RULE_HEADING_RE.finditer(text))
        for i, m in enumerate(headings):
            meta = [p.strip() for p in m.group(2).split("·")]
            scope = meta[1] if len(meta) > 1 else "all-registers"
            end = headings[i + 1].start() if i + 1 < len(headings) else len(text)
            for bad in _BAD_EXAMPLE_RE.findall(text[m.end():end]):
                items.append(
                    KnownBad(m.group(1), bad.strip(), _scope_to_register(scope), name)
                )
    return items
