# Framing-the-agent into Thai-native generation — investigation

**Question**: can we "frame" Claude (or codex) to think and write Thai from
Thai distributional space, instead of thinking-in-English and translating
on output?

Investigation done 2026-05-21. Mixes first-principles reasoning about
transformer mechanics with a literature pass (see Sources at the bottom).
Recommendations are testable in the existing harness.

## TL;DR — what to test, what to skip

| Rank | Technique                                                  | Expected impact | Harness fit  |
| ---- | ---------------------------------------------------------- | --------------- | ------------ |
| 1    | Native Thai exemplars as few-shot prefix (close to task)   | Highest         | Low cost     |
| 2    | Reorder bundle so `examples.md` lands last (near task)     | Medium-high     | Trivial      |
| 3    | Named-author/publication persona priming (specific)        | Modest          | Trivial      |
| 4    | A pre-task Thai "warm-up" paragraph the model writes first | Speculative     | Cheap        |
| 5    | Translate skill meta to Thai                               | Uncertain / -   | Expensive    |
| 6    | Force Thai-language chain-of-thought                       | Likely negative | N/A          |
| —    | Preference tuning / activation steering                    | Highest         | Unavailable  |

The single biggest thing not currently happening: **native Thai exemplars are
not front-loaded close to the task prompt.** Today, the bundle prepends
SKILL.md, then references alphabetically (so `examples.md` lands mid-bundle,
not near the task). Attention decays with distance; nearest tokens shape next
tokens the most. Moving examples to the end of the bundle is the cheapest
high-expected-value change and should be the first A/B.

## The lens — what "thinking in Thai vs translating" actually means

Transformer LLMs don't literally translate. But there's a measurable
phenomenon worth naming: **distributional shadow.** When Claude generates
Thai tokens, it samples from a conditional distribution shaped partly by
*English-translated Thai* in training data — translated Wikipedia, AI-assisted
content farms, Thai SEO that lifts English structures wholesale. The output
carries the statistical fingerprint of those shadow sources, not just native
Thai.

Recent research (Hwang et al., 2024 "Do LLMs Have an English Accent?"; the
Apr 2025 cross-lingual alignment work) confirms two things:

1. **LLMs make key decisions in an English-centric representation space**
   regardless of input/output language — anglocentric processing is a
   structural property, not a prompting problem.
2. **Non-English outputs carry "translationese" artifacts** because training
   exposure to non-English text is partly translated text, and models inherit
   the artifact.

What this implies for prompting: there is no prompt that *fixes* the
underlying anglocentric processing. The fix is preference tuning or
fine-tuning, which we don't control. But we can shift the **conditional
distribution** by changing what comes before the generation. Two main levers:

- **Context shaping** — change the conditioning text. This is all we have via
  prompting.
- **Decoding control** (logit bias, top-p) — unavailable in the Claude / codex
  bare-mode CLIs we use.

Within context shaping, **proximity matters**. Attention weights bias toward
recent tokens. So a native-Thai exemplar 200 tokens before the task prompt
shapes generation more than the same exemplar 5000 tokens before. The
practical implication: bundle ordering matters; everything we can do to put
native Thai prose closer to the task end of the prompt is worth doing.

## Technique inventory

Ordered by expected impact × harness feasibility for kien-thai.

### 1. Native Thai exemplars as few-shot prefix (highest priority)

**Idea.** Prepend 2–3 short native Thai exemplars *from the target register*
immediately before the task prompt. Not as "here are rules" but as "here are
examples of the kind of writing you're producing."

**Mechanism.** In-context learning shifts the output distribution toward the
example shape. Well-documented since GPT-3. Multilingual ICL papers
(2109.07684 "Language Models are Few-shot Multilingual Learners", 2306.10964
"Multilingual Few-Shot Learning via LM Retrieval") confirm the effect
generalizes to non-English target languages — sometimes with stronger gains
than in English, because the model has weaker priors to override.

**Fit.** Easy addition to `kien_thai_bundle()` in `tests/lib.py`. The harness
already has register-scoped `examples.md`; the structural change is to lift
the *target half* of before/after pairs into a separate "exemplars" section
that sits at the end of the bundle (closest to the task), distinct from the
mid-bundle "here are rules with example illustrations" content.

**Risk.** Direct mimicry. Mitigate by varying exemplars per run, or by using
enough diversity that the model abstracts the *style* rather than the
*content*.

**Test design.** Add a `with_skill_primed` config alongside `with_skill` and
`baseline`. Compare via human review on the existing eval set.

### 2. Reorder the bundle so `examples.md` lands last (trivial)

**Idea.** Currently the bundle order is SKILL.md, then references
alphabetically (`ai-tells.md`, `craft.md`, `examples.md`, `forbidden-phrases.md`,
`grammar.md`, `register.md`, `style-rules.md`). `examples.md` lands roughly
in the middle. Move it to the end so the most concentrated native-Thai prose
in the bundle is closest to the task prompt.

**Mechanism.** Recency / proximity in attention. Same as #1 but using existing
content — no new exemplars needed.

