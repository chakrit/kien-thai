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
- [ ] **Rule on the model route vs the exemplar-first premise** — the shipped Typhoon
  route (SKILL.md step-0, `skills/kien-thai/scripts/`) reverses the pivot's stated
  premise ("no better-model escape hatch") but lives only in notes; needs a dated
  `docs/decisions/` entry (supersede or revise). Same pass: promote the locked
  no-LLM-judge ruling into `docs/decisions/` — it is cited as authoritative in three
  docs but recorded nowhere in-repo.
  → [`notes/session-2026-06-09-model-route-probe.md`](notes/session-2026-06-09-model-route-probe.md),
  [`decisions/2026-05-30-exemplar-first-pivot.md`](decisions/2026-05-30-exemplar-first-pivot.md)
- [ ] **Resolve the `ด้วย` conflict + pick one connective budget** — `register.md`
  (Marketing common) budgets `ด้วย` as an overused connective while `f4/duai-additive`
  and `dangling-additive-frame` require it to close additive frames; and the connective
  budget is defined five different ways (token sets, per-sentence vs per-paragraph)
  across SKILL.md / `style-rules.md` / `register.md` / `ai-tells.md` / `test_quant.py`.
  Thai rule content — your ruling; the agent applies it afterward.
- [ ] **Act on the AWS-Thailand b2b-formal re-vet** — flagged suspect (likely
  AI-drafted; `คงปฏิเสธไม่ได้ว่า` opener) with downgrade/remove action items, but all
  three `aws-thailand-*` files still sit in `corpus/curated/marketing/b2b-formal/`.
  → [`notes/source-vetting-2026-05-13.md`](notes/source-vetting-2026-05-13.md)

- [ ] **Expand `personal-blog` corpus beyond one author** — sweep unblocked 2026-06-16
  (browser extension connected); 2 Vicharn Panich walk-diary entries extracted into
  `corpus/curated/personal-blog/` and eval-4 is now in the comparison set. But the
  category is thin and single-author (elderly-academic diary voice). Add a 2nd author —
  Pantip bylined long-form is the staged target — for register variety, and confirm the
  two extracted entries' voice-notes against your ear (frontmatter `notes:` flagged
  pending). Targets: [`notes/personal-blog-sweep-2026-06-16.md`](notes/personal-blog-sweep-2026-06-16.md)
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
