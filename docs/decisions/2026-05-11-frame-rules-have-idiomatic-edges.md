# 2026-05-11 — frame rules (`ทีไร` / `เมื่อไหร่` / `เสมอ` / `ก็`) have idiomatic edges

**Context** — iteration-7 marketing-blurb review surfaced multiple
construction-level questions around the `ทีไร` family. Claude built three
increasingly-confident hypotheses across the session; each was corrected.

**Calls made** — sequential, all by Claude:

1. *"`ทีไร` requires `ไม่เคย…สักที` closure."* Too narrow — that's the
   negative-frustration variant only.
2. *"`ทีไร` requires per-instance closure (positive or negative).
   `ทุกที` / `ทุกครั้ง` interchangeable. `ก็` redundant. `เสมอ` wrong."*
   Partially right; flat in places.
3. *"`เสมอ` + `ทีไร` works for subject-disposition verbs, fails for
   circumstantial event-states."* Predictions on test rows broke.

**Verdict** — each correction surfaced a different layer:

- **`ทุกที` vs `ทุกครั้ง`**: not synonyms. `ทุกที` stays per-instance
  punctual; `ทุกครั้ง` drifts toward aggregate/stative, sliding into the
  same failure class as `เสมอ`. Safe positive closure for `ทีไร` is
  `ทุกที`; `ทุกครั้ง` is a soft drift.
- **`ก็` is frame-scoped, not blanket-redundant**: redundant with `ทีไร`
  (the frame carries the linker) but **required** as `ก็จะ` with
  `ไม่ว่าจะ…เมื่อไหร่` (universal-quantification needs explicit pivot).
- **`เสมอ` with `ทีไร` is partially idiomatic**, not a clean rule.
  Native judgment: `เจอเขาทีไร เขายิ้มเสมอ` ✓ but
  `ขับรถทีไร รถติดเสมอ` ✗; `โทรหาทีไร สายไม่ว่างเสมอ` ✓ but
  `ขอความช่วยเหลือทีไร เขาใจดีเสมอ` reads as two stranded statements.
  Bounded-vs-independent hypothesis captures some pattern but won't
  predict edges reliably. Chakrit: *"starting to think maybe needs to
  learn idiom-by-idiom in this case."*
- **`ทีไร` ≠ `(ไม่ว่าจะ)…เมื่อไหร่`**: distinct constructions. Per-instance
  if-then vs universal-quantification. English "whenever" maps to both;
  pick by intent.

**Takeaway** —

- Don't formalize Thai frame-pairing rules from a few examples. The spine
  is structural (frames require closure; closure must be per-instance;
  frames choose their own linker). The edges are idiomatic — a tagged
  exemplar collection beats a universal rule that will mispredict.
- Skill-design implication: structural rules go in `grammar.md`; idiomatic
  edges go in `examples.md` as a tagged collection of attested pairings
  with verdicts. Calque traps (English "whenever" / "always" collapsing
  Thai distinctions) belong in `ai-tells.md`.
- When Claude proposes a hypothesis that explains *some* cases, resist
  the urge to confidently extend it. Multiple corrections in one thread
  is a signal that the rule has idiomatic structure the formalization is
  flattening.

Cross-reference: [`2026-05-10-english-prose-economy-lens.md`](2026-05-10-english-prose-economy-lens.md)
— same shape of failure (Claude reaches for universal rules where Thai
operates on attested idiom).
