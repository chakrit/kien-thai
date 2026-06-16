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
|    9 | 2026-05-22 | Inline (codex), 4 evals × 2 configs, converged pass 1 | pending  | [feedback.md](iteration-9/feedback.md)  |
|   10 | 2026-05-30 | Inline (codex), 5 evals × 2 configs                   | pending  | [feedback.md](iteration-10/feedback.md) |
|   11 | 2026-06-16 | Typhoon route — 4 evals, draft vs Claude+skill diff   | pending  | —                                       |
|   12 | 2026-06-16 | Claude+skill arm (kode-thai) for iter-11 compare      | —        | —                                       |
|   13 | 2026-06-16 | Claude+skill arm — personal-essay (eval-4 pair)       | —        | —                                       |
|   14 | 2026-06-16 | Typhoon route — all 5 evals, full compare set         | pending  | —                                       |
