# Decisions Log

**Point-in-time defenses against future re-litigation** — rulings made on
a specific date for a specific question, recorded so the same argument
doesn't have to be re-fought next quarter. Each entry is frozen at the
moment of decision; if a later ruling reverses it, write a new dated
decision that links back and mark the old one `superseded`.

## When to add an entry

Add a decision when **the answer goes against the obvious default** —
mainstream practice, what the agent's training data would suggest, or the
project's own prior convention. The point of the log is to capture the
*why* so future arguments don't keep re-discovering it. Examples that
warrant an entry:

- We deliberately deviate from a well-known pattern, and a future agent
  reading our code would assume we just didn't know better.
- A reviewer pushed back on a choice that we then defended; the defense
  is worth preserving.
- Two reasonable approaches were debated and one won — without the entry,
  the next debate replays from scratch.

**Don't** add a decision when the answer is already obvious or matches
the prevailing convention. If there's no future confusion to head off,
just document the result in `../spec/` and move on. A decisions log
cluttered with "we chose the obvious thing" entries makes the actual
load-bearing decisions harder to find.

If your artifact is research, a survey, a draft, a transcript, or any
exploratory write-up — that's notes, not a decision. Use `../notes/`. If
it's forward-looking design, use `../spec/`.

## Prose-direction judgements

A distinct kind of decision in this repo: a **prose-direction call where
chakrit overruled Claude** on a substantive judgment question — a language
norm, register choice, taste/voice call, or rule-scope call. These preserve
the *examples a rule grew from*: native-ear corrections the generalizer
(Claude) cannot self-source. Same frozen, dated shape as any decision; log
them here.

Add one only when **all three** hold:

1. **chakrit is the editor** of the change under discussion — not Claude's
   own work, not a drive-by review of someone else's.
2. **Discussion happened** — actual back-and-forth, not a one-shot review.
3. **Substantive judgment disagreement** — not a mechanical or factual
   mistake-correction (typos, broken links, missed context, wrong altitude).

> **Direction (2026-05-30):** when a judgement's correction generalizes, the
> durable landing is a register-tagged before/after *pair* in
> [`../../skills/kien-thai/references/examples.md`](../../skills/kien-thai/references/examples.md)
> — a rule only when the pair doesn't transfer. See
> [`2026-05-30-exemplar-first-pivot.md`](2026-05-30-exemplar-first-pivot.md).

## Format

One file per decision: `YYYY-MM-DD-slug.md`

```markdown
# Short Title
- **Date:** YYYY-MM-DD
- **PR:** #N (or "manual")
- **Status:** accepted | superseded | revised

## Decision
One-liner.

## Rationale
Why this, and specifically why *not* the obvious alternative — that's
the part that prevents re-litigation.
```

Prose-direction judgements use a lighter shape:

```markdown
# YYYY-MM-DD — short slug

**Context** — what was being reviewed/edited; link to file or PR.
**Call made** — the judgment Claude/reviewer rendered.
**Verdict** — what chakrit actually decided, in their own framing.
**Takeaway** — the durable lesson; if it generalizes, also land it as a
pair (or memory/skill rule) and link from here.
```

## Statuses

- **accepted** — active, follow this decision
- **superseded** — replaced by a newer decision (link to it)
- **revised** — updated in-place with new context
