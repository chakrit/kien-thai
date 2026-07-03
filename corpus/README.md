# corpus

Thai-prose source material backing the rules in `skills/kien-thai/`. Every rule
in the skill should be traceable to a sample here — "rules don't get added on
vibes" (CLAUDE.md).

## Layout

```
corpus/
├── curated/                 # 1–4 paragraph hand-picked snippets
│   └── <category>/<source-slug>.md
└── raw/                     # full article body, HTML/nav/ads stripped
    └── <category>/<source-slug>.md
```

`curated/` files are the study samples — short enough to read at a glance,
classified by register and voice. `raw/` retains more of the article in case
later analysis needs context the snippet drops.

## Categories

| Path                      | Voice                                    |
| ------------------------- | ---------------------------------------- |
| `marketing/saas-sme/`     | warm-direct, SaaS landing for SMB owners |
| `marketing/b2b-formal/`   | advisory authority, enterprise/B2B       |
| `marketing/fintech-warm/` | warm-pro, consumer fintech               |
| `marketing/retail-tech/`  | practical-direct, merchant tooling       |
| `tech-writing/`           | first-person dev war-story / explainer   |
| `personal-blog/`          | plain ผม daily-diary, non-tech personal essay |
| `bank-longform/`          | educational advisory, no body particles  |
| `newspaper-feature/`      | literary analytical long-form            |
| `translation/`            | confident essayist, hybrid vocabulary    |
| `scholarly/`              | reference grammars, linguistics papers, translation-craft essays |

## Per-entry frontmatter

```markdown
---
source_url: https://...
retrieved: 2026-05-10
register: marketing/saas-sme
voice: warm-direct
notes: คุณ throughout, ! at hook, no body particles
---
[prose verbatim]
```

`notes` calls out the voice/register signals that justified inclusion — what
particles, connectives, cadence, person-arity choices the sample demonstrates.

## Out of scope

Per CLAUDE.md locked decisions: no celebrity columnists, no FMCG/insurance ad
sensationalism, no retail flash-sale copy, no translated foreign SaaS landing
pages (likely calqued).

## Provenance-safety (coming axis)

Per the 2026-05-30 direction
([`../docs/decisions/2026-05-30-exemplar-first-pivot.md`](../docs/decisions/2026-05-30-exemplar-first-pivot.md)),
recency is a contamination risk: post-2022 web marketing may itself be AI-drafted (the
AWS-Thailand flag in `workspace/iteration-7/feedback.md`). A `provenance` frontmatter
field — pre/post-2022, print/archive vs live web, established pre-LLM author — is planned
so calibration can down-weight suspect sources. Pre-LLM print, archives, and long-track
pre-2022 authors are safer ground truth.

## Curation index

55 curated entries across 10 categories as of 2026-06-16. Scholarly entries
follow a different frontmatter schema (`author`, `work`, `relevance`) — see
the per-entry files for the actual layout.

### personal-blog (2)

- `vicharn-panich-sriracha-walk-727740` — plain ผม walk-diary, period-light
- `vicharn-panich-tawanron-walk-727886` — companion walk-diary; verbatim author typos noted

> Thin and single-author (วิจารณ์ พานิช). Expand with a second author (Pantip
> bylined long-form) before treating as representative — see
> [`../docs/notes/personal-blog-sweep-2026-06-16.md`](../docs/notes/personal-blog-sweep-2026-06-16.md).

### bank-longform (5)

- `krungsri-loy-krathong-asean` — encyclopedic-neutral, zero person-arity
- `krungsri-online-scammer-report` — light "เรา"-victim frame + imperatives
- `ttb-emergency-saving` — bank-warm hybrid "เรา" + "คุณ", coach-tone
- `ttb-finance-planning` — neutral-bank, age-bracket structured, formula-as-prose
- `ttb-spend-smart-stress-less` — bank-warm coach with `…` ellipsis closer

### marketing/b2b-formal (5)

- `aws-thailand-agentcore` — enterprise-tech "คุณ"-explainer + dev "เรา"
- `aws-thailand-custom-agents` — SDK-tutorial "คุณ"+"เรา", em-dash layout
- `aws-thailand-spip-security` — first-person "ผม" + ครับ tutorial variant
- `bluebik-homepage` — third-person institutional, English-Thai code-switch
- `wisesight-homepage` — light "คุณ"+"ของเรา", verb-first imperatives

### marketing/fintech-warm (5)

