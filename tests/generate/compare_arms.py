#!/usr/bin/env python3
"""Write the Typhoon-vs-Claude comparison artifact for every eval in an iteration.

Discovery and file writing only — the page itself is `lib.render_comparison`,
which pairs each Typhoon draft with a Claude `with_skill` output and states
whether the pair was co-generated.

Run: uv run python tests/generate/compare_arms.py [iteration-N]
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from lib import WORKSPACE, latest_iteration, render_comparison  # noqa: E402


def build(iteration: Path) -> list[str]:
    written: list[str] = []
    for draft in sorted(iteration.glob("*/typhoon/draft/output.md")):
        dest = draft.parents[2] / "comparison.md"
        dest.write_text(render_comparison(draft), encoding="utf-8")
        written.append(str(dest.relative_to(WORKSPACE.parent)))
    return written


def _target_iteration() -> Path:
    if len(sys.argv) > 1:
        iteration = WORKSPACE / sys.argv[1]
        if not iteration.is_dir():
            raise SystemExit(f"no such iteration: {iteration}")
        return iteration

    iteration = latest_iteration()
    if iteration is None:
        raise SystemExit("no iterations in workspace")
    return iteration


def main() -> None:
    iteration = _target_iteration()
    written = build(iteration)

    if not written:
        print(f"no typhoon drafts found in {iteration.name}")
        return
    print(f"wrote {len(written)} comparison(s):")
    for path in written:
        print(f"  {path}")


if __name__ == "__main__":
    main()
