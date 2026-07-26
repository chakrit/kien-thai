# Human queue — tasks that need chakrit

Items that require **chakrit specifically** — native ear, Thai authoring, decisions, or
token spend. An agent cannot clear these. This is the human counterpart to
[`work-queue.md`](work-queue.md) (agent-doable committed work). Consult it when
free; the agent adds items as work blocks on you and removes them when you clear them.

- [x] **Decide the next agent step** — DECIDED 2026-07-07: **(A) Workflow inline-driver
  prototype → then (B) Phase 3 exemplar expansion.** Moved to
  [`work-queue.md`](work-queue.md) → "Next agent step".
- [ ] **Phase 1 review** — iter-8 done (2026-06-08); **iter-9 fully reviewed (2026-07-07);
  iter-10 partial** — `tech-doc-short` done, **`marketing-blurb` / `news-feature-bts` /
  `personal-essay-homecoming` / `exec-brief-oss-bi-hana` still pending your ear.** Verdicts
  landed in the feedback files. skill-clean ≠ chakrit-clean; the gap is the measurement.
  → [`spec/review-protocol.md`](spec/review-protocol.md),
  [`../workspace/iteration-9/feedback.md`](../workspace/iteration-9/feedback.md),
  [`../workspace/iteration-10/feedback.md`](../workspace/iteration-10/feedback.md)
- [ ] **Rule on the run-on probe result** (2026-07-26) — the probe answered the recall
  question and raised two calls only you can make: (a) which slug owns run-ons —
  `mid-paragraph-period`, where the auditor already files them, or
  `conceptual-seam-break`, where we assumed; (b) `skill-clean` turned out
  backend-dependent — claude found 4 issues in prose codex terminated as CLEAN, so the
  protocol needs to name the auditing backend or take the union. Also owed: the "after"
  for the iter-10 line-7 break so it can land as a pair.
  → [`scratch/2026-07-26-runon-recall-probe.md`](scratch/2026-07-26-runon-recall-probe.md)
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
- [x] **Rule on the model route vs the exemplar-first premise** — RULED 2026-07-26:
  **revise**, not supersede. Native model is the preferred drafter where reachable
  (it wins on correctness); kien-thai is the audit-and-voice layer; "no escape hatch"
  narrows to voice, which stays unproven until iter-14 is reviewed. no-LLM-judge
  recorded in the same pass.
  → [`decisions/2026-07-26-model-route-revises-exemplar-first.md`](decisions/2026-07-26-model-route-revises-exemplar-first.md),
  [`decisions/2026-07-26-no-llm-judge.md`](decisions/2026-07-26-no-llm-judge.md),
  [`spec/model-route.md`](spec/model-route.md)
- [x] **Resolve the `ด้วย` conflict + pick one connective budget** — RULED 2026-07-26:
  `ด้วย` is not budgeted (closure particle, not formal connective; weird closure means
  rebuild the sentence, not count the token). Budget unit is **per paragraph** over
  ซึ่ง / โดย / ดังนั้น. Applied across SKILL.md, `style-rules.md`, `register.md`; the
  harness density check is relabelled a separate advisory scale.
- [ ] **Act on the AWS-Thailand b2b-formal re-vet** — flagged suspect (likely
  AI-drafted; `คงปฏิเสธไม่ได้ว่า` opener) with downgrade/remove action items, but all
  three `aws-thailand-*` files still sit in `corpus/curated/marketing/b2b-formal/`.
  → [`scratch/source-vetting-2026-05-13.md`](scratch/source-vetting-2026-05-13.md)

- [ ] **Expand `personal-blog` corpus beyond one author** — sweep unblocked 2026-06-16
  (browser extension connected); 2 Vicharn Panich walk-diary entries extracted into
  `corpus/curated/personal-blog/` and eval-4 is now in the comparison set. But the
  category is thin and single-author (elderly-academic diary voice). Add a 2nd author —
  Pantip bylined long-form is the staged target — for register variety, and confirm the
  two extracted entries' voice-notes against your ear (frontmatter `notes:` flagged
  pending). Targets: [`scratch/personal-blog-sweep-2026-06-16.md`](scratch/personal-blog-sweep-2026-06-16.md)
- [ ] **Ear-review the 5 co-generated comparisons** (batch) —
  `workspace/iteration-14/*/comparison.md` (open in iA Writer). The canonical set —
  supersedes the 4-eval iter-11 batch (now includes personal-essay). Each is
  self-contained: Typhoon draft + Claude+skill (kode-thai loop) + signal table. The
  chakrit-clean verdict per arm is the measurement. Highlights for your ear: Claude runs
  longer throughout (marketing 1891 vs 542) with lower connective density; bare Typhoon is
  terser and clean on forbidden phrases this sampling. NOTE Typhoon is stochastic —
  exec-brief had 3 forbidden hits in iter-11, 0 here; single drafts are noisy. eval-4's
  Typhoon draft was few-shot on Vicharn Panich's elderly-diary voice — judge the
  register transfer to a young-homecoming essay. Verdicts → `iteration-14/feedback.md`.

## How this list is maintained

The agent adds an item when work blocks on you, and removes it when you clear it. Keep it
short — if something is agent-doable, it belongs in `work-queue.md`, not here.
