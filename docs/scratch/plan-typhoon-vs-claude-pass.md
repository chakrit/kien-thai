# Plan: automated Typhoon-vs-Claude comparison pass

<!-- Planning note. Extends the model-route probe (next-step #2). -->

- **Date:** 2026-06-16
- **Goal:** Execute next-step #2 from
  [`session-2026-06-09-model-route-probe.md`](session-2026-06-09-model-route-probe.md):
  the conditioned 5-eval comparison — Typhoon-8B (native draft, few-shot) vs
  Claude + kien-thai skill (the kode-thai loop) — with an automated mechanical diff,
  then chakrit's ear for the naturalness verdict.
- **Status (superseded 2026-07-27):** this pass produced `iteration-14`, which was
  **not co-generated** — its Claude arms came from iterations 12–13, so the pairing
  never isolated the drafter. `iteration-15` re-ran both arms under one iteration pin
  and is the canonical review batch. Everything below describes how the comparison was
  designed, which still holds; the iteration numbers in it do not.

## What "compare" means here — two layers

The naturalness verdict is **chakrit's ear**, not automatable (locked decision: no
LLM-judge until human review proves insufficient; see `user_thai_native` memory —
surface candidates, not verdicts). So the pass splits:

1. **Automated layer (this pass produces):** side-by-side outputs + a *mechanical*
   diff. Mechanical signals only, reusing what the harness already computes:
   - forbidden-phrase hits (`references/forbidden-phrases.md` blocklist)
   - connective density per 1k chars (`tests/test_quant.py`)
   - period-spam / exclamation counts (AI-tell heuristics)
   - length (chars, paragraphs) — does one arm pad?
   These are *conversation starters*, not a quality gate (test_quant's own framing).
2. **Human layer (the actual measurement):** chakrit reads the side-by-side in iA
   Writer, gives the chakrit-clean verdict per arm. The gap between the two arms'
   verdicts is the result. This is the whole point — the automated layer only routes
   attention.

## The two arms — NOT symmetric, and that's deliberate

| Arm                | Generator                          | Audit loop?                      |
| ------------------ | ---------------------------------- | -------------------------------- |
| Claude + skill     | `claude -p` + kien-thai bundle     | yes — kode-thai loop (≤5 passes) |
| Typhoon-8B draft   | `thai-native-draft.py` (ollama)    | no — single draft, few-shot only |

The asymmetry is the experiment. The model-route hypothesis: a Thai-pretrained base,
*even un-audited*, beats English-centric Claude *with* the full audit loop — because
the naturalness lives in pretraining weights, not harness depth. If bare Typhoon draft
≈ looped Claude on chakrit's ear, the skill's job shrinks to an audit layer over a
native draft (which is exactly what the probe's SKILL.md edit already recommends).

A later rung (not this pass) runs Typhoon draft → kode-thai audit *in Claude* — the
hybrid the probe's `thai-route.sh` encodes. This pass measures the bare draft first so
we know how much the audit layer adds on top of a native base.

## Mechanics — reuse, don't rebuild

Typhoon does **not** become a `lib.py` Backend. The `Backend` abstraction assumes a
CLI binary (`shutil.which`, argv, subprocess); Typhoon is an HTTP call and its arm has
no self-audit loop. Forcing it into `Backend`/`Config` distorts both. Instead:

1. **Claude arm** — existing harness, no change:
   `EVAL_BACKENDS=claude uv run pytest -m generate -k claude` → produces
   `iteration-N/<eval>/claude/with_skill/output.md` (the kode-thai loop).
2. **Typhoon arm** — a thin orchestrator script `tests/generate/typhoon_pass.py`
   (or a `scripts/` one-shot) that loops the 5 evals through
   `skills/kien-thai/scripts/thai-native-draft.py -r <corpus-category>` and writes
   `iteration-N/<eval>/typhoon/draft/output.md` + `meta.json` (`mode: "typhoon-draft"`,
   model, temperature, exemplar count). Lands in the **same iteration tree** so the
   diff step reads both arms uniformly.
3. **Diff step** — a script that, per eval, emits `comparison.md`: the two outputs
   side by side + a mechanical-signal table (the four signals above for each arm).
   Reuses `test_quant`'s `FORBIDDEN_PHRASES` and connective list — lift them into
   `lib.py` so both the test and the diff step share one source.
4. **Human gate** — `open -a 'iA Writer'` each `comparison.md`; chakrit's verdict per
   arm goes into `iteration-N/feedback.md` and the probe note's next-step ledger.

## Register → corpus-category mapping (few-shot conditioning)

`thai-native-draft.py -r` pulls exemplars from `corpus/curated/<category>/`. Eval
register slugs differ from corpus dir names — the pass must map them:

| Eval (register)              | Corpus category for `-r` | Notes                       |
| ---------------------------- | ------------------------ | --------------------------- |
| 1 tech-doc (explainer)       | `tech-writing`           | clean                       |
| 2 marketing (saas-sme)       | `marketing`              | clean                       |
| 3 news-feature (news)        | `newspaper-feature`      | clean                       |
| 4 personal-essay (blog)      | **— none —**             | **GAP — decision needed**   |
| 5 exec-brief (explainer)     | `tech-writing`           | or `bank-longform`?         |

`personal-blog` has no curated corpus category, so eval-4 can't be few-shot
conditioned. Three options for that one eval — see Decisions.

## Execution location

Ollama is **not** on the session host (`:11434` refused). The probe ran on chakrit's
local M1/16GB. The Typhoon arm must run where ollama serves `scb10x/
llama3.1-typhoon2-8b-instruct` (4.9GB, already pulled per the probe). The Claude arm
and the diff step run anywhere. So either chakrit runs `typhoon_pass.py` on the
desktop, or points this session at a reachable ollama host.

## Open decisions (gating execution, not the plan)

1. **ollama host** — run the Typhoon arm on chakrit's desktop, or expose a reachable
   host to this session? (Don't want to `ollama serve`/pull on the session host —
   env mutation, possibly wrong machine.)
2. **personal-blog (eval-4) corpus gap** — draft unconditioned (and label it), skip
   eval-4 from the Typhoon arm, or curate a `personal-blog` corpus category first?
3. **eval-5 exec-brief** — `tech-writing` exemplars, or `bank-longform` (closer to
   exec register)? Minor; defaulting to `tech-writing` unless told otherwise.

## What got built (2026-06-16)

- `tests/lib.py` — `EVAL_REGISTER_TO_CORPUS` mapping, `load_forbidden_phrases()`
  (parses the blocklist; strips parenthetical "use-instead" tokens so `สำคัญ` /
  `cta-bang` aren't false-flagged), `mechanical_signals()`.
- `tests/generate/typhoon_pass.py` — drafts corpus-covered evals via
  `thai-native-draft.py`, writes `iteration-N/<eval>/typhoon/draft/`.
- `tests/generate/compare_arms.py` — per-eval `comparison.md`: signal table + both
  prose blocks. Falls back past empty Claude outputs (iter-7 marketing was 0 bytes).
- Suite green (21 passed); changes are additive.

## Results — co-generated (Typhoon draft vs Claude+skill, 2026-06-16)

> **Superseded by the 5-eval regeneration** — the canonical review batch is
> `iteration-14/*/comparison.md` (see Status). This section records the initial
> 4-eval run and its signal table, kept for the trace.

Decisions taken: ollama reachable on host → ran here; eval-4 → curate corpus first
(skipped, later folded in via the 2026-06-16 personal-blog sweep). Mapping resolved:
`marketing-saas-sme` → `marketing/saas-sme`. The Claude arm (full kode-thai loop, all 4
converged to CLEAN in 1–3 passes) ran in `iteration-12`; the initial review artifacts
were the self-contained `iteration-11/<eval>/comparison.md` (each embeds both prose
blocks + the signal table).

Signals are `chars / paragraphs / connectives-per-1k / "!" / forbidden-hits`:

| eval         | typhoon-draft                          | claude+skill (loop)   |
| ------------ | -------------------------------------- | --------------------- |
| tech-doc     | 1058 / 5 / 2.8 / 0 / —                  | 1098 / 4 / 0.0 / 0 / — |
| marketing    |  548 / 3 / 0.0 / 0 / —                  | 1891 / 10 / 0.0 / 0 / — |
| news-feature | 1822 / 6 / 6.0 / 0 / —                  | 2049 / 6 / 1.5 / 0 / — |
| exec-brief   | 1300 / 7 / 4.6 / 0 / มีความสำคัญ・ในเรื่องของ・โดยสรุปแล้ว | 1721 / 5 / 1.2 / 0 / — |

Mechanical read (NOT a verdict): the kode-thai loop does what it's built to —
Claude+skill is clean on forbidden phrases everywhere and runs markedly lower connective
density (news 1.5 vs 6.0; exec 1.2 vs 4.6). Bare Typhoon is terser and doesn't pad —
marketing especially (548 vs Claude's 1891 / 10 paragraphs, where the loop expanded
hard) — but carries more connectives and, in the formal explainer, the stock filler the
audit layer would catch. The open question for the ear: does Typhoon's terseness +
native distribution read more human than Claude's longer, mechanically-cleaner prose?
That gap is the measurement; it is chakrit's call, per eval, on the comparison.md files.
