"""Targeted auditor-recall probe: run-on / under-segmentation.

Not a pytest module — a one-off probe, run directly:

    uv run python tests/probe_runon_recall.py

Question it answers. Run-on sentences keep surviving to `CLEAN` across three
different drafters (Fable-5 F1, iter-9 news paragraph 4, iter-10 tech-doc line
7). Two rules should catch that: `mixed-sentence-length` and
`conceptual-seam-break`. Is the auditor failing to fire them at all, or firing
them in isolation but losing them inside a full document?

The probe feeds native-verified run-on spans through the same audit pass the
kode-thai loop uses, isolated and then in context, and reports which slugs fired.

- fires isolated, misses in context -> recall-miss (dilution); fix anchoring,
  add a pair to the audit bundle. Do not write a new rule.
- misses both ways -> the rule cannot see this; the discourse axis
  (`reads-misstructured`) is the real home. Still not a new sentence rule.

Inputs are quoted verbatim from tracked evidence; no Thai is authored here.
"""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from lib import (  # noqa: E402
    CLAUDE,
    ROOT,
    BundleMode,
    audit_prompt,
    kien_thai_bundle,
)

TIMEOUT_S = 300
SEGMENTATION_SLUGS = ("mixed-sentence-length", "conceptual-seam-break")

# The iteration-10 tech-doc-short prose the auditor declared CLEAN at pass 2.
# chakrit's ear then marked a missing sentence break in line 7.
IT10_CLEAN = (
    ROOT
    / "workspace/iteration-10/tech-doc-short/codex-inline/with_skill/pass-1.md"
)

# Fable-5 baseline probe, finding F1 — verbatim from
# docs/scratch/2026-07-07-fable5-eval1-probe.md. chakrit's verdict: run-on,
# too many ideas chained into one sentence.
FABLE_F1 = (
    "...ช่วยควบคุม cost ของ downstream service ที่คิดเงินตาม usage "
    "เมื่อ request เกิน limit ระบบมักตอบ HTTP 429 พร้อม header "
    "บอกว่าให้รอนานแค่ไหนก่อน retry"
)


@dataclass(frozen=True)
class Probe:
    name: str
    prose: str
    register: str
    note: str


def _audit(prose: str, register: str) -> str:
    bundle = kien_thai_bundle(register=register, mode=BundleMode.AUDIT)
    proc = subprocess.run(
        [*CLAUDE.argv, audit_prompt(prose, bundle, register)],
        capture_output=True,
        text=True,
        timeout=TIMEOUT_S,
    )
    if proc.returncode != 0:
        return f"<backend error {proc.returncode}: {proc.stderr[:200]}>"
    return CLAUDE.parse(proc.stdout).text


def _probes() -> list[Probe]:
    clean_doc = IT10_CLEAN.read_text(encoding="utf-8")
    line7 = clean_doc.splitlines()[6]
    return [
        Probe("fable-f1-isolated", FABLE_F1, "explainer", "native-verified run-on"),
        Probe("it10-line7-isolated", line7, "explainer", "the CLEAN line chakrit broke"),
        Probe("it10-full-doc", clean_doc, "explainer", "reproduces the in-context miss"),
    ]


def main() -> int:
    if not CLAUDE.available:
        print("claude not on PATH", file=sys.stderr)
        return 1

    results = []
    for probe in _probes():
        text = _audit(probe.prose, probe.register)
        fired = [s for s in SEGMENTATION_SLUGS if s in text]
        results.append(
            {
                "probe": probe.name,
                "note": probe.note,
                "clean": text.strip() == "CLEAN",
                "segmentation_slugs_fired": fired,
                "audit_text": text.strip(),
            }
        )
        print(f"{probe.name}: fired={fired or 'NONE'} clean={text.strip() == 'CLEAN'}")

    out = ROOT / "workspace" / "probes" / "runon-recall.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nwrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
