# Human queue — tasks that need chakrit

Items that require **chakrit specifically** — native ear, Thai authoring, decisions, or
token spend. An agent cannot clear these. This is the human counterpart to
[`work-queue.md`](work-queue.md) (agent-doable committed work). Consult it when
free; the agent adds items as work blocks on you and removes them when you clear them.

- [ ] **Decide the next agent step** — Workflow inline-driver prototype vs Phase 3
  exemplar expansion (or the order). Direction call.
  → [`notes/session-2026-05-30-exemplar-pivot.md`](notes/session-2026-05-30-exemplar-pivot.md)
- [ ] **Phase 1 review** — the iter-8/9/10 `CLEAN` outputs. Needs your ear: skill-clean ≠
  chakrit-clean, and the gap is the measurement.
  → [`spec/review-protocol.md`](spec/review-protocol.md)
- [ ] **Reframe the two Thai docs** to the new direction — `README.md` (`หลักคิดของ skill`,
  `วินัยการเพิ่มกฎ`, `Eval ทำงานยังไง`) and `CONTRIBUTING.md` (§1, §5, §6). Thai authoring is
  yours; the agent flags spans but won't write final Thai.
- [ ] **Green-light the full `-m recall` baseline** (~74 claude calls) for the
  before-number. Token spend is your call.
  → [`../tests/test_recall.py`](../tests/test_recall.py)
- [ ] **Decide the `mdfmt` school issue** — whether to file the `<...>`-mangling +
  non-idempotent-wrap bug against the school tracker. School sync is yours.

## How this list is maintained

The agent adds an item when work blocks on you, and removes it when you clear it. Keep it
short — if something is agent-doable, it belongs in `work-queue.md`, not here.
