# Prior art — absorbed session checkpoints

Not spec/decision because: it is a provenance digest over disposable session notes,
recording what each session did and where its durable output landed. Nothing here rules
or designs anything — follow the cross-links for that.

The undated file in `scratch/` (the one carve-out). Sessions whose only artifact was a
resume breadcrumb are folded in here, one section each, cross-linked to the live doc or
commit that carries the durable half. The breadcrumb role now belongs to `.ace/save.md`,
which is current-truth-only and overwritten each save — these notes were its predecessor.

**Current state is never here.** Read [`../work-queue.md`](../work-queue.md),
[`../human-tasks-queue.md`](../human-tasks-queue.md), and `.ace/save.md` for that.

## Still standalone in `scratch/`

Cited from live surfaces, so they keep their own file:

| Note | Cited by |
| ------------------------------------------------------------------------------ | ------------------------------------- |
| [`source-vetting-2026-05-13.md`](source-vetting-2026-05-13.md) | CLAUDE.md, the Register-3 decision, both queues |
| [`chrome-session-2026-05-13.md`](chrome-session-2026-05-13.md) | `style-rules.md`, the Register-3 decision |
| [`proposals-2026-05-13.md`](proposals-2026-05-13.md) | `research-queue.md` |
| [`feedback-2026-05-21-application.md`](feedback-2026-05-21-application.md) | `register.md` |
| [`framing-investigation-2026-05-21.md`](framing-investigation-2026-05-21.md) | `tests/lib.py`, the exemplar-first pivot, `work-queue.md` |
| [`session-2026-05-30-exemplar-pivot.md`](session-2026-05-30-exemplar-pivot.md) | `work-queue.md` |
| [`session-2026-06-08-iter8-review.md`](session-2026-06-08-iter8-review.md) | the model-route probe |
| [`session-2026-06-09-model-route-probe.md`](session-2026-06-09-model-route-probe.md) | `human-tasks-queue.md`, `vendor/model-backends.md`, `scripts/README.md` |
| [`personal-blog-sweep-2026-06-16.md`](personal-blog-sweep-2026-06-16.md) | `corpus/README.md`, `human-tasks-queue.md` |
| [`plan-typhoon-vs-claude-pass.md`](plan-typhoon-vs-claude-pass.md) | the personal-blog sweep |
| [`2026-07-07-fable5-eval1-probe.md`](2026-07-07-fable5-eval1-probe.md) | `workspace/iteration-10/feedback.md` |

---

## 2026-05-19 — chrome-vetting wrap-up

Closed the autonomous session opened 2026-05-13. Landed `mai-yamok-spacing` in
`style-rules.md` (`ต่าง ๆ` always spaced; other reduplications register-scoped),
moved Fictionlog/Tunwalai to dropped sources in `register.md`, and split the
browser-vetting evidence into its own note.

Durable: [`chrome-session-2026-05-13.md`](chrome-session-2026-05-13.md),
[`proposals-2026-05-13.md`](proposals-2026-05-13.md). Commits `019c29e`, `2fbb2e1`.

**The ruling worth remembering:** chakrit declined autonomous school sync — *"Edit in
this repo, i'll handle my own school updates, thanks."* Saved to user memory; do not
propose or run kien-thai school imports.

## 2026-05-21 — Register 6 + the framing literature pass

Traced 11 proposed rules from a transient feedback file against the existing skill. The
headline gap was structural: no official/ministerial/minutes register existed —
`register.md` covered five families. Landed **Register 6 — Official / minutes** with
eight rules, plus `concrete-cases-over-topology` and `positive-capability-framing` in
`craft.md`, and `REGISTER_HEADERS["official"]` in `tests/lib.py`. All Register 6 rules
are tagged **provisional** pending corpus validation — that validation never happened,
and `official` still has no corpus category.

Same session ran the agent-framing literature pass whose conclusions still drive bundle
construction: few-shot exemplars near the task beat persona, bundle ordering matters
(hence `exemplars.md` pinned last), and forcing Thai-language CoT likely backfires at
Thai's resource class.

Durable: [`feedback-2026-05-21-application.md`](feedback-2026-05-21-application.md),
[`framing-investigation-2026-05-21.md`](framing-investigation-2026-05-21.md).

## 2026-05-30 — inline iteration-8 overnight

Ran iteration-8 end-to-end on the inline protocol per an autonomous brief. All four
`with_skill` evals reached `CLEAN` — tech-doc-short and news-feature-bts at pass 1,
marketing-blurb and personal-essay-homecoming at pass 3. No baselines, no codex half:
the brief was audit-to-pristine, not bundle-effect measurement.