**Fit.** A 5-line change in `kien_thai_bundle()`. Could be implemented as: sort
references alphabetically *except* `examples.md` always last.

**Risk.** Very low. The content is unchanged; only position changes. Worst
case is no effect.

**Test design.** Same harness A/B as #1, but as a `with_skill_reordered`
variant. Could be combined with #1.

### 3. Named-author / publication persona priming (modest gains)

**Idea.** Prepend a *specific* persona statement, in Thai, to the bundle:

> คุณเป็นนักเขียนสายธนาคารที่เขียนคอนเทนต์ความรู้ในแบบของ Krungsri The
> COACH มากว่าสิบปี…

Granularity matters. "Act as a Thai writer" is vague enough to land on
translation-shaped defaults. "Act as a senior bank-explainer columnist in the
Krungsri Plearn / SCB Stories tradition" is narrow enough to actually
condition the distribution toward a known target.

**Mechanism.** Persona prompting has a "modest but statistically significant"
effect on subjective/stylistic tasks (Quantifying the Persona Effect, ACL
2024). Stronger when persona variables correlate with the desired output
properties.

**Fit.** A one-line prepend in `build_prompt()` — register-keyed.

**Risk.** Performative-confident output that hits the persona shape but
misses substance. Watch for: faux-elegance, over-stylization, register
drift away from the kien-thai targets.

**Test design.** As a third A/B arm; combine with #1 and #2 to see if effects
stack.

### 4. Thai-language warm-up paragraph (speculative)

**Idea.** Before the real task, instruct the model to write a short
neutral-topic Thai paragraph ("warm up"). The Thai tokens the model produces
become part of the autoregressive context, biasing subsequent generation
toward the Thai distributional regime it just entered.

**Mechanism.** Self-priming — the model's own recent Thai tokens condition
next-token sampling for the actual task. Speculative; haven't seen this
specifically studied for LLMs but the underlying mechanism is sound.

**Fit.** Workflow change — adds latency. Single extra turn or a single
prepend to the first turn.

**Risk.** Model produces an English-shaped warm-up Thai paragraph, in which
case priming is into the wrong distribution. Quality of the warm-up matters.

**Test design.** Cheap to A/B but unclear how to measure isolation cleanly.

### 5. Translate skill meta-instructions to Thai (uncertain; probably negative)

**Idea.** Translate the rule explanations in `references/*.md` to Thai. Keep
slugs and headings English for navigation.

**Mechanism.** Whole-context language match → operate fully in Thai
distributional space.

**Evidence — mixed.** One side: a 2025 study on 35 languages found matching
prompt language to content language gives up to 50% accuracy improvement on
extraction tasks; processing time drops 35%. Other side: machine-translated
prompts (2023 study) often fell below 50% accuracy; English-language prompts
can outperform target-language prompts by 13–15% on some directions.

**Fit.** Poor for kien-thai. Reasons:

- The skill's value is dense rule explanations. Translating risks losing
  precision (the English rule wording was carefully drafted; Thai
  translation introduces interpretation drift).
- Iteration discipline assumes you can edit rules cleanly; bilingual parity
  doubles maintenance.
- The harness's wrapper text in `build_prompt()` is *already Thai*
  (`ใช้แนวทางการเขียนต่อไปนี้`, `งานที่ต้องทำ`), and the eval prompts are
  already Thai. The English content is the dense middle of the bundle, where
  proximity to task is weakest — so the marginal value of translating it is
  low *relative* to #1/#2.

**Risk.** Decreased rule-following quality (English instructions are denser
and probably better-followed by Claude); ongoing maintenance burden.

**Test design.** If tested at all, scope narrowly: try translating
`ai-tells.md` only (the mechanical rules) and see if Thai output changes.
Translating `craft.md` and `style-rules.md` is high cost, uncertain benefit.

### 6. Force Thai-language chain-of-thought (likely negative for Thai)

**Idea.** If the model produces internal "thinking" tokens (extended thinking,
or just a "think step by step" prompt), require it to be in Thai.

**Evidence — negative for mid-resource languages.** Recent multilingual-CoT
work (2510.09555, 2501.16154 AdaCoT, 2508.14828) found:

- For high-resource languages, native-language CoT performs as well as or
  better than English.
- For **mid-resource languages — which Thai is — models struggle to generate
  long CoT in the native language.** Reasoning quality degrades.
- AdaCoT proposes the *opposite* of the naive intuition: route reasoning
  through English (or an "intermediary thinking language") before generating
  the target-language output. Reported gains in factual reasoning quality
  and cross-lingual consistency.

**Fit.** This is the most counter-intuitive finding. The user's natural
instinct — "if we want Thai output, make it think in Thai" — runs against
the literature for Thai's resource class. The model probably already does
the AdaCoT-style routing by default (English-ish internal computation →
Thai surface tokens). Trying to force Thai-only thinking likely hurts.

