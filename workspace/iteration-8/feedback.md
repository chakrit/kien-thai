# Iteration 8 — inline run (claude-inline only)

Mode: `inline` (subagent-driven). Bundle source: `tests.lib.kien_thai_bundle`
with register-scoped two-tier (draft → audit). All four `with_skill` configs
generated and looped through `/kode-thai` audit/fix passes until `CLEAN`.
Baseline (no skill) was not generated this run — focus was on
audit-to-convergence per chakrit's overnight brief.

> **Caveat (per `docs/spec/inline-iteration.md`):** outputs are tagged
> `mode: "inline"` and are not cross-iteration comparable to harness output.
> Treat as audit/probe material — judge prose quality, derive rule traces,
> but don't cite for bundle-effect measurement.

## Results

| Eval                       | Register             | Passes to CLEAN | Converged |
| -------------------------- | -------------------- | --------------: | :-------: |
| tech-doc-short             | explainer            |               1 |     ✓     |
| news-feature-bts           | news                 |               1 |     ✓     |
| marketing-blurb            | marketing-saas-sme   |               3 |     ✓     |
| personal-essay-homecoming  | personal-blog        |               3 |     ✓     |

"Passes to CLEAN" = audit-pass index that returned `CLEAN`. 1 = pass-0 draft
audited clean on first look. 3 = two fix cycles required.

## Audit issues that surfaced (for review)

### marketing-blurb

**pass-1** — `frame-scoped-ko` violation.
Frame `ทีไร` already carries the if-then linker, so `ก็` doubles up.

- Before: `พอปิดบัญชีสิ้นเดือนทีไร ตัวเลขก็ไม่เคยตรงกับที่คาดสักที`
- After:  `พอปิดบัญชีสิ้นเดือนทีไร ตัวเลขไม่เคยตรงกับที่คาดสักที`

**pass-2** — `seam-connective-missing` (Result + means/exception variant).
The seam between a result clause and back-to-back means/exception clauses
needs a bridge particle. `โดย` was added once to cover both negated
exceptions (within the `doi-sprawl` per-paragraph cap).

- Before: `...ใช้ได้จริง ไม่ต้องเปิด Excel ไม่ต้องจ้างบัญชี`
- After:  `...ใช้ได้จริง โดยไม่ต้องเปิด Excel ไม่ต้องจ้างบัญชี`

### personal-essay-homecoming

**pass-1** — two hits.

1. `over-hedging` — marketing hedge stack `น่าจะ X อยู่ด้วยซ้ำ` bled into
   personal-blog register, leaving the line ลังเล instead of assertive.
   - Before: `ผมรู้ว่าราคานี้ป้าน่าจะขาดทุนอยู่ด้วยซ้ำ`
   - After:  `ผมรู้ว่าราคานี้ป้าขาดทุนแน่ๆ`
2. `f5` (demonstratives over pronouns) — `มัน` used for inanimate referent
   (a road), where native Thai prefers a demonstrative or drops the pronoun.
   - Before: `ทั้งที่จริงๆ มันคือถนนเดิมที่เดินมาตั้งแต่เด็ก`
   - After:  `ทั้งที่จริงๆ ก็คือถนนเดิมที่เดินมาตั้งแต่เด็ก`

**pass-2** — two hits, both register/style polish.

1. `mai-yamok-spacing` — personal-blog register defaults to *no* space
   before ๆ; the piece was inconsistent (most drops, two keeps). Normalized
   to no-space throughout (`จริงๆ`, `แน่ๆ`).
2. `em-dash-semicolon` (advisory) — two em-dashes used as appositive /
   list-intro rather than parenthetical aside. One replaced with `ทั้ง`
   enumerator, the other dropped to bare whitespace.

## Patterns worth flagging into the iteration-discipline trace

Nothing here surfaces a gap the existing ruleset doesn't already cover —
every audit citation maps to an existing rule slug. Two observations for
chakrit's review:

1. **`frame-scoped-ko` continues to fire on `ทีไร` frames.** This is the
   same family of double-linker errors that earlier iterations also
   surfaced. Worth checking whether the rule's example coverage is strong
   enough or whether it needs a more prominent anchor in `SKILL.md`.

2. **Register bleed into personal-blog.** The marketing hedge stack
   `น่าจะ X อยู่ด้วยซ้ำ` showed up in a personal-blog draft — the bundle
   is register-scoped, so this isn't cross-register contamination from
   prompt; it's the model defaulting to a hedge shape that's specifically
   tagged as marketing-flavored. May indicate `register.md`'s personal-blog
   section needs a counter-example showing assertive closure where AI
   default would hedge.

Both are observations, not proposed rule changes — surfaced here per the
"trace before you write" discipline in `CLAUDE.md`. Decide before editing
the skill.

## What was NOT done

- No `baseline` (no-skill) configs generated — overnight brief was
  audit-to-pristine, not bundle-effect measurement. Run the pytest harness
  with `-m generate` when you need cross-config comparison.
