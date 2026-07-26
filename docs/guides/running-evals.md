# Running an eval iteration

How to produce a new `workspace/iteration-N/` of Thai prose and leave the repo in a
state the review loop can pick up. Covers both generation modes and the traps that
have cost real iterations.

The *why* — what the numbers mean, why humans judge and not assertions — is
[`../spec/review-protocol.md`](../spec/review-protocol.md). This guide is the *how*.

## Before you start

- `uv sync` once, to install deps (`pythainlp`, pytest 9, pytest-xdist).
- `ANTHROPIC_API_KEY` exported for the claude backend; `codex` logged in for the
  codex backend. Tests skip gracefully when a backend is missing, so a partial
  environment produces a partial matrix rather than an error — check what actually
  ran before recording the iteration.
- A clean working tree. Generation writes into `workspace/`, and you want the
  iteration's inputs (skill content at that commit) pinned by git.

**Decide the mode first.** The pytest harness costs API tokens and produces
publishable cross-iteration measurement. Inline mode (below) costs session tokens
and produces audit/probe evidence. Use the harness when the numbers will be
compared across iterations; use inline for one-off probes.

## Generate — the pytest harness

```sh
uv run pytest                             # sanity only (fast, default, no API calls)
uv run pytest -m generate                 # the real matrix (slow, $$$)
uv run pytest -m generate -k claude        # one backend
uv run pytest -m evaluate                 # advisory heuristics on the latest iteration
uv run pytest -m recall                   # auditor-recall runner (slow, $$$)
```

Markers are opt-out by default — `addopts` in `pyproject.toml` deselects
`generate`, `evaluate`, and `recall`, so a bare `uv run pytest` never spends money.

**Backends are opt-in per run.** `EVAL_BACKENDS` (comma-separated) selects them;
unset means claude only. Unknown names are rejected at the boundary rather than
silently dropped, so a typo fails loudly.

```sh
EVAL_BACKENDS=claude,codex uv run pytest -m generate
```

**Do not pass `-n >1` unpinned.** `iteration_dir` is a session-scoped fixture, and
under pytest-xdist each worker gets its own session — so each worker mints a
*separate* iteration directory and the matrix lands split across them. Iteration-7
was generated this way and had to be merged by hand. `EVAL_ITERATION` (below) pins
every worker to one tree and avoids it; unpinned, run serial or expect to merge.
Tracked in [`../work-queue.md`](../work-queue.md) → "Eval harness: xdist splits
iteration directory across workers".

## Pinning the iteration — `EVAL_ITERATION`

Unset, every entry point mints its own fresh iteration. That is right for a single
self-contained run and wrong for everything else: two arms of one comparison land in
two trees, and a resumed or extended run starts a third.

```sh
EVAL_ITERATION=15 uv run pytest -m generate     # write into iteration-15
EVAL_ITERATION=iteration-15 ...                 # same thing, spelled out
```

The pin creates the directory if absent and is rejected loudly if it is not an
iteration name. Every writer honours it — the pytest matrix and `typhoon_pass.py`
alike — which is what makes a co-generated run possible.

## Generate — the Typhoon arm and the comparison

The model-route arm (`spec/model-route.md`) drafts with Typhoon-2 8B over the ollama
HTTP API, few-shot conditioned from `corpus/curated/<register>/`. Local and free; it
needs `ollama` running with `scb10x/llama3.1-typhoon2-8b-instruct` pulled. It is a
single native draft, **not** a kode-thai loop.

```sh
EVAL_ITERATION=15 uv run python tests/generate/typhoon_pass.py
EVAL_ITERATION=15 EVAL_BACKENDS=claude uv run pytest -m generate -k "claude and with_skill"
uv run python tests/generate/compare_arms.py iteration-15
```

Both arms under one pin, at one commit, under one skill state — that is what
"co-generated" means, and it is the only pairing that isolates the drafter.
`compare_arms.py` writes `workspace/iteration-N/<eval>/comparison.md`: a mechanical
signal table plus both prose blocks. It labels the pair honestly — when it cannot find
a same-iteration Claude arm it falls back to the newest one anywhere and prints **NOT
co-generated**. Iterations 11–14 all carry that caveat; do not spend the ear on them.

Evals whose register has no corpus category are skipped and reported by name — the
drafter has no exemplars to condition on, and synthesizing them is forbidden.

## Generate — inline mode

Session-driven iteration that reuses the same bundle preprocessor and prompt
templates but generates via subagent instead of the subprocess CLIs. Saves API
tokens; outputs are marked `mode: "inline"` in `meta.json`. Protocol:
[`../spec/inline-iteration.md`](../spec/inline-iteration.md).

## Where output lands

```
workspace/iteration-N/<eval>/<backend>/<config>/
    output.md      # the prose
    pass-N.md      # each audit/fix pass
    prompt.txt     # exact prompt sent
    meta.json      # per-pass usage: cache hits, input/output tokens
```

The five evals are defined in `evals/evals.json` (`tech-doc-short`,
`marketing-blurb`, `news-feature-bts`, `personal-essay-homecoming`,
`exec-brief-oss-bi-hana`); configs are `with_skill` and `baseline`.

**Eval subdirectories are gitignored evidence — never edit them.** They regenerate.
The tracked, durable outputs of a run are `workspace/iteration-N/feedback.md` and
whatever graduates into `skills/kien-thai/references/`. The reflex to fix a bad
line where you found it produces nothing that survives the next generation.

## After the run

1. **Add the iteration's row** to [`../../workspace/INDEX.md`](../../workspace/INDEX.md)
   — date, mode/scope, Review `pending`. Do this at creation, not at review time; a
   missing row means the ledger lies about the repo's state.
2. **Check what actually ran.** A skipped backend produces a thinner matrix than the
   row claims. Record the real scope.
3. **Hand off to review** — [`../spec/review-protocol.md`](../spec/review-protocol.md).
   Thai renders wrong in terminal pagers; open outputs with
   `open -a 'iA Writer' <file>`, one file at a time.

## Reading the result

`uv run pytest -m evaluate` (`test_quant.py`) flags forbidden phrases and connective
density. It is **advisory only** — attention routing, never a quality gate. Likewise,
an output looping to `CLEAN` is ruleset-coverage, not naturalness: it means the
auditor found nothing, not that the prose is good. The measurement is the gap between
skill-clean and chakrit-clean.