Two patterns were flagged for chakrit's eye rather than acted on (recurring
`frame-scoped-ko` on `ทีไร` frames; a marketing hedge stack bleeding into a personal-blog
draft) — the trace-before-write discipline working as intended.

Durable: `workspace/iteration-8/feedback.md`. Review verdicts later landed in
[`session-2026-06-08-iter8-review.md`](session-2026-06-08-iter8-review.md).

## 2026-05-30 — INDEX wiring + issue #1

Wired [`workspace/INDEX.md`](../../workspace/INDEX.md) into the iteration entry points so
the ledger stays discoverable: add a row on create (`pending`), flip to `reviewed` and
link the feedback on review. Commit `6c9ad93`.

Fixed issue #1 (@ninyawee): `kien-thai/SKILL.md`'s `description:` carried a bare
colon-space in an unquoted scalar, so the YAML was invalid and the `skills` CLI rejected
it. `tests/test_skill_frontmatter.py` is the regression guard — a strict-YAML pass over
every `skills/*/SKILL.md`. Commit `8a81bd5`.

## 2026-05-30 — docs reorg to ace-docs

Migrated durable docs to the ace-docs structure: judgements folded into `decisions/` as a
documented prose-direction subtype, `tests/REVIEW-PROTOCOL.md` and
`tests/INLINE-ITERATION.md` became [`../spec/review-protocol.md`](../spec/review-protocol.md)
and [`../spec/inline-iteration.md`](../spec/inline-iteration.md), and the three queues
moved to `docs/` root outside the permanence sort. `git mv` throughout, so
`git log --follow` still works. Commit `06cd64f`.

## 2026-07-03 — full instruction-surface audit

Four-way parallel audit of every instruction surface. The harness itself was healthy;
`bb5b325` fixed the mechanical drift (CLAUDE.md layout and commands, register count 5→6
everywhere live, `exemplars.md` into both bundle lists, a false pytest-convergence claim
deleted from CONTRIBUTING/README).

**The root finding stands unresolved: two unreconciled eras.** The accepted exemplar-first
pivot states "no better-model escape hatch"; the shipped Typhoon model route *is* that
escape hatch and lives only in notes. It needs a dated superseding or revising decision.
Queued in [`../human-tasks-queue.md`](../human-tasks-queue.md).

Also surfaced and deliberately *not* queued: ~94 rules across the five rule files carry no
corpus citation and almost nothing is flagged `provisional`. Whether to backfill
retroactively is a direction call, not agent work.

## 2026-07-07 — 1-by-1 human-queue walk + Phase 1 review

Drove the human queue under the 1-by-1 protocol; parked mid-way. Decided the next agent
step order — **(A) Workflow inline-driver prototype, then (B) Phase 3 exemplar
expansion** — now in [`../work-queue.md`](../work-queue.md).

iter-9 fully reviewed; iter-10 partial (`tech-doc-short` only). A side-quest Fable-5
baseline probe captured 10 native corrections in
[`2026-07-07-fable5-eval1-probe.md`](2026-07-07-fable5-eval1-probe.md).

**Strongest emergent signal:** run-on / under-segmentation recurs across backends *and*
survives to skill-clean — Fable F1, iter-9 news ¶4, iter-10 tech-doc line 7. A candidate
recall-miss: the sentence-length rule in `ai-tells.md` is not firing on run-ons that reach
CLEAN. Needs a confirmed recall-check pass, not a reflex rule add.

## 2026-07-11 — docs migration to the single-gate layout

Re-ran `/ace-init` + `/ace-docs`; `docs/notes/` became `docs/scratch/` (15 files, history
preserved), `guides/` and `vendor/` were added as empty signposts, and `docs/README.md`
was rewritten to the single gate. CLAUDE.md's skills list was corrected —
`markdown-writing`, `skill-creator`, and `shell` no longer ship from the school. Commit
`6c247e4`.

A `www/` review site was built and then removed at chakrit's call — not enough
information to warrant it.

## 2026-07-17 — self-talk sweep

Applied the repo-relevant half of a prod9/school audit of the distributed skill bodies:
edit-history narration rewritten as current rules, dated vetting refs moved to HTML
comments, the dropped-source list extracted to
[`../decisions/2026-05-13-register3-source-list-vetting.md`](../decisions/2026-05-13-register3-source-list-vetting.md),
session refs cut from `examples.md`. Commit `793bd2d`.

Scoped out deliberately: the `corpus/` references are *functional* —
`thai-native-draft.py` reads `corpus/curated/<register>/` at runtime, so those paths are
not narration. The distribution-boundary findings (paths invisible to a school consumer)
stay open by design; chakrit handles school sync.
