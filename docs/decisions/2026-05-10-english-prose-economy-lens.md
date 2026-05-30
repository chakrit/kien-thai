# 2026-05-10 — English-prose-economy lens fails on Thai register/aspect markers

**Context** — review of chakrit's edits to `CONTRIBUTING.md`. Several markers
in chakrit's revision read to Claude as filler / verbosity / redundant
nominalization, and were flagged for cutting.

**Call made** — Claude flagged four markers as filler:

- `จะ` in `อยากจะช่วย` (L1) — read as redundant future marker.
- `จะ` in `ก่อนจะเพิ่ม` (L29) — same.
- `ให้` in `ให้ใช้ template` (L36) — read as unneeded directive padding.
- `ลำดับ` in `ลำดับชั้น` (L42) — read as nominalization padding over plain
  `ชั้น`.

The implicit framing was Strunk-and-White English-prose minimalism: cut
words that "don't add meaning."

**Verdict** — every one was load-bearing.

- `จะ` carries aspect/intentionality. Without it the sentence reads flat or
  outright ห้วน (robot-speak). `อยากช่วย` is not a tighter `อยากจะช่วย`; it
  is a different, blunter register.
- `ให้` carries directive register — `ให้ใช้ template` is the polite-
  instructional form. Drop it and the sentence shifts into command voice.
- `ลำดับ` softens ห้วน on its own; `ชั้น` standalone reads abrupt and
  technical in this context.

The shared error: Claude is reading Thai through an English-prose-economy
lens. Thai sentences don't pay rent for these particles the way English
sentences pay rent for adverbs and modal verbs — these markers are doing
register/aspect/grammatical work, not occupying space.

Cross-reference: [`2026-05-10-politeness-not-ai-tell.md`](2026-05-10-politeness-not-ai-tell.md)
— same family of error (Claude treats native Thai register cues as
contamination/padding).

**Takeaway** —

- When an edit *adds* particles or markers that read like filler under an
  English-prose lens, **default-suspect Claude's own reflex** before
  flagging. Check first whether the marker is doing register, aspect, or
  grammatical work that the Thai sentence requires.
- "Tighter" in English ≠ "tighter" in Thai. Removing `จะ`/`ให้`/`ลำดับ`
  often produces ห้วน, not concise.
- This is a sibling failure to the politeness-as-AI-tell error. Both come
  from importing English defaults onto Thai.
