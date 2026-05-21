# Inline iteration — alt to the pytest harness

Run a generation iteration without shelling out to `claude -p` or `codex exec`.
Use the active session (chat-Claude via subagent, or chakrit driving codex
manually) as the generator. Saves API tokens; trades contamination-freedom
for cost.

The Python tooling in `tests/lib.py` and `tests/generate/conftest.py` stays
authoritative. This document describes a parallel procedure that uses the
same bundle preprocessor, prompt templates, and artifact layout — so inline
outputs slot into `workspace/iteration-N/` alongside harness outputs and
remain comparable structurally.

## When to use this vs the harness

| Use case                                                 | Tool                  |
| -------------------------------------------------------- | --------------------- |
| Quick spot-check / probe / sanity                        | Inline                |
| Audit work, rule-validation probes                       | Inline                |
| Publishable iter-N artifacts cited across iterations     | Harness (cold-Claude) |
| Cross-backend signal (claude vs codex disagreement)      | Harness               |
| Bundle-effect measurement under controlled conditions    | Harness               |

**Contamination caveat**: inline generation in a live session is *not*
equivalent to harness output. The session window contains conversation
history, earlier edits, recent corrections — all of which influence the
model's Thai. Outputs are marked `mode: "inline"` in meta.json so future
analysis can filter.

## How chat-Claude runs this (subagent variant)

For each `(eval, config)` to generate, spawn a fresh subagent. The subagent
gets only the bundle + eval prompt — no conversation history — which is the
closest approximation to cold-Claude available without shelling out.

The driving session (chat-Claude) is responsible for:

- Computing the bundle.
- Constructing the prompt.
- Spawning the subagent.
- Writing artifacts to disk.
- Driving the audit/fix loop (one subagent invocation per pass).

## How chakrit runs this with codex manually

Same procedure, executed by hand:

1. Compute the bundle (commands below).
2. Paste the constructed prompt into a fresh `codex` invocation.
3. Save codex's output to the right path.
4. For audit loop: construct the audit prompt, paste, save; if not `CLEAN`,
   construct the fix prompt, paste, save the fixed prose; repeat.

The prompt templates and artifact layout are identical to the chat-Claude
flow.

## Step 1 — pick eval and register

Evals live in `evals/evals.json`. Each has `id`, `name`, `prompt`,
`register`. For example, `marketing-blurb` (register: `marketing-saas-sme`),
`tech-doc-short` (register: `tech-writing`), `news-feature-bts` (register:
`newspaper-feature`).

## Step 2 — compute the bundles

Run both — pass-0 uses the draft bundle; audit and fix passes use the audit
bundle.

```sh
uv run python -c "from tests.lib import kien_thai_bundle; \
  print(kien_thai_bundle(register='<register-slug>', mode='draft'))" \
  > /tmp/bundle-draft.md

uv run python -c "from tests.lib import kien_thai_bundle; \
  print(kien_thai_bundle(register='<register-slug>', mode='audit'))" \
  > /tmp/bundle-audit.md
```

Substitute `<register-slug>` with the eval's register field.

## Step 3 — pass-0 (initial draft)

**Prompt template** (matches `tests/lib.py::build_prompt` for `with_skill`):

```
ใช้แนวทางการเขียนต่อไปนี้:

<skill>
<contents of /tmp/bundle-draft.md>
</skill>

งานที่ต้องทำ:

<eval prompt from evals/evals.json>
```

Save the constructed prompt to
`workspace/iteration-N/<eval-name>/<agent>/with_skill/pass-0-prompt.txt`
before invoking the generator. After generation, save the prose to
`pass-0.md` in the same directory. `<agent>` is `claude-inline` for
subagent-driven, `codex-inline` for chakrit-driven codex.

For `baseline` config (no skill bundle), the prompt is just the eval prompt
verbatim. Save constructed prompt to `input-prompt.txt`, prose to
`output.md`, and skip the audit loop.

