# Skill-change proposals — 2026-05-13 chrome-session follow-up

Companion note to
[`chrome-session-2026-05-13.md`](chrome-session-2026-05-13.md). The browser-
vetting pass produced four findings; three landed immediately (commit
`019c29e`), one (register-leakage rule) was deferred pending recurrence.
This note captures the deferred proposal in landing-ready form plus a
couple of adjacent skill-change candidates the same session surfaced.

Not applied to skill files in this autonomous session. Drop in when
chakrit reviews and the gating conditions are met.

## What already landed (recap)

Committed `019c29e` in this session opener:

- `style-rules.md` — new `mai-yamok-spacing` entry (`ต่าง ๆ` always
  spaced; other reduplications register-scoped).
- `register.md` — Fictionlog/Tunwalai → dropped-sources with out-of-
  scope rationale; Minimore Reference tier backed by a Wayback essay
  citation.
- `research-queue.md` — ๆ-spacing + Fictionlog/Tunwalai entries marked
  resolved; animacy entry reframed as register-leakage.

## Proposal A — Register-leak rule (deferred, draft ready)

**Status.** Drop into the skill *only* when iter-8+ shows ≥1 more
instance of the pattern in Explainer or News-reference outputs. Today
the evidence is one instance (iter-7 tech-doc-short claude/with_skill,
`downstream ทนรับ burst`). One-instance rules violate iteration
discipline (CLAUDE.md → "Iteration discipline").

**Landing.** `register.md` — a new shared rule referenced from both
Register 1 (Explainer) and Register 4 (News / reference). Land once,
cite from both register sections, the way `register-drift` and
`deixis-continuity` already do.

**Slug.** `register-leak-emotional-verb` *(mechanical · explainer +
news · hard)*.

**Draft text — ready to lift verbatim:**

> ### `register-leak-emotional-verb` *(mechanical · explainer + news · hard)*
>
> In Explainer and News-reference register, avoid colloquial-emotional
> verbs on system / infrastructure / abstract subjects. AI imports
> `ทน*` / `เครียด` / `ทรมาน` from English personification (`the server
> *gets stressed*`, `the system *suffers* under load`) and from native
> Thai's *gaming / casual* register — both are attested but neither
> belongs in formal explainer or news prose.
>
> - **Bad** (gaming-register verb in tech-doc body):
>   `downstream ทนรับ burst ได้แค่ไหน`
> - **Good** (neutral verb): `downstream รองรับ burst ได้แค่ไหน`
>
> Neutral alternatives by sense:
>
> - capacity / accepting load → `รองรับ`, `จัดการ`, `จัดสรร`
> - durability / fault-tolerance → `ทนทานต่อ` (preposition-licensed),
>   `รับมือกับ`
>
> **Not a grammar violation.** Native Thai *does* personify systems
> with these verbs in gaming / community register (`เซิร์ฟเวอร์ทนรับ
> ความหนาแน่นของผู้เล่นไม่ไหว`, `เซิร์ฟเวอร์เครียด` — both attested
> with substantial corpus). The wrongness is register-leak, not
> animacy. Re-evaluate per-piece if the target register shifts toward
> gaming/community.

**Cross-references to add.** In Register 1 (Explainer) and Register 4
(News / reference) prose blocks, add a one-liner pointing readers to
`register-leak-emotional-verb`. Same shape as the existing
`register-drift` cross-references.

**Why provisional/deferred.** Animacy hypothesis was falsified by
chrome §4; the reframed register-leak version is only one-instance.
Drop-in condition is iter-8+ recurrence in Explainer or News. If iter-
1..7 codex / baseline reviews (still open per
`workspace/iteration-7/feedback.md` followups) surface a second
instance retroactively, that also satisfies the gate.

## Proposal B — Sharpen iteration discipline on the register axis

**Source.** Chrome §4 falsification — the original "animacy"
hypothesis was a category mistake: native Thai *does* use `ทน*` /
`เครียด` on systems, just in a different register. The right framing
was register-leak, not animacy.

