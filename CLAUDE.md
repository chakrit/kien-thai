# PRODIGY9 Coding School

This project's AI coding environment is managed by [ACE](https://github.com/ace-rs/ace).
Run `ace` to start a coding session. Run `ace setup` if not yet configured.

## Two skill sources — keep them straight

This repo sits at the intersection of **two** skill bodies. They serve opposite
roles and must not be confused.

**1. School skills — authoritative; apply them.** General coding/workflow skills
from the **PRODIGY9 Coding School**, symlinked into `.claude/skills/` from
`~/.local/share/ace/prod9/school/skills/`. These govern *how Claude edits this
repo*: file editing, shell discipline, markdown style, eval harness work, ACE
workflow, school-PR flow. Edits flow back to the school clone through the
symlinks — propose changes back when ready. Run `ace config` / `ace paths` to
debug configuration. See "Load these skills" below for the active set.

**2. `skills/kien-thai/` + `skills/kode-thai/` — artifact under development;
NOT authority.** These two skills live in this repo and **this repo is their
source-of-truth** (the school re-imports from here, not the other way around).
Their target is Thai prose that (1) reads as little like generic AI output as
possible, (2) has a distinct, believably human voice, (3) is easy to read for
native Thai readers, (4) counters training-data skew toward over-formal /
over-polite Thai. Composition: `kien-thai` = content rules (7 frames + ai-tells
+ grammar + craft + style-rules + register + examples + exemplars +
forbidden-phrases);
`kode-thai` = audit-loop trigger that invokes kien-thai to convergence. They
are the **work-in-progress being tested** — do **not** self-apply them to
Claude's own Thai output. Their correctness is what evals measure; freelance
application contaminates the signal. The harness injects them under controlled
conditions; outside the harness they are content under review, edited through
the iteration discipline below.

### Locked decisions — skill content

- No celebrity-columnist source material. Tech writing, bank long-form
  (non-sensational), younger newspaper voices, internationally-minded
  translators.
- No LLM-judge until human review proves insufficient.

---

## 🚨 Iteration discipline — READ FIRST 🚨

> **Rules don't get added on vibes. Trace before you write.**
>
> Every rule in `skills/kien-thai/` was synthesized from research into specific Thai
> writing sources (real tech blogs, bank long-form, young-newspaper features, skilled
> non-fiction translation). Each rule has a *why* — a failure mode it counters or a
> human-writing pattern it captures.
>
> **Rules without provenance rot. Don't grow the skill faster than the evidence does.**

> **Direction (2026-05-30): exemplar-first, auditor-recall-measured.** The default
> durable artifact is now a native before/after *pair*, not a rule — pairs are lossless
> native signal, rules a lossy compression a non-native generalizer (Claude) performs,
> earned only when the pair alone doesn't transfer. The binding constraint is *auditor
> recall*, not drafter quality: the kode-thai loop converges to *skill-clean* (the
> ruleset finds nothing), never to *chakrit-clean* (the native ear finds nothing). Full
> rationale + the eight decisions:
> [`docs/decisions/2026-05-30-exemplar-first-pivot.md`](docs/decisions/2026-05-30-exemplar-first-pivot.md).

When an eval output looks bad, the temptation is to immediately add a new rule or
tighten an existing one. **Resist this.** Trace first:

1. **Find the offending pattern** in the output.
2. **Map it to existing rules** — which rule was supposed to prevent this? Is it in
   `ai-tells.md` (mechanical), `craft.md` (soft), `grammar.md` (surface),
   `style-rules.md`, `register.md`, or `examples.md`? If it's in none, that's a real
   gap.
3. **If a rule exists but didn't fire** (a recall-miss): ask why. Buried? Phrased
   weakly? Conflicting with another rule? Wrong register? Strengthen the existing rule's
   wording, prominence, or anchoring example — or add a native pair to the audit bundle
   so the auditor has a concrete anchor — but don't pile on a new rule that says the
   same thing differently.
4. **If no rule covers it** (a coverage-gap): land it as a register-tagged before/after
   *pair* in `references/examples.md` / `exemplars.md` first — that is the default.
   Promote to a rule only when the pair alone doesn't transfer across outputs, and then
   only with corpus evidence; a rule without a source is speculative — flag it
   `provisional`.
5. **Document the trace** in `iteration-N/feedback.md` so the rule's origin survives.

External contributors follow the same logic via [`CONTRIBUTING.md`](CONTRIBUTING.md)
— that's the public-facing version of this section.

