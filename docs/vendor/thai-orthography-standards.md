<!-- derived from: Claude training-data recall @ 2026-07-26. UNVERIFIED — no title
     here has been checked against a catalogue or a copy. Treat every specific as a
     lookup target, not a fact. Verification is tracked in docs/human-tasks-queue.md. -->

# Thai orthography standards — the prescriptive layer

The published standards that govern Thai *mechanics*: spacing, punctuation,
transliteration, spelling. These are the surfaces where an argument in this repo can
actually be settled by citation rather than by ear.

**Link-first, and genuinely unread.** Nothing below is quoted from a copy. Each entry
names the authority and what it governs so a lookup is cheap; the rule text itself must
be read at the source before it is cited as provenance for anything.

## The authorities

| Body / work | Governs |
| --------------------------------------- | ------------------------------------------- |
| สำนักงานราชบัณฑิตยสภา (Office of the Royal Society, formerly ราชบัณฑิตยสถาน) | The prescriptive standard-setter for Thai. Publishes the dictionary and the หลักเกณฑ์ (criteria) documents below. |
| พจนานุกรมฉบับราชบัณฑิตยสถาน | Official spelling and headword forms. The authority for orthography disputes. Editions are dated (2493 / 2525 / 2542 / 2554) — cite which. |
| หลักเกณฑ์การทับศัพท์ | Transliteration of foreign words into Thai script, per source language. |
| หลักเกณฑ์การเว้นวรรค | Spacing — where Thai puts a space, which is Thai's primary phrase and clause separator. |

The dictionary is the one to reach for first: it is the least ambiguous, most
frequently decisive, and the easiest to check.

## What we would cite it for

Our rules that rest on a mechanical claim, and the standard that would ground them.
None of these citations are in the rule files yet — this table is the shopping list.

| Our slug | Where | Standard that governs it |
| ---------------------- | ---------------- | ----------------------------------------- |
| `mai-yamok-spacing` | `style-rules.md` | เว้นวรรค criteria — spacing around ๆ |
| ทับศัพท์ guide | `style-rules.md` | หลักเกณฑ์การทับศัพท์ |
| `comma-apposition` | audit-time | เว้นวรรค criteria — Thai separates enumerations with space, not comma |
| `mid-paragraph-period` | `ai-tells.md` | เว้นวรรค + punctuation criteria — the space, not the period, is Thai's sentence boundary |
| spelling calls generally | anywhere | พจนานุกรมฯ — the open `กฎ`/`กฏ`, `นัย`/`นัยยะ` question in `work-queue.md` |

`mid-paragraph-period` and `comma-apposition` are the live ones: both fired in the
2026-07-26 audit probe, and both are exactly the kind of claim that should not rest on
a model's intuition when a published standard exists.

## The trap — do not source voice from here

These standards are **prescriptive**. They say what is correct, not what reads native.
That distinction is load-bearing for this repo:

- Cite them for **mechanics** — spacing, spelling, transliteration, punctuation. A
  standard settles those.
- Never cite them for **register, voice, or naturalness**. Prescriptive Thai skews
  formal, and over-formal Thai is the exact failure the skill exists to counter.
  Grounding a style rule in a standards document would import the bias under the
  authority of a citation, which is worse than having no citation.

Same reasoning as the exclusion of school grammars (แบบเรียน) from the authority
search: prescriptive simplification is part of the problem, not the reference.

Voice stays sourced from `corpus/` and chakrit's ear. See
[`thai-reference-grammars.md`](thai-reference-grammars.md) for the descriptive
counterpart, which is a different tool for a different job.

## Access

Royal Society material is published online, and the dictionary has a public lookup.
Note that `WebFetch` is blocked on most Thai sites in this environment — use the
browser MCP, which worked for the 2026-05-13 vetting pass, or paste-in.
