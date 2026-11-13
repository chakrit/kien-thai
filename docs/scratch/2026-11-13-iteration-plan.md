<!-- not spec/decision because: a working plan; settled rulings live in decisions/ and
     committed tasks in work-queue.md, and this file sequences them -->

# Iteration plan — restart after the 2026-07 pause

Restarts the generate → review → graduate loop that stalled on 2026-07-27. Built on the
findings in [`2026-11-13-once-over.md`](2026-11-13-once-over.md) (IDs like M5, T1, C4
refer to that file) and on two rulings made while planning:

- [`../decisions/2026-11-13-matrix-review-methodology.md`](../decisions/2026-11-13-matrix-review-methodology.md)
  — drafters × auditors matrix, ear marks drafts blind, auditors scored against the ear,
  reference drafts, ear vs dictionary authority split, scores inform and never gate.
- [`../decisions/2026-11-13-corpus-pre-chatgpt-cutoff.md`](../decisions/2026-11-13-corpus-pre-chatgpt-cutoff.md)
  — corpus entries must predate 2022-11-30, proven by an archive capture.

The plan is shaped around one constraint: **chakrit's ear is the only judge and the
scarcest resource**, so every phase either spends no ear time or spends it on a small,
pre-ordered batch in the browser review UI.

## Principles

- The ear is the terminal judge; no LLM judges Thai. Auditors flag; scores inform and
  never gate. The work is qualitative — the ruleset will never be complete, and "good
  enough" is chakrit's call.
- Native pairs before rules; rules need provenance. Agents draft pairs, notes, and rule
  wording; chakrit batch-reviews them.
