# 2026-05-10 — politeness ≠ AI-tell

**Context** — review of chakrit's edits to `CONTRIBUTING.md` (commit pending).
Edits softened tone with `ให้ใช้`, `รบกวนรัน eval ... ให้หน่อยนะครับ`,
`เดี๋ยวทางเรา Run ให้เอง`, explicit `คุณ`, etc.

**Call made** — Claude flagged the softening as "register drift toward
over-polite/service voice — the AI skew this repo warns against." Treated
politeness markers (`รบกวน`, `ให้หน่อยนะครับ`, `เดี๋ยว...ให้`) as evidence of
AI-tell contamination.

**Verdict** — wrong frame. Politeness is the **default register in Thai**, not
an AI skew. ครับ/ค่ะ, ให้, ขอ-, รบกวน, นะ are baseline native usage across
instructional, contributor, and professional prose. The kien-thai skill targets
specific failure modes (mechanical tells, register *mismatch*, calques,
nominalization, padding) — not politeness itself.

**Takeaway** —

- Don't conflate "polite" with "AI-ish." Native Thai prose is polite by
  default; the skew Claude is trained on is *over-formal* and
  *register-mismatched*, not *polite*.
- Before calling something an AI-tell, check `references/ai-tells.md` and
  `references/register.md` for what the skill actually flags. Don't invent
  register categories from Claude's prior.
- Encoded in memory: `user_thai_native.md` — politeness is baseline, not a
  tell.
- The original CONTRIBUTING.md flags that *do* hold: `กฏ`→`กฎ` typos x4,
  90-col rewrap regression, dropped `Stage 4 token-audit` bullet (load-bearing
  per CLAUDE.md).
