# Iteration 10 — inline Codex pass

Mode: `inline` (Codex in-session). Backend label: `codex-inline`.

Scope:

- 5 evals from `evals/evals.json`
- `baseline` and `with_skill` for each eval
- `with_skill` outputs audited with the documented inline audit/fix loop
- Artifacts written only under `workspace/iteration-10/`

This is probe material, not cold harness output. Treat it like iteration 8/9:
useful for prose review and rule traces, but not for clean bundle-effect
measurement.

## Results

| Eval                       | Register           | Baseline | with_skill | Passes to CLEAN |
| -------------------------- | ------------------ | -------- | ---------- | --------------: |
| tech-doc-short             | explainer          | written  | written    |               2 |
| marketing-blurb            | marketing-saas-sme | written  | written    |               2 |
| news-feature-bts           | news               | written  | written    |               1 |
| personal-essay-homecoming  | personal-blog      | written  | written    |               1 |
| exec-brief-oss-bi-hana     | explainer          | written  | written    |               2 |

## Audit Issues

### tech-doc-short

Pass 1 caught two issues.

- `verb-calque`: `ถ้า bucket ยังมี token ก็ยิงได้ทันที`
  used `ยิง` for a request passing through a limiter. Fixed to
  `ผ่านได้ทันที`.
- `f4/duai-additive`: the closing pair
  `ถ้าต้องการความยืดหยุ่น เลือก token bucket ถ้าต้องการความนิ่ง...`
  had no bridge or closure beat. Fixed with `ก็` and `ส่วน`.

Pass 2 returned `CLEAN`.

### marketing-blurb

Pass 1 caught two issues.

- `frame-scoped-ko`: `ปิดบัญชีสิ้นเดือนทีไร ตัวเลขก็ไม่เคยหลุด...`
  doubled the linker after `ทีไร`.
- `deixis-continuity`: the final bullet drifted from `คุณ` back to
  unowned `ตัวเลข`. Fixed by tying the benefit back to the reader:
  `คุณไม่ต้องไล่บิลใหม่ทั้งคืน`.

Pass 2 returned `CLEAN`.

### news-feature-bts

Pass 1 returned `CLEAN`.

### personal-essay-homecoming

Pass 1 returned `CLEAN`.

### exec-brief-oss-bi-hana

Pass 1 caught two issues.

- `voice-over-politeness`: opening with `ทำได้ครับ` made the briefing sound like
  a chat reply rather than an executive memo.
- `term-establish-once`: `เข้ามาทำ report` mixed the term bucket after the piece
  had established `reporting` as the process. Fixed to `ทำรายงาน`.

Pass 2 returned `CLEAN`.

## Patterns Worth Review

No issue here requires an immediate skill edit. Every audit hit maps to an
existing rule family.

Two recurring signals are still worth human review:

- `frame-scoped-ko` fired again on a `ทีไร` frame in marketing copy. This matches
  the iteration 8/9 pattern.
- Executive briefing register is still thinly specified inside `explainer`.
  The SAP HANA eval exposed a useful sub-register distinction: concise memo
  tone, no chat-politeness, and stricter term-bucket consistency.

## Verification

- `uv run pytest -m evaluate` — 20 passed
- `uv run pytest` — 20 passed

## Phase 1 review — chakrit's ear (2026-07-07)

Outer-loop *chakrit-clean* verdicts over the skill-clean outputs. **Partial — parked after
#5; marketing-blurb, news-feature-bts, personal-essay-homecoming, exec-brief-oss-bi-hana
still pending chakrit's ear.**

- **tech-doc-short — CLEAN-but-flawed.** Line 7:
  `...service ที่ downstream ไม่รองรับ burst traffic` **‹sentence break›** `ส่ง request เข้า
  bucket ได้...` — run-on; the "what it suits" clause and the "how it works" clause are
  fused, needs a sentence break at chakrit's mark. **Sentence-segmentation** pattern.
- **marketing-blurb — pending.**
- **news-feature-bts — pending.**
- **personal-essay-homecoming — pending.**
- **exec-brief-oss-bi-hana — pending.**

### Cross-cutting signal — run-on / under-segmentation

The strongest emergent finding this session, recurring across backends *and* the
skill-clean layer:

- Fable-5 baseline probe F1 (see `docs/scratch/2026-07-07-fable5-eval1-probe.md`).
- iter-9 news-feature-bts ¶4 (over-dense causal chain).
- iter-10 tech-doc-short line 7 (this finding).

Worth a **recall-check against the sentence-length rule in `ai-tells.md`** — it is not
firing on run-ons that reach the CLEAN state. Overlaps the `reads-misstructured` discourse
axis for the whole-paragraph cases.
