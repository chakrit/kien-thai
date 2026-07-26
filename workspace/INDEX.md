# Iteration index

Generation runs live under `workspace/iteration-N/<eval>/<backend>/<config>/`.
Eval subdirectories are gitignored evidence (`output.md`, `pass-N.md`,
`prompt.txt`, `meta.json`); iteration-root `feedback.md` files are tracked.
See CLAUDE.md → "Workspace outputs are evidence, not artifacts".

| Iter |       Date | Mode / scope                                          | Review   | Feedback                                |
| ---: | ---------: | ----------------------------------------------------- | -------- | --------------------------------------- |
|    1 | 2026-05-10 | Harness, 2 evals × 2 backends × 2 configs (8 outputs) | reviewed | [feedback.md](iteration-1/feedback.md)  |
|    2 | 2026-05-10 | Harness resume — audit-checklist kill, slug migration | —        | —                                       |
|    3 | 2026-05-10 | Harness resume — convergence summary, review order    | —        | —                                       |
|    4 |          — | No record (workspace not committed)                   | —        | —                                       |
|    5 |          — | No record (workspace not committed)                   | —        | —                                       |
|    6 |          — | No record (workspace not committed)                   | —        | —                                       |
|    7 | 2026-05-12 | Harness, 3 evals × 2 backends × 2 configs; first BTS  | reviewed | [feedback.md](iteration-7/feedback.md)  |
|    8 | 2026-05-22 | Inline (subagent), 4 `with_skill` configs to CLEAN    | reviewed | [feedback.md](iteration-8/feedback.md)  |
|    9 | 2026-05-22 | Inline (codex), 4 evals × 2 configs, converged pass 1 | reviewed | [feedback.md](iteration-9/feedback.md)  |
|   10 | 2026-05-30 | Inline (codex), 5 evals × 2 configs                   | partial  | [feedback.md](iteration-10/feedback.md) |
|   11 | 2026-06-16 | Typhoon route — 4 evals, draft vs Claude+skill diff   | pending  | —                                       |
|   12 | 2026-06-16 | Claude+skill arm (kode-thai) for iter-11 compare      | —        | —                                       |
|   13 | 2026-06-16 | Claude+skill arm — personal-essay (eval-4 pair)       | —        | —                                       |
|   14 | 2026-06-16 | Typhoon route — all 5 evals, full compare set         | pending  | —                                       |
|   15 | 2026-07-27 | **Co-generated** Typhoon vs Claude+skill, 5 evals     | pending  | —                                       |

Iteration-15 detail: Typhoon drafted all five (no corpus skips); the Claude arm reached
skill-clean on all five (passes to CLEAN — personal-essay 1, marketing/tech-doc 2,
news/exec-brief 3). Both arms under `EVAL_ITERATION=15`, so every `comparison.md` reads
*co-generated*.

Review: `pending` (untouched by chakrit's ear) · `partial` (some evals verdicted,
rest queued in `docs/human-tasks-queue.md`) · `reviewed` (all evals verdicted) ·
`—` (nothing for the ear to judge — a resume row with no prose, or an arm generated
only to pair against another iteration's).

**Iterations 11–14 are not co-generated.** Each `comparison.md` there pairs a Typhoon
draft against a Claude arm from a different iteration and skill state, so it does not
isolate the drafter. Iteration-15 is the clean pair set; spend the ear there.
