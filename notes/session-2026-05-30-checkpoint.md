# Session checkpoint — 2026-05-30

## User note

> note to review it8 and it20 later.

Both iterations are sitting untracked in `workspace/` and want a human review
pass before any rule changes get derived from them.

## What was done this session

Ran inline iteration-8 end-to-end overnight per chakrit's autonomous brief.
Used the subagent-driven inline protocol from `tests/INLINE-ITERATION.md`
(bundle preprocessor + audit/fix prompts identical to the harness; outputs
marked `mode: "inline"` in meta.json).

All four `with_skill` evals converged to `CLEAN`:

| Eval                       | Passes to CLEAN |
| -------------------------- | --------------: |
| tech-doc-short             |               1 |
| news-feature-bts           |               1 |
| marketing-blurb            |               3 |
| personal-essay-homecoming  |               3 |

Per-eval `output.md` + `meta.json` written under
`workspace/iteration-8/<eval>/claude-inline/with_skill/`. Cross-eval summary
+ audit-trace observations at `workspace/iteration-8/feedback.md`.

No baseline configs, no codex-inline half, no `-m evaluate` heuristics — the
brief was audit-to-pristine, not bundle-effect measurement.

## What's next

1. **Review iter-8 outputs.** Four `output.md` files + `feedback.md`. The
   feedback flags two patterns worth chakrit's eye (do not act on
   unilaterally — iteration discipline says trace before adding rules):
   - Recurring `frame-scoped-ko` on `ทีไร` frames — may want stronger
     anchor in SKILL.md or `references/grammar.md`.
   - Marketing hedge stack (`น่าจะ X อยู่ด้วยซ้ำ`) bled into a
     personal-blog draft — may indicate `references/register.md`
     personal-blog section needs a counter-example.

2. **Review iter-9.** Pre-existing untracked iteration from before this
   session — chakrit asked to review alongside it-8. Contents not inspected
   this session; structure matches harness layout (4 evals + feedback.md).

3. **Decide on commits.** Both `workspace/iteration-8/` and
   `workspace/iteration-9/` are untracked. Per project convention,
   `workspace/iteration-N/feedback.md` IS tracked but the eval subdirs are
   gitignored. Worth confirming the feedback.md files survive `git add` and
   that nothing else got dropped into the iteration root that shouldn't go
   to git.

## Open questions

- Is iter-9 from a prior harness run or a prior inline run? Meta.json
  would tell; not checked.
- For the two patterns flagged in iter-8 feedback: are they gaps in
  existing rules (wording/anchoring), or genuinely new patterns needing
  new rules? Trace per `CLAUDE.md` iteration-discipline before editing.

## Blockers

None.
