# Inline iteration — the default generate mode

**Status:** accepted

Generating an iteration **inline** — in the active session, via a fresh subagent or
chakrit driving Codex — is the default. The cold pytest harness (`pytest -m generate`,
shelling out to `claude -p` / `codex exec`) is the specialized tool: reach for it only
when you need contamination-free, cross-iteration A/B numbers — which, post-pivot, is
rare until an automated gradient + discrimination metric exists. Direction:
[`../decisions/2026-05-30-exemplar-first-pivot.md`](../decisions/2026-05-30-exemplar-first-pivot.md).

Why inline is the default: bundle-effect convergence is demoted as a quality signal
(`CLEAN` = ruleset-coverage, not naturalness), so the cold harness's signature deliverable
is rarely the thing we need. The real signal is the review loop on the generated
outputs, and that runs on inline outputs just as well.

> **CLEAN is not the finish line.** Reaching `CLEAN` makes an output *skill-clean* (the
> ruleset finds nothing), not *chakrit-clean*. Review of skill-clean outputs — and the
> skill-clean-vs-chakrit-clean measurement it collects — is the outer loop, specified in
> [`review-protocol.md`](review-protocol.md).

## Fresh context per generation

Inline generation is shaped by whatever is already in the session. To keep that from
quietly steering the Thai, generate each output from **fresh context**: a fresh subagent
(no conversation history) or a fresh Codex session per output. Tag inline outputs
`mode: "inline"` in `meta.json` so later analysis can filter them — they are
audit/probe and review material, not cross-iteration bundle-effect measurements.

## Drivers

Three ways to run the inline loop. All share the bundle preprocessor, prompt templates,
and artifact layout below — only the generator differs.

### 1. Workflow tool — recommended for the claude-inline half (proposed)

The Workflow tool is the cleanest inline driver: deterministic JS orchestrates fresh
subagents, the LLM is reduced to generate + audit, evals fan out in parallel, and the
audit verdict returns as validated structured output (no fragile first-line string
check). Shape:

```
pipeline(evals,
  eval  => agent(draftPrompt(eval), {schema: PROSE}),        // pass-0, fresh subagent
  draft => auditFixLoop(draft, eval),                        // audit -> fix until CLEAN
)
// auditFixLoop: while !clean && i < 5 { audit (schema: VERDICT); if clean break; fix }
```

Caveats, stated honestly:

- **Claude-only.** Workflow agents are Claude subagents; it cannot spawn Codex. It drives
  the claude-inline half; the Codex half stays chakrit-driven (driver 3).
- **No file I/O in scripts.** The workflow returns structured results; the session writes
  the `workspace/iteration-N/...` artifacts from them.
- **Opt-in + token cost.** Subagents consume tokens (but no external API key / CLI). It is
  also the substrate the automated gradient will later run on — the audit stage becomes
  the hill-climb once a metric exists.

Tracked in [`../work-queue.md`](../work-queue.md); prototype when ready.

### 2. Manual subagent (chat-Claude)

Chat-Claude spawns a fresh subagent per pass via the Agent tool and writes artifacts to
disk itself. The driving session computes the bundle, constructs the prompt, spawns the
subagent, writes the output, and drives the audit/fix loop (one subagent per pass). The
subagent gets only the bundle + prompt — no conversation history — the closest
approximation to cold-Claude without shelling out.

### 3. Manual Codex (chakrit-driven)

The same procedure by hand: compute the bundle, paste the constructed prompt into a fresh
`codex` session, save the output to the right path; for the audit loop, paste the audit
prompt, save; if not `CLEAN`, paste the fix prompt, save the fixed prose; repeat. This is
chakrit's current flow and stays first-class.

## Step 1 — pick eval and register

Evals live in `evals/evals.json`. Each has `id`, `name`, `prompt`, `register`. The
register slug passed to the bundle must be a key the preprocessor knows
(`tests/lib.py:REGISTER_HEADERS`), which is the same value as the eval's `register`
field — not the corpus category name. Current evals:

- `tech-doc-short` → `explainer`
- `marketing-blurb` → `marketing-saas-sme`
- `news-feature-bts` → `news`
- `personal-essay-homecoming` → `personal-blog`
- `exec-brief-oss-bi-hana` → `explainer`

## Step 2 — compute the bundles

Run both — pass-0 uses the draft bundle; audit and fix passes use the audit bundle.

```sh
uv run python -c "from tests.lib import kien_thai_bundle; \
  print(kien_thai_bundle(register='REGISTER_SLUG', mode='draft'))" \
  > /tmp/bundle-draft.md

uv run python -c "from tests.lib import kien_thai_bundle; \
  print(kien_thai_bundle(register='REGISTER_SLUG', mode='audit'))" \
  > /tmp/bundle-audit.md
```

Substitute `REGISTER_SLUG` with the eval's `register` field.

## Step 3 — pass-0 (initial draft)

Prompt template (matches `tests/lib.py:skill_prompt` for `with_skill`):

```
ใช้แนวทางการเขียนต่อไปนี้:

<skill>
[contents of /tmp/bundle-draft.md]
</skill>

งานที่ต้องทำ:

[eval prompt from evals/evals.json]
```

