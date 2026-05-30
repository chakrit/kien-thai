# Iteration 8 — inline run (claude-inline only)

Mode: `inline` (subagent-driven). Bundle source: `tests.lib.kien_thai_bundle`
with register-scoped two-tier (draft → audit). All four `with_skill` configs
generated and looped through `/kode-thai` audit/fix passes until `CLEAN`.
Baseline (no skill) was not generated this run — focus was on
audit-to-convergence per chakrit's overnight brief.

> **Caveat (per `docs/spec/inline-iteration.md`):** outputs are tagged
> `mode: "inline"` and are not cross-iteration comparable to harness output.
> Treat as audit/probe material — judge prose quality, derive rule traces,
> but don't cite for bundle-effect measurement.

## Results

| Eval                       | Register             | Passes to CLEAN | Converged |
| -------------------------- | -------------------- | --------------: | :-------: |
| tech-doc-short             | explainer            |               1 |     ✓     |
| news-feature-bts           | news                 |               1 |     ✓     |
| marketing-blurb            | marketing-saas-sme   |               3 |     ✓     |
| personal-essay-homecoming  | personal-blog        |               3 |     ✓     |

"Passes to CLEAN" = audit-pass index that returned `CLEAN`. 1 = pass-0 draft
audited clean on first look. 3 = two fix cycles required.

## Audit issues that surfaced (for review)

### marketing-blurb

**pass-1** — `frame-scoped-ko` violation.
Frame `ทีไร` already carries the if-then linker, so `ก็` doubles up.

- Before: `พอปิดบัญชีสิ้นเดือนทีไร ตัวเลขก็ไม่เคยตรงกับที่คาดสักที`
- After:  `พอปิดบัญชีสิ้นเดือนทีไร ตัวเลขไม่เคยตรงกับที่คาดสักที`

**pass-2** — `seam-connective-missing` (Result + means/exception variant).
The seam between a result clause and back-to-back means/exception clauses
needs a bridge particle. `โดย` was added once to cover both negated
exceptions (within the `doi-sprawl` per-paragraph cap).

- Before: `...ใช้ได้จริง ไม่ต้องเปิด Excel ไม่ต้องจ้างบัญชี`
- After:  `...ใช้ได้จริง โดยไม่ต้องเปิด Excel ไม่ต้องจ้างบัญชี`

### personal-essay-homecoming

**pass-1** — two hits.

1. `over-hedging` — marketing hedge stack `น่าจะ X อยู่ด้วยซ้ำ` bled into
   personal-blog register, leaving the line ลังเล instead of assertive.
   - Before: `ผมรู้ว่าราคานี้ป้าน่าจะขาดทุนอยู่ด้วยซ้ำ`
   - After:  `ผมรู้ว่าราคานี้ป้าขาดทุนแน่ๆ`
2. `f5` (demonstratives over pronouns) — `มัน` used for inanimate referent
   (a road), where native Thai prefers a demonstrative or drops the pronoun.
   - Before: `ทั้งที่จริงๆ มันคือถนนเดิมที่เดินมาตั้งแต่เด็ก`
   - After:  `ทั้งที่จริงๆ ก็คือถนนเดิมที่เดินมาตั้งแต่เด็ก`

**pass-2** — two hits, both register/style polish.

1. `mai-yamok-spacing` — personal-blog register defaults to *no* space
   before ๆ; the piece was inconsistent (most drops, two keeps). Normalized
   to no-space throughout (`จริงๆ`, `แน่ๆ`).
2. `em-dash-semicolon` (advisory) — two em-dashes used as appositive /
   list-intro rather than parenthetical aside. One replaced with `ทั้ง`
   enumerator, the other dropped to bare whitespace.

## Patterns worth flagging into the iteration-discipline trace

Nothing here surfaces a gap the existing ruleset doesn't already cover —
every audit citation maps to an existing rule slug. Two observations for
chakrit's review:

1. **`frame-scoped-ko` continues to fire on `ทีไร` frames.** This is the
   same family of double-linker errors that earlier iterations also
   surfaced. Worth checking whether the rule's example coverage is strong
   enough or whether it needs a more prominent anchor in `SKILL.md`.

2. **Register bleed into personal-blog.** The marketing hedge stack
   `น่าจะ X อยู่ด้วยซ้ำ` showed up in a personal-blog draft — the bundle
   is register-scoped, so this isn't cross-register contamination from
   prompt; it's the model defaulting to a hedge shape that's specifically
   tagged as marketing-flavored. May indicate `register.md`'s personal-blog
   section needs a counter-example showing assertive closure where AI
   default would hedge.

Both are observations, not proposed rule changes — surfaced here per the
"trace before you write" discipline in `CLAUDE.md`. Decide before editing
the skill.

## What was NOT done

- No `baseline` (no-skill) configs generated — overnight brief was
  audit-to-pristine, not bundle-effect measurement. Run the pytest harness
  with `-m generate` when you need cross-config comparison.
- No `codex-inline` half — only `claude-inline`. Cross-backend signal would
  require codex-driven generation (or running the pytest harness).
- No quant heuristics (`-m evaluate`). Run separately if wanted.
