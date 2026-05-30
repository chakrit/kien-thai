# Chrome session — 2026-05-13 (continuation)

Second-pass browser-assisted research after the morning vetting in
[`source-vetting-2026-05-13.md`](source-vetting-2026-05-13.md). Four
work items, all chrome-dependent because WebFetch is blocked on
target Thai sites.

Tool: Claude-in-Chrome MCP, read-only navigation. Quoting policy
follows the morning pass — short illustrative tidbits only.

---

## 1. Fictionlog / Tunwalai serial-fiction vetting

**Verdict.** Out-of-scope. Do not add as a register slot.

### Evidence — Fictionlog Thai-original 7-day bestseller list

The bestseller browse view
([`/browse?contentRatingIds=1&sortBy=bestseller7Days&languageFilters=original`](https://fictionlog.co/browse?contentRatingIds=1&sortBy=bestseller7Days&languageFilters=original))
returns near-uniformly wuxia / cultivation / system-LitRPG titles,
all tagged `กำลังภายใน` or `แฟนตาซี`. Sample of titles in the top
ranks:

- หมื่นวิถี... หนึ่งกระบี่ พิฆาตสวรรค์ (`กำลังภายใน`)
- มหาจักรพรรดิราชันย์เทพ (`กำลังภายใน`)
- ระบบสัตว์วิญญาณกับวิถีเซียนจ้าวอสูร (`แฟนตาซี`)
- แค่รับศิษย์ ข้าก็เหนือฟ้า (`กำลังภายใน`)
- อสูรข้ามฟ้า (`กำลังภายใน`)

### Sample chapter — อสูรข้ามฟ้า (Free-J, 567 chapters since 2020)

URL: https://fictionlog.co/c/5f3bd6743989d8001bce8a67 (chapter 1)

Free-J is a paid-out author by Fictionlog standards (multi-year run,
567 chapters, active comments). The chapter renders with anti-scrape
zero-width-character injection, but dialogue and structure are
clearly readable. Features:

- Pronouns: `ข้า` 1st-person archaic, `เจ้า` 2nd-person archaic.
- Honorifics: `อาจารย์`, `ศิษย์เอก`, `ฮีโร่` (master, head disciple).
- Dialogue-heavy, third-person narrator, scene-by-scene cuts.
- Wuxia-genre lexicon (`กำลังภายใน`, `เส้นทางธรรม`, `เบญจกายาสัตว์`).
- Cultivation-novel tropes (animal-spirit seals, master-disciple
  rescue mission, inherited mystic markings).

This is *transposed* Chinese cultivation-novel register, not native
Thai non-fiction prose. The conventions don't generalize.

### Evidence — Tunwalai Thai-original homepage

[`https://www.tunwalai.com/`](https://www.tunwalai.com/) homepage
"นิยายรักฟินสุด หยุดไม่ได้" carousel, top 10 titles all categorized as
`รักวัยรุ่น` (teen romance), `รักโรแมนติก` (romance), or `อีโรติก`
(erotica). Sample:

- เหลี่ยมร้ายทวงคืนรัก (`รักวัยรุ่น`)
- เหนือปกครองชวีไท่ (`อีโรติก`)
- หย่ารักผู้กองแสนร้าย (`อีโรติก`)
- พันธะลับนางร้ายตกอับ #Behind the Seotlight (`อีโรติก`)

Different mix from Fictionlog (romance/erotica-dominant rather than
wuxia-dominant) but same shape: heavy genre conventions, dialogue-
driven popular fiction.

### Why out-of-scope, not Register-6

1. **Genre conventions don't generalize.** Wuxia archaic pronouns
   (`ข้า`/`เจ้า`) and romance-trope dialogue would contaminate any
   non-fiction register the skill targets. There is no use-case in
   the kien-thai brief that wants this voice.
2. **Author-pool risk amplified.** Even paid-out authors inhabit the
   genre conventions; the "experienced ≠ stylistically clean for
   non-fiction purposes" gap is structural, not fixable by a better
   author filter.
3. **Existing 5 registers cover the brief.** Adding Register-6 only
   to immediately mark it "do not lift from" creates dead scaffolding.

### Action

- Update `references/register.md` Register-3 to move Fictionlog /
  Tunwalai from "Vetting queued" to "Dropped from source list" with
  the out-of-scope rationale.
- Mark `docs/research-queue.md` Fictionlog/Tunwalai entry resolved.

---

## 2. Minimore — full essay via Wayback

**Verdict.** Reference-only tier confirmed with real prose evidence.
Earlier tier call (snippet-based, morning pass) holds.

### Sample — `#อายุมากขึ้นเราจะมีความสุขน้อยลง?` (พอกลอน ซาเสียง, 2 Jan 2023)

Wayback URL:
[`https://web.archive.org/web/20230605160331/https://minimore.com/b/yqkoe/8`](https://web.archive.org/web/20230605160331/https://minimore.com/b/yqkoe/8)

Features observed (no extended quoting):

- 1st-person `ผม`. Self-help reflective register.
- Numbered sections (1–5), short paragraphs, frequent line breaks.
- ๆ-spacing dropped consistently: `เด็กๆ`, `ไวๆ`, `ว่างๆ`,
  `บางจังหวะ บางวัน บางสัปดาห์`. Casual personal-blog norm.
- Heavy English code-mix (`support` used as a Thai verb, repeated;
  `กองทุนคริปโต`).
- Self-help cliché framing: rhetorical-question opener, "อันดับแรก"
  enumeration, kicker close.
- Visible amateur tells: typo `ความผิดชอบ` in the closing line
  (intended `ความรับผิดชอบ`); inconsistent particle use; sentence
  fragments without intentional rhythm.
- Photo credit at bottom (`ภาพถ่ายโดย Matthias Zomer: pexels.com`),
  view count 36 — low-engagement amateur platform signal.

Confirms what snippet-based vetting inferred: Minimore is a
baseline for "earnest unpolished personal essay," useful as a
counterpoint to AI-polished output, not as a Model.

### Action

- Add this sample as the Reference-only-tier citation in
  `references/register.md` Register-3.

---

## 3. ๆ-spacing — register-scoped style

**Verdict.** ๆ-spacing tracks register and word, not just register
alone. Two patterns:

- **`ต่าง ๆ` is near-universally spaced** in edited Thai across
  registers — formal stock phrase, treated as a multi-word unit
  even by sources that drop the space elsewhere.
- **Other reduplications** (`สั้นๆ`, `ง่ายๆ`, `อะไรๆ`, `เด็กๆ`,
  `เตี้ยๆ`, `อ่อนๆ`) follow register: dropped in personal-blog /
  diary / amateur-essay; preserved in government / institutional
  /formal-edited.

Tech-blog (Blognone) is *internally mixed* in the same publication:
formal `ต่าง ๆ` with space, casual `สั้นๆ`/`ง่ายๆ` without.

### Evidence by register

**Adult-amateur personal blog** (Pantip Blueplanet, settembre):
[`pantip.com/topic/44084956`](https://pantip.com/topic/44084956). 5/5
samples no-space — `สบายๆง่ายๆ`, `จริงๆ` ×2, `เดินๆ`, `อะไรๆ`.

**Plain-diary essay** (GotoKnow, Vicharn Panich):
[`gotoknow.org/posts/727740`](https://www.gotoknow.org/posts/727740).
2/2 samples no-space — `เตี้ยๆ`, `อ่อนๆ`.

**Government / institutional** (Bank of Thailand site):
[`bot.or.th/.../articles.html`](https://www.bot.or.th/th/research-and-publications/articles-and-publications/articles.html).
2/2 samples spaced — `ส่วนต่าง ๆ`, `ตัวเลือกต่าง ๆ` (cookie-banner
prose; institutional editorial style).

**Tech blog (mixed within publication)** (Blognone):
[`blognone.com`](https://www.blognone.com/). 10 samples on the
homepage:

- `ต่าง ๆ` with space — 6 instances (`พันธมิตรต่าง ๆ`,
  `เนื้อหาต่าง ๆ`, `วัตถุต่าง ๆ`, `AI ต่าง ๆ`, `ฝ่ายต่าง ๆ`,
  `คน ๆ เดียว`).
- Other reduplication no-space — 4 instances (`หน้าใหม่ๆ`, `สั้นๆ`
  ×2, `ง่ายๆ`).

**Amateur personal essay** (Minimore, พอกลอน ซาเสียง, sample above):
no-space throughout — `เด็กๆ`, `ไวๆ`, `ว่างๆ`. Same as Pantip /
GotoKnow personal-blog norm.

### Implication for the skill

Two rules, not one. Provisional shapes:

1. **`ต่าง ๆ` always takes the space** in edited Thai. If your
   audit ever sees `ต่างๆ`, flag it — even casual blogs tend to
   space this one.
2. **Other reduplications follow register.** Personal blog /
   marketing-warm / casual: drop the space. Government / academic /
   formal-explainer: keep the space. Tech-blog / news (Register-4):
   sources are mixed; pick one and stay consistent within a piece.

### Action

- Add a `ๆ-spacing` entry to `references/style-rules.md` covering
  the `ต่าง ๆ` carve-out + the register-scoped general rule.
- Mark `docs/research-queue.md` ๆ-spacing entry resolved.
- Caveat: small-N (~20 samples). Confidence is "directional, not
  absolute." Skill rule should be phrased as a default, not a hard
  ai-tells-tier check.

---

## 4. Personification / animacy verbs on systems

**Verdict.** Animacy-restriction hypothesis is wrong. Native Thai
*does* personify systems with `ทน`-class verbs in colloquial /
gaming / community register. The iter-7 `downstream ทนรับ burst`
issue is a **register mismatch**, not a grammar violation.

### Evidence

**`ทนรับ` + system subject — attested.** Google `"ทนรับ" เซิร์ฟเวอร์`:
~11,800 results. Sample (gaming community):

> "เซิร์ฟเวอร์ Virgo แต่แล้วก็ทนรับความหนาแน่นของเหล่าผู้เล่นไม่ไหว
>  (คนเยอะ…)"

— a server "couldn't endure" player density. Native colloquial use,
not a calque.

**`เซิร์ฟเวอร์เครียด` — attested.** Google exact-phrase: ~390 results.
Sample (Reddit Thai gaming):

> "เด็กคนนี้ทำให้ทั้งเซิร์ฟเวอร์เครียดกันเลย ฮ่าๆ"
> "ตอนนี้มีผู้ใช้น้อยลงที่จะทำให้เซิร์ฟเวอร์เครียด"

Native colloquial personification of server-as-stressed.

**`ระบบทน` (exact phrase) on Blognone — not found.** Google
`"ระบบทน" site:blognone.com`: zero exact-phrase matches. Blognone
edited body uses `รองรับ` / `ทนทาน` / `ทนต่อ` (preposition-
licensed) instead.

### Reframe of the rule

What was flagged as "AI personifies systems" is actually
**register leakage from gaming/casual into tech-doc**:

- `ทนรับ` / `เครียด` on systems = colloquial gaming register, fine
  in a Reddit thread.
- Tech-doc / formal-architecture register requires neutral verbs:
  `รองรับ`, `จัดการ`, `จัดสรร`, `ทนทานต่อ`.
- AI errs by mixing colloquial-emotional verbs into formal
  Explainer/News-reference register, not by personifying inanimate
  subjects per se.

The sibling candidates from the research-queue entry —
`ทรมาน`, `เหน็ดเหนื่อย`, `อดทน`, `เครียด`, `สบาย`, `กล้า`, `รู้` —
need re-checking under this reframing. Each is likely register-
restricted, not animacy-restricted.

### Action

- Rewrite `docs/research-queue.md` "Personification verbs"
  entry: drop animacy framing, replace with "colloquial-
  emotional verb leak into Explainer/News register."
- Defer adding a hard rule until iter-8+ shows recurrence; right
  now we have one instance (iter-7 `ทนรับ`) under the new framing.
- If a rule eventually lands, it goes in `references/register.md`
  Register-2/4 ("Avoid colloquial-emotional verbs `ทน*` /
  `เครียด` / `ทรมาน` on system subjects — use neutral
  `รองรับ` / `จัดการ` / `ทนทานต่อ`").

---

## Status

- Task 1 (Fictionlog/Tunwalai) — **resolved out-of-scope.**
- Task 2 (Minimore via Wayback) — **resolved.** Reference-only
  tier now backed by full-essay evidence.
- Task 3 (ๆ-spacing) — **resolved with caveat.** Two-rule shape
  ready for `style-rules.md`. Small-N; phrase as default.
- Task 4 (animacy verbs) — **hypothesis falsified.** Reframed as
  register-leakage; defer rule pending recurrence.

Chrome session ends here per chakrit's session boundary.

---

## Resume notes for next session

**Working tree at session end (uncommitted):**

- `docs/notes/chrome-session-2026-05-13.md` (new — this file)
- `docs/research-queue.md` (resolved 2 entries, reframed 1)
- `skills/kien-thai/references/register.md` (Fictionlog/Tunwalai
  → dropped list; Minimore citation added)
- `skills/kien-thai/references/style-rules.md` (new
  `mai-yamok-spacing` entry)

Sanity tests green (`uv run pytest -x -q` → 16 passed).

**Suggested commit shape** — single commit, scope `kien-thai +
notes`. Message focus: "browser-vetting pass resolves 2 research
items, reframes 1, adds ๆ-spacing rule." Not committed at session
end pending review.

**Open follow-ups (not blocking):**

- ๆ-spacing rule is small-N (~20 samples). Re-evaluate after the
  next eval iteration sees it applied — may need register-specific
  examples in `references/examples.md`.
- The reframed "colloquial-emotional verb leak" item in
  `research-queue.md` waits for iter-8+ recurrence before any rule
  lands. Watch Explainer/News-register outputs for `ทน*` / `เครียด`
  / `ทรมาน` on system subjects.
- Chakrit plans to remove the Claude-in-Chrome MCP connection
  after this session. Future browser-required research will need
  the connection re-added.

