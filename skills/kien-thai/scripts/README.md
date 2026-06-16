# kien-thai scripts — the Thai-native model route

The honest finding behind these scripts: **the single biggest lever on Thai
naturalness is base-model choice, not harness depth.** The machine-sounding
Thai that kien-thai's frames fight is largely an artifact of English-centric
models (Claude, Codex) writing Thai. A Thai-pretrained model carries the native
distribution in its weights. In the 2026-06-09 probe, bare Typhoon-2 8B —
unconditioned, no exemplars — produced Thai that chakrit's native ear found
with **no grammatical fault and no calque**, the failure modes kien-thai spends
most of its rules on. That is the strongest single signal in the repo.

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

This is a validated *direction*, not a closed eval result. The ear-clean verdict
is one register, unconditioned. The conditioned 5-eval comparison (Typhoon +
exemplars vs Claude + skill, judged by chakrit) is the open step — see
`docs/notes/session-2026-06-09-model-route-probe.md`. Wiring the model into the
pytest harness as a third backend (`tests/lib.py` BACKENDS) is the measurement
path, gated on that comparison.
