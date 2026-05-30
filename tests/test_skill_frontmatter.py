r"""Every SKILL.md frontmatter must be strict-parseable YAML.

The `skills` CLI parses `name`/`description` out of the frontmatter with a
strict YAML parser. A bare `colon-space` inside an unquoted scalar (e.g.
`TRIGGER when: user asks ...`) is illegal YAML — strict parsers reject the whole
document and the CLI reports "No valid skills found", silently breaking
`skills update`/`skills add`. See chakrit/kien-thai#1.

This guards against that class of bug for *all* skills in the repo, not just the
one that broke.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

SKILLS_DIR = Path(__file__).parent.parent / "skills"
SKILL_FILES = sorted(SKILLS_DIR.glob("*/SKILL.md"))


def _frontmatter(text: str) -> str:
    """Return the YAML block between the leading `---` fence and its closer."""
    assert text.startswith("---\n"), "SKILL.md must open with a `---` frontmatter fence"
    end = text.index("\n---", 4)
    return text[4:end]


def test_skill_files_discovered():
    assert SKILL_FILES, f"no SKILL.md found under {SKILLS_DIR}"


@pytest.mark.parametrize("skill_file", SKILL_FILES, ids=lambda p: p.parent.name)
def test_frontmatter_is_strict_yaml(skill_file: Path):
    fm = _frontmatter(skill_file.read_text())
    try:
        data = yaml.safe_load(fm)
    except yaml.YAMLError as e:
        pytest.fail(
            f"{skill_file.parent.name}/SKILL.md frontmatter is not valid YAML "
            f"(the `skills` CLI will reject it): {e}"
        )
    assert isinstance(data, dict), "frontmatter must parse to a mapping"
    for key in ("name", "description"):
        assert data.get(key), f"frontmatter missing non-empty `{key}`"
