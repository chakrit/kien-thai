"""Plumbing checks. Cheap, default-on, no API calls."""

from __future__ import annotations

import json

from lib import (
    CLAUDE,
    CODEX,
    EVALS_FILE,
    SKILL_PATH,
    BundleMode,
    Eval,
    kien_thai_bundle,
    skill_prompt,
)


def test_evals_json_loads():
    data = json.loads(EVALS_FILE.read_text(encoding="utf-8"))
    assert data["skill_name"] == "kien-thai"
    assert isinstance(data["evals"], list) and data["evals"], "no evals defined"
    for e in data["evals"]:
        assert {"id", "name", "prompt", "register"} <= e.keys()


def test_skill_file_present():
    assert SKILL_PATH.exists(), f"missing {SKILL_PATH}"
    text = SKILL_PATH.read_text(encoding="utf-8")
    assert text.startswith("---"), "SKILL.md missing frontmatter"
    assert len(text) > 100, "SKILL.md suspiciously empty"


def test_skill_injection_differs_from_baseline(skill_text: str):
    sample = Eval(id=0, name="dummy", prompt="ทดสอบ", register="explainer")
    base = sample.prompt
    injected = skill_prompt(sample, skill_text)
    assert base != injected, "with_skill prompt identical to baseline"
    assert sample.prompt in injected, "task prompt missing from injected version"
    assert "skill" in injected.lower(), "skill content not actually injected"


def test_parse_claude_output():
    blob = json.dumps({
        "type": "result", "result": "Hello world.",
        "usage": {"input_tokens": 10, "cache_read_input_tokens": 1000,
                  "cache_creation_input_tokens": 0, "output_tokens": 4},
    })
    out = CLAUDE.parse(blob)
    assert out.text == "Hello world."
    assert out.usage["cache_read_input_tokens"] == 1000


def test_bundle_unscoped_includes_all_registers():
    bundle = kien_thai_bundle()
    for reg_name in ("Register 1", "Register 2", "Register 3", "Register 4", "Register 5"):
        assert reg_name in bundle, f"unscoped bundle missing {reg_name}"


def test_bundle_register_scoped_filters_correctly():
    explainer = kien_thai_bundle(register="explainer")
    marketing = kien_thai_bundle(register="marketing-saas-sme")
    # Check section headings, not arbitrary substrings — scope notes in
    # craft.md and the "Quick register decision" table reference other
    # registers by name; those are not register definitions.
    assert "## Register 1 — Explainer" in explainer
    assert "## Register 2 —" not in explainer, "explainer leaked Marketing section"
    assert "## Register 3 —" not in explainer, "explainer leaked Personal blog section"
    assert "## Register 4 —" not in explainer, "explainer leaked News section"
    assert "## Register 5 —" not in explainer, "explainer leaked Academic section"
    assert "## Register 2 —" in marketing
    assert "### 2.1 Marketing/SaaS-SME" in marketing
    assert "### 2.2 Marketing/B2B-formal" not in marketing, "saas-sme leaked B2B sub-register"


def test_bundle_examples_register_scoped():
    explainer = kien_thai_bundle(register="explainer")
    marketing = kien_thai_bundle(register="marketing-saas-sme")
    assert "Tech doc paragraph" in explainer
    assert "Marketing landing page" not in explainer
    assert "Marketing landing page" in marketing
    assert "Tech doc paragraph" not in marketing


def test_bundle_exemplars_last_and_scoped():
    # exemplars.md is the few-shot prefix slot — must land last in the bundle
    # so it sits closest to the task prompt. Register-scoped like examples.md.
    explainer = kien_thai_bundle(register="explainer")
    marketing = kien_thai_bundle(register="marketing-saas-sme")
    assert "## reference: exemplars.md" in explainer
    # exemplars must come after every other reference section.
    for other in ("ai-tells.md", "craft.md", "examples.md",
                  "forbidden-phrases.md", "grammar.md", "register.md",
                  "style-rules.md"):
        assert explainer.index("## reference: exemplars.md") > explainer.index(
            f"## reference: {other}"
        ), f"exemplars.md must come after {other}"
    # Register scoping: only the matching exemplar survives.
    assert "Explainer — educational advisory" in explainer
    assert "Marketing/SaaS-SME — feature-tile" not in explainer
    assert "Marketing/SaaS-SME — feature-tile" in marketing
    assert "Explainer — educational advisory" not in marketing


def test_bundle_audit_mode_drops_workflow():
    draft = kien_thai_bundle(register="explainer", mode=BundleMode.DRAFT)
    audit = kien_thai_bundle(register="explainer", mode=BundleMode.AUDIT)
    assert "Workflow when asked" in draft
    assert "Workflow when asked" not in audit
    assert "When asked to translate" in draft
    assert "When asked to translate" not in audit


def test_bundle_strips_frontmatter():
    bundle = kien_thai_bundle()
    assert not bundle.startswith("---"), "frontmatter not stripped"


def test_bundle_strips_default_metadata():
    bundle = kien_thai_bundle()
    # Default `· mechanical · all-registers · hard` should be gone.
    assert "· mechanical · all-registers · hard" not in bundle
    # But the slug line itself should still be present (with at most non-default meta).
    assert "`chueung-stacking`" in bundle


def test_parse_codex_output():
    lines = [
        '{"type":"thread.started","thread_id":"x"}',
        '{"type":"turn.started"}',
        '{"type":"item.completed","item":{"id":"i0","type":"agent_message","text":"Hi."}}',
        '{"type":"turn.completed","usage":{"input_tokens":2000,"cached_input_tokens":1500,"output_tokens":3}}',
    ]
    out = CODEX.parse("\n".join(lines))
    assert out.text == "Hi."
    assert out.usage["cached_input_tokens"] == 1500