- `krungsri-ai-art` — lifestyle-tutorial, mid-conversational
- `krungsri-ai-automation` — bank-as-business-content, no warmth particles
- `krungsri-chatgpt-horoscope` — most slang-vivid (มูเตลู), online-Thai voice
- `scb-just4u-ai` — product-feature warm-pro, mixed "เรา"/"คุณ"
- `scb-multi-skill` — conversational lifestyle-coach, vivid colloquial

### marketing/retail-tech (5)

- `lalamove-2025-results` — corporate annual-results press release
- `lalamove-khonkaen-expansion` — regional-expansion + executive quote
- `lalamove-sme-shipping-cost` — data-driven press release with statistics
- `lalamove-soft-skills-workshop` — PR-press with quoted speakers, third-person
- `lalamove-suburban-delivery` — practical-direct merchant blog, "!" + "สาย-" slang

### marketing/saas-sme (5)

- `flowaccount-food-cost` — definition-first SEO-tutorial, third-person
- `flowaccount-online-selling` — listicle-style "10 tips", numbered imperative
- `foodstory-homepage` — fragment-tile SaaS landing, no person-arity
- `page365-homepage` — testimonial-driven, ครับ/ค่ะ inside customer quotes
- `peakaccount-stamp-duty` — accounting-tutorial mid-formal, no English

### tech-writing (5)

- `somkiat-architect-ivory-tower` — opinion-essay with "!!" + "สวัสดี" closer
- `somkiat-bun-testing` — lower-volume release-note explainer, "อีกด้วย" tic
- `somkiat-high-test-low-quality` — diagnosis essay with "นั่นเอง" tic
- `somkiat-openai-cli` — short release-note, "ได้เลย" cadence repeated
- `somkiat-tech-radar-34` — opinionated commentary, "!!" emphasis high

### newspaper-feature (6)

- `the101-city-for-all` — academic-feature with inline citations
- `thematter-friendship-break-up` — soft lifestyle feature with "นะ" warmth
- `thematter-job-scams` — analytical-feature with `'...'` concept-quoting
- `thematter-why-we-work` — philosophical-explainer with "เรา"-hypothetical
- `way-prasert-mirror-iran` — first-person "ผม" memoir-essay, "ครับ" closer
- `way-prasert-oil-pm25` — diary-style essay, spouse-frame, op-ed cadence

### translation (5)

- `salforest-ai-research` — academic translator, bracketed-bilingual gloss
- `salforest-financing-renew` — opinion-essay with affective formal register
- `salforest-irb-forum-opentalk` — multi-speaker NGO-feature, named experts
- `salforest-sme-sustainability` — development-economics analytical
- `salforest-us-mass-layoff` — foreign-affairs analysis, numbered "ประการ"

### scholarly (12)

Reference grammars, linguistics papers, and translation-craft sources backing
kien-thai rules with citation-grade evidence. Per-entry frontmatter uses
`author` / `work` / `relevance` instead of the prose-corpus schema.

- `iwasaki-ingkaphirom-reference-grammar` — Cambridge functional grammar;
  chapter 30 "Discourse" is the core reference for topic-comment, zero
  anaphora, particles
- `smyth-essential-grammar` — Routledge pedagogical reference; mood particles,
  aspect, register
- `higbie-thinsan-thai-grammar` — Orchid Press spoken-Thai reference; explicit
  formal-vs-spoken register pairings
- `li-thompson-topic-prominent` — Li & Thompson (1976) typological framework
  underpinning Frame 1 (topic-prominence)
- `prasithrathsint-thuk-passive` — establishment of neutral passive vs
  persistence of adversative ถูก; backs `non-adversative-thuk`
- `takahashi-koo-pragmatic-particle` — interpersonal uses of ก็; backs Frame 6
  topic-resumptive bridge (`f6/ko-resumptive`)
- `olsson-iamitive-laew` — typological grouping of แล้ว as iamitive; backs
  Frame 4 closure with แล้ว (`f4/laeo-completion`)
- `thai-discourse-treebank-tacl` — TACL 2024 corpus on Thai connectives;
  backs `chueung-stacking` with the Expansion.GenExpansion sense
- `aclanthology-thai-classifiers` — Singnoi 2001 + Hundius/Kölver 1983
  classifier taxonomy; backs `wrong-classifier`
- `thai-language-com-spacing` — Slayden + thai-notes + Royal Institute
  spacing manual; backs Frame 3 + `mid-paragraph-period`
- `wikipedia-thai-language-grammar` — tertiary aggregator with primary-source
  crosscheck quotes for register / passive / classifier / pro-drop rules
- `barang-thai-literary-translation` — Marcel Barang's translation principles;
  backs `idiom-localize` and `source-fidelity`
