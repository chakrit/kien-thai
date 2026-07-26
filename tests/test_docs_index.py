"""Every durable doc must be reachable from an index.

Discoverability rots silently: a doc lands, nothing links it, and a fresh session
never finds it. These checks make that a build failure instead of a slow leak.

Two invariants:

1. Every `docs/**/*.md` is linked from `docs/README.md` (the complete index).
2. Every top-level entry point is linked from `CLAUDE.md` (the root instruction
   file an agent always loads).

Free — pure filesystem and string work, no LLM, runs in the default suite.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

from lib import EVALS_FILE, ROOT

_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")

DOCS = ROOT / "docs"
DOCS_INDEX = DOCS / "README.md"
CLAUDE_MD = ROOT / "CLAUDE.md"

# Entry points an agent must be able to reach from the root instruction file.
# Paths, not prose — a rename breaks the test, which is the point.
ROOT_ENTRY_POINTS = (
    "docs/README.md",
    "docs/work-queue.md",
    "docs/research-queue.md",
    "docs/human-tasks-queue.md",
    "workspace/INDEX.md",
    "corpus/README.md",
    "CONTRIBUTING.md",
    "](README.md)",  # the repo's own front door — bare "README.md" would match docs/README.md
)


def _docs_markdown() -> list[Path]:
    return sorted(p for p in DOCS.rglob("*.md") if p != DOCS_INDEX)


def test_every_doc_is_indexed():
    index = DOCS_INDEX.read_text(encoding="utf-8")
    missing = [
        str(p.relative_to(ROOT))
        for p in _docs_markdown()
        if str(p.relative_to(DOCS)) not in index
    ]
    assert not missing, (
        "docs not linked from docs/README.md — add a row in the same change "
        f"that adds the file: {missing}"
    )


@pytest.mark.parametrize("entry", ROOT_ENTRY_POINTS)
def test_root_instructions_link_entry_point(entry: str):
    assert entry in CLAUDE_MD.read_text(encoding="utf-8"), (
        f"CLAUDE.md does not reference {entry} — a fresh session cannot discover it"
    )


def test_claude_md_eval_count_matches_the_eval_set():
    """A hand-maintained count in prose rots the moment the set changes.

    CLAUDE.md's decision count did exactly that (said 7, were 9) and was deleted
    rather than corrected. The eval counts earn their place — they tell a reader
    the scale of the test set — so they get a guard instead.
    """
    evals = json.loads(EVALS_FILE.read_text(encoding="utf-8"))["evals"]
    registers = {e["register"] for e in evals}
    claimed = f"{len(evals)} eval prompts across {len(registers)} registers"

    assert claimed in CLAUDE_MD.read_text(encoding="utf-8"), (
        f"CLAUDE.md no longer states the true eval scale — expected {claimed!r}"
    )


def test_index_has_no_dead_links():
    """The index must not point at files that were moved or deleted."""
    targets = _LINK_RE.findall(DOCS_INDEX.read_text(encoding="utf-8"))
    dead = [
        t
        for t in targets
        if not t.startswith(("http", "#", "mailto:"))
        and not (DOCS / t.split("#")[0]).exists()
    ]
    assert not dead, f"docs/README.md links nonexistent targets: {dead}"
