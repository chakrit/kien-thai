# Session checkpoint — 2026-07-17 self-talk sweep

Not spec/decision because: session breadcrumb — narrative of a completed sweep plus
open threads, nothing here rules or designs anything.

## Done

Applied the repo-relevant half of `review.md` (the 2026-07-17 self-talk /
context-reference audit of the distributed kien-thai + kode-thai copies), committed
as `793bd2d`, pushed:

- Edit-history narration rewritten as current rules (`craft.md`).
- Dated vetting/session refs moved to HTML comments in place (`register.md`,
  `style-rules.md`, `craft.md`, SKILL.md Register-6 line).
- Dropped-source list + Minimore access note extracted to
  `docs/decisions/2026-05-13-register3-source-list-vetting.md`; comment pointer left
  in `register.md`.
- `จาก iteration-7` prefixes cut from `examples.md` (trace stays in iteration-7
  feedback); news-exemplar TODO deleted (tracked at `docs/work-queue.md:143`);
  `scripts/README.md` de-personalized, Status compressed to queue pointers.

Sanity suite green (21 passed).

## Deliberately not done (scope call)

- **Functional `corpus/` references kept**: `thai-native-draft.py` reads
  `corpus/curated/<register>/` at runtime — few-shots are *not* baked in, contrary to
  the review's framing. Exemplar `<!-- source: corpus/... -->` comments are mandated
  provenance. Harness notes and CLAUDE.md pointers in kode-thai kept — accurate
  in-repo.
- **No bundle-preprocessor comment-strip**: would only serve the school distribution
  boundary and perturbs the eval bundle; dropped when chakrit scoped to this repo.

## Open threads

- The distribution-boundary findings (corpus paths, harness refs invisible to a school
  consumer) remain unaddressed by design — chakrit handles school sync himself;
  the candidate mechanism discussed was a comment-strip at school import time.
- `review.md` sits untracked at repo root — chakrit's audit input; left as-is.