- No `codex-inline` half — only `claude-inline`. Cross-backend signal would
  require codex-driven generation (or running the pytest harness).
- No quant heuristics (`-m evaluate`). Run separately if wanted.

---

# Outer-loop review — chakrit-clean verdicts (2026-06-08)

Per [`docs/spec/review-protocol.md`](../../docs/spec/review-protocol.md). The audit
trace above is the *skill-clean* terminal (kode-thai found nothing). This section is the
*chakrit-clean* terminal — the native ear on the same four outputs. The gap between them
is the measurement.

Reviewed under **1-by-1** discipline. Items ① and ② were marked in a prior session
(verdicts harvested from inline `output.md` edits); ③ and ④ on 2026-06-08. **All four are
skill-clean and all four are chakrit-clean: no.** CLEAN-but-flawed rate = 4/4.

Pairs below are recorded as **candidate exemplars only** — per review-protocol step 6
(collect, do not apply), nothing lands in `references/examples.md` until the exemplar-work
pass. ③'s `กินทุนเงียบ` and ④'s structural finding owe an "after" from chakrit.

## ① tech-doc-short / claude-inline / with_skill · skill_clean: yes (passes_to_clean: 1)

chakrit_clean: no · reads_flat: no · register: explainer

```
findings:
  - span:       "downstream ... ระบบยอมรับ"
    issue:      "ยอมรับ = consent/accept-as-valid; wrong for absorbing load"
    correction: "ระบบรองรับได้"
    class:      recall-miss · slug: verb-calque
  - span:       "ก็ยังพอหายใจไหว ไม่ล้มทั้งกอง"
    issue:      "result clauses in weak order; the strong negation should lead"
    correction: "จะไม่ล้มทั้งกอง ยังพอหายใจไหว"
    class:      coverage-gap · slug: (none; clause-order-for-emphasis)
  - span:       "งานกัน abuse"
    issue:      "informal/wrong nominal for 'preventing abuse'"
    correction: "การป้องกัน abuse"
    class:      coverage-gap · slug: (none; diction)
  - span:       "หน้าต่างเวลานั้น"
    issue:      "'time window' rendered as a literal noun-compound calque"
    correction: "ช่วงเวลาที่กำหนด"
    class:      coverage-gap · slug: (none; noun-compound calque) — STRONGEST exemplar
  - span:       "ตรงนี้แหละที่ algorithm มีให้เลือก"
    issue:      "English cleft ('this is where…') carried into Thai word order"
    correction: "algorithm ตรงนี้มีให้เลือก"
    class:      coverage-gap · slug: (none; cleft calque) — relates topic-comment-fronting
  - span:       "ทนการกระชาก / เปราะ / กันการกระชาก / ในระบบจริงหลายทีมก็ผสม / ที่ขอบเพื่อรับ / แบบสม่ำเสมอ"
    issue:      "diction cluster: nominal-vs-แรง, bare disyllable, register, typo แบบ"
    correction: "ทนแรงกระชาก / เปราะบาง / กันแรงกระชากได้ / ในความเป็นจริงหลายๆ ทีมมักจะผสม /
                 ที่ขอบการรับ / ด้วยอัตราคงที่ (chakrit: drop typo แบบ, prefer ด้วยอัตราคงที่)"
    class:      mixed · recall-miss(bare-adjective: เปราะ→เปราะบาง) + coverage-gap(rest)
```

## ② news-feature-bts / claude-inline / with_skill · skill_clean: yes (passes_to_clean: 1)

chakrit_clean: no · reads_flat: no · register: news · **+ structural verdict flag (Dao)**

```
findings:
  - span:       "(whole piece)"
    issue:      "needs restructuring — no macrostructure slot in protocol/skill"
    correction: (verdict flag, not a span fix) — routes to research item R
    class:      coverage-gap · slug: (none; discourse macrostructure)
  - span:       "amenity (as ทับศัพท์)"
    issue:      "should not be transliterated/kept-Latin here"
    correction: (chakrit's Thai owed)
    class:      recall-miss · slug: style-rules ทับศัพท์ four-bucket guide
  - span:       "พอ / ภาษาพูด register slips"
    issue:      "informal register bleeding into news"
    correction: (chakrit's Thai owed)
    class:      recall-miss · slug: register (news family)
  - span:       "และ (overused)"
    issue:      "and-chaining beyond connective budget"
    correction: (chakrit's Thai owed)
    class:      recall-miss · slug: connective-budget
  - span:       "ตั้งแต่ต้นปี / ปรับโครงสร้างค่าโดยสาร…เข้ามารวมกับสายหลัก / แพงตามอีก"
    issue:      "journalism gaps: year unstated; fare-change conflated with line-merger
                 (ค่าโดยสาร ≠ การรวมสาย); quote lacks context"
    correction: (out of kien-thai prose scope — factual/journalism)
    class:      coverage-gap · slug: (none; out-of-scope journalism) — routes to R
```

