# The model route — who drafts, who audits

**Status:** accepted (target state; Typhoon is not a `BACKENDS` entry, so step 4 measures
via `typhoon_pass.py` + `compare_arms.py` rather than the standard matrix)

How Thai prose gets produced in this repo, after
[`../decisions/2026-07-26-model-route-revises-exemplar-first.md`](../decisions/2026-07-26-model-route-revises-exemplar-first.md).
The *why* lives in that ruling; this is the current design.

## The split

Two failure modes, two instruments:

| Failure | Instrument |
| --------------------------------------------------- | ----------------------------------- |
| Invalid-but-plausible Thai, calqued structure | A Thai-native drafter — correctness is close to free |
| Flat voice, wrong register, no pulse | kien-thai frames + native exemplars, applied as audit |

A western-focused model reasons in English first and leaks that structure into Thai.
The result reads grammatical to an English-shaped reader and wrong to a native one, so
no amount of auditing *by the same prior* reliably removes it. A Thai-derived model
never takes the translation step. It buys correctness; it does not buy voice.

## The route

1. **Probe.** `skills/kien-thai/scripts/thai-route.sh <register> <prompt>` checks for a
   reachable native model.
2. **Draft.** Present → draft with it (`thai-native-draft.py`, few-shot conditioned from
   `corpus/curated/<register>/`, exit 0). Absent → exit 3, kien-thai drafts directly.
   **The skill stands alone; the model makes it better.**
3. **Audit.** Either way the draft enters the kode-thai loop — the un-scriptable half.
   Auditing Thai against the frames is language judgment, not a transform.
4. **Measure.** Review protocol as usual:
   [`review-protocol.md`](review-protocol.md). The drafter changed; the measurement did
   not.

Scripted vs agent-driven is deliberate: model availability, draft capture, register
conditioning, and the route decision are scripts. The audit is an agent.

## Constraints that bind

- **Ollama HTTP API with `"stream": false`, never `ollama run`.** The CLI leaks its
  streaming re-render into redirected output and silently corrupts Thai. Details:
  [`../vendor/model-backends.md`](../vendor/model-backends.md).
- **Drafting is not judging.** A native model drafting prose does not make it a judge —
  [`../decisions/2026-07-26-no-llm-judge.md`](../decisions/2026-07-26-no-llm-judge.md).
- **Conditioning pulls from the vetted corpus only.** The drafter never fabricates its
  own exemplars, and a register with no corpus category has no coverage — surface the
  gap rather than synthesizing prose to fill it.

## Open — and the correctness claim is thin too

**Evidence audit, 2026-07-26.** The correctness claim rests on exactly one native-ear
reading of bare, unconditioned Typhoon-2 8B: no grammatical fault, no calque. One
register, one draft, unreplicated. It has been repeated across this repo's docs often
enough to sound established; it is not.

Everything generated since is unreviewed, and its mechanical signals do not support the
claim:

| eval | typhoon c/1k | claude+skill c/1k |
| -------------------- | -----------: | ----------------: |
| news-feature-bts | 8.7 | 1.5 |
| exec-brief-oss-bi-hana | 3.4 | 1.2 |
| tech-doc-short | 2.3 | 0.0 |
| marketing-blurb | 0.0 | 0.0 |
| personal-essay | 0.0 | 0.0 |

Formal-connective density is *higher* for the native draft on three of five. Two further
problems need no Thai judgment: the marketing draft emits outline labels instead of
prose, and the exec-brief opens with a greeting. Length runs consistently shorter
(marketing 542 vs 1891 chars) — terseness or under-delivery, undetermined.

**The clean pair set now exists — iteration-15 (2026-07-27).** Iterations 11–14 were
contaminated: every `comparison.md` there declares "NOT co-generated", pairing a Typhoon
draft against a Claude arm from a different iteration and skill state. Iteration-15 ran
both arms under one `EVAL_ITERATION` pin at one commit, so the pair isolates the drafter.
It is generated and **awaiting chakrit's ear**; until those verdicts land, everything
above stands.

So this spec claims **neither** correctness nor voice as settled. The route is the
direction under test, and the review of iteration-15 is what settles it — not further
argument.

Not yet built: Typhoon as a third entry in `tests/lib.py:BACKENDS`. `typhoon_pass.py`
writes into the same iteration tree and `compare_arms.py` reads both arms uniformly, so
a co-generated comparison no longer needs it; a *measured cross-iteration* one still
does. Tracked in [`../work-queue.md`](../work-queue.md).
