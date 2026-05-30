# docs

Durable artifacts about the project, sorted by **permanence** — the three
sub-dirs differ in how long their claims should be considered current.

- [`notes/`](notes/) — **impermanent.** Research, surveys, drafts,
  transcripts, exploratory write-ups. *What we explored.* Today's notes
  may be obsolete next week.
- [`decisions/`](decisions/) — **point-in-time.** Rulings made on a
  specific date for a specific question. *What we decided.* Frozen at the
  moment of decision; later reversals are new decisions that supersede.
- [`spec/`](spec/) — **current understanding.** Forward-looking design
  specs, RFCs, interface contracts. *What we intend to build.* Updated in
  place as understanding evolves; reflects the present, not history.

Default for "this might be useful later" is `notes/`. Move to `decisions/`
or `spec/` only when it actually fits one of those shapes.

## Operational queues

Three live backlogs sit at this level, outside the permanence sort — they are
working state, not durable artifacts, and get rewritten continuously:

- [`work-queue.md`](work-queue.md) — agent-doable committed work (the
  question is *how*, not *whether*).
- [`research-queue.md`](research-queue.md) — speculative items awaiting
  evidence.
- [`human-tasks-queue.md`](human-tasks-queue.md) — tasks that need chakrit
  specifically (native ear, Thai authoring, decisions, token spend).
