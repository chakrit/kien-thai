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
  `personal-essay-homecoming` / `exec-brief-oss-bi-hana` still pending your ear.**
  Verdicts landed in the feedback files. skill-clean ≠ chakrit-clean; the gap is the
  measurement.
  → [`spec/review-protocol.md`](spec/review-protocol.md),
  [`../workspace/iteration-9/feedback.md`](../workspace/iteration-9/feedback.md),
  [`../workspace/iteration-10/feedback.md`](../workspace/iteration-10/feedback.md)
- [ ] **Verify the Thai authority candidates** — two vendor cribs are staged from
  training-data recall and are **unverified**; nothing in them is provenance until a
  title resolves to a real catalogue record. Highest value first: `หลักภาษาไทย`
  (กำชัย ทองหล่อ) and Iwasaki & Ingkaphirom. The Typhoon-generated list is separately
  flagged as likely confabulated. `WebFetch` is blocked on Thai sites — browser MCP.
  → [`vendor/thai-orthography-standards.md`](vendor/thai-orthography-standards.md),
  [`vendor/thai-reference-grammars.md`](vendor/thai-reference-grammars.md),
  [`scratch/2026-07-26-thai-authority-candidates.md`](scratch/2026-07-26-thai-authority-candidates.md)
- [ ] **Rule on the run-on probe result** (2026-07-26) — the probe answered the recall
  question and raised two calls only you can make: (a) which slug owns run-ons —
  `mid-paragraph-period`, where the auditor already files them, or
  `conceptual-seam-break`, where we assumed; (b) `skill-clean` turned out
  backend-dependent — claude found 4 issues in prose codex terminated as CLEAN, so the
  protocol needs to name the auditing backend or take the union. Also owed: the "after"
  for the iter-10 line-7 break so it can land as a pair.
  → [`scratch/2026-07-26-runon-recall-probe.md`](scratch/2026-07-26-runon-recall-probe.md)
- [ ] **Decide `reads-misstructured` / discourse axis** — iter-8 surfaced a
  discourse-level finding class the sentence-scoped skill + protocol can't hold
  (② whole-piece restructure, ④ inter-sentence cohesion). A per-register macrostructure
  axis + a protocol verdict flag is your call; the corpus-evidence half is queued for
  the agent.
  → [`research-queue.md`](research-queue.md) → "Discourse / composition axis"
- [ ] **Owe the iter-8 "after" rewrites** — pairs blocked on your Thai before they can
  graduate to exemplars: ③ `กินทุนเงียบ` (opaque coinage, no replacement given); ② `amenity`
  ทับศัพท์ + `พอ`/`ภาษาพูด` register slips + `และ` overuse; ④ flags A/B/C
  (`เหมือนเข้าบ้านเพื่อน…` simile, `ทอนเงิน`, `อะไรที่เรียกไม่ถูก`) marked but not rewritten.
  → [`../workspace/iteration-8/feedback.md`](../workspace/iteration-8/feedback.md)
- [ ] **Ratify the Thai written for you on 2026-07-27** — you told the agent to fix
  everything rather than flag it, so the factual drift in the two Thai docs was closed:
  `README.md` gained the Typhoon arm, the `recall` marker, the `EVAL_ITERATION` pin, and
  a rewritten `สถานะ`; `CONTRIBUTING.md` §5 gained the pin note. Drafted through
  `opencode run -m ace-sakana/fugu` against the surrounding voice, **not** hand-written by
  Claude and **not** passed through kien-thai. It is unratified Thai in the repo's public
  front door until your ear clears it. The directional reframe of `หลักคิดของ skill` /
  `วินัยการเพิ่มกฎ` / §1 / §6 is still yours and still open.
- [ ] **Green-light the full `-m recall` baseline** (~74 claude calls) for the
  before-number. Token spend is your call.
  → [`../tests/test_recall.py`](../tests/test_recall.py)
- [ ] **Decide the `mdfmt` school issue** — whether to file the `<...>`-mangling +
  non-idempotent-wrap bug against the school tracker. School sync is yours.
- [x] **Rule on the model route vs the exemplar-first premise** — RULED 2026-07-26:
  **revise**, not supersede. Native model is the preferred drafter where reachable
  (it wins on correctness); kien-thai is the audit-and-voice layer; "no escape hatch"
  narrows to voice, which stays unproven until the comparison set is reviewed — that
  set is now **iteration-15**, not the contaminated iter-14. no-LLM-judge
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
  pending). Targets:
  [`scratch/personal-blog-sweep-2026-06-16.md`](scratch/personal-blog-sweep-2026-06-16.md)
  - [ ] **Ear-review the 5 co-generated comparisons** —
  `workspace/iteration-15/*/comparison.md` (open in iA Writer, one at a time). **This is
  the clean set**, generated 2026-07-27: both arms in one iteration at one commit under
  one skill state, so the pair isolates the drafter. It supersedes the iter-11/14 batches,
  which every `comparison.md` there declares NOT co-generated — do not spend the ear on
  those. Each file is self-contained: Typhoon draft + Claude+skill (kode-thai loop) +
  advisory signal table. **The chakrit-clean verdict per arm is the measurement**, and it
  settles the open question in [`spec/model-route.md`](spec/model-route.md) §Open —
  whether the native drafter wins on voice, or at all. Two standing cautions: Typhoon is
  stochastic, so a single draft is noisy (exec-brief had 3 forbidden hits in iter-11, 0 in
  iter-14); and eval-4's Typhoon draft is few-shot on Vicharn Panich's elderly-diary
  voice, so judge the register transfer to a young-homecoming essay. Verdicts →
  `iteration-15/feedback.md`, then flip the INDEX row.

## How this list is maintained

The agent adds an item when work blocks on you, and removes it when you clear it. Keep it
short — if something is agent-doable, it belongs in `work-queue.md`, not here.
