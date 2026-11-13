# 2026-11-13 — Review across a model matrix; the ear marks drafts, not loop outputs

**Status:** Accepted · 2026-11-13

**Revises:** the outer loop in [`../spec/review-protocol.md`](../spec/review-protocol.md)
(rewritten to match), and qualifies decisions 3 and 7 of
[`2026-05-30-exemplar-first-pivot.md`](2026-05-30-exemplar-first-pivot.md). Leaves
[`2026-07-26-no-llm-judge.md`](2026-07-26-no-llm-judge.md) intact: auditors flag, only
the native ear decides.

**Scope:** how an iteration is generated, reviewed, and scored, and who is the authority
on which kind of correctness.

## Context

The outer loop reviewed only outputs that the kode-thai loop had driven to `CLEAN`
("skill-clean"), and its headline number was the share of those the ear still marked up
(the CLEAN-but-flawed rate), tracked across iterations to detect the prompt-only
ceiling. That made the auditor's verdict the filter for what the ear ever saw, so the
number depended on which model audited:

- In the 2026-07-26 run-on probe, a Claude auditor found 4 issues in prose a codex
  auditor had passed as `CLEAN`. Iteration 8 was audited by Claude, 9–10 by codex, so
  their numbers measured different bars.
- Choosing one auditor does not fix it. Claude is a major source of the AI-slop Thai the
  skill exists to remove, so "the stricter auditor" is not evidence of the better one,
  and an auditor that shares the drafter's model is blind to that drafter's errors.

The models fail differently, so one backend's audit applied to everyone forces every
model through the same path. The bar itself stays single — there is one native judge,
not a panel of linguists — but the path to it should not depend on one backend.

## Decision

1. **Matrix.** Every model in the run drafts every eval. Every model audits every draft —
   one pass, no fixes — including its own drafts (the diagonal measures self-blindness).
2. **The ear marks drafts, once, blind.** Chakrit marks spans in each draft without
   seeing any auditor's flags. Ear cost scales with the number of drafters, not
   drafters × auditors.
3. **Scoring is mechanical.** A script matches auditor flags to the ear's marks by span
   overlap (ambiguous matches confirmed by chakrit) and reports, per auditor, how many
   flags the ear agreed with and how many marks it caught; per drafter, a failure
   profile; and the flaws every auditor missed. The auditor used in shipped loops is
   chosen from these numbers. `skill-clean` remains only the loop's stop signal, with
   its auditor recorded — it is no longer a metric.
4. **Reference drafts.** Chakrit writes one draft per eval prompt, once, reused across
   iterations. It is held out of the skill bundle and exemplars — otherwise the evals
   would test the skill on its own examples. Uses: a register-matched native text for
   auditor false-positive checks, a mechanical distance (connective density, sentence
   length, particles, transliteration rate) to order drafts for review, and a native
   answer to each prompt. Registers chakrit does not write day to day (official,
   academic, news-wire) lean on the corpus instead.
5. **Two authorities.** The native ear decides naturalness and voice. The Royal
   Institute dictionary and the orthography standards
   ([`../vendor/thai-orthography-standards.md`](../vendor/thai-orthography-standards.md))
   decide spelling and prescriptive convention. Chakrit's own Thai is native, not
   book-author-proofed: a flag on his reference draft or rewrite is a false positive if
   it is a style rule, and a candidate slip for him to confirm if it is a checked
   orthography point. Nothing is auto-corrected.
6. **Rules and pairs are decided against the whole matrix,** never against one model's
   output. A pattern that recurs across drafters and that auditors miss earns a pair,
   then possibly a rule; a single drafter's quirk goes into that drafter's failure
   profile.
7. **Fix loops are reviewed only for the one or two routes meant to ship** (e.g. the
   native drafter followed by the kode-thai audit).
8. **Turning marks into skill content:** the agent drafts pairs, notes, and rule wording;
   chakrit batch-reviews them later (chakrit chose this over gating every agent note).
9. **Scores inform; they never gate.** The work is qualitative and the ruleset will
   never be complete. Chakrit: *"we will never arrive at a perfect ruleset. this whole
   effort has be treated qualitatively."* The pivot's decision 7 — stop when the numbers
   go flat — becomes chakrit's judgment, informed by the trend.

Chakrit's ruling on points 1–7: *"that's a much more solid setup. lock this in."*

## Why not the alternatives

- **One fixed auditor** (Claude or codex): keeps the metric hostage to that model's
  blind spots, and nothing ever measures whether its flags are right.
- **Union of auditors as the `CLEAN` bar:** strictest, but fix passes then chase two
  auditors at once, which reproduces the thrash seen when fix passes ran on slimmed
  bundles in iteration 6 — and it still never scores the auditors against the ear.
- **Reference drafts instead of marks:** prose has many valid versions, so difference
  from chakrit's draft is not a flaw; turning differences into verdicts would need a
  judge. Marks stay the source of pairs; the reference complements them.

## Consequences

- `review-protocol.md` is rewritten around the matrix; the CLEAN-but-flawed rate and
  the recall-miss/coverage-gap classification by agent judgment are retired in favour of
  the mechanical scoring in point 3.
- The harness needs a drafts × auditors mode with no fix passes, flag output in a
  span-addressable form, and a scoring script; the review UI needs a mode that hides
  auditor flags and a page for writing reference drafts.
- Whether the auditor should see each rule's hard/soft severity becomes a test inside
  the matrix (one auditor run with the tags, one without), not a preference.
- Which slug owns run-on sentences waits for the first matrix to show where auditors
  file them.
