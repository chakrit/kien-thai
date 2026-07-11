<!-- not spec/decision because: session resume breadcrumb, not a ruling -->
# 2026-07-11 — session checkpoint: docs restructure to ace-docs layout

## Done (landed + pushed, `6c247e4`)

Re-ran `/ace-init` + `/ace-docs`; migrated `docs/` to the ace-docs single-gate layout.

- `docs/notes/` → `docs/scratch/` (15 files, `git mv`, history preserved). Impermanent
  == residual/disposable, exact semantic match.
- Added `docs/guides/` + `docs/vendor/` signposts (both empty — no content today;
  vendor will sit empty until a first third-party crib lands).
- `decisions/` and `spec/` unchanged. Three queues (`work-`, `research-`,
  `human-tasks-queue.md`) stay at `docs/` root, outside the routing gate.
- `docs/README.md` rewritten to the single gate + operational-queues section.
- CLAUDE.md: layout tree + Durable-artifacts para rewritten to the gate; **skills-list
  fixed** — `markdown-writing` / `skill-creator` / `shell` no longer ship from the
  school (their doctrines are inlined), list now matches `ace skills`.
- Reference sweep `docs/notes` → `docs/scratch` across CLAUDE.md, corpus/README, the
  exemplar-pivot ADR, kien-thai references, `tests/lib.py`, workspace feedback, and
  moved-file cross-refs. The frozen 2026-05-30 reorg record was left as-is (rewriting
  its paths would falsify the event it narrates).
- `test_skill_consistency` + `test_sanity` green (17 passed).

## Dropped

Built an ace-docs `www/` review site, then removed it at chakrit's call — not enough
info to warrant it. No `www/`, no `scripts/docs-site-deploy.sh` in the tree.

## Open / next

Nothing pending from this session — tree clean, pushed. Substantive work resumes at the
pre-existing next step from `6c247e4`'s predecessor (`94f86d2`): (A) Workflow
inline-driver → (B) exemplar expansion. See `docs/work-queue.md` +
`docs/human-tasks-queue.md`.

No school-bound edits: the kien-thai reference sweeps are path-ref updates to the
artifact this repo owns (school re-imports from here), not school-skill changes.
