"""Auditor-recall seed + runner.

Each rule's own **Bad** example is a labeled known-bad item: fed to the audit
pass, it should make the auditor cite that rule's slug. The default test
validates extraction (free, no LLM). The runner — marked `recall` — feeds each
example through the audit pass and reports per-slug hit/miss; costly, opt-in
(`uv run pytest -m recall`).

This is the seed for the Phase-2 auditor-recall measure. It tests recall on
*isolated* tells; the review loop's in-context misses (Phase 1) expand the set.
See tests/REVIEW-PROTOCOL.md and notes/decisions/2026-05-30-exemplar-first-pivot.md.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

from lib import (
    CLAUDE,
    WORKSPACE,
    BundleMode,
    KnownBad,
    audit_prompt,
    extract_known_bad,
    kien_thai_bundle,
)

TIMEOUT_S = 300


def test_known_bad_seed_extracts():
    items = extract_known_bad()
    assert len(items) >= 20, f"too few known-bad items extracted: {len(items)}"
    assert all(it.bad for it in items), "empty Bad example extracted"
    assert all(it.slug for it in items), "missing slug"


@pytest.mark.recall
def test_auditor_recall():
    if not CLAUDE.available:
        pytest.skip("claude not on PATH")
    rows = [(it, _audit_cites_slug(it)) for it in extract_known_bad()]
    assert rows, "no known-bad items to audit"
    hits = sum(fired for _, fired in rows)
    _write_report(rows, hits / len(rows))


def _audit_cites_slug(it: KnownBad) -> bool:
    bundle = kien_thai_bundle(register=it.register, mode=BundleMode.AUDIT)
    proc = subprocess.run(
        [*CLAUDE.argv, audit_prompt(it.bad, bundle, it.register)],
        capture_output=True,
        text=True,
        timeout=TIMEOUT_S,
    )
    if proc.returncode != 0:
        return False
    return it.slug in CLAUDE.parse(proc.stdout).text


def _write_report(rows: list[tuple[KnownBad, bool]], rate: float) -> Path:
    hits = sum(fired for _, fired in rows)
    misses = [it for it, fired in rows if not fired]
    lines = [
        "# Auditor-recall report",
        "",
        "Seed: each rule's own Bad example. Miss = the audit pass did not cite the",
        "rule's slug when fed that rule's own canonical Bad example.",
        "",
        f"Recall: {hits}/{len(rows)} = {rate:.0%}",
        "",
        "## Misses",
        "",
    ]
    lines += [f"- `{it.slug}` ({it.source}) — {it.bad[:70]}" for it in misses] or [
        "- none"
    ]
    report = WORKSPACE / "recall-report.md"
    report.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return report
