# The model route — who drafts, who audits

**Status:** accepted (target state; the harness wiring in step 4 is not built yet)

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

## Open — the voice question

The correctness claim is backed by a native-ear verdict on bare, unconditioned
Typhoon-2 8B: no grammatical fault, no calque. The **voice** claim is not backed yet.
One register, unconditioned, is thin.

`workspace/iteration-14/*/comparison.md` holds the conditioned five-eval Typhoon vs
Claude+skill set, generated and awaiting chakrit's ear. That review answers whether the
native drafter also wins on voice, or whether it needs the exemplar layer to get there.
Until then this spec claims correctness only.

Not yet built: Typhoon as a third entry in `tests/lib.py:BACKENDS`, which is what a
measured cross-iteration comparison needs. Tracked in
[`../work-queue.md`](../work-queue.md).
