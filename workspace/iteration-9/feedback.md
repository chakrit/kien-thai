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
