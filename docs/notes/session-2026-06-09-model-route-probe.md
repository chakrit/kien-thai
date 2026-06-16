# Session: Thai-native model route — feasibility probe

<!-- ACE session checkpoint. Written by /ace-save. -->

- **Date:** 2026-06-09
- **Task:** Investigate training/fine-tuning a model good at native Thai prose,
  as an alternative to the kien-thai skill (the skill's goal minus the harness).
- **Status:** in-progress — feasibility confirmed AND first naturalness read in:
  chakrit reviewed bare 8B output at the desktop, **found no grammatical fault and
  no calque**. Step-1 conditioned comparison (Typhoon+exemplars vs Claude+skill)
  still pending.

## Context

The "machine-sounding Thai" problem the kien-thai skill fights is largely a
Claude/Codex artifact — English-centric models writing Thai. A Thai-pretrained
base model carries the native distribution in weights, so the lever may be
*base-model choice*, not harness depth. Probed whether that's testable locally.

## Progress this session

- Researched Thai-native open models: **Typhoon 2** (SCB10X; 1/3/7/8B + 70B,
  Llama3.1/Qwen2 base), **SEA-LION v3.5/v4** (Gemma-based), **OpenThaiGPT
  1.5/1.6** (Qwen2.5 base; 7/14/72B) + **R1 32B** (reasoning — skip for prose).
- Key finding: **all published benchmarks (ThaiExam, HumanEval-TH, MATH-TH) are
  knowledge/reasoning — none measure prose naturalness.** Model choice can't be
  made off leaderboards; only chakrit's ear on the 5 evals decides.
- Confirmed local feasibility: pulled `scb10x/llama3.1-typhoon2-8b-instruct`
  (4.9GB) via ollama, generated marketing-saas-sme copy on M1/16GB in seconds.
  Output at `/tmp/typhoon-test.md` (ephemeral — not yet reviewed by chakrit).
- Candidate AI-tells in the bare output (NOT verdicts — chakrit's call):
  `ตอบโจทย์ทุกความต้องการ`, exclamation marks, `ไม่ต้องกังวล!`,
  `มาร่วมเป็นส่วนหนึ่งของครอบครัว SME ไทย`.
- Explore pass on repo assets: corpus ~53 curated snippets / ~20K words,
  8 chakrit-clean review verdicts as the strongest signal (iter-8). Density
  is high, **volume is ~4–8× thin for cold SFT/DPO.**

## Update 2026-06-14 — first ear-review + harness caveat

- **chakrit's verdict on bare, unconditioned 8B output: no grammatical fault, no
  calque.** Even without exemplars or register conditioning, the failure modes the
  skill spends most rules on were absent. Strongest single data point for the
  model route so far.
- **Harness caveat (load-bearing):** capture Typhoon via the ollama HTTP API
  (`POST /api/generate`, `"stream":false`), **never `ollama run`** — the CLI leaks
  its streaming re-render into redirected output: duplicated line fragments and
  dropped chars mid-UTF-8. First clean capture used a python urllib call to the API.
- Step-1 next-step #1 (chakrit reviews the tmp output) is now **done**; the
  remaining step-1 work is the conditioned 5-eval comparison vs Claude+skill.

## Update 2026-06-14 — route folded into the skill + scripted

The finding is now a first-class recommendation in the skill, and the route runs
as a script rather than as prose an agent has to follow:

- `skills/kien-thai/SKILL.md` — new "Best output: draft with a Thai-native model"
  section + a step-0 "route first" in the workflow. Skill still stands alone when
  no model is reachable.
- `skills/kode-thai/SKILL.md` — note that the audit loop's best input is a
  native-model draft; the loop is the un-scriptable (LLM-judgment) audit half.
- `skills/kien-thai/scripts/thai-native-draft.py` — ollama HTTP-API drafter,
  `stream:false` caveat baked in, `--check` for availability, `--register`
  few-shots from `corpus/`. Never fabricates Thai; conditioning pulls from the
  vetted corpus.
- `skills/kien-thai/scripts/thai-route.sh` — encodes the route decision (model
  present → draft; absent → exit 3, fall back to kien-thai).
- `skills/kien-thai/scripts/README.md` — rationale, scripted-vs-agent split,
  caveat, status.

Scriptable steps are now scripts; the kode-thai audit loop stays agent-driven
(language judgment, not a transform). Next rung unchanged: the conditioned
5-eval comparison, then wiring the model as a third harness backend.

## Decisions

- **From-scratch pretraining: rejected.** Seven-figure, reproduces Typhoon/
  SEA-LION work, arrives worse. The naturalness lives in post-training, not
  pretraining.
- **Eval criteria barely change** under the model route: the generate→review
  harness stays; swap generator from `claude -p` to an ollama call. The
  chakrit-clean verdict remains the gate. (Confirms locked decision: no
  LLM-judge until human review proves insufficient.)
- **8B is the floor, not the ceiling** — don't kill the approach on bare-8B
  output; few-shot + register conditioning, then 70B/LoRA, are the next rungs.

## Next steps

1. **chakrit reviews `/tmp/typhoon-test.md` at home** with a Thai-readable tool
   — regenerate if the tmp file is gone (ollama call in the Bash history; model
   `scb10x/llama3.1-typhoon2-8b-instruct`).
2. **Step-1 real test:** Typhoon 8B + existing exemplars (few-shot) vs
   Claude+skill, all 5 evals in `evals/evals.json`, judged by chakrit. The bare
   probe this session was unconditioned — not the real comparison.
3. If 8B promising: wire Typhoon into the eval harness as a third backend
   (`tests/lib.py` BACKENDS + a generate test) for apples-to-apples cross-iter
   measurement.
4. Also probe OpenThaiGPT 1.5-7B (Qwen base) side-by-side — chakrit has friends
   who worked on it; legitimate peer to Typhoon.

## Open questions / blockers

- **Blocker:** no Thai-readable review tool over SSH this session. Terminal
  pagers mangle Thai; iA Writer is local-only. Review deferred to when chakrit
  is at the desktop. (This session: iA Writer disabled by user; file-path-only.)
- If 8B voice disappoints with few-shot: is cloud 70B or a LoRA on 8B the next
  move? Decide after step-1.
- Corpus volume gap for the training route (SFT/DPO) — expand by chunking
  `corpus/raw/` longer articles before any tuning attempt.

## Key files / locations

- `/tmp/typhoon-test.md` — bare Typhoon 8B output (ephemeral, unreviewed).
- `evals/evals.json` — the 5 eval prompts that are the real test set.
- `corpus/` — ~53 curated native snippets; the training-data asset (thin).
- `docs/notes/session-2026-06-08-iter8-review.md` — the chakrit-clean verdicts
  that would seed DPO preference pairs.
