# Review protocol — the outer loop

**Status:** accepted · rewritten 2026-11-13 for the matrix methodology
([`../decisions/2026-11-13-matrix-review-methodology.md`](../decisions/2026-11-13-matrix-review-methodology.md)).
The harness pieces it needs — drafts × auditors mode, span-addressable flags, the
scoring script, the browser review UI — are not built yet; they are queued in
[`../work-queue.md`](../work-queue.md).

kode-thai is the **inner loop**: audit → fix until the auditor returns `CLEAN`. This
protocol is the **outer loop**: several models draft and audit each other, the native
ear marks the drafts, and a script scores every auditor against the ear. The ear is the
only judge (see [`../decisions/2026-07-26-no-llm-judge.md`](../decisions/2026-07-26-no-llm-judge.md));
scores are signals to read, never gates — the work is qualitative and the ruleset will
never be complete.

Counterpart to `inline-iteration.md` (the generate protocol). Direction:
[`../decisions/2026-05-30-exemplar-first-pivot.md`](../decisions/2026-05-30-exemplar-first-pivot.md).

## Definitions

- **matrix** — every drafter × every auditor for one iteration's evals. Audits are one
  pass, no fixes; the diagonal (a model auditing its own draft) is included.
- **mark** — a span chakrit flags in a draft, with an optional note and an optional
  rewrite (the pair's "after").
- **flag** — a span an auditor cites, with the rule slug it cites.
- **agreement** (per auditor) — the share of its flags that overlap a mark. Low
  agreement means the auditor flags native-acceptable Thai.
- **catch rate** (per auditor) — the share of marks that one of its flags overlaps.
- **all-missed** — marks no auditor caught. The real coverage gaps.
- **failure profile** (per drafter) — the marks on that drafter's drafts, grouped.
- **reference draft** — chakrit's own answer to an eval prompt, written once, held out
  of the skill bundle and exemplars.
- **reads-flat** — a draft with no discrete flaw that still reads AI-flat. A verdict
  flag, not a mark.
- **skill-clean** — the auditor returned `CLEAN`. Only the inner loop's stop signal,
  recorded with the auditor that issued it; never a metric.

## Two authorities

The native ear decides naturalness and voice. The Royal Institute dictionary and the
orthography standards decide spelling and prescriptive convention. Chakrit's Thai is
native, not book-author-proofed, so:

- an auditor flag on his reference draft or his rewrite is a **false positive** when it
  cites a style or naturalness rule;
- it is a **candidate slip** for him to confirm when it cites a checked orthography
  point. Nothing is auto-corrected.

## The lever

The agent does everything except the verdict. Chakrit's time goes only to the native
call — read and mark. Generation, staging, matching, scoring, recording, and routing are
agent or script work. Ear cost scales with the number of drafts, not with the matrix.

## Workflow

1. **[agent] Generate.** Every drafter drafts every eval under one iteration pin
   (`EVAL_ITERATION=N`), runs stamped with model, commit, and bundle hash. Every auditor
   audits every draft, one pass, no fixes.
2. **[agent] Stage.** Build a review batch for the browser review UI: drafts only,
   arms shuffled and labelled neutrally, auditor flags hidden. Order drafts by
   mechanical distance from the reference draft where one exists, furthest first, so a
   session that ends early has covered the most informative drafts.
3. **[chakrit] Mark.** Read each draft end-to-end. Mark spans; add a note or a rewrite
   where useful; flag `reads-flat` where it applies. Drafts not reached wait for the
   next session.
4. **[script] Score.** Match flags to marks by span overlap. The agent proposes matches
   for ambiguous overlaps; chakrit confirms. Output per auditor (agreement, catch rate),
   per drafter (failure profile), and the all-missed list. Reference drafts give each
   auditor's false-positive count on native text.
5. **[agent] Record** structured entries in the iteration's tracked verdict files
   (`workspace/iteration-N/verdicts/`) and render `workspace/iteration-N/feedback.md`
   from them. Never treat gitignored `output.md` as the home of a verdict.
6. **[agent] Route — collect, do not apply.**
   - Marks with rewrites → candidate before/after pairs, register-tagged, drafted with
     notes by the agent; chakrit batch-reviews them later.
   - All-missed patterns that recur across drafters → the trace-before-write queue
     (pair first, rule only if the pair does not transfer).
   - A single drafter's quirk → that drafter's failure profile, not a rule.
   - Every confirmed mark → the known-bad set for the recall harness.
7. **[agent] Fix-loop review, shipped routes only.** For the one or two routes meant to
   ship, run the kode-thai loop to `CLEAN` and stage the final outputs for a second,
   lighter read.
8. **[agent] Update** `workspace/INDEX.md` (Review → `reviewed`, link the feedback) and
   append the iteration's row to the trend.

## Record format

One block per draft:

```
iter / eval / drafter · reads_flat: no
marks:
  - span:    "<offending Thai>"
    note:    "<chakrit's framing, verbatim>"
    rewrite: "<native rewrite — the pair's 'after'>"
    caught_by: [codex/f6/ko-resumptive]     # auditor/slug, from scoring
  - span:    "<…>"
    caught_by: []                           # all-missed
flags_unmatched:                            # auditor flags the ear did not share
  - auditor: claude · slug: em-dash-semicolon · span: "<…>"
```

## Reading the trend

- **An auditor with high catch rate but low agreement** over-flags; its fixes will
  rewrite native Thai toward its own prior. Prefer it only as a secondary pass.
- **A long all-missed list** that recurs across drafters is a genuine ruleset gap — land
  pairs.
- **A failure profile concentrated in one drafter** argues for routing that drafter's
  output differently, not for a universal rule.
- **High reads-flat** is an exemplar problem; no rule fixes it.
- **Flat numbers across iterations** inform chakrit's call on whether the prompt-only
  ceiling is reached; they do not decide it.
