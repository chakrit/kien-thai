# Iteration 7 — feedback and rule-candidate trace

Iteration 7 produced 12 outputs (3 evals × 2 backends × 2 configs) under
the same skill bundle as iteration-6 — no skill edits between iter-6 and
iter-7. The intent was to capture `news-feature-bts` (new register) for
the first time and a fresh comparison set on the other two evals.

Harness note: `pytest -m generate -n 4` split the 12 outputs across
`iteration-7/` and `iteration-8/` (6 each) because `iteration_dir` is a
session-scoped fixture and xdist gives each worker its own session.
Manually consolidated post-run. Bug logged in `docs/work-queue.md`.

Review status: only `tech-doc-short/claude/with_skill` and
`marketing-blurb/claude/with_skill` reviewed in this session. The other
ten outputs (codex backends, baselines, news-feature-bts both backends)
remain unreviewed and are candidates for a follow-up pass.

## Patterns observed

### tech-doc-short (claude/with_skill)

- **Personification verb on system subject** — `downstream ทนรับ burst
  ได้แค่ไหน`. `ทน` (endure) requires an animate subject; `downstream` is
  not human. Native fix: `downstream รองรับ burst ได้แค่ไหน`. `ทน` reads
  organic on humans, wrong on systems.
- **Idiom mis-selection** — `Leaky bucket มองกลับด้าน` ("the other way
  around"). Native preference: `มองกลับกัน` (more idiomatic Thai for
  "viewed inversely / mirrored"). Borderline — may be lexical preference
  rather than rule.

### marketing-blurb (claude/with_skill)

- **Cognitive-vs-affective verb collocation** — `ตัวเลขไม่ตรงกับที่
  รู้สึก`. Quantitative subject + affective verb = wrong register. Fix:
  `ตัวเลขไม่เคยตรงกับที่คาดสักที` (cognitive verb + per-instance closure
  for `ทีไร` frame). Two errors stacked: verb choice + missing frame
  closure.
- **`ทีไร` frame closure missing** — bare `แต่พอ … ทีไร X` endings do
  not parse as complete. Frame requires per-instance closure on the
  right clause: `ทุกที` (positive, safest), `ไม่เคย…สักที` / `…เลย`
  (negative). `ทุกครั้ง` is a soft drift toward `เสมอ`-class.
- **Person-deixis discontinuity** — `แต่ไม่มีใครรู้` introduced
  third-party `ใคร` into an implicit-2nd-person passage (lines 1–6 run
  zero-deixis; `คุณ` only appears at L7). Native fix: `โดยไม่รู้ตัว`
  keeps the implicit-2nd-person frame intact.
- **Hedge-stack collapse needed** — `น่าจะขาดทุนอยู่ด้วยซ้ำ`
  (modal + progressive + emphatic stack) reads timid. Marketing register
  wants assertion: `กลายเป็นขาดทุน`. AI default in marketing is to pile
  hedges; native voice asserts.
- **Loose afterthought tail → modifier** — same line, `แต่ไม่มีใครรู้`
  promoted to `โดยไม่รู้ตัว`. Surface restructure; the underlying rule is
  person-deixis continuity (above).
- **`มา` insertion for intentional come-and-do** — `นั่งคิด` →
  `มานั่งคิด`. The `มา` adds a temporal/intentional shading absent in
  the bare form. May be a recurring marketing-register polish move or a
  one-off — needs more examples.
- **Constitutive-vs-causal `ก็` mis-placement** — `ราคาวัตถุดิบขยับ
  เมื่อไหร่ ต้นทุนต่อจาน**ก็**ขยับตาม`. `ก็` marks consequence in causal
  pairs (rain→wet). Fails here because cost↔ingredient-prices is a
  *constitutive* relationship — cost *is* ingredient prices summed, not
  *caused by* them. Native rewrite drops `ก็`:
  `ต้นทุนต่อจานขยับตามทันที`, with `ทันที` closing the `เมื่อไหร่`
  frame. The third clause `คุณจะเห็นกำไรที่แท้จริงของเมนูเสมอ` is a
  separate future-promise frame with its own `จะ…เสมอ` binding.
