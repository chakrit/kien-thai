# Human queue — tasks that need chakrit

Items that require **chakrit specifically** — native ear, Thai authoring, decisions, or
token spend. An agent cannot clear these. This is the human counterpart to
[`work-queue.md`](work-queue.md) (agent-doable committed work). Consult it when
free; the agent adds items as work blocks on you and removes them when you clear them.

- [ ] **Decide the next agent step** — Workflow inline-driver prototype vs Phase 3
  exemplar expansion (or the order). Direction call.
  → [`notes/session-2026-05-30-exemplar-pivot.md`](notes/session-2026-05-30-exemplar-pivot.md)
- [ ] **Phase 1 review** — **iter-8 done (2026-06-08)**; iter-9 / iter-10 `CLEAN` outputs
  remain. Needs your ear: skill-clean ≠ chakrit-clean, and the gap is the measurement.
  → [`spec/review-protocol.md`](spec/review-protocol.md),
  [`../workspace/iteration-8/feedback.md`](../workspace/iteration-8/feedback.md)
- [ ] **Decide `reads-misstructured` / discourse axis** — iter-8 surfaced a discourse-level
  finding class the sentence-scoped skill + protocol can't hold (② whole-piece restructure,
  ④ inter-sentence cohesion). A per-register macrostructure axis + a protocol verdict flag
  is your call; the corpus-evidence half is queued for the agent.
  → [`research-queue.md`](research-queue.md) → "Discourse / composition axis"
- [ ] **Owe the iter-8 "after" rewrites** — pairs blocked on your Thai before they can
  graduate to exemplars: ③ `กินทุนเงียบ` (opaque coinage, no replacement given); ② `amenity`
  ทับศัพท์ + `พอ`/`ภาษาพูด` register slips + `และ` overuse; ④ flags A/B/C
  (`เหมือนเข้าบ้านเพื่อน…` simile, `ทอนเงิน`, `อะไรที่เรียกไม่ถูก`) marked but not rewritten.
  → [`../workspace/iteration-8/feedback.md`](../workspace/iteration-8/feedback.md)
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