## ③ marketing-blurb / claude-inline / with_skill · skill_clean: yes (passes_to_clean: 3)

chakrit_clean: no · reads_flat: no · register: marketing-saas-sme

```
findings:
  - span:       "เมนูไหนกินทุนเงียบ"
    issue:      "opaque AI-coined Thai (NOT a calque). ทุน = capital/cost, not margin.
                 Intended sense 'dishes that quietly eat into cost' does not parse for a
                 native reader."
    correction: (after PENDING chakrit's rewrite)
    class:      coverage-gap · slug: (none; failed-coinage / opaque-metaphor) — AMBIGUOUS,
                could read as craft empty-coinage; confirm at exemplar time
```

Rest of the blurb: chakrit-clean (explicitly confirmed good).

## ④ personal-essay-homecoming / claude-inline / with_skill · skill_clean: yes (passes_to_clean: 3)

chakrit_clean: no · reads_flat: no · register: personal-blog

```
findings:
  - span:       "ที่ยังเหมือนเดิมก็มี"
    issue:      "cohesion error. Two parts: (1) contrast should mirror prior sentence's
                 verb (บ้านเปลี่ยน… → ไม่เปลี่ยน), not switch to เหมือนเดิม; (2) additive ก็มี
                 mis-signals continuation where the move is contrast against a change-
                 statement, with no prior list of like items to append to."
    correction: "ที่ยังเหมือนเดิมไม่เปลี่ยนแปลงก็มี"
    class:      coverage-gap · slug: (none; inter-sentence cohesion) — HEADLINE; feeds R
  - span:       "เหมือนเข้าบ้านเพื่อนที่ย้ายไปอยู่ใหม่"
    issue:      "incoherent simile — AI imagery that doesn't cohere"
    correction: (chakrit flag; no rewrite)
    class:      coverage-gap · slug: (none; incoherent-imagery)
  - span:       "ไม่กล้าทอนเงินคืน"
    issue:      "wrong verb-sense: ทอน is the seller's action; logic inverted (buyer
                 would over-pay, not give change)"
    correction: (chakrit flag; no rewrite)
    class:      coverage-gap · slug: (none; verb-sense/logic)
  - span:       "หรืออะไรที่เรียกไม่ถูก"
    issue:      "empty-profundity filler — textbook AI-essay move"
    correction: (chakrit flag; no rewrite)
    class:      coverage-gap · slug: (none; empty-profundity-closure) — relates craft
  - span:       "ให้ไม่ได้ต่างหาก / ความรู้สึกว่ามีคน / ขากลับขึ้นรถทัวร์ / แค่พยักหน้า แล้วโบกมือ"
    issue:      "diction + dropped subject + cohesion polish"
    correction: "ให้ไม่ได้เหมือนกัน / ความรู้สึกเวลามีคน / ขากลับผมขึ้นรถทัวร์ /
                 แค่พยักหน้าแล้วก็โบกมือ"
    class:      mixed · recall-miss(topic-pronoun-drop: restore ผม) + coverage-gap(rest)
```

## Aggregate — outer-loop dashboard (iter-8)

| Metric                     | Value                                                       |
| -------------------------- | ---------------------------------------------------------- |
| CLEAN-but-flawed rate      | 4/4 (100%) — every skill-clean output red-inked            |
| recall-miss : coverage-gap | ~5 : ~11 — skewed to genuine holes, not auditor blindness  |
| dominant coverage cluster  | **discourse/cohesion** (④ L5, ② structure) + calque diction |
| reads-flat count           | 0 (all had discrete spans; ② carries a structural flag)    |
| recall-miss slugs          | verb-calque, bare-adjective, ทับศัพท์-guide, register-news,  |
|                            | connective-budget, topic-pronoun-drop                      |

**Reading.** Mostly coverage-gaps → genuine ruleset holes, not auditor blindness; per the
protocol, land as pairs first, trace before any rule. The standout is a **discourse-level
cluster** the sentence-scoped ruleset is structurally blind to — ④'s inter-sentence
cohesion-marker error and ②'s whole-piece macrostructure. Both feed research item **R**
(discourse/composition axis). The recall-misses are ordinary single-rule under-fires; no
new rule warranted for them — they want stronger anchors/exemplars, not more rules.

**Ambiguous classifications flagged for chakrit:** ①'s `หน้าต่างเวลา` (noun-compound
calque vs an existing calque slug) and ③'s `กินทุนเงียบ` (coverage-gap vs craft
empty-coinage). Confirm at exemplar-promotion time.

**No cross-iteration plateau tracker exists yet** — the protocol references one (step 7)
but no file backs it. iter-8 is the first outer-loop dashboard; the tracker should be
created when iter-9/10 are reviewed and a trend line is possible. Noted, not scaffolded.
