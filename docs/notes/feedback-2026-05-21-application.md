# Application trail — feedback.md 2026-05-21

Trail of edits applied to the kien-thai skill from a transient `feedback.md`
at repo root (since deleted after application). Input was a single drafting
session of Thai government meeting minutes (ป.ป.ท. / Samarterware) with
corrections by a native Thai writer. Output: a new Register 6 — Official /
minutes — in `references/register.md`, plus a handful of register-scope
adjustments to existing rules in `grammar.md` and `craft.md`.

Each rule below cites: (1) the feedback.md item it derives from, (2) where it
landed in the skill, (3) provisional status.

## Per-rule trace

### Rule 1 → `concrete-cases-over-topology` in `craft.md`

- **Source**: feedback.md §1 (abstract topology vs concrete case-by-case).
- **Landed at**: `references/craft.md` under new section "Voice and framing".
- **Tag**: `craft · all-registers · soft`. Strictest in official/operational.
- **Status**: provisional — single-session origin. Worth corroborating against
  bank long-form and translated non-fiction registers (feedback claims it
  applies broadly but strictest in operational contexts).

### Rule 2 → register-scope of existing `capability-modal` in `grammar.md`

- **Source**: feedback.md §2 (`X ทำได้` vs `สามารถ X ได้`).
- **Landed at**: `references/grammar.md` — added "Register-aware" note to the
  existing `capability-modal` rule. Also surfaced as the dedicated
  `formal-capability-frame` rule under Register 6 in `register.md`.
- **Tag**: existing rule remains `mechanical · all-registers · hard`; the
  Register 6 entry is `mechanical · official · hard`.
- **Status**: not provisional for the underlying construction (`สามารถ + V +
  ได้` is documented Thai grammar). Provisional only on the register-scope
  boundary — i.e., where the "Acceptable (informal)" lenience ends.
- **Note**: The `ทำ → ดำเนินการ` substitution is handled separately under
  `formal-procedural-vocab`.

### Rules 3, 9, 10 → `no-telegraphic-shorthand` under Register 6

- **Source**: feedback.md §3 (prepositional shorthand), §9 (slash-separated
  numeric series), §10 (inline arithmetic). Folded into one umbrella rule
  with three subtypes per the trace in the prior analysis.
- **Landed at**: `references/register.md` Register 6 §`no-telegraphic-shorthand`.
- **Tag**: `mechanical · official · hard`.
- **Status**: provisional — single-session origin.

### Rule 4 → `purpose-chain-required` under Register 6

- **Source**: feedback.md §4 (`เพื่อ X เพื่อ Y` required, not avoided).
- **Landed at**: `references/register.md` Register 6 §`purpose-chain-required`.
- **Tag**: `mechanical · official · hard`.
- **Status**: provisional. Explicit carve-out from `connective-budget` in
  `style-rules.md` — that rule does not apply to `เพื่อ` chains in this
  register. The carve-out is documented inline in the rule text.

### Rule 5 → `time-bounds-need-anchor` under Register 6

- **Source**: feedback.md §5 (`ภายใน X เดือน` + `นับจาก [event]`).
- **Landed at**: `references/register.md` Register 6 §`time-bounds-need-anchor`.
- **Tag**: `mechanical · official · hard`.
- **Status**: provisional.

### Rule 6 → `name-document-by-function` under Register 6

- **Source**: feedback.md §6 (generic noun phrases → specific document names).
- **Landed at**: `references/register.md` Register 6 §`name-document-by-function`.
- **Tag**: `mechanical · official · hard`.
- **Status**: provisional. Included a small starter vocabulary
  (`ใบรับสำนวน`, `ใบเซ็นชื่อ`, `แบบ ทร. 14`, etc.) — list will grow as more
  procedural document types surface.

### Rule 7 → `positive-capability-framing` in `craft.md`

- **Source**: feedback.md §7 (enforcement chain → positive capability with
  condition).
- **Landed at**: `references/craft.md` "Voice and framing" section.
- **Tag**: `craft · all-registers · soft`.
- **Status**: provisional. The `ก็ต่อเมื่อ` construction itself is standard
  Thai; what's provisional is the framing preference (positive-with-condition
  over enforcement-chain) as a general pattern.

### Rule 8 → `formal-procedural-vocab` + `four-part-procedural` under Register 6

- **Source**: feedback.md §8 (procedural vocab swaps + four-part sentences).
- **Landed at**: `references/register.md` Register 6 §`formal-procedural-vocab`
  and §`four-part-procedural` (split into two rules — the vocab table and the
  sentence-structure observation are independent and serve different
  audit-time needs).
