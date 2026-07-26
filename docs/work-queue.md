# Work queue

Decided work items awaiting design/build. Distinct from `research-queue.md`
(speculative items needing evidence) and `decisions/` (point-in-time rulings,
incl. prose-direction judgements). Items here are committed scope — the question is
*how*, not *whether*.

---

## Next agent step — inline-driver, then exemplar expansion ← reordered 2026-07-27

**Reordered (chakrit, 2026-07-27).** The co-generated comparison run went first and is
now iteration-15, awaiting the ear. The 2026-07-07 ordering below predates the
model-route ruling that made that run the gating evidence, and the run turned out to
need no new driver — only an iteration pin. A and B resume once iteration-15 is
reviewed, since its verdict decides what the driver is measuring.

**Decided (chakrit, 2026-07-07).** Order set for the two candidate next steps from the
exemplar-first pivot: **(A) inline-driver prototype first, then (B) Phase 3
exemplar expansion.** Rationale (per
[`scratch/session-2026-05-30-exemplar-pivot.md`](scratch/session-2026-05-30-exemplar-pivot.md)):
the inline-driver infra makes running and measuring exemplar batches cheaper, so B gets
cheaper after A.

- **A — Inline-driver prototype (harness-neutral).** Session-driven iteration reusing the
  bundle preprocessor + prompt templates instead of the subprocess CLIs. Spec:
  [`spec/inline-iteration.md`](spec/inline-iteration.md).

  **Re-specced 2026-07-26. The question to build against is "we need an eval loop —
  how do we build a harness-agnostic one?"** Not which available tool can drive it.
  The original entry named Claude Code's `Workflow` tool; chakrit rejected it —
  *"your workflow tool is tied to your proprietary harness. i don't want it… this is
  exactly the harness-lock-in problem that using the workflow would produce and then
  locking this skill into claude code entirely."*

  The eval loop is how this skill is built, validated, and iterated, so binding it to
  one vendor's harness binds the skill itself, however portable the rule content looks.
  Plain Python, shell, ordinary test harnesses. The capability is **not** optional —
  the repo's premise is that agent-generated Thai *without this skill* is bad, so
  measurement is the product — but it ships portable or it does not ship.
- **B — Phase 3 exemplar expansion.** Sweep `corpus/curated/` for anchor exemplars, lift
  short register-tagged excerpts, stage as **candidate before/after pairs** in
  `references/examples.md` / `exemplars.md`, hand chakrit an approve/cull list (agent
  stages, native ear ratifies). Then the wider arc: exemplar inversion + SKILL.md/reference
  reframing around pairs.

**Block.** None. A is the immediate next build.

---

## Rerun the Typhoon-vs-Claude comparisons co-generated ← ran 2026-07-27 as iteration-15

**Status.** Token spend approved (chakrit, 2026-07-27) and the run is iteration-15 — both
arms, all five evals, one iteration tree, one skill state. This also reordered the
2026-07-07 call that put the inline driver first: that ordering predates the model-route
ruling that made this run the gating evidence, and the run needed no new driver.

The harness could not co-generate before this: `typhoon_pass.py` and the pytest
`iteration_dir` fixture each minted their own directory, so the arms always landed apart.
`lib.resolve_iteration_dir()` now honours `EVAL_ITERATION`, both callers use it, and
`lib.claude_arm()` prefers the same-iteration arm and marks the pair co-generated —
`compare_arms.py` only prints the contamination caveat when it is earned. The pin also
removes the xdist split below, since workers share it.

**Left to do.** Chakrit's ear on the five `workspace/iteration-15/*/comparison.md`;
verdicts → `iteration-15/feedback.md`; flip the INDEX row. That settles the open question
in
[`decisions/2026-07-26-model-route-revises-exemplar-first.md`](decisions/2026-07-26-model-route-revises-exemplar-first.md)
and `spec/model-route.md` §Open — whether the native drafter wins on voice, or at all.

---

## Finish the self-talk sweep — kode-thai + the distribution boundary ← added 2026-07-27

**Need.** The 2026-07-17 audit of the *distributed* skill bodies was applied to kien-thai
only (`793bd2d`). Its kode-thai findings and every distribution-boundary finding are
still open, and until 2026-07-27 the finding-list itself was an untracked file at the
repo root. Now filed:
[`scratch/2026-07-17-skill-self-talk-audit.md`](scratch/2026-07-17-skill-self-talk-audit.md).

**Scope.** `skills/kode-thai/SKILL.md`: the two-tier-injection aside and the "follow the
iteration discipline in the project `CLAUDE.md`" line both point at maintainer files a
consumer never receives; the `skills/kien-thai/scripts/` path reaches into the sibling
skill's internals and should reduce to a skill-name handoff. Separately, decide the
in-body provenance convention — a defined confidence tag (cf. de-slop's
Empirical/Curated/Field legend) instead of dated session refs.

**Out of scope by design.** The `corpus/` references in kien-thai are *functional* —
`thai-native-draft.py` reads `corpus/curated/<register>/` at runtime. Those paths are not
narration.

