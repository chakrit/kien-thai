# docs

Durable artifacts. **File by the gate below** — walk it top to bottom and stop at the first
yes. The bottom (`scratch/`) charges a toll, so nothing lands there by default.

## Where does this go?

1. A ruling you'd defend if someone reopened it? → [`decisions/`](decisions/) — dated,
   never edited.
2. Third-party facts you keep to look up (a framework, an external API/CLI)? →
   [`vendor/`](vendor/) — link-first, mark provenance.
3. A how-to — using the product *or* operating the repo? → [`guides/`](guides/) — script
   repeatable operations; the guide holds the judgment.
4. How our system is built or meant to work, including its own config/CLI surface? →
   [`spec/`](spec/).
5. None of the above — genuinely unsettled exploration → [`scratch/`](scratch/). Open with
   a one-line "not spec/decision because ___."

Each folder's README states its one test precisely. `CLAUDE.md` / `AGENTS.md` points here
as the index.

## Operational queues

Three live backlogs sit at this level, outside the routing gate — they are working state,
not durable artifacts, and get rewritten continuously:

- [`work-queue.md`](work-queue.md) — agent-doable committed work (the question is *how*,
  not *whether*).
- [`research-queue.md`](research-queue.md) — speculative items awaiting evidence.
- [`human-tasks-queue.md`](human-tasks-queue.md) — tasks that need chakrit specifically
  (native ear, Thai authoring, decisions, token spend).

**Task discovery reads all three**, not just `work-queue.md`.

---

## Complete index

Every file under `docs/`. A doc that is not listed here is undiscoverable, so
`tests/test_docs_index.py` fails the build when one goes missing — add the row in the
same change that adds the file.

### Decisions — dated rulings, frozen

| Doc | Ruling |
| ----------------------------------------------------------------------------------- | ------ |
| [`2026-05-10-english-prose-economy-lens.md`](decisions/2026-05-10-english-prose-economy-lens.md) | English prose-economy instincts do not transfer wholesale to Thai. |
| [`2026-05-10-politeness-not-ai-tell.md`](decisions/2026-05-10-politeness-not-ai-tell.md) | Politeness is register, not an AI tell — do not strip it reflexively. |
| [`2026-05-11-cognitive-vs-affective-verbs.md`](decisions/2026-05-11-cognitive-vs-affective-verbs.md) | Cognitive and affective verbs behave differently; the rules must not merge them. |
| [`2026-05-11-frame-rules-have-idiomatic-edges.md`](decisions/2026-05-11-frame-rules-have-idiomatic-edges.md) | The naturalness tail is not rule-shaped. Feeds the exemplar-first pivot. |
| [`2026-05-11-person-deixis-discourse-over-syntax.md`](decisions/2026-05-11-person-deixis-discourse-over-syntax.md) | Person deixis is a discourse call, not a syntactic slot. |
| [`2026-05-13-register3-source-list-vetting.md`](decisions/2026-05-13-register3-source-list-vetting.md) | Which Register-3 sources survived vetting, and which were dropped. |
| [`2026-05-30-exemplar-first-pivot.md`](decisions/2026-05-30-exemplar-first-pivot.md) | **Revised.** Pairs over rules; auditor recall is the binding constraint. |
| [`2026-07-26-model-route-revises-exemplar-first.md`](decisions/2026-07-26-model-route-revises-exemplar-first.md) | **Current direction.** Native drafter preferred; kien-thai is the audit-and-voice layer. |
| [`2026-07-26-no-llm-judge.md`](decisions/2026-07-26-no-llm-judge.md) | No LLM judges Thai prose. The native ear is the only verdict. |
| [`decisions/README.md`](decisions/README.md) | What earns a decision entry; the prose-direction-judgement subtype. |

### Spec — our design, living