> **Workspace outputs are evidence, not artifacts.** Eval outputs under
> `workspace/iteration-N/<eval>/<backend>/<config>/` (`output.md`, `pass-N.md`,
> prompts, meta) are gitignored generation evidence — what the model produced under
> the current skill bundle. Read them to derive rules, register-tagged exemplars,
> and judgements. **Do not edit them.** The "find a bug, fix the file" reflex from
> normal coding work does not apply here: the bug is in the model's behavior, the
> fix is in the skill content. Edits to gitignored outputs vanish on the next
> regeneration and produce nothing durable.
>
> The tracked, durable artifacts are: `skills/kien-thai/references/*.md` (rules),
> `references/examples.md` (before/after exemplars), `docs/decisions/`
> (rulings + judgements), and `workspace/iteration-N/feedback.md` (per-iteration
> trace — note: feedback files at the iteration root are tracked; only the eval
> subdirectories are ignored). When a corrected version of an output line teaches a
> generalizable pattern, lift it into `references/examples.md` with the trace — that
> is where "before → after" content lives durably.
>
> **The iteration ledger.** [`workspace/INDEX.md`](workspace/INDEX.md) is the tracked
> table of every iteration — date, mode/scope, review status, feedback link. It is
> the entry point for "what iterations exist and where do they stand". Update it at
> two moments: **when you create an iteration** (add a row with date + mode/scope,
> Review `pending`), and **when you finish reviewing one** (flip its Review cell to
> `reviewed` and link the feedback file). A row without these updates means the ledger
> lies about the repo's state.

> **1-by-1 review protocol.** When chakrit invokes "1-by-1" on a stretch of review
> work, discuss each item to resolution one at a time and **log agreed edits to a
> task batch** as decisions are reached. Do not apply edits mid-discussion. Actual
> work — file edits, skill additions, commits — starts only after all items in the
> queue have been discussed. The point is to keep the discussion thread coherent
> without context-switching into file edits between items. Confusing 1-by-1 with
> propose-then-wait (which permits per-item apply on approval) is a recurring
> failure mode; under 1-by-1, even approved items get queued, not applied.

---

## Authoring the skill

Everything below is about *how we build and iterate the skill*, not about Thai prose
itself.

### Repo map — everything, linked

Every top-level entry. A fresh session should need nothing beyond this table to find
its way; if something is not reachable from here, that is a bug in this file.

| Path | What it is |
| ------------------------------------------------ | --------------------------------------------- |
| [`skills/kien-thai/`](skills/kien-thai/) | The artifact under test — content rules. Tree below. |
| [`skills/kode-thai/`](skills/kode-thai/SKILL.md) | Audit-loop trigger over kien-thai. |
| [`evals/evals.json`](evals/evals.json) | The 5 eval prompts — the real test set. |
| [`tests/`](tests/) | Eval harness + sanity suite. Tree below. |
| [`workspace/`](workspace/) | Generation runs + `probes/`. Eval subdirs gitignored; `feedback.md` tracked. |
| [`workspace/INDEX.md`](workspace/INDEX.md) | **The iteration ledger** — what exists, what's reviewed. |
| [`corpus/`](corpus/README.md) | Vetted native-Thai source material. Prose gitignored; see below. |
| [`docs/`](docs/README.md) | Durable artifacts, single routing gate. Index below. |
| [`README.md`](README.md) | Public front door (Thai). |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Public-facing iteration discipline for outside contributors. |
| `.ace/` | Session trail (`save.md`, `save.ledger.md`) + agent logs. Gitignored; read it when resuming. |
| `ace.toml` | ACE config — school + the skill set auto-loaded here. |

### Durable docs — the full index

