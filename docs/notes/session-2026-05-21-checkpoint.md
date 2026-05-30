# Session checkpoint — 2026-05-21

Single-day session. Committed cleanly; working tree clean.

## What was done

1. **Analyzed transient `feedback.md`** (act-5 minutes drafting corrections
   from 2026-05-14) and traced each of its 11 proposed rules against the
   existing kien-thai skill. Headline gap: no official / ministerial /
   minutes register existed in `references/register.md` (only 5 families
   covered).

2. **Applied all 11 corrections** as a sixth register family in
   `references/register.md` (`Register 6 — Official / minutes`), plus
   register-scope adjustments to existing rules (commit on this branch).
   New rules:

   - Under Register 6: `formal-capability-frame`, `formal-procedural-vocab`,
     `four-part-procedural`, `time-bounds-need-anchor`,
     `purpose-chain-required` (with carve-out from `connective-budget`),
     `name-document-by-function`, `no-telegraphic-shorthand` (umbrella for
     prepositional / numeric-series / arithmetic subtypes),
     `formal-issue-vocab`.
   - In `references/craft.md` (new "Voice and framing" section):
     `concrete-cases-over-topology`, `positive-capability-framing`.
   - In `references/grammar.md`: `capability-modal` got a register-aware
     note pointing at the new Register 6 rule.
   - `SKILL.md` workflow list now lists six families.
   - `tests/lib.py:REGISTER_HEADERS` gains `"official": ("Register 6",)`
     for harness scoping. Verified scoping works (Register 6 appears only
     when `register="official"` is passed).

   All Register 6 rules tagged **provisional** in the section preamble
   pending corpus validation. Per-rule application trail lives in
   [`docs/notes/feedback-2026-05-21-application.md`](feedback-2026-05-21-application.md).

3. **Researched agent-framing techniques** for shifting Claude toward
   Thai-native generation. Literature pass (English-accent paper,
   multilingual ICL, persona-effect, multilingual CoT) plus first-
   principles analysis. Conclusion in
   [`docs/notes/framing-investigation-2026-05-21.md`](framing-investigation-2026-05-21.md).

   Key updates to the prior "Act as Thai writer" intuition: (a) few-shot
   exemplars near the task are the bigger lever than persona; (b) bundle
   ordering matters — `examples.md` sits mid-bundle today, should be near
   the task end; (c) forcing Thai-language CoT likely **backfires** for
   Thai's resource class (mid-resource languages struggle to generate long
   native-language CoT); (d) the real fix is preference tuning, which we
   don't control — prompt techniques are mitigations.

4. **Committed and tidied** — committed in one commit; deleted the
   transient `feedback.md` (its content is preserved in the application
   trail file).

## What's next

Ordered by priority:

1. **Corpus validation for Register 6** — surface NACC / Royal Gazette /
   ministerial-minutes corpora; cross-check whether the 8 Register 6 rules
   hold beyond the single Samarterware session. Drop the provisional tag
   when validated.

2. **Test framing-experiment #1+#2** — bundle reorder (put `examples.md`
   last) + native-prose exemplar priming. Cheapest test arm; highest
   expected value per the framing investigation. Added as a work-queue
   entry; see `docs/work-queue.md`.

3. **Add an eval for `register=official`** in `evals/evals.json`. Seed
   prompt from the Samarterware session or write a fresh minutes-drafting
   task.

4. **Grow `formal-procedural-vocab` list** as more drafting sessions
   surface pairs. The starter list (8 entries) is thin.

## Open questions

- Should the `connective-budget` carve-out for `เพื่อ` chains extend to
  News and Academic registers, or stay official-only?
- Should some Register 6 vocab pairs (e.g. `ทำ → ดำเนินการ`) move to the
  broader `register-drift` table for wider applicability?
- Expected effect sizes for the framing experiments are unknown. The
  English-accent paper warns prompt-level methods can be "marginal or
  inconsistent" — manage expectations.

## State of the tree

- Branch `main`, ahead of `gh/main` by 2 commits (today's commit + the
  earlier session-checkpoint).
- Working tree clean apart from this checkpoint file.
- All 16 sanity + consistency tests pass.

## Files touched in this session

- `skills/kien-thai/SKILL.md`
- `skills/kien-thai/references/register.md`
- `skills/kien-thai/references/grammar.md`
- `skills/kien-thai/references/craft.md`
- `tests/lib.py`
- `docs/notes/feedback-2026-05-21-application.md` (new)
- `docs/notes/framing-investigation-2026-05-21.md` (new)
- `feedback.md` (deleted; content preserved in application trail file)
- `docs/work-queue.md` (entry to be added during this checkpoint)
- `docs/notes/session-2026-05-21-checkpoint.md` (this file)
