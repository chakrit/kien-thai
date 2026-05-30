# Session checkpoint — 2026-05-30 (exemplar-first pivot + recall instrument)

Distinct from the other two 2026-05-30 checkpoints (INDEX-wiring/issue-1, and the
iter-8/9 review-pending note). This session reframed the project's approach and built the
Phase-2 auditor-recall instrument.

## What was decided

Pivot to **exemplar-first, auditor-recall-measured**, with **inline as the default
mode**. Full rationale + eight decisions:
[`decisions/2026-05-30-exemplar-first-pivot.md`](decisions/2026-05-30-exemplar-first-pivot.md).
Core: the kode-thai loop converges to *skill-clean* (ruleset finds nothing), never
*chakrit-clean* (native ear finds nothing); the binding constraint is **auditor recall**,
not drafter quality; native before/after **pairs** are the default artifact, a rule a last
resort.

## What was done

**Phase 0 — doc reframe (English surfaces done):**

- New: `notes/decisions/2026-05-30-exemplar-first-pivot.md`; `tests/REVIEW-PROTOCOL.md`
  (the outer review loop — skill-clean vs chakrit-clean, CLEAN-but-flawed rate,
  recall-miss/coverage-gap, agent does everything except the verdict).
- Edited: `CLAUDE.md` (iteration discipline → pairs-first; Stage 2 → recall + the
  CLEAN-≠-quality caveat), `notes/work-queue.md` (framing work committed; new
  harness-efficiency workstream — SDK caching, code-side mechanical audit),
  `notes/research-queue.md`, `notes/judgements/README.md`, `corpus/README.md` (pointers +
  provenance-safety axis).
- Rewrote `tests/INLINE-ITERATION.md` → inline-as-default + three drivers (Workflow
  recommended, manual subagent, manual Codex); fixed stale register slugs (`tech-writing`,
  `newspaper-feature` → `explainer`, `news`).

**Phase 2 — auditor-recall instrument (built, proven, green):**

- `tests/lib.py`: `audit_prompt`, `extract_known_bad` (74-item labeled seed from each
  rule's own Bad example), `KnownBad`. `tests/generate/conftest.py` delegates to
  `audit_prompt`. `pyproject.toml`: `recall` marker (opt-in). `tests/test_recall.py`: free
  extractor test + `-m recall` runner → writes `workspace/recall-report.md`.
- Smoke test (6 claude calls): recall 5/6 on mechanical/local tells, including the subtle
  recurring ones (`frame-scoped-ko`, `quant-subject-cog-verb`). The lone miss was an
  extraction bug (fixed — colon-anchored regex) plus the discourse-rule limitation:
  context-dependent rules can't be recall-tested on isolated snippets; they converge via
  Phase-1 in-context review.
- Default suite green (21 passed).

## What's next

**Live decision (unanswered when session paused):** next agent step —

1. Workflow inline-driver prototype (small token cost), or
2. Phase 3 exemplar expansion — lift candidate exemplars from `corpus/curated/` for chakrit
   to approve/cull.

Recommended 1 first (infra makes 2 cheaper to run and measure). Later phases: 3 (exemplar
inversion + SKILL.md/references framing), 4 (provenance frontmatter field, plateau
tracking), 5 (deferred: register-as-axes, eval-as-demand, triage-not-judge model).

## Gated on chakrit (no rush)

- Phase 1 review — iter-8/9/10 CLEAN outputs via `REVIEW-PROTOCOL.md` (his ear).
- Two Thai docs — `README.md`, `CONTRIBUTING.md` reframe (Thai authoring is his). Spans:
  README `หลักคิดของ skill` / `วินัยการเพิ่มกฎ` / `Eval ทำงานยังไง`; CONTRIBUTING §1, §5, §6.
- Green light to spend the full `-m recall` baseline (~74 calls) for the before-number.

## Open questions

- Workflow vs Phase 3 first (above).
- Discourse-rule recall needs in-context items — fold into Phase-1 review output.

## Recommended school issue (not filed — chakrit handles school sync)

`mdfmt.py` (the `markdown-writing` school skill) mangles `<...>` inline-code in prose and
is not idempotent with this repo's conservative hand-wrap. Candidate school-tracker issue.

## Blockers

None.
