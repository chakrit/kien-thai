# Research queue

Speculative items needing evidence before they can graduate into a rule. Items
here are *questions*, not verdicts. Each entry should name the question, the
hypothesis (if any), the scope of work that would settle it, and where the
finding would land.

> **Direction (2026-05-30):** items here that surface a recurring pattern now land as
> register-tagged before/after *pairs* first (rules only when the pair doesn't transfer),
> and graduate only with the auditor-recall data from the review loop — see
> [`decisions/2026-05-30-exemplar-first-pivot.md`](decisions/2026-05-30-exemplar-first-pivot.md)
> and [`spec/review-protocol.md`](spec/review-protocol.md).

Resolved items are one line each at the bottom, pointing at where the answer landed.
The superseded question text lives in git history, not here.

---

## Discourse / composition axis — macrostructure + inter-sentence cohesion

**Provenance.** iter-8 outer-loop review (2026-06-08), two findings the sentence-scoped
ruleset is structurally blind to. See
[`../workspace/iteration-8/feedback.md`](../workspace/iteration-8/feedback.md) → ② and ④.

**Question (a) — macrostructure.** The skill + review protocol run entirely
sentence-to-paragraph. The frames' "structural" tag means *clause* structure;
`style-rules.md §Structure` caps at single-paragraph. There is no per-register
macrostructure (news arc, essay shape) and no discourse-level finding class — the only
holistic verdict is `reads-flat` (voice). ②'s `news-feature-bts` was chakrit-clean: no on a
**whole-piece restructure** (Dao's flag) that no slot can hold. Does kien-thai need a
per-register macrostructure axis and a `reads-misstructured` verdict flag in the protocol?

**Question (b) — inter-sentence cohesion.** Finer than (a): ④'s `ที่ยังเหมือนเดิมก็มี` was
a connective error *between adjacent sentences* — additive `ก็มี` used where the discourse
move is contrast against the prior sentence's `เปลี่ยน`. Fix mirrored the prior verb
(`ไม่เปลี่ยนแปลง`) to license the marker. No slug covers cross-sentence connective-choice
logic; every connective rule (`connective-budget`, `seam-connective-missing`, `doi-sprawl`)
is within-sentence. Is inter-sentence cohesion a distinct rule class, or does it fold into
the macrostructure axis above?

**Hypothesis.** (a) and (b) are the same axis at two scales — discourse cohesion the skill
has never modeled because generation/audit operate a sentence at a time. Likely a real
coverage hole, but **gate any rule on corpus evidence of native macrostructure per
register** — without attested news-arc / essay-shape patterns this stays speculative.

**Scope to investigate.** Survey `corpus/curated/` per register for macrostructure
signatures (lede/nut-graf in news-feature, turn-structure in personal essay) and for
inter-sentence contrast/continuation marker choice. Tabulate whether native writing has a
consistent shape worth encoding vs being too author-variable to rule.

**Landing place.** Pairs first into `references/examples.md` (the ④ cohesion pair is ready:
`ที่ยังเหมือนเดิมก็มี` → `ที่ยังเหมือนเดิมไม่เปลี่ยนแปลงก็มี`, register `personal-blog`).
Macrostructure → possibly a new `references/structure.md` or a `register.md` per-family
shape note. The `reads-misstructured` **protocol-flag decision is chakrit's** — tracked in
[`human-tasks-queue.md`](human-tasks-queue.md).

---

## Comma-listing as register/formality feature; formality as a missing axis

**Question (a).** Does Thai-prose comma-listing (e.g. `A, B, หรือ C`) track
register, formality, both, or neither? Is it always wrong, always fine, or
context-dependent?

**Question (b).** Is "formality" a missing or replacement axis to the current
5-register taxonomy in `references/register.md`? Right now register is one
flat axis; formality may cut across it (a `personal-blog` post can be casual
or formal independently of the register family).

**Method.** Survey the curated corpus in `corpus/curated/` across families.
Tabulate comma-listing density by family. Tabulate formality cues
independently and check whether they co-vary or are orthogonal to register.

**Landing place.** New dimension in `references/register.md` (feature-by-
register matrix), or a separate formality axis layered on top of the
existing register taxonomy.

---

## Hedge-stack pattern beyond `น่าจะ X อยู่ด้วยซ้ำ`

**Question.** Does the broader multi-particle hedge-stack pattern in
marketing-register body copy generalize beyond the one stack shape now
captured in `over-hedging`?

**Hypothesis.** AI defaults to hedge-stacking in marketing register
because the training data conflates "warmth" with "softening." Native
marketing copy asserts (`กลายเป็นขาดทุน`) and reserves hedging for
disclaimer-adjacent lines, not body-pain-point claims.

**Status so far.** The `น่าจะ X อยู่ด้วยซ้ำ` instance from iter-7
marketing-blurb L4 landed in `ai-tells.md#over-hedging` as the marketing
example. The general "does multi-particle stacking in pain-point copy
generalize?" question is still unanswered.

**Scope to investigate.** Look at iteration-1 through iteration-7
marketing outputs for other instances of multi-particle hedge stacks
(`อาจจะ … คงจะ … น่าจะ …`, `อาจ … อยู่ … บ้าง …`, etc.) in body copy
making a pain-point claim. If the pattern is recurring with different
stack shapes, promote `over-hedging` to a register-aware rule (or split
into a marketing-specific entry in `register.md`).

**Landing place.** Extend `ai-tells.md#over-hedging` with more attested
stack shapes, or new `register.md` marketing entry specifically about
pain-point assertion vs hedging.

---

## Colloquial-emotional verbs leaking into Explainer/News register

**Reframed 2026-05-13** — the original animacy hypothesis was falsified by browser
vetting in
[`scratch/chrome-session-2026-05-13.md`](scratch/chrome-session-2026-05-13.md) §4.
Native Thai *does* apply `ทนรับ` and `เครียด` to system subjects in
gaming/community register (`เซิร์ฟเวอร์ทนรับ … ไม่ไหว`, `เซิร์ฟเวอร์เครียด`, both
attested with substantial Google hits). Do **not** land this as a `grammar.md`
animacy rule.

**Question.** Is the iter-7 `ทนรับ` issue a **register-leakage** pattern: AI mixes
colloquial-emotional verbs (`ทน*` / `เครียด` / `ทรมาน`) into Explainer/News register
where neutral verbs (`รองรับ`, `จัดการ`, `จัดสรร`, `ทนทานต่อ`) are expected? Same
candidate verb list (`ทรมาน`, `เหน็ดเหนื่อย`, `อดทน`, `เครียด`, `สบาย`, `กล้า`, `รู้`) —
but checked for register-restriction, not animacy-restriction.

**Provenance.** Still one instance (iter-7 `downstream ทนรับ burst`; chakrit's rewrite
`downstream รองรับ burst`), but the framing is now register-mismatch, not grammar
violation.

**Scope to investigate.** Look at iter-1 through iter-7 Explainer and News-reference
outputs for colloquial-emotional verbs on system subjects. Cross-check Blognone /
Bangkok Post Tech / `รู้รอบ`-style explainer corpora — these should never use `ทน*` /
`เครียด` on systems; if they do, the pattern is even more relaxed than hypothesized.

**Landing place.** If recurrence appears in iter-8+, add a register-aware entry to
`references/register.md` Register-2 (Explainer) and Register-4 (News): "Avoid
colloquial-emotional verbs on system subjects — use neutral
`รองรับ`/`จัดการ`/`ทนทานต่อ`."

**Draft text ready.** Slug `register-leak-emotional-verb`, full landing-ready section in
[`scratch/proposals-2026-05-13.md`](scratch/proposals-2026-05-13.md) § Proposal A. Drop
in when the gating condition (iter-8+ recurrence, or a retroactive 2nd instance in
iter-1..7 codex/baseline review) is met.

---

## Closer-binding scope reading discipline

**Question.** Where does the "read closure-binding scope before judging
pair-compatibility" discipline belong? It's a review-process rule, not a
prose-content rule.

**Hypothesis.** Belongs in `skills/kien-thai/SKILL.md` review workflow
(applies to both generation-time self-review and audit-pass) rather than
`skills/kode-thai/SKILL.md` (audit-loop only). Generation-time
self-review benefits equally from getting binding scope right before
calling a pair incompatible.

**Provenance so far.** One instance — iteration-7 marketing-blurb L11
variant E reading: Claude misparsed `เมื่อไหร่ + เสมอ` as a direct pair
when `ทันที` had already closed `เมื่อไหร่` and `เสมอ` belonged to a
separate `จะ…เสมอ` frame.

**Scope to investigate.** See whether other audit-pass misreads in
iter-7 outputs (across the un-reviewed remaining 10) involve similar
binding-scope errors. If yes, the discipline lands in the audit-loop
side; if also at generation time, it lands in the kien-thai workflow.

**Landing place.** TBD between `skills/kien-thai/SKILL.md` workflow
section, `skills/kode-thai/SKILL.md` audit pass, or a new checklist
file under `skills/`. Pick after seeing more instances.

---

## Resolved

| Question | Resolution |
| ------------------------------------------- | ------------------------------------------ |
| ๆ-spacing register-scoped? (2026-05-13) | Yes, two-rule shape. `ต่าง ๆ` is spaced near-universally; other reduplications follow register. Landed in `style-rules.md#mai-yamok-spacing`; evidence in [`scratch/chrome-session-2026-05-13.md`](scratch/chrome-session-2026-05-13.md) §3. |
| Vet non-tech personal-blog sources (2026-05-13) | Vetted via browser MCP. Promotions and drops in [`decisions/2026-05-13-register3-source-list-vetting.md`](decisions/2026-05-13-register3-source-list-vetting.md); notes in [`scratch/source-vetting-2026-05-13.md`](scratch/source-vetting-2026-05-13.md). |
| Fictionlog / Tunwalai as a fiction register? (2026-05-13) | Out of scope — genre conventions and an untrained author pool; a Register-6 marking "do not lift from" would be dead scaffolding. Same decision record; evidence in [`scratch/chrome-session-2026-05-13.md`](scratch/chrome-session-2026-05-13.md) §1. |