- No single backend defines quality: every model drafts and audits in a matrix.
- **The repo as a pipeline of defined steps** (direction only — not acted on yet). Each
  process — corpus verification, pair staging, generation, ear review, graduation —
  should eventually be a named step with declared inputs, outputs, and a gate type
  (script, agent, or ear), so the whole loop could be rebuilt as steps in a generic
  workflow engine (n8n is chakrit's example). New work in this plan should already take
  that shape where it costs nothing extra.

## Status of the iteration-15 gate

`work-queue.md` blocked all agent work on chakrit's iteration-15 review. Chakrit will
review iteration-15 (2026-11-13), but the gate now covers only the drafter question;
hygiene, the Phase 1 pairs, and corpus growth proceed without it.

## Phase 0 — Hygiene and matrix plumbing (agent; no ear)

English or code only; nothing here writes Thai.

1. **Stamp every run** (T1): pin `--model`; record model ID, CLI version, commit + dirty
   flag, bundle hash, register, timestamp in `meta.json`; ollama digest for Typhoon.
2. **Guard iteration numbering** (T4): refuse an unpinned run when `INDEX.md` lists
   iterations that do not exist locally.
3. **Bare baseline** (T5): run baseline subprocesses from a temp cwd outside the repo so
   the CLI cannot load this repo's `CLAUDE.md`; verify.
4. **Matrix mode:** drafts × auditors, one audit pass, no fixes; auditor output in a
   span-addressable form (quoted span + slug). `_run_loop` accepts an external pass-0
   draft (T2) so a native draft can go through the loop; Typhoon joins `BACKENDS`.
5. **Scoring script:** span-overlap matching of flags to marks; per-auditor agreement and
   catch rate, per-drafter failure profile, all-missed list, false positives on
   reference drafts; renders `feedback.md` and the trend row.
6. **Register→corpus map into `thai-native-draft.py`** (T3); fail loudly on zero files.
7. **kode-thai guards** (C10): pass cap, oscillation check, one line that CLEAN ≠
   natural.
8. **Mechanical content fixes** (C6, C12, C7's dangling ref): ซึ่ง budget wording in
   `ai-tells.md:16`; forbidden-phrase loader handles `...`; the nonexistent collection
   reference in `grammar.md:157`.
9. **Housekeeping** (T7–T9): dedupe the Typhoon model ID and ollama call; `ace.toml`
   and the CLAUDE.md skill list; stale `typhoon_pass.py` comment.
10. **Recall harness** (T6, M8): CLI error ≠ miss; a hit must be a cited finding;
    stamped per-iteration report; in-document seeding into native corpus paragraphs.
11. **Issue #2:** document "prompt the native model in Thai, by function, specifically"
    in `scripts/README.md` and SKILL step 0.

## Phase 0.5 — Browser review UI (agent; before any ear session)

Replaces reading `.md` files in iA Writer and editing gitignored `output.md`.

- **Server:** one Python stdlib script (`http.server`), in a visible tmux pane, bound to
  `0.0.0.0`, port from the control agent (8000–9000), reachable from either Mac over the
  tailnet. `GET` a batch, `POST` a response.
- **Page:** one static HTML file, plain JavaScript and CSS, no build step.
- **Generic batches** written by the agent; the page renders any of them:
  - *drafts to mark* — arms shuffled and neutrally labelled; auditor flags hidden;
    ordered by distance from the reference draft;
  - *comparison* — for iteration-15, arms blind, key applied after verdicts;
  - *pair review* — agent-drafted pairs and notes, batch approve/cull/edit;
  - *owed rewrite* — a flagged line, type the "after";
  - *reference draft* — the eval prompt and an empty editor;
  - *corpus spot-check* — excerpt, voice notes, date evidence.
- **Marks:** select any Thai span → note, optional rewrite. Stored as quoted span +
  character offsets.
- **Saving:** autosave to tracked `workspace/iteration-N/verdicts/<batch>.json`
  (`.gitignore` exception), so verdicts sync through git.
- Out of scope: accounts, multi-user, hosting beyond the tailnet, editing skill files.

## Phase 1 — Close the loop on evidence in hand (agent stages; ear session 1)

- Agent drafts candidate pairs from every iteration 8–10 finding that has chakrit's
  "after", with notes and the trace.
- Agent lists findings still missing an "after" (iter-8 ②③④, iter-10 line 7) and the
  shipped-example defects (C4: `เจ้าของร้าน` in Example 2, em-dashes in Good/After
  text, Example 4's notes; C5: unsourced Examples 1–5).
- **Ear:** batch-review the pairs; write owed "afters"; rule on the defective examples;
  PR #3 (`ticket` vs `ตั๋ว`, as a pair).
- Agent lands approved pairs and adds them to the recall seed.

## Phase 2 — Corpus verification and growth (agent with Chrome; ear spot-checks)

- **Verify existing:** backfill `published:` on the 43 curated prose entries with
  archive-capture evidence; move failures and undatable entries (including the three
  `aws-thailand-*`) to `corpus/quarantine/`.
- **Grow**, pre-2022-11-30 only, archive-dated: official notices, news-wire, academic
  prose, a second personal-blog author, b2b-formal replacements. Current tech and
  marketing vocabulary will be thin; accepted.
- **Tooling:** Claude in Chrome (WebFetch is blocked on most Thai sites); which Mac's
  Chrome is asked at the start of the phase.
- **Ear:** short spot-check batch on voice notes. Then lift excerpts into
  `exemplars.md` for the registers that ship none today (news, b2b-formal, official).

## Phase 3 — Reference drafts and drafter probe (ear; ~1 session)

- **Reference drafts:** chakrit writes one per eval prompt in the UI, for the registers
  he writes day to day; held out of the bundle.
- **Drafter probe:** Typhoon 2.5 (Qwen3 30B-A3B), Typhoon 2.1 (Gemma3 12B),
  Typhoon-S-ThaiLLM-8B, optionally a ThaiLLM-8B variant, on two evals. Pulls are
  resource-heavy — chakrit's go first, `nice -n 19`. Ear ranks blind; one native drafter
  goes forward.

## Phase 4 — Iteration-15 review, then iteration-16 matrix

- **Iteration-15:** chakrit's review in the UI, arms blind (10 outputs).
- **Iteration-16 matrix,** five evals:
  - drafters: Claude + skill, codex + skill, the chosen native drafter (few-shot), and
    bare Claude (the no-skill premise check);
  - auditors: Claude, codex, plus a with/without-severity-tags pair for one auditor
    (tests whether the auditor should see hard/soft);
  - ear marks 20 drafts blind; scoring as in the decision.
- **Fix-loop read:** native drafter → kode-thai loop with the best-scoring auditor, five
  final outputs, a lighter read.
- **Then decide** which slug owns run-ons from where auditors filed them.

## Phase 5 — Steady state

Each iteration: graduate the last session's marks → regenerate the skill-dependent
drafts → audit matrix → one ear session → trend row. Held-out prompts (official,
b2b-formal, academic) join from iteration-17 so rules meet prompts they were not derived
from; prompt Thai is drafted through fugu and ratified by chakrit. Whether the ceiling
is reached is chakrit's call, informed by the trend.

## Ear budget

| Session | Phase | Content                                            | Est.    |
| ------- | ----- | -------------------------------------------------- | ------- |
| 1       | 1     | Pair batch-review, owed "afters", PR #3            | ~60 min |
| 2       | 2     | Corpus spot-check                                  | ~30 min |
| 3       | 3     | Reference drafts + drafter probe ranking           | ~90 min |
| 4–5     | 4     | Iteration-15 review (10 outputs)                   | ~2×50   |
| 6–8     | 4     | Iteration-16 marks (20 drafts) + fix-loop read (5) | ~3×80   |

Estimates assume ~10 minutes per short Thai output; correct them after session 1.

## Rulings made while planning (2026-11-13)

| Question                             | Ruling                                                    |
| ------------------------------------ | --------------------------------------------------------- |
| Retire or review iteration-15        | chakrit reviews it; gate narrowed to the drafter question |
| Corpus cutoff                        | Pre-ChatGPT (before 2022-11-30), archive-dated            |
| Which auditor defines `skill-clean`  | Replaced by the matrix methodology                        |
| Run-on slug ownership                | Deferred to the first matrix                              |
| Severity tags visible to the auditor | Tested inside the iteration-16 matrix                     |
| How marks become skill content       | Agent drafts, chakrit batch-reviews                       |
