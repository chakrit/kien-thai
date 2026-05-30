# 2026-05-11 — person deixis (discourse) outranks tail polish (syntax)

**Context** — iteration-7 marketing-blurb review (claude/with_skill, L4–5).
The eval produced:

> วัตถุดิบขึ้นราคาทุกอาทิตย์ จานเดิมที่เคยกำไรดี ตอนนี้น่าจะขาดทุนอยู่
> ด้วยซ้ำ แต่ไม่มีใครรู้

Chakrit proposed rewriting the tail clause `แต่ไม่มีใครรู้` to
`โดยไม่รู้ตัว`. Claude characterized this as "afterthought → modifier" — a
syntactic-weight observation.

**Call made** — Claude framed the fix at the syntax level (loose tail
clause becomes prepositional modifier).

**Verdict** — the framing missed the actual rule. Chakrit reframed at
discourse level: lines 1–6 of the copy run in **implicit-2nd-person /
zero-deixis mode** — addressing the shop-owner without explicit pronoun
(`คุณ` only appears at L7). Inserting `ใคร` ("no one") drops a
third-party indefinite reference into an implicit-2nd-person passage,
breaking deixis continuity mid-paragraph. The reader briefly has to ask
"wait, who's the *someone* now?" The fix `โดยไม่รู้ตัว` keeps the frame
implicit-2nd-person (*you* don't realize).

The syntactic observation is real but secondary. The generalizable rule
is at discourse level:

> Person deixis must stay consistent within a stretch of prose. AI tends
> to slip an indefinite-someone (`ใคร`, `คน`, `ใครๆ`) into passages
> running in implicit-2nd-person mode, because English freely
> interpolates "no one" / "someone" without breaking address. Thai
> readers track person deixis tighter — the slip reads as a fragment
> with a missing subject.

**Takeaway** —

- Default scan altitude for Thai prose review is discourse-level (person
  deixis, register, frame continuity) **first**, syntax-level (tail
  shape, particle placement) **second**. The syntactic fix is often a
  surface of a deeper discourse violation; naming the discourse violation
  produces a generalizable rule, naming the syntactic fix produces only
  a polish.
- Existing skill already has Person deixis sections in `SKILL.md` and
  `references/register.md` covering *which* deixis to pick per register.
  Missing piece is *continuity* — once a deixis is established (including
  zero/implicit), the rest of the passage must hold it. Indefinite-someone
  references (`ใคร`, `คน`, `ใครๆ`) are particularly prone to breaking
  the frame.
- This is the same shape as the existing English-prose-economy-lens
  judgement: Claude defaults to English-trained syntactic intuition; the
  correct frame is Thai-discourse semantics.

Cross-reference: [`2026-05-10-english-prose-economy-lens.md`](2026-05-10-english-prose-economy-lens.md),
[`2026-05-10-politeness-not-ai-tell.md`](2026-05-10-politeness-not-ai-tell.md).
