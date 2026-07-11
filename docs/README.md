# docs

Durable artifacts. **File by the gate below** — walk it top to bottom and stop at the first
yes. The bottom (`scratch/`) charges a toll, so nothing lands there by default.

## Where does this go?

1. A ruling you'd defend if someone reopened it? → [`decisions/`](decisions/) — dated,
   never edited.
2. Third-party facts you keep to look up (a framework, an external API/CLI)? →
   [`vendor/`](vendor/) — link-first, mark provenance.
3. A how-to — using the product *or* operating the repo? → [`guides/`](guides/) — script
   repeatable operations; the guide holds the judgment.
4. How our system is built or meant to work, including its own config/CLI surface? →
   [`spec/`](spec/).
5. None of the above — genuinely unsettled exploration → [`scratch/`](scratch/). Open with
   a one-line "not spec/decision because ___."

Each folder's README states its one test precisely. `CLAUDE.md` / `AGENTS.md` points here
as the index.

## Operational queues

Three live backlogs sit at this level, outside the routing gate — they are working state,
not durable artifacts, and get rewritten continuously:

- [`work-queue.md`](work-queue.md) — agent-doable committed work (the question is *how*,
  not *whether*).
- [`research-queue.md`](research-queue.md) — speculative items awaiting evidence.
- [`human-tasks-queue.md`](human-tasks-queue.md) — tasks that need chakrit specifically
  (native ear, Thai authoring, decisions, token spend).

**Task discovery reads all three**, not just `work-queue.md`.