| Doc | Answers |
| --------------------------------------------------------------------- | ------------------------------ |
| [`docs/README.md`](docs/README.md) | **The routing gate.** Where does this go? |
| [`docs/spec/review-protocol.md`](docs/spec/review-protocol.md) | The outer loop: skill-clean → chakrit-clean, and what the numbers mean. |
| [`docs/spec/inline-iteration.md`](docs/spec/inline-iteration.md) | Session-driven generation without the subprocess CLIs. |
| [`docs/guides/running-evals.md`](docs/guides/running-evals.md) | How to produce an iteration and what to update after. |
| [`docs/vendor/model-backends.md`](docs/vendor/model-backends.md) | claude / codex / ollama surface + the Thai-corrupting `ollama run` trap. |
| [`docs/vendor/thai-orthography-standards.md`](docs/vendor/thai-orthography-standards.md) | Royal Society standards — spacing, ทับศัพท์, spelling. Mechanics only, never voice. |
| [`docs/vendor/thai-reference-grammars.md`](docs/vendor/thai-reference-grammars.md) | Descriptive grammars — what a structural claim in `grammar.md` should cite. |
| [`docs/decisions/`](docs/decisions/README.md) | Dated rulings. Frozen; supersede, never edit. |
| [`docs/decisions/2026-05-30-exemplar-first-pivot.md`](docs/decisions/2026-05-30-exemplar-first-pivot.md) | **Current direction.** Read this before proposing rule work. |
| [`docs/scratch/`](docs/scratch/README.md) | Research dumps + investigations. Residual; disposable. |
| [`docs/scratch/prior-art.md`](docs/scratch/prior-art.md) | Digest of absorbed session notes — what each session did, where it landed. |
| [`docs/work-queue.md`](docs/work-queue.md) | Agent-doable committed work. |
| [`docs/research-queue.md`](docs/research-queue.md) | Speculative, awaiting evidence. |
| [`docs/human-tasks-queue.md`](docs/human-tasks-queue.md) | Needs chakrit — ear, Thai authoring, rulings, token spend. |

**Task discovery reads all three queues** — `/ace`, or any "what's next" — not just
`work-queue.md`. Agent threads routinely gate on a `human-tasks-queue.md` decision, so
one queue is never enough.

### Layout

```
skills/kien-thai/
├── SKILL.md                 # frames + person deixis + workflow + model route
├── scripts/                 # Thai-native model route: thai-route.sh,
│                            #   thai-native-draft.py (Typhoon via ollama)
└── references/
    ├── ai-tells.md          # mechanical Thai-correctness violations (hard)
    ├── grammar.md           # surface grammar (classifiers, modals, calques)
    ├── craft.md             # voice/taste preferences (soft)
    ├── style-rules.md       # positive style rules + ทับศัพท์ guide
    ├── register.md          # 6 register families + person deixis
    ├── examples.md          # before/after, register-tagged
    ├── exemplars.md         # native corpus excerpts, pinned last in bundle
    └── forbidden-phrases.md # blocklist for audit pre-check
skills/kode-thai/
└── SKILL.md                 # audit-loop trigger over kien-thai
evals/evals.json             # 5 eval prompts across 4 registers
tests/
├── lib.py                   # bundle preprocessor, BACKENDS, parsers,
│                            #   iteration pinning + arm pairing
├── conftest.py              # skill_text fixture (unscoped, default)
├── test_sanity.py           # plumbing + bundle preprocessor coverage
├── test_iteration.py        # EVAL_ITERATION pinning + co-generated pairing
├── test_docs_index.py       # every doc reachable from an index
├── test_skill_consistency.py # cross-ref + slug uniqueness checks
├── test_skill_frontmatter.py # strict-YAML frontmatter guard
├── test_quant.py            # advisory heuristics, -m evaluate
├── test_recall.py           # auditor recall on rule Bad-examples, -m recall
├── probe_runon_recall.py    # one-off probes (not pytest modules); evidence
├── probe_thai_authorities.py #   lands in workspace/probes/
└── generate/
    ├── conftest.py          # run_eval fixture, register-scoped two-tier
    ├── test_claude.py       # -m generate
    ├── test_codex.py        # -m generate
    ├── typhoon_pass.py      # Typhoon draft arm (not a pytest module)
    └── compare_arms.py      # per-eval comparison.md, Typhoon vs Claude
workspace/                   # gitignored: iteration-N/<eval>/<backend>/<config>/
└── probes/                  # gitignored one-off probe evidence, cited from
                             #   docs/scratch/ notes
```

