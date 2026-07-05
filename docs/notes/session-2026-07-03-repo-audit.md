# Session checkpoint — full repo/docs audit + truth-sweep (2026-07-03)

<!-- Session note. Resume breadcrumb for the next /ace. -->

- **Date:** 2026-07-03 (saved 2026-07-05)
- **Status:** audit done, mechanical fixes landed as `bb5b325` on `main` — **unpushed**.

## What happened

Four-way parallel audit of every instruction surface (CLAUDE.md vs reality, docs/
tree, skill bodies, ledger/corpus/harness). Harness itself healthy: sanity suite
green, no dead links, gitignore and bundle preprocessor match their docs.

`bb5b325` fixed everything mechanical: CLAUDE.md layout/commands (scripts/,
exemplars.md, test_recall/test_skill_frontmatter/typhoon_pass/compare_arms,
`-m recall`), register count 5→6 everywhere live, exemplars.md into both skills'
bundle lists + kode-thai audit-mode note, CONTRIBUTING/README numeric fixes +
false pytest-convergence claim deleted, work-queue Framing-experiments re-scoped
(#1/#2 landed via exemplars.md pinned last), Typhoon plan-note Results marked
superseded by iter-14, corpus count 54→55, test_claude docstring, lib.py
docstring, gitignore recall-report entry. Three new human-tasks-queue items
(see below).

## Open — chakrit said "we'll decide next session"

1. **Push `bb5b325`** — committed, awaiting say-so.
2. **The audit's root finding: two unreconciled eras.** The accepted
   exemplar-first pivot says "no better-model escape hatch"; the shipped Typhoon
   model route is that escape hatch and lives only in notes. Needs a dated
   superseding/revising decision + a `docs/decisions/` file for the locked
   no-LLM-judge ruling. Queued in `human-tasks-queue.md`.
3. **`ด้วย` conflict + connective budget** — register.md caps the particle the
   closure rules require; budget defined five different ways. Queued.
4. **AWS-Thailand b2b-formal re-vet** — action items from source-vetting still
   unexecuted. Queued.
5. **Provenance backfill scope** — ~94 rules across the five rule files carry no
   corpus citation and almost nothing is flagged `provisional`. Deliberately NOT
   queued: whether to backfill retroactively (vs discipline applying only to new
   rules) is a direction call.
6. **workspace/INDEX.md left untouched** — iters 9/10 stay `pending` (their
   feedback.md files look like pre-review agent notes; `reviewed` is the outcome
   of chakrit's ear pass); "No record" rows for 4/5/6 are accurate for tracked
   state. Revisit only if chakrit disagrees.
7. **Exemplar coverage gaps** — scoped bundles for marketing-b2b-formal /
   fintech-warm / retail-tech / official ship no pair and no native exemplar;
   news has no native exemplar. Recorded in the re-scoped work-queue Framing
   item; excerpting from existing corpus categories is agent-doable, `official`
   has no corpus category (surface, don't synthesize).

## For the next /ace

Start from `docs/human-tasks-queue.md` (three new audit items + the pre-existing
iter-14 ear review) and item 1–2 above. No in-flight code work; working tree
clean.
