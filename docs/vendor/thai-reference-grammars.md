<!-- derived from: Claude training-data recall @ 2026-07-26. UNVERIFIED — no title
     here has been checked against a catalogue or a copy, and confidence is stated
     per entry. Treat every entry as a lookup target, not a fact. -->

# Thai reference grammars — the descriptive layer

Works that *describe* how Thai behaves, as opposed to the standards that prescribe how
it should be written ([`thai-orthography-standards.md`](thai-orthography-standards.md)).
These are what a structural claim in `grammar.md` should rest on.

**Recalled, not read.** These come from training-data recall, which is a different
capability from judging Thai prose — but it is still unverified, and the confidence
column is my own estimate, not evidence. The 2026-07-26 Typhoon probe returned a
bibliography that was probably mostly confabulated; the correct response to a second
model's list is the same catalogue check, not more trust.

## Candidates

| Work | Author | Confidence | Good for |
| ------------------------------------ | ---------------------------- | ---------- | ----------------------------- |
| หลักภาษาไทย | กำชัย ทองหล่อ | high | The canonical general Thai grammar reference. First stop. Notably absent from Typhoon's list. |
| ไวยากรณ์ไทย | นววรรณ พันธุเมธา | high | Modern academic Thai grammar; widely used at university level. |
| A Reference Grammar of Thai (Cambridge, 2005) | Iwasaki & Ingkaphirom | high | English-language, descriptive, discourse-aware. The most directly usable for our purposes — it describes particles and clause linkage rather than prescribing them. |
| โครงสร้างภาษาไทย | วิจินตน์ ภาณุพงศ์ | medium | Thai syntax / sentence structure. |
| Work on Thai nominalization and grammaticalization | Amara Prasithrathsint (Chula) | medium | Journal-article literature rather than one book; titles need looking up. |

## What we would cite them for

| Our slug / area | Where | What we would be citing |
| ------------------------------ | -------------- | ------------------------------------------ |
| `wrong-classifier` | `grammar.md` | Classifier system and selection |
| `capability-modal`, modal use | `grammar.md` | Modal and aspect marking (`จะ`, `ได้`, `ต้อง`) |
| `f6/ko-resumptive`, `f6/ko-pacing` | SKILL.md frames | `ก็` as resumptive / discourse particle — the frame rules lean on this heavily and cite nothing |
| `khong-chain`, `verb-over-nominal` | `craft.md`, audit | Nominalization with `การ-` / `ความ-` and `ของ` linkage — Prasithrathsint's area |
| `topic-comment-fronting` | `style-rules.md` | Topic-comment structure vs SVO |
| `dangling-additive-frame`, `f4/duai-additive` | SKILL.md, `ai-tells.md` | Sentence-final particles closing additive clauses |

The `ก็` and nominalization rows are the highest-value: both are frames the skill uses
constantly, both are structural claims a descriptive grammar can settle, and both
currently rest on nothing but the generalizer's intuition.

## Where these help, and where they stop

A descriptive grammar can tell us whether a construction is *possible* and how it
typically behaves. It cannot tell us whether a passage reads native, flat, or
machine-made — that is register and voice, and it stays with `corpus/` and chakrit's
ear. The `reads-flat` axis has no book.

The useful division across all three sources:

| Question | Source |
| --------------------------------- | ----------------------------------- |
| Is this spelled/spaced correctly? | Royal Society standards |
| Is this structure real, and how does it behave? | Reference grammars (here) |
| Does this read like a person wrote it? | `corpus/` + chakrit. No substitute. |

## Verification

Nothing here is provenance until a title resolves to a real catalogue record. Suggested
order: กำชัย ทองหล่อ and Iwasaki & Ingkaphirom first — highest confidence and highest
usefulness — then the rest. `WebFetch` is blocked on Thai sites; use the browser MCP.
