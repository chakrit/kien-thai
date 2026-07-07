# Iteration 9 — inline codex pristine pass

Originally landed as `iteration-20` (manually picked to avoid a feared collision
with another agent's helper-selected next directory); renumbered to `9` after
the fact since the gap served no purpose.

## Scope

- Backend label: `codex-inline`
- Mode: `inline`
- Evals: all four current evals in `evals/evals.json`
- Configs: `with_skill` and `baseline`
- Audit loop: `with_skill` outputs only, `kode-thai` protocol, converged on
  pass 1 for every eval

## Audit trace

The first reread caught three issues before the saved clean pass. All mapped to
existing rules or ordinary clarity; no durable skill edit needed.

- `marketing-blurb`: `พอปิดบัญชีสิ้นเดือนทีไร ตัวเลขก็ไม่เคยตรง...`
  violated the existing `frame-scoped-ko` rule for `ทีไร` frames. Fixed to
  `พอปิดบัญชีสิ้นเดือนทีไร ตัวเลขไม่เคยตรงกับที่คาดสักที`.
- `tech-doc-short`: `ถ้าเต็มเพดานแล้ว` was semantically ambiguous in the quota
  explanation. Fixed to `ถ้าใช้โควตาหมดแล้ว`.
- `personal-essay-homecoming`: `โรงพยาบาลดี ๆ อยู่ไกลกว่าเดิมเมื่อเทียบกับอายุ
  ของพ่อแม่` made the comparison target unclear. Fixed to `โรงพยาบาลดี ๆ
  ดูไกลขึ้นเมื่อเทียบกับอายุของพ่อแม่ที่เพิ่มขึ้น`.

After those edits, the saved `pass-1-audit.md` files for all with-skill outputs
are `CLEAN`.

## Verification

- Direct blocklist scan over `workspace/iteration-9/*/*/*/output.md`: clean
- `uv run pytest -m evaluate`: 16 passed
- `uv run pytest`: 17 passed

Note: `rtk pytest` reported "No tests collected" for this repo, so verification
used `rtk proxy uv run pytest ...` to keep the command under RTK without the
pytest wrapper altering collection.

## Phase 1 review — chakrit's ear (2026-07-07)

The outer loop: these outputs are all *skill-clean* (the audit above converged to CLEAN).
This section records the *chakrit-clean* verdict — the gap is the measurement. Findings
here are CLEAN-but-flawed unless noted. Classifications (recall-miss vs coverage-gap) are
chakrit-flagged spans + my provisional mapping; confirm before promoting to rules/pairs.

- **tech-doc-short — CLEAN-but-flawed.** Span:
  `คุณอยากคุมความเรียบของ traffic มากกว่าความยืดหยุ่นหรือไม่`. Bad collocation — you don't
  `คุม ความเรียบ` in Thai; reads as an English calque ("control the smoothness of
  traffic"). chakrit rewrite: `คุณต้องการให้ Traffic เสถียรหรือยืดหยุ่นได้แค่ไหน`
  (`เสถียร`/`ความเรียบ` sense-shift judged immaterial here). **Provisional recall-miss**
  against a calque/collocation rule (`grammar.md` calques); if none anchors "verb +
  abstract-noun collocation," flips to coverage-gap → candidate pair.
- **marketing-blurb — chakrit-clean.** Skill-clean = chakrit-clean, no gap.
- **news-feature-bts — CLEAN-but-flawed.** Three findings:
  - ¶4 (`การเปลี่ยนแปลงนี้เกิดพร้อมกับเมืองรอบสถานีที่แพงขึ้น...`): whole paragraph reads
    weird — no single span. ¶1–3 are concrete (people, quotes); ¶4 snaps into an abstract
    gentrification causal-chain (rents→push out shops→live farther→still pay fare), four
    steps packed dense with no human anchor. Mid-piece register/texture break + over-dense
    causal chaining. **Coverage-gap → `reads-misstructured` discourse axis** (human-queue
    item; sentence-scoped skill structurally can't hold it).
  - ¶5: `บริการสาธารณะพื้นฐาน หรือเป็นโครงสร้างพื้นฐาน` — `พื้นฐาน` repeated x2, reads
    confusing/redundant (chakrit inline note `พื้นฐานซ้ำ x2 งง`). Lexical redundancy.
  - ¶6: chakrit flagged but the inline note did not land in the regenerated output;
    **not reconstructed** (no native verdict invented). Provisional-only suspicion: line 24
    is a long run-on internal-monologue sentence — unconfirmed.
- **personal-essay-homecoming — no findings** (advanced without an explicit verdict;
  recorded as passed, not an affirmative chakrit-clean).