**Observation.** Current `CLAUDE.md` "Iteration discipline" step 3
mentions "Wrong register applied" among the diagnostics for why an
existing rule didn't fire. Step 4 (no rule covers it) asks for source-
research evidence. Neither explicitly says: *if the form is attested
only in casual / gaming / colloquial register but is wrong in your
target register, the rule belongs in `register.md`, not
`grammar.md`/`ai-tells.md`*. CONTRIBUTING.md §0 line 16 is closer
(`feedback ในลักษณะ "กฎข้อนี้ผิด" จริง ๆ แล้วส่วนใหญ่จะเป็น
register-mismatch`) but addresses contributors, not the iteration-
discipline checklist.

**Proposed addition.** In `CLAUDE.md` "Iteration discipline" between
existing steps 3 and 4, insert a 3.5 (or fold into step 4 prose):

> 3.5. **Check the register axis before promoting to a universal
> rule.** If you're about to add a rule that says "X is wrong in
> Thai," first ask: is X wrong *everywhere*, or only wrong in the
> active register? Native Thai often allows in casual / gaming /
> community register what reads as broken in Explainer / News /
> Academic. If the form is register-attested elsewhere, the rule
> lands in `register.md` (register-scoped), not in `grammar.md` or
> `ai-tells.md` (universal). Tag as `register-leak-*` when this
> framing applies.

**Why.** Would have caught the iter-7 → iter-8 path: the animacy
framing was treated as a grammar rule candidate; the register-leak
framing routes to `register.md` and avoids polluting `grammar.md`
with a register-conditional rule mis-tagged as universal.

**Status.** Lightweight; no gating evidence required because this is
process discipline, not a prose rule. Land when chakrit reviews.

## Defer — `mai-yamok-spacing` examples in `examples.md`

The rule landed today, but `examples.md` carries no register-tagged
before/after pair for ๆ-spacing. Tempting to lift one now (e.g.,
"Personal-blog `เด็กๆ`" vs "Government `ต่าง ๆ`"), but:

- Small-N evidence (~20 samples across 5 sources, per chrome §3).
- No eval-time failure mode yet — AI's ๆ-spacing behavior across iter-
  1..7 hasn't been audited for the register-mix-up specifically.
- `examples.md` exemplars are most valuable when the eval has actually
  surfaced the failure. Adding before/after pairs ahead of the eval
  evidence creates orientation noise.

**Defer condition.** If iter-8+ outputs show AI getting ๆ-spacing
wrong in a recognizable register-mix-up (e.g., personal-blog body
with formal `ต่าง ๆ` spacing or explainer body dropping the space on
`ต่าง ๆ`), lift the offending → corrected pair into `examples.md`
tagged for the active register at that point.

## Not proposed (and why)

- **Person-deixis roles (1st / 2nd / 3rd).** Chrome-session findings
  do not touch the person-deixis axis. `deixis-continuity` already
  landed from iter-7 (commit history). No additional rule warranted.
- **Source-tier maintenance pattern.** The Fictionlog/Tunwalai +
  Minimore + readthecloud.co + Storylog + Readery entries already
  carry verdict reasoning inline (per the existing pattern in
  `register.md` "Dropped from source list"). The discipline is
  implicit and working; documenting it explicitly in CONTRIBUTING.md
  or notes would be dead scaffolding right now.
- **`mai-yamok-spacing` → `ai-tells.md` promotion.** Small-N (~20
  samples) and currently phrased as a default. Promoting to a hard
  audit-time check would over-fit the evidence.

## Trail for next session

- This file: `docs/scratch/proposals-2026-05-13.md`.
- Chrome-session evidence: `docs/scratch/chrome-session-2026-05-13.md`.
- Reframed research-queue entry: `docs/research-queue.md`
  → "Colloquial-emotional verbs leaking into Explainer/News register"
  — now links here for draft text.
- Iter-7 feedback (open followups, 10 unreviewed outputs):
  `workspace/iteration-7/feedback.md` § Followups. A pass through the
  unreviewed iter-7 codex/baseline outputs for `ทน*` / `เครียด` /
  `ทรมาน` on system subjects could supply the second instance the
  Proposal A gating needs.

When chakrit returns and accepts Proposal A, the diff is one new
section in `register.md` plus two one-line cross-references. When
accepting Proposal B, the diff is one paragraph in `CLAUDE.md`. Both
are landed-ready as written above.