## Step 4 — audit loop (with_skill only; up to 5 passes)

Loop counter `i` starts at 1. Per pass:

### 4a — audit prompt

Template (matches `_audit_prompt`):

```
ใช้แนวทางการเขียนต่อไปนี้:

<skill>
<contents of /tmp/bundle-audit.md>
</skill>

prose นี้เป็น register `<register-slug>`

งาน: อ่าน prose ทั้งหมดให้จบก่อน แล้วค่อย flag issues — อย่าสแกนทีละบรรทัด. Pre-check: scan `forbidden-phrases.md` blocklist กับ prose (เฉพาะ occurrence ที่ไม่ได้อยู่ใน backtick — use/mention exemption). จากนั้น audit ตามกฎใน skill เต็มชุด. สำหรับทุก issue ให้ cite ด้วย slug ก่อน (เช่น `f4/targhak-closure`, `wrong-classifier`, `f6/ko-resumptive`); ยกข้อความที่ผิดมาประกอบทุกครั้ง. ถ้าผ่านทุกข้อ ให้ตอบบรรทัดเดียวว่า `CLEAN` ห้าม output prose

<prose>
<current prose>
</prose>
```

Save constructed prompt to `pass-<i>-audit-prompt.txt`. Run generator. Save
output to `pass-<i>-audit.md`.

**Convergence check**: if the audit output's first non-empty line starts
with `CLEAN` (case-insensitive), stop the loop. Current prose is final.

### 4b — fix prompt

Only runs if audit was not `CLEAN`. Template (matches `_fix_prompt`):

```
ใช้แนวทางการเขียนต่อไปนี้:

<skill>
<contents of /tmp/bundle-audit.md>
</skill>

prose นี้เป็น register `<register-slug>`

issue ที่ต้องแก้:

<audit output from 4a>

prose ปัจจุบัน:

<prose>
<current prose>
</prose>

งาน: แก้ prose ตาม issue ข้างบน output เฉพาะ prose ที่แก้แล้ว ห้ามใส่คำอธิบาย ห้ามใส่หัวเรื่อง
```

Save constructed prompt to `pass-<i>-fix-prompt.txt`. Run generator. Save
output to `pass-<i>.md`. This prose becomes the input to the next audit
pass.

**Max passes**: 5. If still not `CLEAN` after pass 5, stop; record
`converged: false`.

## Step 5 — finalize

- Copy the last prose (last `pass-<i>.md` if loop ran, else `pass-0.md` if
  pass-1 audit returned `CLEAN`) to `output.md` in the same directory.
- Write `meta.json`:

```json
{
  "backend": "claude-inline" | "codex-inline",
  "config": "with_skill" | "baseline",
  "eval_id": <id>,
  "eval_name": "<name>",
  "mode": "inline",
  "loop_passes": <last i that ran, 0 if baseline>,
  "converged": <true|false>,
  "passes": [
    {"pass": 0, "kind": "initial"},
    {"pass": 1, "kind": "audit", "clean": false},
    {"pass": 1, "kind": "fix"},
    {"pass": 2, "kind": "audit", "clean": true}
  ]
}
```

`usage` and `duration_s` fields are omitted — no telemetry available in
inline mode.

## Artifact layout

Identical to harness output, with `<agent>` slot taking `claude-inline` or
`codex-inline`:

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

Iteration directory: use the next-iteration helper to pick `N` —

```sh
uv run python -c "from tests.lib import next_iteration_dir; \
  print(next_iteration_dir())"
```

— or reuse an existing iteration directory if extending a partial run.

## Notes on register-slug values

The slug passed to `kien_thai_bundle(register=...)` matches the `register`
field in `evals/evals.json`, not the human-readable register family name in
`references/register.md`. Examples currently in evals:

- `marketing-saas-sme`
- `tech-writing`
- `newspaper-feature`

Check `evals/evals.json` for the authoritative list.