- **Marketing-promise structure** — `กำไรที่แท้จริง…เสมอ` carries the
  actual value-prop (truth-guarantee), not the speed (`ทันที`). Adjective
  intensification + universal-aspect is the natural shape for the
  promise. AI tends to lead with the feature; native marketing leads
  with the universal guarantee.

## Rule candidates surfaced

Tracking each candidate's provenance, formulation, landing target, and
confidence. Some need corpus evidence before encoding.

| Candidate                                                | Provenance                          | Landing                              | Confidence       |
| -------------------------------------------------------- | ----------------------------------- | ------------------------------------ | ---------------- |
| R-a: quantitative subjects take cognitive verbs (`คาด`/`คิด`/`หวัง`), not affective (`รู้สึก`); `ตรง` not `ซ้ำ` for match | marketing-blurb L3 + dashboard ex.  | `grammar.md` collocations slot       | High — clean trace |
| R-b spine: `ทีไร` requires per-instance closure on right clause; safest closures `ทุกที`, `ไม่เคย…สักที / เลย` | marketing-blurb L3 + extended thread | `grammar.md` paired-constructions    | High             |
| R-b idiomatic edges: `เสมอ` + `ทีไร` partially attested; bounded-to-trigger hypothesis captures *some* cases | extended thread, four test rows     | `examples.md` tagged collection      | Low — idiomatic  |
| R-b linker: `ก็` redundant with `ทีไร`; `ก็จะ` required with `ไม่ว่าจะ…เมื่อไหร่` (frame-scoped) | extended thread                     | `grammar.md` paired-constructions    | High             |
| `ทีไร` ≠ `(ไม่ว่าจะ)…เมื่อไหร่`: distinct frames, English "whenever" trap | extended thread                     | `ai-tells.md` calque-trap entry      | High             |
| Person-deixis continuity: once deixis (incl. zero/implicit) is established, holds across the passage | marketing-blurb L4–5                | `register.md` person-deixis section  | High             |
| Hedge-stack collapse in marketing register: `น่าจะ X อยู่ด้วยซ้ำ` → `กลายเป็น X` | marketing-blurb L4                  | `register.md` marketing-saas-sme     | Medium — one example |
| Constitutive-vs-causal `ก็` placement: causal pairs only; constitutive pairs use bare or `จะ` | marketing-blurb L11                 | `grammar.md` linker rules            | Medium — one example |
| Personification verbs on system subjects: `ทน` requires animate subject | tech-doc-short                      | `grammar.md` or `ai-tells.md`        | Medium — one example, may generalize |
| Marketing promise structure: adjective intensification + universal aspect carries the value-prop | marketing-blurb L11                 | `register.md` marketing-saas-sme     | Low — needs more examples |
| Closer-binding scope discipline (process note, not prose rule) | extended thread, variant E read     | `SKILL.md` review workflow or `kode-thai/SKILL.md` | Process |

## Trace per CLAUDE.md iteration discipline

For each pattern, check existing rules before adding new ones.

| Pattern                                | Existing rule                          | Status                               | Action                                                          |
| -------------------------------------- | -------------------------------------- | ------------------------------------ | --------------------------------------------------------------- |
| Wrong verb-object collocation (ตัวเลข + รู้สึก) | None directly                         | New gap                              | Propose `grammar.md` collocations slot covering quantitative-subject + verb constraints |
| `ทีไร` frame requires closure          | None directly                          | New gap                              | Propose `grammar.md` paired-constructions section; structural rule only |
| `ทีไร` + `เสมอ` edge cases             | None                                   | Idiomatic — resist universal rule    | Propose `examples.md` tagged collection of attested pairings    |
| `ก็` frame-scoped (`ทีไร` vs `ไม่ว่าจะ…เมื่อไหร่`) | None                              | New gap                              | Propose `grammar.md` linker rule with both frames               |
| English "whenever" calque (`ทีไร` vs `เมื่อไหร่`) | `ai-tells.md` covers some calques    | Adjacent; not specific               | Propose `ai-tells.md` entry for this specific mapping           |
| Person-deixis discontinuity            | `SKILL.md` + `register.md` cover which deixis, not continuity | Continuity gap | Propose addition to `register.md` person-deixis section         |
| Hedge-stack in marketing               | `register.md` marketing covers tone, not hedge collapse | Not directly covered | Defer until 2+ examples (one-instance evidence)              |
| Constitutive `ก็` mis-placement        | None                                   | New gap                              | Defer until 2+ examples                                         |
| Personification verbs on systems       | None                                   | New gap                              | Defer until 2+ examples                                         |
| Marketing promise structure (adj-intensification + universal aspect) | None                | New gap                              | Defer until 2+ examples                                         |

