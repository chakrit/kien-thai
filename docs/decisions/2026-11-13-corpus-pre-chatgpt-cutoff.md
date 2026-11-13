# 2026-11-13 — Corpus sources must predate ChatGPT

**Status:** Accepted · 2026-11-13

**Sharpens:** decision 6 of
[`2026-05-30-exemplar-first-pivot.md`](2026-05-30-exemplar-first-pivot.md), which called
pre-2022 sources "safer" without drawing a line.

**Scope:** which texts may enter `corpus/curated/` as native-voice evidence, and how a
text's date is proven. Does not govern the Royal Society / reference-grammar material in
`docs/vendor/`, which is cited for mechanics, not voice.

## Context

Every rule and exemplar in kien-thai is supposed to trace to `corpus/`. A corpus entry
that was itself AI-drafted teaches the skill AI Thai while labelling it native, and
nothing downstream can catch that: the auditor and the drafter share the prior that
produced it. Three b2b-formal entries (`aws-thailand-*`) were already flagged as likely
AI-drafted in 2026-05.

Growing the corpus came up again after a four-month pause. Chakrit first floated a
looser line — "before Claude Opus 4.6" (released 2026-02-05) — on the reasoning that
earlier machine Thai was clumsy enough to screen by ear. That reading was weighed and
rejected: screening costs the ear on every entry, and AI-drafted text that a person
edited keeps subtle calque that is hard to hear.

## Decision

1. **Cutoff:** a corpus entry must have been published **before 2022-11-30**, the day
   ChatGPT was released. Chakrit's ruling: *"stick with existing ruling of pre-gpt."*
2. **Proof of date:** a dated archive capture (Wayback Machine snapshot before the
   cutoff, quoted from the capture itself) or a dated print/PDF issue. The live page's
   own date does not count — live pages get edited.
3. **Existing entries:** every curated entry gets a `published:` field with its
   evidence. Entries that fail the cutoff or cannot be dated move to
   `corpus/quarantine/`, not into deletion, so their history stays inspectable.

## Consequences

- Corpus growth starts with registers that have deep pre-2022 archives: official
  notices, news, academic prose. Current tech and marketing vocabulary will be thinner;
  that gap is accepted rather than filled with post-cutoff text.
- The open human-queue item to re-vet the `aws-thailand-*` entries becomes an agent task
  under point 3.
