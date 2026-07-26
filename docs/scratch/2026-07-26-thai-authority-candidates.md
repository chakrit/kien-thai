<!-- not spec/decision because: unverified model output staged for chakrit's check;
     nothing here is provenance until a title is confirmed to exist. -->

# 2026-07-26 — Candidate Thai-language scholarly authorities (UNVERIFIED)

chakrit's proposal: ask a Thai-trained model which Thai-language scholarly works it
knows, so rule provenance can lean on Thai authorities rather than English style
manuals. Scholarly only — school grammars (แบบเรียน) excluded, since prescriptive
simplification is plausibly part of the over-formal skew the skill fights.

Runner: `tests/probe_thai_authorities.py`. Model: Typhoon-2 8B via the ollama HTTP API.
Raw: `workspace/probes/thai-authorities.md` (gitignored).

> **Nothing below is provenance.** These are candidate titles from an 8B model asked to
> recall bibliography — the failure mode is a fluent, confidently attributed invention.
> The probe deliberately asked for *titles* (checkable) and never for *rulings*
> (not checkable). Each entry needs confirming that the work exists before it is cited
> anywhere.

## What came back

| # | Title | Attributed author | Year | Attributed publisher |
| - | ------------------------ | ------------------------- | ---------- | ---------------------- |
| 1 | ไวยากรณ์ภาษาไทย | ประเสริฐ ณ นคร | 2520 / 1977 | จุฬาลงกรณ์มหาวิทยาลัย |
| 2 | สัทศาสตร์ภาษาไทย | วิไลวรรณ ขนิษฐานนท์ | 2530 / 1987 | มหาวิทยาลัยธรรมศาสตร์ |
| 3 | การใช้ภาษาไทย | สุภาพร สุขะวิริยะ | 2540 / 1997 | มหาวิทยาลัยเกษตรศาสตร์ |
| 4 | สไตล์การเขียนภาษาไทย | ชลธิชา สุดมุข | 2550 / 2007 | จุฬาลงกรณ์มหาวิทยาลัย |
| 5 | โครงสร้างประโยคภาษาไทย | สมชาย วงศ์วิเศษ | 2535 / 1992 | มหาวิทยาลัยเชียงใหม่ |

Coverage as claimed: 1 grammar, 2 phonetics, 3 usage, 4 written style, 5 sentence
structure. For this repo's purposes 4 and 3 would be the relevant ones, then 5.

## Flags for your check

Raised as observations to verify, not verdicts — the Thai bibliographic call is yours.

- **The canonical work is missing.** No `หลักภาษาไทย` (กำชัย ทองหล่อ), which is the
  reference any real recall of Thai grammar scholarship would surface first. Its absence
  is the strongest evidence that this list is at least partly confabulated rather than
  recalled.
- **Author plausibility varies sharply.** ประเสริฐ ณ นคร and วิไลวรรณ ขนิษฐานนท์ are
  real, prominent scholars — but a real name attached to a plausible title is exactly
  how a confabulated citation looks. Entries 3–5 read more generic.
- **Round-number years** (1977, 1987, 1992, 1997, 2007) across all five is a
  distribution worth distrusting.
- **Phonetics is off-target** even if real — this repo needs usage, style, and syntax.

## Recommended next move

Treat this as a **search seed, not a bibliography**. The checkable version is to look
up titles 1, 3, 4 in a library catalogue (CU/TU/NLT) and keep only what resolves to a
real record. If the hit rate is poor, the honest conclusion is that an 8B cannot serve
as a bibliographic source and the authority list has to come from a catalogue search or
your own shelf — which is a fine outcome for a cheap probe to establish.

Worth repeating the probe against a larger model before drawing a conclusion about the
method itself; 8B is the floor, and bibliographic recall is exactly where parameter
count tends to show.