| Doc | Covers |
| ------------------------------------------------------- | ------------------------------------ |
| [`review-protocol.md`](spec/review-protocol.md) | The outer loop: skill-clean → chakrit-clean, and the dashboard. |
| [`inline-iteration.md`](spec/inline-iteration.md) | Session-driven generation without the subprocess CLIs. |
| [`model-route.md`](spec/model-route.md) | Who drafts, who audits, and the open voice question. |
| [`spec/README.md`](spec/README.md) | What belongs in spec. |

### Guides — how to do it

| Doc | Task |
| --------------------------------------- | ------------------------------------------------ |
| [`running-evals.md`](guides/running-evals.md) | Produce an iteration; both modes, traps, what to update after. |
| [`guides/README.md`](guides/README.md) | What belongs in guides. |

### Vendor — third-party lookup

| Doc | Surface |
| ------------------------------------------------------------------- | ------------- |
| [`model-backends.md`](vendor/model-backends.md) | claude / codex / ollama flags, and the `ollama run` Thai-corruption trap. |
| [`thai-orthography-standards.md`](vendor/thai-orthography-standards.md) | Royal Society standards. Mechanics only — never voice. |
| [`thai-reference-grammars.md`](vendor/thai-reference-grammars.md) | Descriptive grammars for structural claims. |
| [`vendor/README.md`](vendor/README.md) | What belongs in vendor. |

### Scratch — unsettled, disposable

| Doc | What it holds |
| ------------------------------------------------------------------- | ------------- |
| [`prior-art.md`](scratch/prior-art.md) | Digest of absorbed session notes. The undated one. |
| [`source-vetting-2026-05-13.md`](scratch/source-vetting-2026-05-13.md) | Source vetting pass; cited by CLAUDE.md and a decision. |
| [`chrome-session-2026-05-13.md`](scratch/chrome-session-2026-05-13.md) | Browser-vetting evidence behind `style-rules.md` entries. |
| [`proposals-2026-05-13.md`](scratch/proposals-2026-05-13.md) | Skill-change proposals A and B, still undecided. |
| [`feedback-2026-05-21-application.md`](scratch/feedback-2026-05-21-application.md) | Per-rule trail for the Register-6 landing. |
| [`framing-investigation-2026-05-21.md`](scratch/framing-investigation-2026-05-21.md) | Bundle-ordering and exemplar-proximity literature pass. |
| [`session-2026-05-30-exemplar-pivot.md`](scratch/session-2026-05-30-exemplar-pivot.md) | Working notes behind the pivot decision. |
| [`session-2026-06-08-iter8-review.md`](scratch/session-2026-06-08-iter8-review.md) | iter-8 chakrit-clean verdicts. |
| [`session-2026-06-09-model-route-probe.md`](scratch/session-2026-06-09-model-route-probe.md) | Thai-native model feasibility probe + the ollama caveat. |
| [`personal-blog-sweep-2026-06-16.md`](scratch/personal-blog-sweep-2026-06-16.md) | personal-blog corpus sweep; category still single-author. |
| [`plan-typhoon-vs-claude-pass.md`](scratch/plan-typhoon-vs-claude-pass.md) | Plan for the comparison arms. |
| [`2026-07-07-fable5-eval1-probe.md`](scratch/2026-07-07-fable5-eval1-probe.md) | Fable-5 baseline probe; 10 native corrections. |
| [`2026-07-26-runon-recall-probe.md`](scratch/2026-07-26-runon-recall-probe.md) | Run-on recall result; backend-dependent skill-clean. |
| [`2026-07-26-thai-authority-candidates.md`](scratch/2026-07-26-thai-authority-candidates.md) | Typhoon bibliography output, flagged unverified. |
| [`scratch/README.md`](scratch/README.md) | What belongs in scratch, and the two carve-outs. |

### Queues — working state, rewritten continuously

[`work-queue.md`](work-queue.md) · [`research-queue.md`](research-queue.md) ·
[`human-tasks-queue.md`](human-tasks-queue.md)
