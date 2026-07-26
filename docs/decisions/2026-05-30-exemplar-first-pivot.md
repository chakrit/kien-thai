# 2026-05-30 — Pivot: exemplar-first, auditor-recall-measured

**Status:** Revised · 2026-05-30, revised 2026-07-26 by
[`2026-07-26-model-route-revises-exemplar-first.md`](2026-07-26-model-route-revises-exemplar-first.md)

> **Revision (2026-07-26).** The "no better model escape hatch" premise in Context
> below is narrowed to *voice*. A Thai-native model is now the preferred drafter where
> reachable, because it wins on correctness; kien-thai is the audit-and-voice layer over
> it. Decisions 1–8 stand unchanged. Read the revision before acting on the Context
> paragraph. Also stale: the last Consequences bullet names Claude Code's `Workflow`
> tool as a candidate inline driver — rejected 2026-07-26 as harness lock-in. The
> inline driver stays; it is built harness-neutral.

**Scope:** how we build and measure kien-thai / kode-thai. This does not rewrite the
skill's rule content — it changes what we invest in, what counts as progress, and the
default shape of a new artifact.

## Context

kien-thai is a prompt-only product: a general, English-centric model coaxed into native
Thai via context. There is no "better model" escape hatch — if a Thai-native model were
adopted, this skill would not exist. So the only lever we will ever have is what sits in
the context window, and the kode-thai audit loop is the recommended way to use the skill.
One-shot generation is a welcome side-effect, not the goal.

Three of our own artifacts, read together, say the current architecture invests in the
weaker bet:

- The framing investigation (`docs/scratch/framing-investigation-2026-05-21.md`) ranks native
  exemplars near the task as the highest-impact lever and English rules as a mitigation.
- The idiomatic-edges judgement
  (`docs/decisions/2026-05-11-frame-rules-have-idiomatic-edges.md`) concludes the long
  tail of naturalness is not rule-shaped.
- Every recent `feedback.md` notes that loop-to-CLEAN is "not for bundle-effect
  measurement."

Yet the skill is ~2,300 lines of English rules against ~65 lines of exemplars, and
convergence-to-CLEAN gets reported as if it were a quality result. The investment is
inverted relative to our own stated theory of what works.

## Decision

1. **The binding constraint is auditor recall, not drafter quality.** The kode-thai loop
   converges to *skill-clean* (the ruleset finds nothing), never to *chakrit-clean* (the
   native ear finds nothing). The gap between them is exactly the idiomatic/voice tail
   that resists rules, and it is invisible from inside the loop.

2. **skill-clean is ruleset-coverage, not naturalness.** Never report "passes to CLEAN" as
   a quality signal. A fast CLEAN is ambiguous: either the draft was good, or the auditor
   is too coarse to see what is wrong.

3. **chakrit is the authoritative terminal.** Thai-born, Thai-schooled — the spec, not a
   sample. We do not average in other readers; that adds noise against the target. We do
   reduce what his scarce attention must cover, so it is spent only on the irreducible
   native verdict.

4. **The default durable artifact is the native before/after pair, not the rule.** Pairs
   are lossless native signal; rules are a lossy compression performed by a non-native
   generalizer. A pattern earns an English rule only when the pair alone does not
   transfer. This inverts the current rule-first habit.

5. **Exemplars are the primary lever; rules are cleanup.** Grow exemplars — drafted from
   chakrit's pairs and the corpus — and feed them to both the draft bundle (one-shot
   quality, shorter passes-to-CLEAN) and the audit bundle (auditor recall). Invert the
   2,300:65 ratio over time.

6. **Provenance-safety is a corpus vetting axis.** Post-2022 web marketing is suspect — it
   may itself be AI-drafted (the AWS-Thailand flag in iteration-7 feedback). Pre-LLM
   print, archives, and established pre-2022 authors are safer ground truth.

7. **The ceiling is detected, not guessed.** When N iterations of additions stop moving
   the auditor-recall and CLEAN-but-flawed numbers, the prompt-only ceiling is reached —
   stop adding. The framing investigation predicts this ceiling exists; we make it visible
   instead of pushing past it on faith.

8. **A Thai-tuned model may later triage, never judge.** Used only to route chakrit's
   attention to likely problems, never to overrule his verdict. Deferred; revisit only if
   review throughput proves to be the wall. Distinct from the locked "no LLM-judge"
   decision, which was aimed at self-judge bias (Claude grading Claude).

## What stays unchanged

- **Trace-before-you-write.** Extended, not replaced: the default landing is now a pair,
  and recall is measured before assuming a rule is missing — but no artifact lands on
  vibes.
- **Corpus as the single source of truth** for native voice.
- **Two-stage evals:** subjective prose is judged by humans, not assertions.
- **The kode-thai loop as the recommended product path.**

## Consequences

- The review loop becomes a first-class, repeatable workflow that collects the
  skill-clean-vs-chakrit-clean data as a byproduct. Spec: `docs/spec/review-protocol.md`.
- Work is sequenced measurement-first; the rollout phases live in `docs/work-queue.md`
  ("Framing experiments" graduates from speculative to committed direction).
- This formalizes the framing-investigation recommendations (#1, #2) that have sat at
  Block: None, and the iteration-7 idiomatic-edges judgement.
- **Inline is the default iteration mode.** Because bundle-effect convergence is demoted
  (decision #2), the cold pytest harness's signature deliverable — contamination-free
  cross-iteration A/B — is rarely needed. Generate inline (fresh subagent / fresh Codex
  session per output, so session history doesn't shape the Thai), review via the
  protocol, and reach for the cold harness only when a future automated gradient +
  discrimination metric needs clean A/B. The Workflow tool is a candidate driver for the
  claude-inline half (deterministic code orchestrating fresh subagents, parallel across
  evals, structured audit output); the Codex half stays chakrit-driven.