**Block.** None. School sync stays chakrit's.

---

## Thai-aware markdown wrap tooling

**Need.** Enforce the CLAUDE.md hard-wrap-90 rule on Thai-heavy markdown.
Naïve codepoint-based wrapping overshoots ~10–15% on Thai prose because Thai
combining marks (vowel signs, tone marks) are zero-width but count as
codepoints. Thai also has no word spaces, so line-break candidates need
dictionary-based segmentation rather than splitting on whitespace.

**Scope.** Uniform across every `.md` the repo produces or maintains —
`SKILL.md`, `references/*.md`, `docs/**/*.md`, `CONTRIBUTING.md`, eval feedback
files. Includes both authoring help and CI enforcement.

**Findings so far.**

- `pythainlp` is already in deps and provides `word_tokenize` for
  segmentation.
- `wcwidth` handles display-width counting for the codepoint-vs-display
  problem.
- ICU4C is the heavier alternative; full Unicode-segmentation, but a much
  bigger dependency.

**Open design choices.**

- Stack: Python + pythainlp + wcwidth, vs ICU, vs something else.
- Integration point: standalone CLI, pre-commit hook, generator post-
  processor, or all three.

**Block.** Do not hand-fix Thai-prose wrap regressions until this exists —
the manual fixes won't survive the next eval generation pass.

---

## Thai dictionary lookup capability

**Need.** When uncertain about Thai spelling or word usage, both Claude and
contributors should be able to verify against an authoritative Thai source
rather than rely on memory or web search. Today there is no project-local
way to confirm `กฎ` vs `กฏ`, `นัย` vs `นัยยะ`, etc.

**Scope.**

- Source: Royal Institute Dictionary published forms? pythainlp-bundled
  dictionary? other?
- Storage: gitignored or checked in (depends on size and license).
- Access: CLI tool, Python helper for tests, or raw file lookup.

**Open.** Licensing — RID dictionaries may not be redistributable, in which
case this becomes a per-developer download with a setup script rather than
a checked-in resource.

**Block.** Do not make confident orthography claims in skill or contributor
docs until this exists. Today every spelling call is from-memory and
unverifiable.

---

## Browser tooling for Thai source vetting ✅ unblocked 2026-05-13

**Status.** Claude-in-Chrome MCP wired up. Used for the 2026-05-13 vetting
pass — see [`scratch/source-vetting-2026-05-13.md`](scratch/source-vetting-2026-05-13.md).
Worked well for GotoKnow, readthecloud.co, storyloggroup.com, Pantip.
Minimore continues to return empty body even via Chrome (same JS-render
block as WebFetch); use Wayback / paste-in for those.

**Outstanding constraint.** Some sites still don't yield prose:

- Minimore — SPA renders empty in the MCP context. Use Archive.org or
  user paste-in.
- Subscription-gated content (if ever needed) would require logged-in
  profile; current setup is clean profile, read-only.

The original block-condition on the broadened Register 3 Models list is
resolved — `references/register.md` is now evidence-backed.

Below is the original entry for archive.

---

**Need.** Autonomous source-research for Thai prose models is blocked because
WebFetch hits 403 / empty-render across the primary candidate sites (GotoKnow,
readthecloud.co, minimore.com, fungjaizine.com). Without rendered prose,
grammar-discipline tier verdicts can't be made — see
[`research-queue.md`](research-queue.md) → "Vet non-tech personal-blog source
candidates."

**Decided.** Wire up a Chrome / browser MCP so Claude can navigate JS-rendered
pages, get past bot blocks, and extract verbatim Thai prose. Chakrit (2026-05-13)
confirmed this is the unblock path.

**Open design choices.**

- Which MCP: Chrome DevTools MCP, browser-MCP, or playwright-mcp.
- Auth/profile: should the browser run with a clean profile or chakrit's
  logged-in profile (relevant if we ever want subscription-gated content).
- Scope: vetting reads only, no form-submission / write actions.

**Block.** Do not ship the broadened Register 3 Models list (currently
provisional in `references/register.md`) as evidence-backed until this lands
and the vetting pass completes.

---

## Framing experiments for Thai-native generation