**Recommendation.** Don't intervene on thinking language. Let the model
route reasoning through its strongest representation space and shape the
*output distribution* via exemplars (#1) instead.

### Out of scope — needs model access we don't have

- **Preference tuning / RLHF for Thai-natural output.** This is the actual
  fix per the English-accent paper, but requires training-side access.
- **Activation steering / language vectors.** Compute a "Thai direction"
  in activation space, add it as an offset to hidden states (2602.02326
  language-steering work). Needs API access we don't have for Claude or
  codex bare-mode CLIs.
- **Decoded-vocabulary constraints (logit_bias).** Could ban specific AI-tell
  tokens at sampling time. The Claude `-p` mode and codex `exec` don't expose
  this. Would need Anthropic API or codex SDK with appropriate parameter.

## What's already happening that shouldn't be undone

Some Thai-framing is already in place — worth keeping inventory so we don't
accidentally regress when iterating:

- **`build_prompt()` wrapper is Thai.** Lines 358–364 of `tests/lib.py`:
  `ใช้แนวทางการเขียนต่อไปนี้` opens, `งานที่ต้องทำ` separates the skill
  from the task. This is the language-match-prompt-to-content technique,
  applied at the outermost layer.
- **All `evals/evals.json` prompts are Thai.** Task content is Thai. Good.
- **Examples in references are Thai** (`Bad:` / `Good:` lines). The model
  sees substantial Thai prose in-bundle, just not concentrated near the task.

## What this updates in the previous "Act as Thai writer" answer

The 2026-05-21 first-pass answer leaned "mild positive on top of skill, not
transformative." Research updates that to:

- **Mild positive holds** — confirmed by persona-effect work.
- **The bigger lever is few-shot priming**, not persona. Reorder priority
  accordingly.
- **The framing "stop translating and think in Thai" intuition is partly
  wrong** for Thai's resource class. The model's English-centric internal
  computation may be what's *producing* the surface-Thai output coherently;
  forcing Thai-only thinking may hurt.
- **The real fix is preference tuning**, which is structural, not prompt.
  Prompt techniques are mitigations, not solutions. Set expectations
  accordingly when reporting results.

## Recommended next experiments (ordered)

1. **Bundle reorder** — `examples.md` last. 5-line change in
   `tests/lib.py:kien_thai_bundle()`. Re-run iteration; compare by human
   review.
2. **Add curated native-prose exemplars** — `corpus/native-exemplars/<register>.md`
   with 2–3 short pieces per register. Append to bundle after `examples.md`.
   Re-run.
3. **Specific persona prepend** — register-keyed, in Thai, naming a specific
   publication/voice. A/B against (1)+(2).
4. **(Optional, lower priority) Thai warm-up paragraph** — workflow step.
   Cheap but speculative.

Each test arm gets its own `iteration-N/<eval>/<backend>/<config>/` directory
per the existing harness convention. Human-review judgements as usual.

## Caveats

- All recommendations are testable but the effect sizes are not predictable
  in advance. The English-accent paper specifically warns that prompt-level
  methods can be "marginal or inconsistent" — expect noise.
- Thai is mid-resource for Claude. The ceiling on prompt-only improvements is
  bounded. If we want substantially better Thai output, the answer is a
  Thai-tuned model (Typhoon, OpenThaiGPT, SEA-LION) — but those are out of
  the current harness scope.
- Few-shot priming risks contamination: if exemplars are too uniform, output
  collapses to mimicry. Vary by run if pooling exemplars is feasible.

## Sources

- ["Do Large Language Models Have an English Accent? Evaluating and Improving
  the Naturalness of Multilingual LLMs"](https://arxiv.org/pdf/2410.15956) —
  the central paper on the phenomenon and prompt-level vs preference-tuning
  interventions.
- ["Can you map it to English? The Role of Cross-Lingual Alignment in
  Multilingual Performance of LLMs"](https://arxiv.org/html/2504.09378v1) —
  on English-centric representation space.
- ["Language Models are Few-shot Multilingual Learners"](https://arxiv.org/abs/2109.07684)
  — multilingual ICL evidence base.
- ["Multilingual Few-Shot Learning via Language Model Retrieval"](https://arxiv.org/pdf/2306.10964)
  — exemplar-retrieval methods.
- ["Language Steering for Multilingual In-Context Learning"](https://arxiv.org/pdf/2602.02326)
  — activation-level techniques (out of scope but useful frame).
- ["Quantifying the Persona Effect in LLM Simulations"](https://aclanthology.org/2024.acl-long.554/)
  — persona-prompting effect sizes.
- ["A Comprehensive Evaluation of Multilingual Chain-of-Thought
  Reasoning"](https://arxiv.org/abs/2510.09555) — CoT-language findings,
  including the mid-resource backfire risk.
- ["AdaMCoT: Rethinking Cross-Lingual Factual Reasoning"](https://arxiv.org/pdf/2501.16154)
  — intermediary-thinking-language routing.
- ["Why Your LLM Prompts Should Match Your Content Language"](https://ryanstenhouse.dev/why-your-llm-prompts-should-match-your-content-language/)
  — 2025 cross-language extraction study (50% accuracy improvement).
- ["Typhoon: Thai Large Language Models"](https://arxiv.org/abs/2312.13951) —
  context on Thai-tuned models that outperform general-purpose models on Thai.
