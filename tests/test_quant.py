"""Advisory quantitative checks on the latest iteration's outputs.

These are NOT a quality verdict — prose quality is a human call.
They flag mechanical AI tells: forbidden filler phrases and excessive
formal connectives. Treat failures as conversation starters, not gates.

Skipped automatically when no iteration exists yet.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

from lib import CONNECTIVES, latest_iteration, load_forbidden_phrases

pytestmark = pytest.mark.evaluate

# Forbidden phrases and connectives are now sourced from references/ via lib so
# this advisory check and compare_arms.py share one list — no drift. The
# blocklist is grep-able by design (forbidden-phrases.md). Substring match is
# advisory; the kode-thai audit handles use/mention exemption.
CONNECTIVE_DENSITY_LIMIT = 15.0  # occurrences per 1000 chars


def _output_files() -> list[Path]:
    iter_dir = latest_iteration()
    if iter_dir is None:
        return []
    return list(iter_dir.glob("*/*/*/output.md"))


def pytest_generate_tests(metafunc: pytest.Metafunc):
    if "output_file" in metafunc.fixturenames:
        files = _output_files()
        if not files:
            pytest.skip("no iteration outputs yet — run `pytest -m generate` first")
        metafunc.parametrize(
            "output_file", files, ids=[str(p.relative_to(p.parents[3])) for p in files]
        )


def test_no_forbidden_phrases(output_file: Path):
    text = output_file.read_text(encoding="utf-8")
    hits = [p for p in load_forbidden_phrases() if p in text]
    assert not hits, f"forbidden filler in {output_file.parent.name}: {hits}"


def test_connective_density(output_file: Path):
    text = output_file.read_text(encoding="utf-8")
    if not text.strip():
        pytest.skip("empty output")
    count = sum(len(re.findall(c, text)) for c in CONNECTIVES)
    density = count / max(len(text), 1) * 1000
    assert density <= CONNECTIVE_DENSITY_LIMIT, (
        f"{output_file.parent.name}: {density:.1f} connectives/1k chars "
        f"(limit {CONNECTIVE_DENSITY_LIMIT})"
    )
