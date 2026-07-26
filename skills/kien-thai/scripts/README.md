# kien-thai scripts — the Thai-native model route

The idea behind these scripts: **base-model choice may be a bigger lever on Thai
naturalness than harness depth.** The machine-sounding Thai that kien-thai's
frames fight is largely an artifact of English-centric models (Claude, Codex)
writing Thai. A Thai-pretrained model carries the native distribution in its
weights rather than translating into it.

**Evidence status: one data point, unreplicated.** In a single native-ear
reading, bare Typhoon-2 8B — unconditioned, no exemplars — produced Thai with
no grammatical fault and no calque, the failure modes kien-thai spends most of
its rules on. One register, one draft, never repeated. The comparison runs
generated since have **not** been ear-reviewed, and their mechanical signals cut
both ways: the native draft carries higher formal-connective density on three of
five evals, runs much shorter throughout, and has emitted outline scaffolding
instead of prose. The route is a promising direction under test, not a settled
result — do not cite it as one.

So when a Thai-native model is reachable, the best output comes from **drafting
with it and auditing with kien-thai**, not from drafting with kien-thai alone.
The frames do not go away — they become the audit layer (the kode-thai loop)
over a native-drafted base. When no such model is reachable, kien-thai drafts
and audits directly, exactly as before. **The skill stands alone; the model
makes it better.**

These scripts encode that route so it *runs* rather than being prose an agent
has to follow.

## Scripts

| Script                 | Does                                                          |
| ---------------------- | ------------------------------------------------------------ |
| `thai-route.sh`        | The routing decision. Native model present → draft with it; absent → exit 3 (fall back to kien-thai). |
| `thai-native-draft.py` | Draft via the model. `--check` probes availability; `--register` few-shots from `corpus/`. |

```sh
# End-to-end: draft with the best available model, then audit
skills/kien-thai/scripts/thai-route.sh marketing "เขียน landing page สั้นๆ ขายระบบสต๊อกร้านค้า"
# exit 0 → pipe/hand the draft into the kode-thai audit loop
# exit 3 → no native model; draft with kien-thai directly

# Just probe whether a native model is up (0 yes, 3 no)
python3 skills/kien-thai/scripts/thai-native-draft.py --check
```

## What is scripted vs agent-driven

Scriptable steps are scripts; LLM-judgment steps stay with the agent.

- **Scripted:** model-availability check, draft capture, register→corpus
  few-shot conditioning, the route decision.
- **Agent-driven:** the kode-thai audit loop. Auditing Thai against the seven
  frames is language judgment, not a transform — it is not scriptable and runs
  through `/kode-thai`. The route hands its draft *to* that loop; it does not
  replace it.

## The ollama caveat (load-bearing)

`thai-native-draft.py` talks to the **ollama HTTP API with `stream:false`**, and
you must too. Never capture `ollama run` into a file or pipe — the CLI leaks its
streaming re-render into redirected output: duplicated line fragments and chars
dropped mid-UTF-8, which silently corrupts Thai. The script exists partly to
make that mistake impossible.

## Default model

`scb10x/llama3.1-typhoon2-8b-instruct` (Typhoon-2 8B; pull with
`ollama pull scb10x/llama3.1-typhoon2-8b-instruct`). 8B is the floor, not the
ceiling — few-shot + register conditioning, then 70B or a LoRA, are the next
rungs. Override with `--model`. OpenThaiGPT and SEA-LION are legitimate peers;
swap them in the same way.

## Status

A *direction* under test, not a closed eval result — the ear-clean verdict is one
register, unconditioned, never replicated. A co-generated five-eval comparison against
Claude+skill now exists and is awaiting the native ear; until those verdicts land,
neither correctness nor voice is settled.
