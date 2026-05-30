# Judgements

Append-only trail of prose-direction calls where chakrit overruled Claude on
a substantive judgment question. The point: when Claude (or a future
contributor) is about to make the same wrong call again, this directory
catches it. Memory captures the rule; these entries capture the *examples*
the rule grew from.

> **Direction (2026-05-30):** when a judgement's correction generalizes, the durable
> landing is a register-tagged before/after *pair* in
> [`../../skills/kien-thai/references/examples.md`](../../skills/kien-thai/references/examples.md)
> (rules only when the pair doesn't transfer) — see
> [`../decisions/2026-05-30-exemplar-first-pivot.md`](../decisions/2026-05-30-exemplar-first-pivot.md).

## Layout

One file per entry, named `YYYY-MM-DD-slug.md`. Slug is kebab-case, short,
and points at the durable lesson — not at the immediate edit. Newest entries
are discovered by filename sort; no global index is maintained.

## When to add an entry

Add an entry only when **all three** hold:

1. **chakrit is the editor** of the change under discussion. (Not Claude's
   own work, not a drive-by review of someone else's work.)
2. **Discussion happened** — actual back-and-forth, not a one-shot review
   with no reply.
3. **Substantive judgment disagreement** — a language norm, register choice,
   design tradeoff, taste/voice call, or rule-scope call. Not a
   mistake-correction.

## When NOT to add an entry

Explicitly do **not** log:

- Claude getting basic facts wrong.
- Audience mismatch (Claude wrote at the wrong altitude).
- Missed context (Claude didn't read the file/spec it should have).
- Mechanical or factual errors (typos, broken links, miscounted things).
- Things Claude should have known by reading the codebase.

The log exists to preserve trails of taste and judgment that future Claude
can re-learn from. It is **not** a generic mistake tracker; padding it with
mechanical errors devalues the entries that capture real judgment work.

## Entry shape

```markdown
# YYYY-MM-DD — short slug

**Context** — what was being reviewed/edited; link to file or PR.
**Call made** — the judgment Claude/reviewer rendered.
**Verdict** — what the user actually decided, in their own framing.
**Takeaway** — the durable lesson. If it generalizes, also encode it as a
memory or skill rule and link from here.
```
