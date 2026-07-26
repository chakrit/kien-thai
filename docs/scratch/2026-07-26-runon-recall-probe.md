<!-- not spec/decision because: a probe result awaiting chakrit's read; it proposes
     where the fix goes but rules nothing. -->

# 2026-07-26 — Run-on recall probe: the rule fires, the slug is wrong, context eats it

Targeted recall check authorized by chakrit ("run now") on the cross-cutting run-on /
under-segmentation signal. Three claude audit calls, not the ~74-call `-m recall`
baseline. Runner: `tests/probe_runon_recall.py`. Raw:
`workspace/probes/runon-recall.json` (gitignored).

## What was asked

Run-ons survive to `CLEAN` across three drafters (Fable-5 F1, iter-9 news ¶4, iter-10
tech-doc line 7). Two rules should catch them — `mixed-sentence-length` and
`conceptual-seam-break`. Is the auditor failing to fire them at all (coverage-gap) or
firing them isolated and losing them in a full document (recall-miss / dilution)?

## Inputs

All native-verified bad, quoted verbatim from tracked evidence:

| Probe | Input |
| --------------------- | -------------------------------------------------------- |
| `fable-f1-isolated` | Fable-5 F1 span, chakrit's verdict "run-on; too many ideas chained" |
| `it10-line7-isolated` | iter-10 tech-doc line 7 at pass-1 — the prose codex declared CLEAN, before chakrit's break mark |
| `it10-full-doc` | the whole pass-1 document, reproducing the in-context condition |

## Result

**Neither hypothesized slug fired anywhere.** `mixed-sentence-length` and
`conceptual-seam-break` were cited zero times across all three probes — isolated or in
context. The premise that "the sentence-length rule is not firing" was aimed at the
wrong rules.

**But the phenomenon was caught — under a different slug.** On
`it10-line7-isolated` the auditor cited **`mid-paragraph-period`** and landed on the
exact seam chakrit marked, quoting the join and noting a reader takes the two tokens
either side as one unit on first pass. Independent agreement with the native verdict,
at the right position, from a different instrument.

**In the full document that finding vanished.** `it10-full-doc` returned four issues —
`missing-cha-modal`, `khong-chain`, `comma-apposition`, `no-recap-close` — and none of
them was the line-7 seam. Same auditor, same prose, same bundle; the only difference is
how much surrounded it.

## Reading

1. **Recall-miss, dilution kind — not a coverage-gap.** A rule covers this and the
   auditor can find it. It loses it when the document gives it more to look at. No new
   rule is warranted; per the exemplar-first pivot the fix is anchoring and a pair in
   the audit bundle, not more rule text.
2. **A taxonomy error on our side.** We filed run-ons under sentence-length; the auditor
   files them under punctuation/boundary (`mid-paragraph-period`). Worth deciding which
   is the real home before anchoring anything — anchoring the wrong slug fixes nothing.
3. **The discourse case is untested.** iter-9 ¶4 is a whole-paragraph structural
   failure with no single span, so it was not probed. The `reads-misstructured` question
   stands untouched by this result.

## Second finding, unplanned — auditor variance across backends

`it10-full-doc` is prose the **codex** auditor terminated as `CLEAN` at pass 2. The
**claude** auditor, same bundle, same register, found four citable issues. So
*skill-clean is backend-dependent*: the terminal the loop converges to is a property of
which model audits, not of the prose.

That is a measurement problem, not a prose problem. The review protocol reports
CLEAN-but-flawed as though `skill-clean` were one bar; it is at least two. Nothing in
`docs/spec/review-protocol.md` currently says which auditor defines the terminal.

## Proposed next steps

Not applied — these need chakrit's call:

- Decide the home slug for run-ons: `mid-paragraph-period` (where the auditor already
  puts it) or `conceptual-seam-break` (where we assumed it lived).
- Land the line-7 case as a before/after pair once chakrit supplies the "after" — the
  break position is his mark, so the pair is native-sourced. Then re-run this probe to
  see whether the in-context miss closes.
- Name the auditing backend in the review protocol, or audit with both and treat the
  union as skill-clean.
