"""Generation-stage fixtures: baseline single-shot, with_skill = kode-thai loop."""

from __future__ import annotations

import json
import os
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path

import pytest

from lib import (
    Backend,
    BundleMode,
    Config,
    Eval,
    PassKind,
    audit_prompt,
    kien_thai_bundle,
    load_evals,
    next_iteration_dir,
    skill_prompt,
    wrap_markdown,
    wrap_skill,
)

MAX_LOOP = 5
TIMEOUT_S = 300


@pytest.fixture(scope="session")
def iteration_dir() -> Path:
    return next_iteration_dir()


def pytest_generate_tests(metafunc: pytest.Metafunc):
    if "eval_case" in metafunc.fixturenames:
        evals = load_evals()
        metafunc.parametrize("eval_case", evals, ids=[e.name for e in evals])
    if "config" in metafunc.fixturenames:
        metafunc.parametrize("config", list(Config), ids=[c.value for c in Config])


@dataclass(frozen=True)
class Invocation:
    text: str
    usage: dict
    returncode: int
    duration_s: float


def _invoke(backend: Backend, prompt: str) -> Invocation:
    """Run backend on prompt."""
    cmd = [*backend.argv, prompt]
    t0 = time.monotonic()
    proc = subprocess.run(
        cmd, capture_output=True, text=True, timeout=TIMEOUT_S, env={**os.environ}
    )
    dur = time.monotonic() - t0
    if proc.returncode != 0:
        return Invocation(proc.stdout, {}, proc.returncode, dur)
    out = backend.parse(proc.stdout)
    return Invocation(out.text, out.usage, proc.returncode, dur)


def _run_once(backend: Backend, prompt: str, out_dir: Path, label: str) -> Invocation:
    (out_dir / f"{label}-prompt.txt").write_text(prompt, encoding="utf-8")
    inv = _invoke(backend, prompt)
    assert inv.returncode == 0, f"{backend.name} {label} exited {inv.returncode}: {inv.text[:500]}"
    assert inv.text.strip(), f"{backend.name} {label} empty output"
    return inv


def _audit_prompt(prose: str, bundle: str, register: str) -> str:
    return audit_prompt(prose, bundle, register)


def _fix_prompt(prose: str, audit: str, bundle: str, register: str) -> str:
    # bundle is already register-scoped.
    return (
        wrap_skill(bundle)
        + f"prose นี้เป็น register `{register}`\n\n"
        "issue ที่ต้องแก้:\n\n" + audit + "\n\n"
        "prose ปัจจุบัน:\n\n<prose>\n" + prose + "\n</prose>\n\n"
        "งาน: แก้ prose ตาม issue ข้างบน output เฉพาะ prose ที่แก้แล้ว "
        "ห้ามใส่คำอธิบาย ห้ามใส่หัวเรื่อง"
    )


def _is_clean(audit: str) -> bool:
    txt = audit.strip()
    if not txt:
        return False
    return txt.splitlines()[0].strip().upper().startswith("CLEAN")


def _run_baseline(backend: Backend, eval_case: Eval, out_dir: Path) -> dict:
    inv = _run_once(backend, eval_case.prompt, out_dir, "input")
    (out_dir / "output.md").write_text(wrap_markdown(inv.text), encoding="utf-8")
    return {"duration_s": round(inv.duration_s, 2), "usage": inv.usage}


def _run_loop(backend: Backend, eval_case: Eval, out_dir: Path) -> dict:
    register = eval_case.register
    # Two register-scoped bundles: 'draft' for pass-0 (keeps workflow sections),
    # 'audit' for audit/fix passes (drops draft-time advice).
    draft_bundle = kien_thai_bundle(register=register, mode=BundleMode.DRAFT)
    audit_bundle = kien_thai_bundle(register=register, mode=BundleMode.AUDIT)

    initial_prompt = skill_prompt(eval_case, draft_bundle)
    initial = _run_once(backend, initial_prompt, out_dir, "pass-0")
    prose = initial.text
    (out_dir / "pass-0.md").write_text(wrap_markdown(prose), encoding="utf-8")
    passes: list[dict] = [{
        "pass": 0,
        "kind": PassKind.INITIAL,
        "duration_s": round(initial.duration_s, 2),
        "usage": initial.usage,
    }]

    converged = False
    last_pass = 0
    for i in range(1, MAX_LOOP + 1):
        audit = _run_once(
            backend, _audit_prompt(prose, audit_bundle, register), out_dir, f"pass-{i}-audit"
        )
        (out_dir / f"pass-{i}-audit.md").write_text(audit.text.strip() + "\n", encoding="utf-8")
        clean = _is_clean(audit.text)
        passes.append({
            "pass": i,
            "kind": PassKind.AUDIT,
            "duration_s": round(audit.duration_s, 2),
            "clean": clean,
            "usage": audit.usage,
        })
        last_pass = i
        if clean:
            converged = True
            break
        fix = _run_once(
            backend, _fix_prompt(prose, audit.text, audit_bundle, register), out_dir, f"pass-{i}-fix"
        )
        prose = fix.text
        (out_dir / f"pass-{i}.md").write_text(wrap_markdown(prose), encoding="utf-8")
        passes.append({
            "pass": i,
            "kind": PassKind.FIX,
            "duration_s": round(fix.duration_s, 2),
            "usage": fix.usage,
        })

    (out_dir / "output.md").write_text(wrap_markdown(prose), encoding="utf-8")
    return {"loop_passes": last_pass, "converged": converged, "passes": passes}


@pytest.fixture
def run_eval(iteration_dir: Path):
    def _run(backend: Backend, eval_case: Eval, config: Config) -> Path:
        if not backend.available:
            pytest.skip(f"{backend.name} not on PATH")
        out_dir = iteration_dir / eval_case.name / backend.name / config
        out_dir.mkdir(parents=True, exist_ok=True)
        if config == Config.BASELINE:
            extra = _run_baseline(backend, eval_case, out_dir)
        else:
            extra = _run_loop(backend, eval_case, out_dir)
        (out_dir / "meta.json").write_text(
            json.dumps(
                {
                    "backend": backend.name,
                    "config": config,
                    "eval_id": eval_case.id,
                    "eval_name": eval_case.name,
                    **extra,
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        return out_dir / "output.md"

    return _run