Save the constructed prompt to `pass-0-prompt.txt` in the output dir before invoking the
generator. After generation, save the prose to `pass-0.md` in the same dir. The agent
slot is `claude-inline` for subagent-driven, `codex-inline` for chakrit-driven Codex.

For the `baseline` config (no skill bundle), the prompt is just the eval prompt verbatim.
Save the constructed prompt to `input-prompt.txt`, the prose to `output.md`, and skip the
audit loop.

## Step 4 — audit loop (with_skill only; up to 5 passes)

Loop counter `i` starts at 1. Per pass:

### 4a — audit prompt

Template (matches `_audit_prompt`):

```
ใช้แนวทางการเขียนต่อไปนี้:

<skill>
[contents of /tmp/bundle-audit.md]
</skill>

prose นี้เป็น register `REGISTER_SLUG`

งาน: อ่าน prose ทั้งหมดให้จบก่อน แล้วค่อย flag issues — อย่าสแกนทีละบรรทัด. Pre-check: scan `forbidden-phrases.md` blocklist กับ prose (เฉพาะ occurrence ที่ไม่ได้อยู่ใน backtick — use/mention exemption). จากนั้น audit ตามกฎใน skill เต็มชุด. สำหรับทุก issue ให้ cite ด้วย slug ก่อน (เช่น `f4/targhak-closure`, `wrong-classifier`, `f6/ko-resumptive`); ยกข้อความที่ผิดมาประกอบทุกครั้ง. ถ้าผ่านทุกข้อ ให้ตอบบรรทัดเดียวว่า `CLEAN` ห้าม output prose

<prose>
[current prose]
</prose>
```

Save to `pass-i-audit-prompt.txt`. Run generator. Save output to `pass-i-audit.md`.

**Convergence check**: if the audit output's first non-empty line starts with `CLEAN`
(case-insensitive), stop the loop. Current prose is final. (Reaching this point is
*skill-clean* — the review loop still applies; see `review-protocol.md`.)

### 4b — fix prompt

Only runs if audit was not `CLEAN`. Template (matches `_fix_prompt`):

```
ใช้แนวทางการเขียนต่อไปนี้:

<skill>
[contents of /tmp/bundle-audit.md]
</skill>

prose นี้เป็น register `REGISTER_SLUG`

issue ที่ต้องแก้:

[audit output from 4a]

prose ปัจจุบัน:

<prose>
[current prose]
</prose>

งาน: แก้ prose ตาม issue ข้างบน output เฉพาะ prose ที่แก้แล้ว ห้ามใส่คำอธิบาย ห้ามใส่หัวเรื่อง
```

Save to `pass-i-fix-prompt.txt`. Run generator. Save output to `pass-i.md`. This prose
becomes the input to the next audit pass.

**Max passes**: 5. If still not `CLEAN` after pass 5, stop; record `converged: false`.

## Step 5 — finalize

- Copy the last prose (last `pass-i.md` if the loop ran, else `pass-0.md` if pass-1 audit
  returned `CLEAN`) to `output.md` in the same dir.
- Write `meta.json`:

```json
{
  "backend": "claude-inline | codex-inline",
  "config": "with_skill | baseline",
  "eval_id": 0,
  "eval_name": "name",
  "mode": "inline",
  "loop_passes": 0,
  "converged": true,
  "passes": [
    {"pass": 0, "kind": "initial"},
    {"pass": 1, "kind": "audit", "clean": false},
    {"pass": 1, "kind": "fix"},
    {"pass": 2, "kind": "audit", "clean": true}
  ]
}
```

`usage` and `duration_s` are omitted — no telemetry in inline mode.

## Artifact layout

Identical to harness output; the agent slot takes `claude-inline` or `codex-inline`:

```
workspace/iteration-N/<eval-name>/<agent>/<config>/
├── pass-0-prompt.txt           # with_skill only
├── pass-0.md                   # with_skill only
├── pass-1-audit-prompt.txt
├── pass-1-audit.md
├── pass-1-fix-prompt.txt       # only if pass-1 audit was not CLEAN
├── pass-1.md                   # only if fix ran
├── ...
├── input-prompt.txt            # baseline only
├── output.md                   # final prose
└── meta.json
```

Pick the iteration number with the helper, or reuse an existing dir to extend a partial
run:

```sh
uv run python -c "from tests.lib import next_iteration_dir; print(next_iteration_dir())"
```

When you create a fresh iteration `N`, add a row to
[`../../workspace/INDEX.md`](../../workspace/INDEX.md) — date, mode/scope (note `inline`), Review
`pending` — and flip that cell to `reviewed` with a feedback link once it is reviewed per
[`review-protocol.md`](review-protocol.md). The INDEX is the tracked ledger of what
iterations exist; an unrecorded run leaves it lying about the repo's state.

## Notes on register-slug values

The slug passed to `kien_thai_bundle(register=...)` is the eval's `register` field, which
must be a key in `tests/lib.py:REGISTER_HEADERS`: `explainer`, `marketing-saas-sme`,
`marketing-b2b-formal`, `marketing-fintech-warm`, `marketing-retail-tech`,
`personal-blog`, `news`, `academic`, `official`. These are *register* keys, not corpus
category names — `evals/evals.json` is the authoritative source for which eval uses which.
