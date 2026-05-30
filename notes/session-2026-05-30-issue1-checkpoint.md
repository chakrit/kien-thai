# Session checkpoint — 2026-05-30 (INDEX wiring + issue #1)

Separate from `session-2026-05-30-checkpoint.md`, which tracks the still-open
iter-8/iter-9 review work. This session was docs + a bug fix; both shipped.

## What was done

1. **Wired `workspace/INDEX.md` into iteration entry points** so the ledger
   stays discoverable and gets updated on create/review. Pointers added in
   `CLAUDE.md` (evidence block + Stage-2 review note), `tests/INLINE-ITERATION.md`,
   `README.md`, `CONTRIBUTING.md`. Rule: add a row on create (Review `pending`),
   flip to `reviewed` + link feedback on review. Commit `6c9ad93`, pushed.

2. **Fixed issue #1** (@ninyawee) — `skills/kien-thai/SKILL.md` `description:`
   had bare `colon-space` in an unquoted scalar → invalid YAML → `skills`
   CLI rejected it. Quoted the value. `kode-thai` was already fine (no
   colon-space) — confirmed via PyYAML, not assumed. Added
   `tests/test_skill_frontmatter.py`: strict-YAML guard over every
   `skills/*/SKILL.md`; `pyyaml` added to dev group. Commit `8a81bd5`, pushed.
   Issue auto-closed; clarifying comment posted (with AI-disclosure footnote).

3. **Disclosure rule** — global `~/.claude/CLAUDE.md` gained an "Acting under
   my name" section: always footnote AI-generated content posted under
   chakrit's identity. Saved to memory (`feedback_disclose_ai_under_my_name`).

## What's next

Nothing pending from this session in this repo — tree is clean.

## Open / dangling

- `~/dotfiles/claude/.claude/CLAUDE.md` (symlink target of global CLAUDE.md)
  has the "Acting under my name" edit **unstaged** in the dotfiles repo —
  separate repo, not committed here. Commit on next dotfiles sync.
- The iter-8/iter-9 review obligations in the sibling checkpoint still stand.

## Blockers

None.
