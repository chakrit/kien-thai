<!-- derived from: tests/lib.py, skills/kien-thai/scripts/,
     docs/scratch/session-2026-06-09-model-route-probe.md @ 2026-07-26 -->

# Model backends — CLI and API surface

The slice of each generator's third-party surface this repo actually depends on.
Upstream owns these; re-read upstream when a crib is wrong. How we *use* them is
[`../guides/running-evals.md`](../guides/running-evals.md); the wiring is
`tests/lib.py`.

All three are invoked in **bare mode** — no skill auto-loading, no session state.
The skill reaches the model only as a prompt prepend, so the sole delta between
`with_skill` and `baseline` is the prompt text.

## claude

```
claude --disable-slash-commands --output-format json -p
```

| Flag | Why we need it |
| ------------------------- | ------------------------------------------------------ |
| `-p` | Non-interactive; prompt on argv. |
| `--output-format json` | Emits usage stats — token counts, cache hit/miss — which land in `meta.json`. |
| `--disable-slash-commands` | Bare mode. Without it the CLI can pull in its own machinery and the config delta stops being just the prompt. |

Output shape: **one JSON object**. Text at `result`, usage at `usage`.

Requires `ANTHROPIC_API_KEY`.

## codex

```
codex exec --json
```

Output shape: **JSONL event stream**, not a single object. Two event types matter:

| Event | Carries |
| ---------------------------------------- | ---------------------------- |
| `item.completed` with `item.type == "agent_message"` | the text, at `item.text` |
| `turn.completed` | usage, at `usage` |

Parse defensively — unparseable lines are skipped rather than fatal, since the
stream interleaves events we do not consume. Requires `codex` logged in.

## ollama — Typhoon (Thai-native drafter)

Default model `scb10x/llama3.1-typhoon2-8b-instruct` (Typhoon-2 8B, SCB10X,
Llama-3.1 base):

```sh
ollama pull scb10x/llama3.1-typhoon2-8b-instruct
```

**Use the HTTP API, never `ollama run`.** `POST /api/generate` with
`"stream": false`. This is load-bearing, not a preference: the CLI leaks its
streaming re-render into redirected output — duplicated line fragments and
characters dropped mid-UTF-8 — which silently corrupts Thai. Corruption is
invisible in a terminal and only surfaces when a native reader hits garbled
syllables. `thai-native-draft.py` exists partly to make that mistake impossible.

Peers, swappable the same way: OpenThaiGPT 1.5/1.6 (Qwen2.5 base), SEA-LION
v3.5/v4 (Gemma base). 8B is the floor, not the ceiling.

**Benchmarks do not help here.** Every published Thai benchmark (ThaiExam,
HumanEval-TH, MATH-TH) measures knowledge or reasoning; none measures prose
naturalness. Model choice for this repo is settled by chakrit's ear on the five
evals, not by a leaderboard.

Typhoon is not wired as a harness backend — it runs through
`skills/kien-thai/scripts/thai-route.sh` and the comparison harness
(`tests/generate/typhoon_pass.py`, `compare_arms.py`). Wiring it into
`BACKENDS` is queued in [`../work-queue.md`](../work-queue.md).
