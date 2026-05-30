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

# Bare-mode invocations. Skills are injected via prompt prepend, never via
# the backend's own skill-loading machinery — so the only delta between
# `with_skill` and `baseline` is the prompt. Output-format flags emit usage
# stats (token counts + cache hit/miss) for per-pass instrumentation.


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


@dataclass(frozen=True)
class Eval:
    id: int
    name: str
    prompt: str
    register: str


def load_evals() -> list[Eval]:
    data = json.loads(EVALS_FILE.read_text(encoding="utf-8"))
    evals: list[Eval] = []
    for e in data["evals"]:
        if "register" not in e:
            raise ValueError(
                f"eval {e.get('name', e.get('id'))!r} missing required `register` field"
            )
        evals.append(Eval(**e))
    return evals


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
    n = (int(last.name.split("-")[1]) + 1) if last else 1
    d = WORKSPACE / f"iteration-{n}"
    d.mkdir(parents=True, exist_ok=True)
    return d


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


def wrap_markdown(text: str, width: int = 90) -> str:
    """Wrap markdown for terminal readability. Thai-aware via pythainlp.

    Preserves fenced code blocks. Wraps paragraphs, headers, list items, and
    blockquotes while keeping their leading markers and continuation indent.
    """
    out: list[str] = []
    in_fence = False
    fence_marker: str | None = None
    for line in text.split("\n"):
        m = _FENCE_RE.match(line)
        if m:
            if in_fence and m.group(2) == fence_marker:
                in_fence = False
                fence_marker = None
            elif not in_fence:
                in_fence = True
                fence_marker = m.group(2)
            out.append(line)
            continue
        if in_fence or not line.strip():
            out.append(line)
            continue
        if (h := _HEADER_RE.match(line)):
            p = h.group(1)
            out.extend(_wrap_paragraph(line[len(p):], width, prefix=p, cont=" " * len(p)))
        elif (li := _LIST_RE.match(line)):
            p = li.group(1)
            out.extend(_wrap_paragraph(line[len(p):], width, prefix=p, cont=" " * len(p)))
        elif (bq := _BLOCKQUOTE_RE.match(line)):
            p = bq.group(1)
            out.extend(_wrap_paragraph(line[len(p):], width, prefix=p, cont=p))
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


def _strip_frontmatter(text: str) -> str:
    return _FRONTMATTER_RE.sub("", text, count=1)


def _strip_default_meta(text: str) -> str:
    r"""Drop default meta from rule headings.

    Matches `### \`slug\` *(type · scope · severity)*`. When all fields are
    default, collapses to `### \`slug\``. Non-default fields are preserved.
    """
    def repl(m: re.Match[str]) -> str:
        heading = m.group(1)
        meta_inner = m.group(2)
        fields = [p.strip() for p in meta_inner.split("·") if p.strip()]
        defaults = {"mechanical", "all-registers", "hard", "craft", "style", "soft"}
        kept = [f for f in fields if f not in defaults]
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

    lines = text.splitlines(keepends=True)
    out: list[str] = []
    in_register_section = False
    keep_register_section = True
    in_marketing_subreg = False
    keep_marketing_subreg = True

    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith("## Register "):
            in_register_section = True
            in_marketing_subreg = False
            # Keep this section if its heading mentions one of our keys.
            keep_register_section = any(k in line for k in keys)
            if keep_register_section:
                out.append(line)
            continue
        if in_register_section and stripped.startswith("## "):
            in_register_section = False
            in_marketing_subreg = False
        if in_register_section and "Register 2" in keys[0] and stripped.startswith("### "):
            # Marketing sub-register subsection
            in_marketing_subreg = True
            # Keep if heading number matches our sub-key (e.g. "2.1")
            sub_key = keys[1] if len(keys) > 1 else None
            keep_marketing_subreg = bool(sub_key and sub_key in line)
            if keep_register_section and keep_marketing_subreg:
                out.append(line)
            continue
        if in_register_section:
            if "Register 2" in keys[0] and in_marketing_subreg:
                if keep_register_section and keep_marketing_subreg:
                    out.append(line)
            elif keep_register_section:
                out.append(line)
            continue
        out.append(line)
    return "".join(out)


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
    notes/framing-investigation-2026-05-21.md).
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
