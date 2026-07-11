# Session checkpoint — 2026-07-07 (1-by-1 human-queue walk + Phase 1 review)

Session drove the `human-tasks-queue.md` under the **1-by-1 protocol**. Parked mid-way;
chakrit tired. This is the resume breadcrumb.

## What was done

- **Human-queue item 1 — DECIDED.** Next agent step order: **(A) Workflow inline-driver
  prototype → then (B) Phase 3 exemplar expansion.** Recorded in `work-queue.md` → "Next
  agent step"; item 1 closed in `human-tasks-queue.md`.
- **Human-queue item 2 — Phase 1 review, partial.** chakrit's ear over the skill-clean
  CLEAN outputs (the *chakrit-clean* measurement):
  - **iter-9 fully reviewed** → verdicts in `workspace/iteration-9/feedback.md`:
    tech-doc-short (calque `คุมความเรียบ`), marketing-blurb (clean), news-feature-bts (¶4
    discourse / `reads-misstructured`, ¶5 `พื้นฐาน` x2), personal-essay (no findings).
  - **iter-10 partial** → `workspace/iteration-10/feedback.md`: tech-doc-short done (line-7
    run-on). **Pending chakrit's ear: marketing-blurb, news-feature-bts,
    personal-essay-homecoming, exec-brief-oss-bi-hana** (review files #6–9).
- **Fable-5 baseline probe** (side quest) — one generation pass, eval-1, no skill, no loop,
  to see raw Fable-5 Thai. chakrit's 10 native corrections (F1–F10) captured in
  `docs/scratch/2026-07-07-fable5-eval1-probe.md`. Raw draft: `workspace/probes/` (gitignored).

## Where we stopped / next `/ace`

- **Resume the review**: open iter-10 review files #6–9 one at a time in iA Writer (one
  file only — chakrit gets confused by multiple tabs), log verdicts to
  `iteration-10/feedback.md`, then flip iter-9/iter-10 Review cells in `workspace/INDEX.md`
  to `reviewed`.
- **Then the rest of the human queue** — items 3–12 still open (discourse axis, iter-8
  rewrites, Thai doc reframes, recall baseline, mdfmt school issue, model-route decision,
  `ด้วย` conflict, AWS-Thailand re-vet, personal-blog corpus, iter-14 comparisons).

## Deferred (not dropped)

- **A — Workflow inline-driver prototype**: decided but not started (chakrit parked the
  session). This is the immediate next *build*.
- **kode-thai loop on the Fable-5 draft**: deferred — **Fable quota low**, do not re-run.

## Strongest emergent signal

**Run-on / under-segmentation** recurs across backends and the skill-clean layer: Fable F1,
iter-9 news ¶4, iter-10 tech-doc line 7. Candidate **recall-miss** — the sentence-length
rule in `ai-tells.md` is not firing on run-ons that reach CLEAN. Overlaps the
`reads-misstructured` discourse axis. Needs a confirmed recall-check pass, not a reflex rule
add.

## Durable-knowledge routing

Nothing school-bound (kien-thai is this repo's own artifact, not a school skill). No new
user-MEMORY or CLAUDE.md fact. All learnings landed in `docs/` + the feedback files above.
