<!-- not spec/decision because: an audit finding-list; each item resolves into an edit,
     a queue entry, or a ruling elsewhere. Nothing here is itself durable. -->

# 2026-07-26 — Documentation pass

Full sweep of `docs/`, `CLAUDE.md`, `workspace/INDEX.md`, and the queues. The structure
is healthy — the 2026-07-11 single-gate migration and the 2026-07-26 index test did
their job. What follows is drift on top of a sound layout, plus one unfiled artifact.

## Gaps

1. **`review.md` sits untracked at the repo root.** It is the 2026-07-17 self-talk audit
   of the *distributed* skill bodies. The kien-thai half was applied in `793bd2d`; the
   **kode-thai half and every distribution-boundary finding are unapplied and appear in
   no queue**. `decisions/2026-05-13-register3-source-list-vetting.md:8` cites it by name,
   so the citation dangles against a file git does not have. Resolve: file it as
   `scratch/2026-07-17-skill-self-talk-audit.md`, queue the open half in `work-queue.md`,
   repoint the decision.

2. **`workspace/probes/` is undiscoverable.** Gitignored, holds `fable5-eval1-baseline.md`,
   `runon-recall.json`, `thai-authorities.md` — all cited from scratch notes as evidence.
   Named in neither the CLAUDE.md repo map nor `workspace/INDEX.md`. A fresh session
   reading a probe note cannot find what it refers to.

3. **CLAUDE.md's `tests/` tree is stale.** Missing `test_docs_index.py`,
   `probe_runon_recall.py`, `probe_thai_authorities.py`. `test_docs_index.py` enforces
   the *docs* index but nothing enforces this tree, so it rots silently.

4. **No guide covers the Typhoon arm.** `guides/running-evals.md` documents claude and
   codex only. `thai-route.sh`, `thai-native-draft.py`, `typhoon_pass.py`, and
   `compare_arms.py` — the exact machinery the repo's one open question turns on — are
   documented nowhere operational. `spec/model-route.md` describes the design, not the run.

## Stale text

5. **`spec/inline-iteration.md` §Drivers is broken by the 2026-07-26 edit.** It announces
   "Three ways to run the inline loop", then lists a binding-constraint section, `### 2.
   Manual subagent`, `### 3. Manual Codex`. Driver 1 was superseded and removed; the count
   and the numbering were not repaired. Two drivers exist.

6. **`workspace/INDEX.md` legend contradicts its own rows.** `—` is defined as "no
   generation run", but iterations 12 and 13 *were* generation runs (the Claude arms for
   the iter-11/14 comparisons) and carry `—`. Rows 2–6 are placeholders for runs whose
   workspace was never committed.

7. **`work-queue.md` → "Framing experiments" predates the model-route decision.** Status
   dated 2026-07-03; it still poses the `corpus/native-exemplars/` vs
   `references/exemplars.md` question its own status paragraph says was already resolved.

## Duplication

8. **The Typhoon evidence audit is written out four times.** Near-verbatim in the decision
   addendum, `spec/model-route.md` §Open, the `work-queue.md` rerun item, and the
   `human-tasks-queue.md` hold note. Four copies drift the moment the evidence changes —
   which is precisely what the next run does. One canonical statement (the spec) and three
   pointers.

9. **Queue archive bloat.** `research-queue.md` is 374 lines, of which roughly 200 are
   "Below is the original entry for archive" under items resolved back in May (ๆ-spacing,
   personal-blog vetting, Fictionlog). `work-queue.md` carries the same pattern for browser
   tooling and framing experiments. A resolved item wants one line and a link to where the
   resolution landed; the archive body is what git history is for.

10. **Two hand-synced lists of the same scratch files.** `scratch/prior-art.md` §"Still
    standalone in scratch" and the scratch table in `docs/README.md`. Only the latter is
    test-enforced, so the former is the one that will go wrong.

## Not findings

The routing gate, the three-queue discovery rule, the review protocol, and the decision
chain are coherent and mutually consistent. `docs/README.md`'s index is complete against
the filesystem. The exemplar-first pivot and its 2026-07-26 revision read cleanly in
sequence, and the revision's confidence downgrade is propagated everywhere it is repeated
(that the repetition itself is finding 8 is a separate matter).
