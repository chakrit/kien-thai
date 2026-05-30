# 2026-05-11 — cognitive-vs-affective verbs for quantitative subjects

**Context** — iteration-7 marketing-blurb review (claude/with_skill, L3).
The eval produced:

> เปิดร้านมาหลายปี ลูกค้าก็เข้าเรื่อย ๆ แต่พอปิดบัญชีสิ้นเดือนทีไร ตัวเลข
> ไม่ตรงกับที่รู้สึก

Chakrit flagged it as broken. Claude offered three closure-particle options
for the tail (`+เลย`, `+ทุกครั้ง`, mid-`กลับ`) and proposed picking among
them.

**Call made** — Claude diagnosed the failure as missing tail closure on the
`แต่พอ … ทีไร` construction and treated it as a register-particle selection
problem.

**Verdict** — wrong altitude. The actual error was two layers deeper than
the tail:

1. **Verb-object collocation error**: `ตัวเลข + รู้สึก` is wrong. Numbers
   are cognitive objects, not affective ones. Quantitative subjects
   (`ตัวเลข`, `ยอด`, `ราคา`, `ต้นทุน`) take expectation verbs — `คาด`
   (sharpest, no opinion-bleed), `คิด`, `หวัง`. `รู้สึก` reads as an
   English calque ("doesn't match what I *feel*"), made tempting because
   affective register sounds "warmer" for marketing.
2. **Frame closure**: `ทีไร` does not accept bare endings. It requires a
   per-instance closure on the right clause — `ไม่เคย…สักที`,
   `ไม่เคย…เลย`, `ทุกที` (positive). The three particles Claude offered
   were band-aids on a missing frame; none reconstructed the right paired
   construction.

Correct rewrite: `ตัวเลขไม่เคยตรงกับที่คาดสักที`.

A separate sub-call landed under the same axis: Claude generated `ไม่เคย
ซ้ำสักที` as a candidate for "the numbers never match"; `ซ้ำ` is calque
again (repeat/duplicate ≠ match). The right verb for "numbers match" is
`ตรง` (align). Same shape of error — wrong-register verb reached for under
English collocation pressure.

**Takeaway** —

- When a Thai sentence is flagged broken, audit verb choice and
  verb-object collocation **before** optimizing the tail. The reported
  symptom (truncated closure) was downstream of a deeper lexical error.
- Quantitative/factual subjects in Thai prose take cognitive verbs, not
  affective ones. English freely collapses the distinction; Thai does not.
- `ทีไร` is a paired construction with mandatory per-instance closure on
  the right clause — not a bare-endable adverbial.
- Default-suspect Claude's affective-verb reach when "warmer" register is
  the temptation. Marketing register does not equal affective verbs on
  inanimate objects.

Cross-reference: [`2026-05-10-english-prose-economy-lens.md`](2026-05-10-english-prose-economy-lens.md)
— same family of error (English-lens default overriding Thai semantics).