**Status (2026-07-03): experiments #1/#2 landed in the default bundle** — no separate
configs were needed. `references/exemplars.md` (curated native corpus excerpts) exists
and `kien_thai_bundle` pins it last, adjacent to the task prompt (`tests/lib.py`);
the exemplar home resolved to `skills/kien-thai/references/exemplars.md` (the
`corpus/native-exemplars/` candidate was never created — treat the "where do exemplars
live" open question below as closed). Remaining scope: #3
`with_skill_persona`, plus register coverage — after register-scoping, the
`marketing-b2b-formal` / `marketing-fintech-warm` / `marketing-retail-tech` /
`official` bundles ship no before/after pair and no native exemplar, and `news` has
no native exemplar — `exemplars.md` covers `explainer`, `marketing-saas-sme`, `academic`,
and `personal-blog` only (the TODO comment that used to record this is gone; the gap is
not). Committed direction per
[`decisions/2026-05-30-exemplar-first-pivot.md`](decisions/2026-05-30-exemplar-first-pivot.md).

Below is the original entry for archive.

---

**Need.** Bundle ordering and exemplar proximity matter for shifting
Claude's output distribution toward Thai-native prose. Literature
(multilingual ICL, English-accent paper, persona effect, multilingual
CoT) confirms prompt-level techniques have measurable — though
"marginal or inconsistent" — effects. The biggest under-used lever in
the current harness: `examples.md` sits mid-bundle alphabetically, so
the most concentrated native-Thai prose in the bundle is *not* adjacent
to the task prompt where attention recency would amplify it.

**Scope.** Add new harness configs alongside `with_skill` and `baseline`
in `tests/lib.py:CONFIGS`. Three ranked experiments per the framing
investigation:

1. `with_skill_reordered` — `examples.md` last in bundle. 5-line change
   in `kien_thai_bundle()`. Zero new content.
2. `with_skill_primed` — adds curated native-prose exemplars from
   `corpus/native-exemplars/<register>.md` after `examples.md`. Needs a
   small curated corpus (2–3 short pieces per register) before this can
   run.
3. `with_skill_persona` — register-keyed Thai-language persona prepend
   naming a specific publication/voice. Tested against #1+#2.

**Findings so far.** Literature lens, recommended ordering, and the
"don't force Thai-language CoT for mid-resource languages" caveat
captured in
[`scratch/framing-investigation-2026-05-21.md`](scratch/framing-investigation-2026-05-21.md).

**Open design choices.**

- Whether the three variants A/B independently or stack into a single
  `with_skill_primed` super-variant.
- Where curated exemplars live (`corpus/native-exemplars/` vs
  `references/exemplars.md`).
- How to measure improvement — `test_quant.py` advisory heuristics +
  human review (the existing convention), or add LLM-judge later.

**Block.** None. Independent of in-flight skill work.

---

## Eval harness: xdist splits iteration directory across workers ✅ workaround 2026-07-27

**Status.** `EVAL_ITERATION=N` pins every caller to one tree
(`lib.resolve_iteration_dir()`), which is what the fix candidates below were reaching
for — workers no longer each mint their own. Unpinned runs still split, so the guidance
stands: either pin or run serial. Closing this properly means resolving the dir in the
controller pre-fork so the default is safe too.

Below is the original entry for archive.

---

**Need.** `tests/generate/conftest.py` exposes `iteration_dir` as a
session-scoped pytest fixture that calls `next_iteration_dir()`. Under
`pytest-xdist -n N`, each worker has its own session, so each worker mints
a fresh iteration directory. A single `pytest -m generate -n 4` run produces
N iteration dirs containing partial slices of the matrix instead of one
complete iteration.

**Repro.** Iteration-7 generation (2026-05-11): one `pytest -m generate -n 4`
run produced 12 outputs split 6/6 across `iteration-7/` and `iteration-8/`.
Manual consolidation required before review.

**Fix candidates.**

- Resolve the iteration dir in the xdist controller pre-fork and broadcast
  via env var or `--iteration-dir` CLI flag.
- Use `tmp_path_factory`-style shared-state mechanism that xdist plugins
  already support.
- Drop session scope; have one designated rank-0 worker write a manifest
  the others read.

**Block.** Do not run `-m generate -n >1` until fixed, or expect to
manually merge iteration directories afterward.

---

## Harness efficiency — SDK caching + code-side mechanical audit

**Status (2026-05-30): recorded, not started.** Tactical token/latency wins surfaced
while scoping the refactor. Orchestration is already deterministic Python
(`tests/generate/conftest.py`); the LLM is already just generate + audit. So the wins are
in bundle×passes and the LLM calls, not the orchestration language.

**Levers, ranked.**

1. **Prompt caching via the Anthropic SDK.** The bundle is a static prefix reused across
   every pass and every eval in a register — the ideal cache target (~90% off the static
   part on a hit). `meta.json` already records `cache_read` / `cache_creation`. Cheap
   first move: check whether the current `claude -p` CLI runs hit cache at all; if ~0,
   move the generate/audit calls to the SDK for explicit `cache_control`.
2. **Code-side mechanical audit.** `forbidden-phrases` + connective density are already
   grepped in `test_quant.py` with no LLM. Grow that into a regex + pythainlp linter for
   the pattern-matchable tells; reserve the LLM audit for discourse frames that need
   understanding. Shrinks the LLM audit, makes the cheap layer instant and deterministic.
3. **Batch API** for the non-interactive generation matrix (~50% off).
4. **Bundle shrink** — falls out of the exemplar inversion (rules → pairs).

**Open.** SDK migration touches `tests/lib.py` BACKENDS + `_invoke`; keep CLI parity for
the codex backend (not an Anthropic model). The linter's scope boundary — what is
mechanical enough for code vs needs the LLM — tracks the recall data; promote a check to
code only once it is reliably pattern-matchable.

**Block.** None, but lower priority than the measurement phases — efficiency compounds the
loop, it does not create the gradient.