## Judgements logged

Three judgements from this session, in `docs/decisions/`:

- [`2026-05-11-cognitive-vs-affective-verbs.md`](../../docs/decisions/2026-05-11-cognitive-vs-affective-verbs.md)
- [`2026-05-11-frame-rules-have-idiomatic-edges.md`](../../docs/decisions/2026-05-11-frame-rules-have-idiomatic-edges.md)
- [`2026-05-11-person-deixis-discourse-over-syntax.md`](../../docs/decisions/2026-05-11-person-deixis-discourse-over-syntax.md)

A fourth call (Claude treating workspace outputs as editable artifacts) was
diagnosed as a context defect rather than a prose-judgement override —
the fix is in project `CLAUDE.md` (Iteration discipline → "Workspace
outputs are evidence, not artifacts"), not a retrospective judgement.

## Followups

- Review the remaining 10 outputs (codex backends, baselines, news-feature-bts
  both backends) — un-reviewed in iter-7 session.
- Resolve the xdist iteration-dir split before the next `-n N` generation
  run (see `docs/work-queue.md`).

## Done

- Rule candidates marked "Action: Propose" — landed in `grammar.md`
  (`quant-subject-cog-verb`, `tirai-frame-closure`, `frame-scoped-ko`),
  `ai-tells.md` (`whenever-calque`), `register.md` (deixis-continuity
  block).
- L3, L4–5, L11 before/after pairs lifted into `references/examples.md`
  as Examples 6–8 (register-tagged marketing-saas-sme).

## Out-of-band edit (2026-05-22) — `empty-intensifier` recalibration

Spot-check of `craft.md::empty-intensifier` Bad list against `corpus/`. Findings:

- `อย่างมาก` traces to Somkiat tech-writing
  (`corpus/raw/tech-writing/somkiat-architect-ivory-tower.md:51`,
  `somkiat-tech-radar-34.md:50`) — native, not an AI tell.
- `อย่างมีประสิทธิภาพ` traces across vetted marketing/b2b-formal corpus: AWS
  Thailand (`aws-thailand-spip-security.md`, `aws-thailand-agentcore.md`),
  Wisesight (`wisesight-homepage.md`), Bluebik (`bluebik-homepage.md` ×2),
  SCB (`scb-just4u-ai.md`). Register convention in b2b-formal/fintech-warm.

Edits to `craft.md`:
- Scope changed `all-registers → scoped`.
- Bad list narrowed to genuinely overheated forms
  (`อย่างมหาศาล / น่าทึ่ง / ไม่น่าเชื่อ`).
- Added "Not on the Bad list" subsection with corpus-traced exceptions.

Origin: out-of-band review, not tied to a specific iter-7 output. Lumping-by-
association was the failure mode — the rule grouped overheated calques with
forms that have native trace. Logged here so the trace survives.

## Out-of-band edit (2026-05-22) — `positive-capability-framing` rewrite

Spot-check of `craft.md::positive-capability-framing` exposed three issues:

1. **Thin corpus trace.** `ก็ต่อเมื่อ` × 1 in corpus, in *translation*
   register only (`corpus/curated/translation/salforest-sme-sustainability.md`
   :29). The rule asserted it as "the natural Thai 'only-when' pivot" with
   definite-article confidence; one translation-register hit doesn't earn that.

2. **Semantic shift in the prescribed Good form.** Probe-generation pair
   (booking + payment): native correction surfaced that `จะ X ได้ก็ต่อเมื่อ Y`
   reads as *permission* (system is permitted to X once Y), not *automatic
   execution* (system X-es automatically once Y). For most system-spec
   sentences the intent is auto-execution, so the rule's "Good" form changes
   the spec's meaning rather than just its style.

3. **Misidentified Bad pattern.** The earlier claim that `ต้อง Y ก่อน X ได้`
   reads as English-projection enforcement chain was wrong — that sequencing
   chain is native standard Thai. The actually-bad part of the original Bad
   example is `บังคับ` on an inanimate system subject (animacy issue,
   mechanical), not the temporal chain. Also surfaced: `ถึงจะ` is the native
   "only-then" pivot in operational register (`เมื่อ Y แล้ว X ถึงจะ Z ได้`),
   missing from the rule entirely.

Edits to `craft.md`:
- Scope changed `all-registers → scoped`; added `provisional` tag.
- Rule split into (a) `บังคับ`-animacy issue and (b) sequencing-pivot choice.
- `ถึงจะ` added as primary operational pivot; `ก็ต่อเมื่อ` demoted to
  formal/policy register.
- Semantic caveat added warning against mechanical `ก็ต่อเมื่อ + ได้`
  substitution.
- Provisional note citing corpus gap.

Corpus gap (no curated operational/system-spec material) logged in
`docs/scratch/source-vetting-2026-05-13.md` with candidate source directions.

Method note: native-checked one of the Good forms by probe-generating
candidate pairs and getting per-item correction. Pair-4 form
`เมื่อยืนยันตัวตนผ่านแล้ว บัญชีถึงจะถอนเงินได้` is the validated example;
the other examples in the rewritten rule are derived from the same pattern
and remain candidate.

## Out-of-band edit (2026-05-22) — `forbidden-phrases.md` corpus pass

Audited blocklist against corpus. Findings:

- **`ทำการ`** — 14 corpus hits, dominantly Somkiat tech-writing. Used as
  dummy verb hosting English-borrowed verbs (`ทำการ run`, `ทำการ capture`,
  `ทำการ balance`, `ทำการอธิบาย`, `ทำการตรวจสอบ`, `ทำการปรับปรุง`,
  `ทำการวางแผน`). Native tech-writing pattern for English-term integration,
  not padding. **Removed from blocklist.**
- **`อย่างมีประสิทธิภาพ` / `อย่างมาก`** — already established native in
  b2b-formal/tech-writing per the empty-intensifier edit above. **Removed
  from blocklist** for consistency. `อย่างมหาศาล` retained (clean AI-tell).
- **`การที่`** (16 bare hits) — native in newspaper-feature
  (`การที่เมืองสมัยใหม่...` in the101). Blocklist entry is the specific
  `การที่...นั้น` heavy-nominalizer combo, not bare `การที่`. No change.
- **`ปฏิเสธไม่ได้ว่า`** (4 hits, 2 unique files: Salforest translation +
  AWS Thailand b2b-formal). Thin native trace — keeping on blocklist; two
  unique files is too sparse to override a clean AI-tell. See corpus-
  quality concern below.
- **`ในยุคปัจจุบัน` / `เป็นที่ทราบกันดี`** — appear in corpus only as
  *mentions* (scholarly source discussing AI anti-patterns). Use-vs-mention
  rule works correctly. No change.
- **Zero-hit entries** (`ในส่วนของ`, `โดยสรุปแล้ว`, `กล่าวโดยสรุป`,
  `ในโลกปัจจุบัน`): no corpus presence as far as our sources show. Keep.

### Corpus-quality concern surfaced

`ปฏิเสธไม่ได้ว่า` and `มีความสำคัญ` both have native hits in AWS Thailand
b2b-formal marketing copy (`aws-thailand-agentcore.md`,
`aws-thailand-spip-security.md`). Marketing copy in 2024-2026 is itself a
plausible vector for AI-influenced phrasing — large-vendor Thai marketing
output increasingly drafted with LLM assistance. AWS Thailand corpus
entries should not be treated as gold-standard native for blocklist-
calibration purposes; they may themselves reflect AI-shaped Thai. Flagged
in `docs/scratch/source-vetting-2026-05-13.md` for a re-vet pass.