**Durable artifacts** live in [`docs/`](docs/README.md), filed by the single routing gate
in [`docs/README.md`](docs/README.md): a ruling → `decisions/` (dated, frozen);
third-party lookup → `vendor/`; a how-to → `guides/`; our own design/surface → `spec/`;
unsettled exploration → `scratch/` (residual — opened with a "not spec/decision
because ___" line, never a default). Nothing defaults to `scratch/`. Every file is
linked from the index above; **decide a doc's target folder at plan time, not when
filing it.**

### Eval strategy

Two-stage, per skill-creator doctrine — subjective prose is judged by humans, not
assertions.

- **Stage 1 (generate)**: `pytest -m generate` invokes
  `claude --disable-slash-commands --output-format json -p` and `codex exec --json`.
  Skill is injected via prompt prepend (only diff between with_skill and baseline).
  Bundle is register-scoped via `kien_thai_bundle(register, mode)` and uses
  two-tier injection — pass-0 ('draft' mode) keeps workflow sections; audit
  and fix passes share the same 'audit' bundle with workflow sections dropped.
  Outputs land in
  `iteration-N/<eval>/<backend>/<config>/{output.md,prompt.txt,meta.json}`.
  meta.json tracks per-pass usage (cache hits, input/output tokens).
- **Stage 2 (review)**: the outer loop — see
  [`docs/spec/review-protocol.md`](docs/spec/review-protocol.md). A skill-clean output
  goes to chakrit's ear for the *chakrit-clean* verdict; the gap between the two is the
  measurement. **Never read loop-to-CLEAN as a quality result — it is ruleset-coverage,
  not naturalness.** Primary signals: the *CLEAN-but-flawed rate* and *auditor recall*
  (recall-miss vs coverage-gap). Consolidated notes + the aggregate go to
  `iteration-N/feedback.md` and graduate into pairs (`references/examples.md` /
  `exemplars.md`) first, rules only when the pair doesn't transfer. Flip the iteration's
  Review cell to `reviewed` in [`workspace/INDEX.md`](workspace/INDEX.md) and link the
  feedback file.
- **`test_quant.py`** is advisory only — flags forbidden phrases and connective
  density. Not a quality gate.
- **`test_recall.py`** measures auditor recall: each rule's own Bad example is a
  labeled known-bad item that should make the audit pass cite that rule's slug.
  Seed extraction runs free in the default suite; the LLM runner is opt-in via
  `-m recall`.

### Commands

```
uv sync                                  # one-time deps
uv run pytest                            # sanity (fast, default)
uv run pytest -m generate                # produce artifacts (slow, $$$)
uv run pytest -m generate -k claude      # one backend
uv run pytest -m evaluate                # advisory heuristics on latest iteration
uv run pytest -m recall                  # auditor-recall runner (slow, $$$)
```

Requires `ANTHROPIC_API_KEY` and `codex` logged in. Tests skip gracefully if a backend
is missing. **Never `-m generate -n >1`** — xdist gives each worker its own session, so
the matrix lands split across separate iteration directories (bit us on iteration-7).
Full procedure, traps, and what to update after a run:
[`docs/guides/running-evals.md`](docs/guides/running-evals.md). Backend flags and the
`ollama run` Thai-corruption trap:
[`docs/vendor/model-backends.md`](docs/vendor/model-backends.md).

**Inline alternative**: [`docs/spec/inline-iteration.md`](docs/spec/inline-iteration.md)
documents a session-driven
iteration mode that reuses the bundle preprocessor and prompt templates but
generates via subagent (or codex driven manually) instead of subprocess CLIs.
Saves API tokens; outputs marked `mode: "inline"` in meta.json. Use for
audits/probes; use the pytest harness for publishable cross-iteration measurement.

### Locked decisions — tooling

- Backends: claude + codex, both in bare modes (no skill auto-loading), JSON
  output for usage telemetry.
- Skill injection: register-scoped bundle prepended under `<skill>...</skill>`.
  Source files keep verbose form (consistency test parses them); preprocessor
  in `tests/lib.py:kien_thai_bundle` strips frontmatter, dead refs, default
  metadata, and filters by register at bundle time.
- Two-tier injection: pass-0 (draft) → full register-scoped bundle. Audit
  and fix passes → drop draft-time workflow sections (audit-mode bundle).
  **Fix passes always run with the full register-scoped audit bundle —
  never a slimmed cited-rules-only variant.** Tried in iter-6 and rejected:
  per-pass slimming strips sibling-rule context and the fixer thrashes,
  introducing new violations as fast as it patches cited ones. Iteration
  is tested with the full ruleset applied; do not re-attempt slimming.
- Python: 3.13+ via `uv`. pytest 9 + pytest-xdist.

---

## Cached native-Thai corpus

`corpus/` holds vetted native-Thai source material — **this is the canonical
source for every rule and every exemplar in `skills/kien-thai/`.** Do not
fabricate Thai prose, do not lift Claude-authored output from
`workspace/iteration-N/...` or from the After-blocks in `references/examples.md`
when you need a native-voice anchor. Pull from here instead.

```
corpus/
├── README.md                # category map (tech-writing, bank-longform,
│                            #   marketing/<sub-register>, newspaper-feature,
│                            #   personal-blog, scholarly, translation, etc.)
├── RESUME.md                # resume protocol for the corpus research agent
├── curated/<category>/*.md  # 1–4 paragraph hand-picked snippets, with
│                            #   frontmatter (source_url, retrieved, voice notes)
└── raw/<category>/*.md      # full article body retained for deeper analysis
```

When pulling excerpts for `references/exemplars.md` or rule provenance, keep
them **short** (fair-use sized) and cite the corpus file path in an HTML
comment above the block.

Gaps (registers with no curated entry yet) are tracked in
`docs/scratch/source-vetting-2026-05-13.md` and the work-queue. If a register has no
corpus file, surface that — don't paper over it with synthesized prose.

## Markdown style for this repo

All Markdown files in this repo follow these rules. Durable here so open-source
contributors follow them without needing the school skill.

**Hard-wrap at column 90.** Wrap every line at 90 columns. Break before the limit,
never after. Apply to prose, bullet items, and blockquotes. Do not wrap inside fenced
code blocks, tables, or URLs.

Indent bullet continuations under the first character after the marker:

```markdown
- A long bullet item that exceeds ninety characters must wrap cleanly at the limit,
  with the second line aligned under the first letter of the bullet text.
```

Practical exemptions — treat as atomic, like URLs:

- YAML frontmatter (`description:` fields stay single-line).
- Long Thai sentences inside inline backticks or blockquotes — splitting mid-string
  breaks rendering.
- Verbatim source quotes (English originals for translation examples, etc.).

**Align table columns.** Pad cells with spaces so pipes line up vertically. Size the
separator dashes to the widest cell in each column. Match padding direction to
alignment: left-aligned and default columns pad right; right-aligned columns pad left;
centered columns pad both sides. Apply to header cells too — a right-aligned column
gets a right-aligned header.

```markdown
| Name  | Role                  |  Yrs |
| ----- | --------------------- | ---: |
| Alice | Engineer              |    4 |
| Bob   | Senior Staff Engineer | 1024 |
```

Repad the whole column whenever any cell in it changes width.

**`mdfmt` caveats.** The `markdown-writing` skill bundles `mdfmt.py`, but: this repo's
`.md` files are hand-wrapped conservatively (≤90, not `mdfmt`'s greedy fill), so
`mdfmt --check` flags them wholesale — it is **not** the enforced standard; the ≤90 rule
above is. And `mdfmt` mangles `<...>` inline-code in prose (splits the span, overruns 90).
Hand-wrap to ≤90 and **do not run `mdfmt --write` on existing files** — it reformats them
entirely and can mangle inline-code such as `<skill>`.

## Load these skills

School skills only (per "Two skill sources" above) — narrows ACE auto-load. The active
set resolved by `ace skills`:

- `general-coding` — Python edits in `tests/`, eval harness work (project-declared).
- `copywriting` — marketing-register eval prose (project-declared).
- `ace-*` family — `ace`, `ace-afk`, `ace-audit`, `ace-connect`, `ace-docs`, `ace-init`,
  `ace-realign`, `ace-save`, `ace-school`: ACE workflow + school-PR flow.
- User-global includes also active here: `fact-check`, `find-skills`, `lowfat-pantry`,
  `visualise`.

`markdown-writing`, `skill-creator`, and `shell` are no longer shipped by the school —
their doctrines survive inline: the markdown hard-wrap-90 + table-align rules under
"Markdown style for this repo" below, and skill-creator's two-stage-eval doctrine under
"Eval strategy". Run `ace skills` for the live resolved set.

## Opening files for review or markdown editing

Terminal pagers (`less`, `bat`, `cat`) mangle Thai rendering — combining marks
misalign, line-breaks split syllables. When chakrit says "open X for review",
"open X in a markdown editor", or anything similar that calls for human-readable
display or hand-editing of a markdown file, hand it off to **iA Writer**:

```
open -a 'iA Writer' <filename>
```

Default to this for any Thai-prose target — eval outputs under
`workspace/iteration-N/...`, `references/*.md`, `docs/decisions/*`,
`skills/kien-thai/**/*.md`, etc. — and for any "open in markdown editor" /
"open the markdown" request regardless of Thai content.

Check availability with `ls /Applications/'iA Writer.app'` if uncertain;
fallback to terminal display only when iA Writer is missing.