- **Tag**: both `mechanical · official · hard`.
- **Status**: provisional. Vocab list will grow as more pairs surface in
  future drafting sessions.
- **Note**: The English gloss for `นำเข้า` was adjusted from "ingress"
  (feedback.md original) to "load in" — closer to actual usage in Thai
  procedural contexts.

### Rule 11 → `formal-issue-vocab` under Register 6

- **Source**: feedback.md §11 (`คำถามค้าง` → `ประเด็นที่ยังต้องการคำชี้แจง`).
- **Landed at**: `references/register.md` Register 6 §`formal-issue-vocab`.
- **Tag**: `mechanical · official · hard`.
- **Status**: provisional.

## Register-6 itself

- Created in `references/register.md` as a full sixth register family.
- Added row to "Quick register decision" table.
- Added to `## Workflow when asked to write Thai prose` register list in
  `SKILL.md`, marked provisional.
- Added `"official": ("Register 6",)` to `REGISTER_HEADERS` in `tests/lib.py`
  so the harness can register-scope register.md bundles. Verified scoping
  works via a one-liner that confirms `## Register 6` appears in the bundle
  only when `register="official"` is passed.

## What was NOT done

- **No new eval added to `evals/evals.json`** for the official register. The
  user's request was "do all the suggested edits" — that scope was about the
  skill content, not adding evals. An eval for the official register would
  need a real minutes-drafting task prompt; the ป.ป.ท. session pairs can seed
  one but adding it is out of scope for this pass.
- **No corpus expansion under `corpus/curated/`** for the official register.
  Bigger validation work — surface government meeting summaries, Royal
  Gazette notices, etc. — is deferred.
- **No school-PR sync.** The kien-thai/kode-thai skills are this repo's
  source-of-truth (the school re-imports from here, per CLAUDE.md "Two skill
  sources"). No further school plumbing is needed at this point.

## Iteration-discipline notes

Per CLAUDE.md's "iteration discipline":

> Trace before you write. Each rule has a *why* — a failure mode it counters
> or a human-writing pattern it captures.

The trace for Register 6 is the act-5 minutes drafting session captured in
`feedback.md`. That's a **single drafting session**, not a corpus survey.
Iteration discipline says new rules without corpus backing should be
**provisional** and tagged as such. Every Register 6 rule is marked
provisional in the register's preamble; the dependency is "needs corpus
validation" which is the next iteration step.

The discipline also says:

> If a rule exists but didn't fire: ask why.

In the trace, only one rule was a real "didn't fire" case — `capability-modal`
in `grammar.md` already existed but tolerated `V + ได้`-alone as
"Acceptable (informal)". The fix was to register-scope that lenience: it does
**not** apply to the new official register. The existing rule got a small
"Register-aware" note appended pointing at `formal-capability-frame` in
Register 6.

The remaining 10 rules had **no existing coverage**. Their gaps were real,
and the additions are additive — not displacing research-grounded rules.

## What to look at on return

1. The new Register 6 section in `references/register.md` — read top to
   bottom and sanity-check the eight rules against your own Thai intuition.
2. The two new craft rules in `references/craft.md` ("Voice and framing"
   section).
3. The register-aware note appended to `capability-modal` in
   `references/grammar.md`.
4. The provisional flag on Register 6 — the wording can be tightened or the
   provisional tag dropped after corpus validation.
5. Whether the `connective-budget` carve-out for `เพื่อ` chains is wide
   enough (it currently only applies in Register 6 — should it also apply in
   News? Academic?). Worth a re-read.
6. The `formal-procedural-vocab` list — small now; will need to grow.
   Consider whether some entries (`ทำ → ดำเนินการ`) belong in the broader
   `register-drift` casual↔formal table instead, since they have wider
   applicability.

## Files changed in this pass

- `skills/kien-thai/SKILL.md` — register list updated.
- `skills/kien-thai/references/register.md` — Register 6 added (full section);
  quick-decision table row added.
- `skills/kien-thai/references/grammar.md` — `capability-modal`
  register-aware note added.
- `skills/kien-thai/references/craft.md` — two new rules under "Voice and
  framing".
- `tests/lib.py` — `REGISTER_HEADERS` entry for `official`.
- `feedback.md` — deleted after application; this trail file now subsumes
  its role.
- `docs/notes/framing-investigation-2026-05-21.md` — separate investigation file
  (the agent-framing question; not part of this trail).

Trail file: this one (`docs/notes/feedback-2026-05-21-application.md`).
