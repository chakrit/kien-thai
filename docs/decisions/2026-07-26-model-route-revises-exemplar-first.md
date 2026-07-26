# 2026-07-26 — The Thai-native model route revises the exemplar-first pivot

**Status:** Accepted · 2026-07-26
**Revises:** [`2026-05-30-exemplar-first-pivot.md`](2026-05-30-exemplar-first-pivot.md)
(narrows its opening premise; leaves decisions 1–7 standing)

**Scope:** what drafts Thai, and what kien-thai is *for*. Does not change the rule
content, the review protocol, or the measurement.

> **Addendum, same day — the evidence base is thinner than this entry implies.**
> Written before the prior evidence was audited. What exists for Typhoon is **one**
> native-ear reading, one register, unconditioned, never replicated. The comparison
> runs since are unreviewed, and their mechanical signals cut against on connective
> density (higher than Claude+skill on three of five evals, 8.7 vs 1.5 per 1k on
> news), with instruction-following lapses visible without any Thai judgment. The
> comparison files also declare themselves **not co-generated**, so even that
> unreviewed signal is contaminated.
>
> Decision 1 below ("preferred drafter, not an experiment") overstates what is
> established. Read it as the *direction* this repo is testing, conditional on the
> iteration-14 review. Nothing here is retracted — the reasoning about the two
> failure modes stands on its own — but the confidence is downgraded, and that is
> exactly why this was a revise and not a supersede.

## Context

The pivot opens with a premise stated as fact: *"There is no 'better model' escape
hatch — if a Thai-native model were adopted, this skill would not exist."* Six weeks
later the repo shipped exactly that escape hatch — `SKILL.md` step-0,
`scripts/thai-route.sh`, `scripts/thai-native-draft.py` — routing to Typhoon-2 8B
when it is reachable.

The contradiction was never recorded. The 2026-07-03 audit named it the root finding;
until this entry it lived only in scratch notes and a scripts README, so a fresh agent
reading `decisions/` would conclude the shipped route should not exist.

## The premise was wrong in a specific way

The pivot's framing assumes one failure mode — a model that cannot write Thai. There
are two, and they call for opposite responses:

1. **Capability gap.** The model lacks the Thai to be fluent at all. Not fixable by
   prompting.
2. **Calque bias.** The model has ample Thai but reasons in English first, so English
   structure leaks into the output. This *is* fixable by context — it is what a
   de-calquing ruleset catches.

Frontier western-focused models are mostly the second case, and the output that
results is **not** "grammatical but foreign-flavored." Per chakrit's ear, it is
*seemed-to-be-grammatical-but-so-weird-it's-invalid* — surface-plausible constructions
that are wrong in Thai. That distinction is load-bearing: an English-shaped reader
(Claude included) cannot detect the invalidity, so it survives the kode-thai loop to
`CLEAN`. The auditor shares the drafter's prior and is blind to the drafter's
signature error.

Typhoon inverts the setup rather than mitigating it. It is Thai-derived by original
purpose, so its training data is geared toward correct Thai and correctness costs
little effort — there is no translate-from-English step to leak structure.

## Decision

1. **Where a Thai-native model is reachable, it is the preferred drafter.** Not a
   fallback, not an experiment. Correctness comes close to free; spending audit passes
   to claw it back out of a western prior is the worse trade.

2. **kien-thai is the audit-and-voice layer, not primarily a drafter.** The frames do
   not go away — they move on top of a native-drafted base, which is the kode-thai loop
   over a better input. The skill still stands alone when no native model is reachable.

3. **The pivot's "no escape hatch" is narrowed to voice.** The hatch is real for
   *correctness* (grammar, calque, invalid-but-plausible construction). It is unproven
   for *voice* — register, pulse, the `reads-flat` axis — which is what the exemplar
   program targets, and where prompt-only context remains the only lever we have.

4. **Pivot decisions 1–7 stand unchanged.** Auditor recall is still the binding
   constraint; skill-clean is still ruleset-coverage and never a quality result;
   chakrit is still the authoritative terminal; pairs are still the default durable
   artifact. Changing the drafter changes the input to the loop, not the measurement of
   it.

5. **Pivot decision 8 is unaffected.** "A Thai-tuned model may triage, never judge"
   governs the *review* side. Drafting with Typhoon is not judging with it; the
   authoritative verdict stays chakrit's ear. See
   [`2026-07-26-no-llm-judge.md`](2026-07-26-no-llm-judge.md).

## Why revise and not supersede

Supersede would claim the model route replaces the exemplar program. The evidence does
not reach that far. What exists is one native-ear verdict on bare, unconditioned 8B
output in a single register — strong on correctness, silent on voice. The conditioned
five-eval comparison that would test voice (`workspace/iteration-14/*/comparison.md`)
is generated but still unreviewed.

Revising keeps both bets live and makes the open question explicit rather than settling
it on one data point.

## Consequences

- `work-queue.md` item A is re-specced: the inline driver is kept, the harness-specific
  `Workflow` tool is dropped (chakrit, 2026-07-26: *"your workflow tool is tied to your
  proprietary harness. i don't want it."*). Eval capability is not optional — the repo's
  premise is that agent Thai **without this skill** is bad, so the measurement is the
  point.
- The route needs a living design home rather than a scripts README:
  [`../spec/model-route.md`](../spec/model-route.md).
- Wiring Typhoon as a third harness backend moves from speculative to committed
  direction — it is now the preferred drafter, so it belongs in the measured matrix.
- The voice question is the open one. It is answered by reviewing iteration-14, not by
  further argument.
