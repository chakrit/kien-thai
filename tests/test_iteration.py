"""Iteration pinning and arm pairing — what makes a run co-generated.

Both arms of a model-route comparison must land in one iteration tree, and the
comparison must state honestly whether the pair it built was co-generated.
Cheap, default-on, no API calls.
"""

from __future__ import annotations

from pathlib import Path

import pytest

import lib
from lib import ITERATION_ENV, claude_arm, render_comparison, resolve_iteration_dir


@pytest.fixture
def workspace(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    monkeypatch.setattr(lib, "WORKSPACE", tmp_path)
    monkeypatch.delenv(ITERATION_ENV, raising=False)
    return tmp_path


def _claude_output(workspace: Path, number: int, eval_name: str, text: str) -> Path:
    out = workspace / f"iteration-{number}" / eval_name / "claude" / "with_skill"
    out.mkdir(parents=True)
    (out / "output.md").write_text(text, encoding="utf-8")
    return out / "output.md"


def _typhoon_draft(workspace: Path, number: int, eval_name: str) -> Path:
    out = workspace / f"iteration-{number}" / eval_name / "typhoon" / "draft"
    out.mkdir(parents=True)
    (out / "output.md").write_text("ร่าง", encoding="utf-8")
    return out / "output.md"


class TestResolveIterationDir:
    def test_mints_a_fresh_iteration_when_unpinned(self, workspace: Path):
        (workspace / "iteration-4").mkdir()
        assert resolve_iteration_dir().name == "iteration-5"

    def test_pin_by_number_reuses_that_iteration(
        self, workspace: Path, monkeypatch: pytest.MonkeyPatch
    ):
        (workspace / "iteration-9").mkdir()
        monkeypatch.setenv(ITERATION_ENV, "9")
        resolved = resolve_iteration_dir()
        assert resolved == workspace / "iteration-9"

    def test_pin_by_full_name_is_equivalent(
        self, workspace: Path, monkeypatch: pytest.MonkeyPatch
    ):
        monkeypatch.setenv(ITERATION_ENV, "iteration-12")
        assert resolve_iteration_dir() == workspace / "iteration-12"

    def test_pin_creates_the_directory_when_absent(
        self, workspace: Path, monkeypatch: pytest.MonkeyPatch
    ):
        monkeypatch.setenv(ITERATION_ENV, "15")
        assert resolve_iteration_dir().is_dir()

    def test_every_caller_pinned_alike_lands_in_one_tree(
        self, workspace: Path, monkeypatch: pytest.MonkeyPatch
    ):
        """The whole point: separate processes (pytest matrix, typhoon_pass)
        share one iteration instead of each minting its own."""
        monkeypatch.setenv(ITERATION_ENV, "15")
        assert resolve_iteration_dir() == resolve_iteration_dir()

    @pytest.mark.parametrize("pin", ["../escape", "iteration-x", "7/../../etc", "15 16"])
    def test_rejects_a_pin_that_is_not_an_iteration_name(
        self, workspace: Path, monkeypatch: pytest.MonkeyPatch, pin: str
    ):
        monkeypatch.setenv(ITERATION_ENV, pin)
        with pytest.raises(ValueError, match=ITERATION_ENV):
            resolve_iteration_dir()

    @pytest.mark.parametrize("pin", ["", "   "])
    def test_a_blank_pin_means_unset_not_invalid(
        self, workspace: Path, monkeypatch: pytest.MonkeyPatch, pin: str
    ):
        (workspace / "iteration-4").mkdir()
        monkeypatch.setenv(ITERATION_ENV, pin)
        assert resolve_iteration_dir().name == "iteration-5"


class TestClaudeArm:
    def test_same_iteration_pair_is_co_generated(self, workspace: Path):
        _typhoon_draft(workspace, 15, "tech-doc-short")
        expected = _claude_output(workspace, 15, "tech-doc-short", "ข้อความ")
        arm = claude_arm("tech-doc-short", workspace / "iteration-15")
        assert arm is not None
        assert arm.path == expected
        assert arm.co_generated

    def test_falls_back_to_the_latest_other_iteration_and_says_so(self, workspace: Path):
        _claude_output(workspace, 12, "tech-doc-short", "เก่า")
        expected = _claude_output(workspace, 13, "tech-doc-short", "ใหม่กว่า")
        _typhoon_draft(workspace, 15, "tech-doc-short")
        arm = claude_arm("tech-doc-short", workspace / "iteration-15")
        assert arm is not None
        assert arm.path == expected
        assert not arm.co_generated

    def test_same_iteration_wins_over_a_higher_numbered_one(self, workspace: Path):
        expected = _claude_output(workspace, 15, "tech-doc-short", "ร่วมรุ่น")
        _claude_output(workspace, 16, "tech-doc-short", "ใหม่กว่าแต่คนละรุ่น")
        arm = claude_arm("tech-doc-short", workspace / "iteration-15")
        assert arm is not None and arm.path == expected and arm.co_generated

    def test_empty_output_does_not_count_as_an_arm(self, workspace: Path):
        """Failed generations leave 0-byte outputs (iter-7 marketing)."""
        _claude_output(workspace, 15, "tech-doc-short", "   \n")
        expected = _claude_output(workspace, 13, "tech-doc-short", "ของจริง")
        arm = claude_arm("tech-doc-short", workspace / "iteration-15")
        assert arm is not None
        assert arm.path == expected
        assert not arm.co_generated

    def test_no_claude_output_anywhere_is_none(self, workspace: Path):
        _typhoon_draft(workspace, 15, "tech-doc-short")
        assert claude_arm("tech-doc-short", workspace / "iteration-15") is None

    def test_pairs_per_eval_not_across_evals(self, workspace: Path):
        _claude_output(workspace, 15, "marketing-blurb", "คนละ eval")
        assert claude_arm("tech-doc-short", workspace / "iteration-15") is None


class TestRenderComparison:
    """The artifact chakrit actually reads. Rendering must survive every arm state."""

    def test_co_generated_pair_declares_itself_clean(self, workspace: Path):
        draft = _typhoon_draft(workspace, 15, "tech-doc-short")
        _claude_output(workspace, 15, "tech-doc-short", "ข้อความจาก Claude")

        page = render_comparison(draft)

        assert "co-generated — same iteration" in page
        assert "NOT co-generated" not in page
        assert "ข้อความจาก Claude" in page

    def test_cross_iteration_pair_carries_the_caveat(self, workspace: Path):
        draft = _typhoon_draft(workspace, 15, "tech-doc-short")
        _claude_output(workspace, 13, "tech-doc-short", "คนละรุ่น")

        page = render_comparison(draft)

        assert "NOT co-generated" in page

    def test_renders_with_no_claude_arm_at_all(self, workspace: Path):
        draft = _typhoon_draft(workspace, 15, "tech-doc-short")

        page = render_comparison(draft)

        assert "no with_skill output for this eval yet" in page
        assert "no Claude output yet" in page

    def test_both_arms_get_a_signal_row(self, workspace: Path):
        draft = _typhoon_draft(workspace, 15, "tech-doc-short")
        _claude_output(workspace, 15, "tech-doc-short", "ข้อความ")

        page = render_comparison(draft)

        assert "typhoon-draft" in page
        assert "claude+skill" in page
