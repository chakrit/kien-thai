# 2026-07-26 — No LLM judge; the native ear is the only verdict

**Status:** Accepted · locked since 2026-05-10, recorded 2026-07-26

**Scope:** who renders the quality verdict on Thai prose. Does not restrict LLM use for
drafting, auditing, triage, or mechanical checks.

## Context

This ruling has governed the repo since the first iteration and is cited as
authoritative in at least three places — `CLAUDE.md` ("Locked decisions — skill
content: No LLM-judge until human review proves insufficient"),
[`../spec/review-protocol.md`](../spec/review-protocol.md), and the eval-strategy
section that sends subjective prose to humans rather than assertions. It was recorded
nowhere in `decisions/`, so the one thing holding the measurement honest existed only
as a repeated claim.

Written down late, and unchanged — this entry is a transcription, not a new call.

## Decision

**No LLM judges Thai prose quality.** chakrit's ear is the terminal verdict
(*chakrit-clean*). Adding an LLM judge — to score outputs, to gate iterations, or to
stand in for review when his attention is scarce — is out of bounds until human review
demonstrably fails as the bottleneck, and that failure is demonstrated, not assumed.

## Rationale

**Self-judge bias is the original reason.** An LLM grading LLM output rewards its own
distribution. Claude scoring Claude's Thai measures agreement with Claude's priors,
which is precisely the thing under test.

**The 2026-07-26 sharpening makes it stronger than a bias argument.** Claude's
characteristic failure in Thai is not ungrammatical output — it is output that *seems*
grammatical while being invalid, weird in ways a native reader catches instantly and an
English-shaped reader cannot see at all. A judge sharing the drafter's prior is blind
to exactly the error class that matters most. This is not a calibration problem that a
better rubric fixes; the judge lacks the perceptual access.

The repo already measures the consequence. `skill-clean` means the auditor found
nothing; the **CLEAN-but-flawed rate** counts how often the native ear red-inks prose
the auditor passed. That gap is the product's actual quality signal. An LLM judge would
be scored against the same blind spot it has, so it would report the gap as closed
while it stayed open.

**Why not the obvious alternative.** Standard practice is an LLM-judge rubric for
subjective generation quality — it scales, it is cheap, it produces a number per
iteration. We decline it because a number that cannot see the failure mode is worse
than no number: it converts an open question into false confidence, and the review
protocol's whole design is aimed at keeping that question visible.

## Boundaries — what is still allowed

- **Auditing** inside the kode-thai loop. The audit pass cites rule slugs; it does not
  render a quality verdict. Its terminal is `skill-clean`, explicitly *not* naturalness.
- **Drafting** with any model, including a Thai-native one. See
  [`2026-07-26-model-route-revises-exemplar-first.md`](2026-07-26-model-route-revises-exemplar-first.md).
- **Mechanical checks** — `test_quant.py` forbidden-phrase and connective-density
  heuristics. Advisory, never a gate.
- **Triage**, per pivot decision 8: a Thai-tuned model may route chakrit's attention to
  likely problems, never overrule his verdict. Still deferred; revisit only if review
  throughput proves to be the wall.
- **Candidate generation** — a model may propose rules, pairs, or source candidates for
  chakrit to ratify. Model output is a candidate, never provenance.

## Revisit condition

Only when human review is demonstrated to be the binding constraint on iteration
speed — measured, not asserted — and even then triage comes before judging.
