"""Generate artifacts using `claude --bare --disable-slash-commands -p`.

Run: `uv run pytest -m generate tests/generate/test_claude.py`
Skipped automatically if `claude` is not on PATH.
"""

from __future__ import annotations

import pytest

from lib import CLAUDE, Config, Eval, enabled_backends

pytestmark = pytest.mark.generate


def test_claude(run_eval, eval_case: Eval, config: Config):
    if CLAUDE not in enabled_backends():
        pytest.skip("claude not in EVAL_BACKENDS")
    run_eval(CLAUDE, eval_case, config)
