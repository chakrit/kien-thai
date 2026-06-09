# Review protocol — the outer loop

**Status:** accepted

kode-thai is the **inner loop**: audit→fix until *skill-clean* (the ruleset finds no
citable violation). This protocol is the **outer loop**: a skill-clean output goes to the
native ear for the *chakrit-clean* verdict. The gap between the two terminals is the
measurement. Closing it across iterations is the product improving; a gap that stops
shrinking is the prompt-only ceiling.

Counterpart to `inline-iteration.md` (the generate protocol). Direction and rationale:
`docs/decisions/2026-05-30-exemplar-first-pivot.md`.

## Definitions

- **skill-clean** — kode-thai's terminal. The audit pass returned `CLEAN`; the ruleset
  finds nothing. Equals ruleset-coverage, not naturalness.
- **chakrit-clean** — the outer terminal. The authoritative native reader finds nothing to
  red-ink. The actual quality bar.
- **recall-miss** — a finding for which a slug already exists that should have fired in
  the audit pass but did not. An auditor-recall failure.
- **coverage-gap** — a finding no slug covers. A genuine ruleset hole.
- **reads-flat** — passes every rule yet has no voice. The additive gap no slug catches;
  the most important signal and the hardest to act on.

## The lever

The agent does everything except the verdict. Chakrit's time is spent only on the
irreducible native call — read, judge, mark. Prep, classification, recording, routing, and
aggregation are all agent work. This is deliberate: the judge is both the bottleneck and
the spec, so the protocol shrinks the human surface to the ear alone.

## Workflow

1. **[agent] Gather.** Enumerate skill-clean outputs for the iteration (`with_skill`,
   `converged: true`). For each, pull `output.md`, the pass that returned `CLEAN`, and the
   audit trace (which slugs did fire).

2. **[agent] Stage.** Open each output in iA Writer (Thai renders wrong in terminal
   pagers; the command is in CLAUDE.md). **Open exactly one file at a time — never several
   at once — and before opening it, state the verdict format: how and where chakrit marks
   corrections.** Register labelled, audit trace visible so chakrit can see what the
   auditor claimed was clean. Pre-fill a record with identity + `skill_clean` fields;
   leave findings blank.

   Editing the staged `output.md` inline is an accepted way to give the verdict — the
   rewrite *is* the before/after pair's "after". But `output.md` is gitignored evidence
   that regenerates, so harvest the edit immediately: diff it against the pass that
   returned CLEAN (`pass-0.md` when it converged at pass-0) to recover the "before", lift
   the pair into the queue, and do not treat `output.md` as the durable home.

3. **[chakrit] Verdict.** Read end-to-end — not span-scan. Call it: chakrit-clean, yes/no.
   If no, mark each offending span and the correction in your own words. If the piece is
   technically fine but reads AI-flat with no discrete span, flag `reads-flat`.

4. **[agent] Classify** each finding against the skill: `recall-miss` (a slug exists that
   should have fired — grep to confirm) or `coverage-gap` (none does). Confirm only the
   ambiguous calls with chakrit. `reads-flat` carries forward as a verdict flag, not a
   finding.

5. **[agent] Record** structured entries into the iteration's **tracked** feedback
   (`workspace/iteration-N/feedback.md` — the eval subdirs are gitignored and will not
   survive). Compute the aggregate table.

6. **[agent] Route — collect, do not apply.** Under 1-by-1 discipline even agreed items
   queue; no skill edits land mid-review.
   - before/after pairs → candidate exemplars (register-tagged) for the exemplar work.
   - recall-misses → the known-bad set for the auditor-recall harness, with the slug that
     should have fired.
   - coverage-gaps → the trace-before-write queue.

7. **[agent] Update** `workspace/INDEX.md` (Review → `reviewed`, link the feedback) and
   the plateau tracker.

## Record format

One block per skill-clean output:

```
iter / eval / backend / config · skill_clean: yes (passes_to_clean: N)
chakrit_clean: no · reads_flat: no
findings:
  - span:       "<offending Thai>"
    issue:      "<what is wrong — chakrit's framing>"
    correction: "<native rewrite — the pair's 'after'>"
    class:      recall-miss · slug: f6/ko-resumptive
  - span:       "<…>"
    correction: "<…>"
    class:      coverage-gap · slug: (none; proposed …)
```

Per-iteration aggregate — the dashboard:

| Metric                      | Meaning                                               |
| --------------------------- | ----------------------------------------------------- |
| CLEAN-but-flawed rate       | skill-clean outputs the native ear still red-inks     |
| recall-miss : coverage-gap  | auditor blind to existing rules vs ruleset incomplete |
| per-slug recall-miss counts | which rules under-fire in the audit pass              |
| reads-flat count            | passes every rule but has no pulse                    |

## Reading the dashboard

- **Mostly recall-misses** → the ruleset is adequate, the auditor is blind. Invest in
  exemplars and the audit bundle, not new rules.
- **Mostly coverage-gaps** → genuine holes. Trace-before-write; land as pairs first.
- **High reads-flat** → the subtractive loop has sanded out voice. A pure exemplar-quality
  problem; no rule will fix it.
- **Numbers flat across iterations** → the prompt-only ceiling. Stop adding; per the
  decision record, that is the answer, not a cue to push harder.
