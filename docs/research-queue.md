# Research queue

Speculative items needing evidence before they can graduate into a rule. Items
here are *questions*, not verdicts. Each entry should name the question, the
hypothesis (if any), the scope of work that would settle it, and where the
finding would land.

> **Direction (2026-05-30):** items here that surface a recurring pattern now land as
> register-tagged before/after *pairs* first (rules only when the pair doesn't transfer),
> and graduate only with the auditor-recall data from the review loop — see
> [`decisions/2026-05-30-exemplar-first-pivot.md`](decisions/2026-05-30-exemplar-first-pivot.md)
> and [`spec/review-protocol.md`](spec/review-protocol.md).

---

## Discourse / composition axis — macrostructure + inter-sentence cohesion

**Provenance.** iter-8 outer-loop review (2026-06-08), two findings the sentence-scoped
ruleset is structurally blind to. See
[`../workspace/iteration-8/feedback.md`](../workspace/iteration-8/feedback.md) → ② and ④.

**Question (a) — macrostructure.** The skill + review protocol run entirely
sentence-to-paragraph. The frames' "structural" tag means *clause* structure;
`style-rules.md §Structure` caps at single-paragraph. There is no per-register
macrostructure (news arc, essay shape) and no discourse-level finding class — the only
holistic verdict is `reads-flat` (voice). ②'s `news-feature-bts` was chakrit-clean: no on a
**whole-piece restructure** (Dao's flag) that no slot can hold. Does kien-thai need a
per-register macrostructure axis and a `reads-misstructured` verdict flag in the protocol?

**Question (b) — inter-sentence cohesion.** Finer than (a): ④'s `ที่ยังเหมือนเดิมก็มี` was
a connective error *between adjacent sentences* — additive `ก็มี` used where the discourse
move is contrast against the prior sentence's `เปลี่ยน`. Fix mirrored the prior verb
(`ไม่เปลี่ยนแปลง`) to license the marker. No slug covers cross-sentence connective-choice
logic; every connective rule (`connective-budget`, `seam-connective-missing`, `doi-sprawl`)
is within-sentence. Is inter-sentence cohesion a distinct rule class, or does it fold into
the macrostructure axis above?

**Hypothesis.** (a) and (b) are the same axis at two scales — discourse cohesion the skill
has never modeled because generation/audit operate a sentence at a time. Likely a real
coverage hole, but **gate any rule on corpus evidence of native macrostructure per
register** — without attested news-arc / essay-shape patterns this stays speculative.

**Scope to investigate.** Survey `corpus/curated/` per register for macrostructure
signatures (lede/nut-graf in news-feature, turn-structure in personal essay) and for
inter-sentence contrast/continuation marker choice. Tabulate whether native writing has a
consistent shape worth encoding vs being too author-variable to rule.

**Landing place.** Pairs first into `references/examples.md` (the ④ cohesion pair is ready:
`ที่ยังเหมือนเดิมก็มี` → `ที่ยังเหมือนเดิมไม่เปลี่ยนแปลงก็มี`, register `personal-blog`).
Macrostructure → possibly a new `references/structure.md` or a `register.md` per-family
shape note. The `reads-misstructured` **protocol-flag decision is chakrit's** — tracked in
[`human-tasks-queue.md`](human-tasks-queue.md).

---

## ๆ-spacing as register-scoped style ✅ resolved 2026-05-13

**Resolution.** Browser-vetted across 5 registers (see
[`scratch/chrome-session-2026-05-13.md`](scratch/chrome-session-2026-05-13.md) §3).
Two-rule shape:

1. **`ต่าง ๆ` is near-universally spaced** in edited Thai across
   all registers — formal stock phrase, even Pantip/Minimore-style
   amateur writing tends to space this one. Treat as a hard
   default.
2. **Other reduplications** (`สั้นๆ`, `ง่ายๆ`, `อะไรๆ`, `เด็กๆ`,
   `เตี้ยๆ`, `อ่อนๆ`) follow register: dropped in personal-blog /
   diary / amateur-essay; preserved in government / institutional
   / formal-edited. Tech-blog (Blognone) is internally mixed.

**Landing place.** `references/style-rules.md` — entry covering
the `ต่าง ๆ` carve-out + the register-scoped general rule. Phrase
as default, not hard `ai-tells.md`-tier check (small-N evidence:
~20 samples).

Below is the original entry for archive.

---

**Question.** Is the spacing convention around ๆ (e.g. `แย่ ๆ` vs `แย่ๆ`)
register-dependent in real Thai writing, or is one form correct everywhere?

**Hypothesis (chakrit's speculation, NOT verdict).** Formal / contributor-doc /
official-leaning prose tracks Royal-Institute spacing (`คำ ๆ`); marketing and
casual prose drop the space (`คำๆ`).

**Scope to investigate.** Tech blog, bank long-form, newspaper รุ่นใหม่,
dev-casual blog, government, academic, marketing copy. Look at how each
register actually handles ๆ; check whether any register is internally
consistent.

**Landing place.** New or amended rule in `references/style-rules.md`, or a
register-scoped slot in `references/register.md`. Not a hard `ai-tells.md`
rule unless the formal-strict form turns out to be universal.

---

## Comma-listing as register/formality feature; formality as a missing axis

**Question (a).** Does Thai-prose comma-listing (e.g. `A, B, หรือ C`) track
register, formality, both, or neither? Is it always wrong, always fine, or
context-dependent?

**Question (b).** Is "formality" a missing or replacement axis to the current
5-register taxonomy in `references/register.md`? Right now register is one
flat axis; formality may cut across it (a `personal-blog` post can be casual
or formal independently of the register family).

**Method.** Survey the curated corpus in `corpus/curated/` across families.
Tabulate comma-listing density by family. Tabulate formality cues
independently and check whether they co-vary or are orthogonal to register.

**Landing place.** New dimension in `references/register.md` (feature-by-
register matrix), or a separate formality axis layered on top of the
existing register taxonomy.

---

## Hedge-stack pattern beyond `น่าจะ X อยู่ด้วยซ้ำ`

**Question.** Does the broader multi-particle hedge-stack pattern in
marketing-register body copy generalize beyond the one stack shape now
captured in `over-hedging`?

**Hypothesis.** AI defaults to hedge-stacking in marketing register
because the training data conflates "warmth" with "softening." Native
marketing copy asserts (`กลายเป็นขาดทุน`) and reserves hedging for
disclaimer-adjacent lines, not body-pain-point claims.

**Status so far.** The `น่าจะ X อยู่ด้วยซ้ำ` instance from iter-7
marketing-blurb L4 landed in `ai-tells.md#over-hedging` as the marketing
example. The general "does multi-particle stacking in pain-point copy
generalize?" question is still unanswered.

**Scope to investigate.** Look at iteration-1 through iteration-7
marketing outputs for other instances of multi-particle hedge stacks
(`อาจจะ … คงจะ … น่าจะ …`, `อาจ … อยู่ … บ้าง …`, etc.) in body copy
making a pain-point claim. If the pattern is recurring with different
stack shapes, promote `over-hedging` to a register-aware rule (or split
into a marketing-specific entry in `register.md`).

**Landing place.** Extend `ai-tells.md#over-hedging` with more attested
stack shapes, or new `register.md` marketing entry specifically about
pain-point assertion vs hedging.

---

## Colloquial-emotional verbs leaking into Explainer/News register

**Reframed 2026-05-13** — animacy hypothesis (see archive below) was
falsified by browser vetting in
[`scratch/chrome-session-2026-05-13.md`](scratch/chrome-session-2026-05-13.md) §4.
Native Thai *does* apply `ทนรับ` and `เครียด` to system subjects in
gaming/community register (`เซิร์ฟเวอร์ทนรับ … ไม่ไหว`,
`เซิร์ฟเวอร์เครียด`, both attested with substantial Google hits).

**Reframed question.** Is the iter-7 `ทนรับ` issue a
**register-leakage** pattern: AI mixes colloquial-emotional verbs
(`ทน*` / `เครียด` / `ทรมาน`) into Explainer/News register where
neutral verbs (`รองรับ`, `จัดการ`, `จัดสรร`, `ทนทานต่อ`) are
expected? Same candidate verb list (`ทรมาน`, `เหน็ดเหนื่อย`, `อดทน`,
`เครียด`, `สบาย`, `กล้า`, `รู้`) — but now check each for
register-restriction, not animacy-restriction.

**Provenance.** Still one instance (iter-7 `downstream ทนรับ burst`),
but the framing is now register-mismatch, not grammar violation.

**Scope to investigate.** Look at iter-1 through iter-7 Explainer
and News-reference outputs for colloquial-emotional verbs on system
subjects. Cross-check Blognone / Bangkok Post Tech / `รู้รอบ`-style
explainer corpora — these should never use `ทน*` / `เครียด` on
systems; if they do, the pattern is even more relaxed than
hypothesized.

**Landing place.** If recurrence appears in iter-8+, add a
register-aware entry to `references/register.md` Register-2
(Explainer) and Register-4 (News): "Avoid colloquial-emotional
verbs on system subjects — use neutral `รองรับ`/`จัดการ`/`ทนทานต่อ`."
Do **not** land as `grammar.md` animacy rule (the animacy framing
is wrong).

**Draft text ready.** Slug `register-leak-emotional-verb`, full
landing-ready section in
[`scratch/proposals-2026-05-13.md`](scratch/proposals-2026-05-13.md) §
Proposal A. Drop in when the gating condition (iter-8+ recurrence,
or retroactive 2nd instance in iter-1..7 codex/baseline review) is
met.

Below is the original entry for archive.

---

**Question.** Is `ทน` the only personification verb AI mis-applies to
non-human subjects, or part of a broader class? Candidate verbs:
`ทรมาน`, `เหน็ดเหนื่อย`, `อดทน`, `เครียด`, `สบาย`, `กล้า`, `รู้`.

**Hypothesis.** AI applies a wider set of human-only or animate-only
verbs to systems/abstractions because English freely personifies
("the system *suffers* under load," "the server *gets tired*"). Thai
constrains animacy more tightly.

**Provenance so far.** One instance — iteration-7 tech-doc-short
(claude/with_skill): `downstream ทนรับ burst ได้แค่ไหน`. Chakrit's
rewrite: `downstream รองรับ burst`.

**Scope to investigate.** Look at tech-doc and explainer outputs from
iterations 1–7 for verbs marked as requiring animate subjects but
applied to system-state subjects. Cross-check against a list of Thai
animacy-restricted verbs.

**Landing place.** `grammar.md` new entry "animacy-restricted verbs," or
folded into `ai-tells.md` as a calque-pattern entry. If only a handful
of verbs are involved, an explicit list works; if it's open-ended, a
heuristic rule may be needed.

---

## Vet non-tech personal-blog source candidates ✅ resolved 2026-05-13

**Resolution.** Vetted via Claude-in-Chrome MCP. Full notes in
[`scratch/source-vetting-2026-05-13.md`](scratch/source-vetting-2026-05-13.md).
Outcome applied to [`skills/kien-thai/references/register.md`](../skills/kien-thai/references/register.md):

- **Promoted to Model (verified):** Vicharn Panich on GotoKnow
  (author-scoped, plain-diary); Pantip Blueplanet/Klai Baan/Greenzone
  bylined long-form posters.
- **Dropped:** readthecloud.co (live site pivoted to "CloudPang" and
  shows AI-assist tells); Storylog.co (defunct, redirects to
  corporate site); Readery / Bookmoby (podcast/shop, not blog).
- **Kept Reference-only:** Minimore (amateur-essay caveat; live SPA
  still won't render via MCP).
- **Spawned new vetting item:** Fictionlog/Tunwalai serial-fiction
  register (see below).

Below is the original entry for archive.

---

**Question.** The current Register 3 Models list was broadened (this session) with
non-tech candidates: GotoKnow.org, Readery / Bookmoby, bylined The Cloud features,
per-author-vetted Medium non-tech writers — plus a Reference-only tier listing
Storylog, Minimore, Pantip long-form. These were added on plausibility, not on
verified source-reading. The vetting pass is queued here.

**Why vetting is blocked.** Autonomous WebFetch probes hit 403/empty across the
primary candidates: GotoKnow (403), readthecloud.co (403), minimore.com
(empty JS render), fungjaizine (522). Only Happening & Friends and theMatter
returned full prose, and both are news-feature / lifestyle journalism rather
than first-person essay — they confirm those *platforms* read like news/feature,
not personal-blog. Without verbatim prose from the actual candidate sources, a
grammar-discipline judgement would be speculation.

**What one verified data point showed.**
[`happeningandfriends.com/article-detail/87`](https://www.happeningandfriends.com/article-detail/87)
(เดือนเพ็ญ จุ้ยประชา, Readery profile feature): high grammar discipline,
3rd-person narrative, edited-magazine voice. Sits firmly in news-feature
register, not personal-blog. Useful as confirmation that "Readery" the *brand*
is covered by lifestyle journalism — but their own output is podcast/social,
not long-form essay. So the Readery-as-personal-blog-model entry is doubly
weak: their primary medium isn't blog, and they're more often *subject of*
features than authors of personal essays.

**Status of provisional entries (need browser-paste vetting):**

| Candidate                          | Tier as listed   | Status                                                            |
| ---------------------------------- | ---------------- | ----------------------------------------------------------------- |
| GotoKnow.org (educator reflections)| Model (essay)    | WebFetch 403. Plausible; need 1-2 representative posts pasted.    |
| Readery / Bookmoby                 | Model (literary) | Likely mis-tiered — primary medium is podcast/shop, not blog.     |
| Bylined The Cloud features         | Model (edited)   | WebFetch 403. Edited-magazine voice — closer to news-feature with personal byline. |
| Medium Thai non-tech               | Model (per-author)| Per-author; no platform-level guarantee. Identify named authors first. |
| Storylog.co                        | Reference-only   | Plausible; need spot-check.                                       |
| Minimore                           | Reference-only   | Empty JS render. Need spot-check.                                 |
| Pantip long-form                   | Reference-only   | Plausible; need spot-check.                                       |

**Scope to investigate (next pass — chakrit-driven or different fetch tool).**

1. Paste 2-3 verbatim paragraphs from a GotoKnow educator reflection and a
   Minimore/Storylog personal essay into a working note under `scratch/`.
2. Assess each for: first-person discipline, classifier accuracy, calque
   density, sentence-rhythm shape, period frequency.
3. Either confirm the Model/Reference tier as listed, or reclassify.
4. For Readery/Bookmoby specifically: decide whether to drop entirely or
   move to a "voice references" non-prose tier (podcast scripts, social
   posts) that we explicitly do not lift grammar patterns from.

**Landing place.** Final source-tier list in `references/register.md`
Register 3 Models section. If any verified source produces a strong
before/after exemplar for non-tech personal essay, lift into
`references/examples.md` tagged `personal-blog`. Until vetted, the existing
broadened Models list in `register.md` should be read as **provisional**.

---

## Closer-binding scope reading discipline

**Question.** Where does the "read closure-binding scope before judging
pair-compatibility" discipline belong? It's a review-process rule, not a
prose-content rule.

**Hypothesis.** Belongs in `skills/kien-thai/SKILL.md` review workflow
(applies to both generation-time self-review and audit-pass) rather than
`skills/kode-thai/SKILL.md` (audit-loop only). Generation-time
self-review benefits equally from getting binding scope right before
calling a pair incompatible.

**Provenance so far.** One instance — iteration-7 marketing-blurb L11
variant E reading: Claude misparsed `เมื่อไหร่ + เสมอ` as a direct pair
when `ทันที` had already closed `เมื่อไหร่` and `เสมอ` belonged to a
separate `จะ…เสมอ` frame.

**Scope to investigate.** See whether other audit-pass misreads in
iter-7 outputs (across the un-reviewed remaining 10) involve similar
binding-scope errors. If yes, the discipline lands in the audit-loop
side; if also at generation time, it lands in the kien-thai workflow.

**Landing place.** TBD between `skills/kien-thai/SKILL.md` workflow
section, `skills/kode-thai/SKILL.md` audit pass, or a new checklist
file under `skills/`. Pick after seeing more instances.

---

## Fictionlog / Tunwalai serial-fiction register ✅ resolved 2026-05-13

**Resolution.** Out-of-scope. Vetted via Claude-in-Chrome MCP (see
[`scratch/chrome-session-2026-05-13.md`](scratch/chrome-session-2026-05-13.md) §1).
Fictionlog Thai bestsellers are uniformly cultivation/wuxia with
archaic pronouns and Chinese-genre lexicon; Tunwalai is dominated by
romance/erotica genre fiction. Even paid-out experienced authors
inhabit the genre conventions — the structural mismatch with kien-
thai's non-fiction targets isn't fixable by a better author filter.
Adding as Register-6 only to mark "do not lift from" would create
dead scaffolding. Outcome captured in `references/register.md`
Register-3 dropped-sources list.

Below is the original entry for archive.

---



**Question.** Storylog Group's successor platforms (Fictionlog,
Tunwalai) host very high-volume native-Thai serial fiction. Should
they enter the source list as a new fiction / web-novel register
slot, distinct from the current 5 register families?

**Provenance.** chakrit raised during 2026-05-13 vetting pass. See
[`scratch/source-vetting-2026-05-13.md`](scratch/source-vetting-2026-05-13.md).

**Scope to investigate.**

1. Author filter — only experienced / paid-out authors. Fictionlog
   publicly lists per-author earnings; treat that as a discoverability
   filter. Skip the amateur long tail.
2. Sample 2-3 chapters from each platform across genres (romance,
   fantasy, slice-of-life). Capture only short illustrative tidbits
   (no extended quoting / redistribution).
3. Decide whether serial-fiction register deserves its own register
   slot (Register 6?) or is out-of-scope. Genre conventions (heavy
   dialogue, narrative tropes, popular-fiction pacing) shouldn't
   bleed into non-fiction registers.

**Author-pool caveat (chakrit, 2026-05-13).** A large share of fiction
on these platforms is written by teenagers and other untrained
writers. Even the *fiction* register would be unsafe to lift from
blindly without the paid-out-author filter — amateur conventions
(clichéd dialogue, school-essay vocabulary, narrative-trope mimicry)
would contaminate any patterns extracted.

**Landing place.** Either:

1. New "Register 6 — Popular fiction / web-novel" section in
   `references/register.md`, with strict author-pool scoping; or
2. Explicit out-of-scope note (kien-thai targets non-fiction registers
   only). Pinto e-book is also out-of-scope — retail, not authoring.
