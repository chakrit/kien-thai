# Fable-5 baseline probe — eval-1 (rate-limiting explainer), 2026-07-07

One-off probe: how does **Fable 5** write Thai? Single generation pass on eval-1
(`explainer`, rate-limiting / token-bucket vs leaky-bucket), **baseline — no skill
injected, no kode-thai loop**. Raw Fable-5 voice.

- Prompt: eval id `1` in `evals/evals.json`.
- Draft: `workspace/probes/fable5-eval1-baseline.md` (gitignored; corrections below are the
  durable record).
- Comparable to iter-9 / iter-10 `tech-doc-short` (same register + topic).

> **Deferred:** run the **kode-thai loop** on this Fable-5 draft before judging it against
> looped Claude output — the probe skipped the loop, which is why it reads unaudited. Do
> **not** re-run now — Fable quota low (chakrit, 2026-07-07).

## chakrit native corrections (before → after)

chakrit's ear over the raw draft. `after` = chakrit-authored native Thai — valid exemplar
anchors. These are captured as trace; graduate to `references/examples.md` pairs (and
recall-check the calque cluster) only on a focused confirmed pass.

| #  | Before → After                                                                                              | Pattern                                            |
| -- | ----------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| F1 | `...ช่วยควบคุม cost ของ downstream service ที่คิดเงินตาม usage เมื่อ request เกิน limit ระบบมักตอบ HTTP 429 พร้อม header บอกว่าให้รอนานแค่ไหนก่อน retry` → **break up** | run-on; too many ideas chained into one sentence   |
| F2 | `จุดเด่นคือยอมให้เกิด burst ได้` → `จุดเด่นคือระบบจะยอมให้เกิด burst ได้`                                      | dropped subject → restore `ระบบจะ`                  |
| F3 | `ถ้า client เงียบไปพักหนึ่ง token จะสะสมในถัง แล้วจะยิง request รัวๆ ได้ชั่วครู่` → `ถ้า client เงียบไปพักหนึ่ง token จะสะสมอยู่ในถัง แล้วหลังจากผ่านไปสักพัก client จะกลับมายิง request รัวๆ ได้อีก` | over-tight clause join; re-subject `client`; `สะสมใน`→`สะสมอยู่ใน` |
| F4 | `อัตราเฉลี่ยระยะยาวไม่เกิน limit` → `อัตราเฉลี่ยในระยะยาวจะยังอยู่ใน limit`                                    | add `ใน`, aspect `จะยัง`; `ไม่เกิน`→`อยู่ใน`         |
| F5 | `ถ้าถังเต็ม request ใหม่จะถูกทิ้งหรือเข้าคิวรอ` → `ถ้าถังเต็ม request ใหม่จะถูกตัดทิ้งไป หรือต้องเข้าคิวรอ`    | `ทิ้ง`→`ตัดทิ้งไป`; add `ต้อง` + disconnect          |
| F6 | `API ทั่วไปที่ client มีจังหวะใช้งานเป็นช่วงๆ` → `API ทั่วไปที่ client มีจังหวะใช้งานหนักเป็นช่วงๆ`            | add `หนัก`                                          |
| F7 | `เหมาะกับแบบนี้ เพราะ burst สั้นๆ ไม่ควรโดนลงโทษ` → `จะเหมาะกับแบบนี้ เพราะ burst สั้นๆ จะไม่โดนตัดทิ้ง`      | add `จะ`; **`โดนลงโทษ`** = anthropomorphic calque    |
| F8 | `รับ load ไม่สม่ำเสมอไม่ได้` → `รับ load กระชากไม่ได้` *(replacement tentative)*                              | **`ไม่สม่ำเสมอ`** = calque (uneven); fix provisional |
| F9 | `เช่น ต้อง protect database ที่มี capacity ตายตัว` → `เช่น ต้อง protect database ที่มี capacity จำกัด`        | `ตายตัว`→`จำกัด`                                     |
| F10| `หรือส่งงานเข้า third-party API` → `หรือต้องการส่งงานเข้า third-party API`                                     | add `ต้องการ`                                       |

## Triage buckets (for a later confirmed pass)

- **Calque cluster (highest-value negative exemplars):** `ไม่สม่ำเสมอ` (F8, uneven),
  `โดนลงโทษ` (F7, punished), `ตายตัว` (F9, fixed). Recall-check against
  `grammar.md` / `ai-tells.md`.
- **Dropped subject / weak aspect:** F2, F3, F4 — restoring `ระบบจะ` / `client` / `จะยัง`.
- **Run-on chaining:** F1 — feeds the `reads-misstructured` discourse axis and the
  cross-cutting run-on signal (also in iter-9 news ¶4, iter-10 tech-doc line 7).
