# Session checkpoint — 2026-05-30 (docs/ reorg to ace-docs)

Fourth 2026-05-30 session (after exemplar-pivot, issue-1, iter-8/9 review). This one
committed the pivot session's uncommitted WIP, then migrated the repo's durable docs to
the ace-docs three-peer structure.

## What was done

**1. Committed the exemplar-pivot session's WIP** (uncommitted at session start), as three
logical commits:

- `8609634` docs: pivot to exemplar-first, auditor-recall-measured direction
- `ce76753` feat(tests): auditor-recall instrument (-m recall)
- `7788cbe` notes: 2026-05-30 session checkpoints

**2. Reorganized durable docs to ace-docs `docs/{decisions,spec,notes}`** (`06cd64f`):

- `notes/judgements/` + the pivot decision → `docs/decisions/`. Judgements fold in as a
  documented "prose-direction judgement" subtype (entry criteria preserved in
  `docs/decisions/README.md`).
- `tests/REVIEW-PROTOCOL.md` / `tests/INLINE-ITERATION.md` →
  `docs/spec/review-protocol.md` / `docs/spec/inline-iteration.md` (+ `Status:` headers).
- session / chrome / framing / vetting / proposals / feedback notes → `docs/notes/`.
- `notes/work-queue.md` + `notes/research-queue.md` → `docs/`; `HUMAN.md` →
  `docs/human-tasks-queue.md`. Queues sit at `docs/` root as operational backlogs,
  outside the permanence sort.
- 4 ace-docs README templates dropped in (`docs/`, and per-dir). All cross-refs updated
  repo-wide — CLAUDE.md layout tree + a new "Durable artifacts" pointer, corpus, skill
  provenance links, two code comments, and the dated notes/feedback prose. `git mv`
  preserved history.
- Verified: markdown link-checker **0 broken**, `uv run pytest` **21 passed**, wrap clean
  (residual >90 lines are atomic links / tables / URLs).

## What's next

- **Push status:** chakrit pushed the session's work to `gh/main` (now at the reorg
  commit `06cd64f`) — the 12 accumulated commits are up. Only this session-checkpoint
  commit remains local/unpushed; push at next convenience.
- Chakrit-gated items unchanged in `docs/human-tasks-queue.md`: next-agent-step decision
  (Workflow inline-driver prototype vs Phase-3 exemplar expansion), Phase-1 review of
  iter-8/9/10, Thai-content reframe of `README.md` / `CONTRIBUTING.md`, recall-baseline
  green-light (~74 calls), mdfmt school-issue call.

## Open questions

- Push now, or hold for review?
- `README.md` / `CONTRIBUTING.md` carried no structural path refs, so the reorg left them
  untouched; their separate Thai-content reframe to the exemplar-first direction is still
  gated to chakrit.

## Blockers

None.
