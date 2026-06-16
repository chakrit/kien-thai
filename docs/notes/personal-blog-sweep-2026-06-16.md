# Personal-blog corpus sweep — 2026-06-16

<!-- Sweep to fill the corpus/curated/personal-blog/ gap that gates eval-4 in the
     Typhoon-vs-Claude pass. See plan-typhoon-vs-claude-pass.md. -->

## Why

`corpus/curated/personal-blog/` is empty, so the Typhoon drafter has no few-shot
exemplars for the `personal-blog` register and eval-4 (homecoming essay) is skipped
from the model-route comparison. `register.md` Register 3 already lists *vetted*
personal-blog Models — they just were never extracted into the corpus. This sweep
extracts verbatim snippets from those verified sources.

## Outcome (2026-06-16, later same day)

Browser extension connected; sweep ran. **2 entries extracted** into
`corpus/curated/personal-blog/` — both วิจารณ์ พานิช `ชีวิตที่พอเพียง` walk-diaries
(727740 Sriracha, 727886 Hat Tawan Ron). `EVAL_REGISTER_TO_CORPUS["personal-blog"]`
flipped on; eval-4 now generates and is in the iteration-14 comparison set. Method note:
GotoKnow post-title links are JS handlers (not anchors) — `find` exposes their hrefs
reliably; navigate by the returned `/posts/<id>`. **Still thin/single-author** — the
Pantip target below remains open for register variety. Original blocker notes kept below.

## Blocker (resolved — was, this session)

Autonomous extraction is blocked — same wall as the 2026-05-13 sweep:

- **GotoKnow** → WebFetch `HTTP 403`.
- **web.archive.org** → harness refuses the fetch.
- **Claude-in-Chrome MCP** → extension not connected (`tabs_context_mcp` reports not
  connected). Browser MCP was the unblock path on 2026-05-13; it needs the extension
  running + Chrome logged into the same claude.ai account, and may be unreachable if
  this session is driven remotely (session host ≠ the machine running Chrome).

**Unblock — either:** (a) connect the browser extension and say go, and I'll drive the
extraction live; or (b) paste the verbatim Thai body of the target posts below and I'll
stage them with frontmatter.

## Targets — verified Models (extract first, highest confidence)

Each becomes `corpus/curated/personal-blog/<slug>.md`. Frontmatter pre-filled; the
`[verbatim Thai body]` is the only missing piece. Keep excerpts fair-use sized (1–4
paragraphs per the corpus convention). Voice notes seeded from the 2026-05-13 vetting;
chakrit confirms/edits on extraction.

1. **Vicharn Panich — `ชีวิตที่พอเพียง` diary** (GotoKnow). Verified Model-tier,
   plain-diary register. Pre-LLM long-track author → safe ground truth (provenance).
   - Verified-good post: `https://www.gotoknow.org/posts/727740` → slug
     `vicharn-panich-life-sufficient-727740`.
   - Pull 1–2 sibling `ชีวิตที่พอเพียง` entries for variety (same author page).
   - Frontmatter:

     ```markdown
     ---
     source_url: https://www.gotoknow.org/posts/727740
     retrieved: 2026-06-16
     register: personal-blog
     provenance: pre-2022 long-track author (GotoKnow), pre-LLM-safe
     voice: plain ผม daily-diary, period-light Thai-comma flow, no marketing tells
     notes: [confirm on extraction — first-person discipline, classifier accuracy,
       sentence-rhythm, period frequency]
     ---
     [verbatim Thai body]
     ```

2. **Pantip bylined long-form** (Blueplanet / Klai Baan / Greenzone posters). Verified
   adult-amateur personal blog. Bylined multi-post authors only — NOT anonymous/teen
   pool. One representative long-form post → slug `pantip-<author>-<topic>`. Same
   frontmatter shape, `register: personal-blog`, `provenance: amateur-adult, live web`.

## Targets — literary-essay sub-register (extract, but tag the voice)

3. **Vicharn Panich / GotoKnow literary-memoir** (the "My way" / archaic-narrative
   authors, e.g. post `727737`). Model **only** for the literary-essay sub-register;
   voice is archaic — `notes:` must flag "do not lift archaic lexicon as default
   personal-blog voice." Keep separate from the plain-diary samples above.

## Do NOT pull

Per 2026-05-13 verdicts: readthecloud.co (AI-assist tells now), Storylog (defunct),
Fictionlog/Tunwalai (genre fiction, out of scope), Minimore (reference-only, SPA won't
render). Pedagogy/teacher-notes GotoKnow posts (e.g. `727736`) are not personal-essay.

## After extraction

- Flip `EVAL_REGISTER_TO_CORPUS["personal-blog"]` in `tests/lib.py` from `None` to
  `"personal-blog"` so `typhoon_pass.py` picks it up.
- Re-run `typhoon_pass.py` + `compare_arms.py` to add eval-4 to the comparison set.
- Note the new entries in `corpus/README.md`'s curation index count.
