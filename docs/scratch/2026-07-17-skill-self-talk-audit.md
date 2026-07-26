<!-- not spec/decision because: a finding-list against the distributed skill bodies.
     Each item resolves into an edit or a queue entry; the list itself is disposable. -->

# Self-talk / context-reference audit (2026-07-17)

**Status.** The kien-thai half was applied in `793bd2d`. The **kode-thai half below
and the distribution-boundary findings are open** — queued in
[`../work-queue.md`](../work-queue.md). Line numbers are from the school's synced copy
at the time of writing; re-grep before editing.

From a prod9/school audit of distributed skill bodies: consumers receive only the skill
directory, so authoring narration and references to files that don't ship with it are
dead weight for the cold reader. Findings below are in the distributed copies of
**kien-thai** and **kode-thai**; line numbers are from the school's synced copy
(prod9/school `3c0e502`) — re-grep here before editing.

## kien-thai

- `SKILL.md`
  - L46 — "few-shot conditioning from `corpus/` are baked into …": `corpus/` doesn't
    ship in the skill dir.
  - L161-162 — HTML comment narrating how the example was authored, citing
    `corpus/curated/tech-writing/somkiat-bun-testing.md`.
  - L285-286 — "Provisional (added 2026-05-21, awaiting corpus expansion)": edit-date
    narration to the maintainer.
  - L350-355 — harness-scoping note + "Scholarly provenance lives in
    `corpus/curated/scholarly/` — not in the bundle": packaging meta-commentary.
- `references/craft.md`
  - L106-107 — "Earlier framing of this rule conflated two distinct issues. Split:" —
    edit-history narration.
  - L121-122 — "the earlier claim … was wrong" — corrects a prior version, addressed
    to reviewer; restate as the current rule only.
  - L139-142 — "Provisional: corpus has no curated operational/system-spec register …
    Revisit when operational corpus exists."
- `references/examples.md` — L148, L172-173, L200-201: "จาก iteration-7
  marketing-blurb review" — session refs the reader can't know.
- `references/exemplars.md` — L8, L12, L20, L33, L41, L55: `<!-- source:
  corpus/curated/... -->` provenance comments (live URLs are fine; the `corpus/…`
  paths aren't); L64-65: TODO-to-author about future corpus entries.
- `references/register.md`
  - L260-261, L267, L309-311 — "(verified — vetted 2026-05-13, see
    `docs/scratch/source-vetting-2026-05-13.md` / `chrome-session-2026-05-13.md`)".
  - L286-291 — tooling-session narrative + `docs/scratch/` ref.
  - L295 — "Dropped from source list (verified 2026-05-13):" — editorial-session
    narration.
  - L318 — "Do not add as Register-6 — would create dead scaffolding": skill-design
    note to the maintainer, not the consuming agent.
  - L391-394 — "Provisional (added 2026-05-21): synthesized from a single drafting
    session … trail lives in `docs/scratch/feedback-2026-05-21-application.md`".
- `references/style-rules.md`
  - L63-64 — "(vetted 2026-05-13, see `docs/scratch/chrome-session-2026-05-13.md`
    §3)".
  - L76-81 — evidence/justification paragraph reads as reviewer-facing confidence
    weighting (borderline; keep the "default, not hard check" instruction, drop the
    sample-size narration or fold into a provenance convention).
- `scripts/README.md`
  - L3-10 — narrates the 2026-06-09 probe, names chakrit, "in the repo".
  - L27, L43 — few-shots "from `corpus/`" (unshipped).
  - L68-73 — open-step/status narration + `docs/scratch/session-2026-06-09-…` and
    `tests/lib.py` harness refs.

General pattern: dated vetting/session provenance belongs in this repo's docs
(`docs/scratch/…` stays here), not in the distributed skill body. If confidence
weighting is wanted in-body, adopt a defined tag convention (cf. de-slop's
Empirical/Curated/Field legend) instead of dated session refs.

## kode-thai

- `SKILL.md`
  - L21-25 — "(The pytest harness injects a leaner audit-mode bundle … see the project
    CLAUDE.md 'Two-tier injection')": school-harness + maintainer-file refs, invisible
    to a consumer.
  - L74 — "follow the iteration discipline in the project `CLAUDE.md`" — same.
  - L65-66 — `skills/kien-thai/scripts/` path into the sibling skill's internals;
    reduce to a skill-name handoff or ship the script.

> 🤖 Drafted by Claude on chakrit's behalf.
