#!/usr/bin/env python3
"""Typhoon arm of the model-route comparison pass.

Drafts each corpus-covered eval with the Thai-native model (Typhoon-8B via
ollama), few-shot conditioned from corpus/curated/. Writes outputs into a fresh
iteration tree alongside the Claude arm so compare_arms.py reads both uniformly.

This is NOT a kode-thai loop — a single native draft (the experiment is whether
a Thai-pretrained base, un-audited, rivals looped Claude on chakrit's ear). Evals
whose register has no corpus category (personal-blog) are skipped and reported.

Run: uv run python tests/generate/typhoon_pass.py
"""

from __future__ import annotations

import json
import subprocess
import sys
import time
from dataclasses import asdict, dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from lib import (  # noqa: E402
    EVAL_REGISTER_TO_CORPUS,
    ROOT,
    Eval,
    load_evals,
    mechanical_signals,
    next_iteration_dir,
    wrap_markdown,
)

DRAFTER = ROOT / "skills" / "kien-thai" / "scripts" / "thai-native-draft.py"
MODEL = "scb10x/llama3.1-typhoon2-8b-instruct"
TEMPERATURE = 0.8
EXEMPLARS = 3
TIMEOUT_S = 300


@dataclass(frozen=True)
class Draft:
    text: str
    stderr: str
    duration_s: float


def draft(prompt: str, corpus: str) -> Draft:
    cmd = [
        sys.executable, str(DRAFTER), prompt,
        "-r", corpus, "-n", str(EXEMPLARS),
        "-m", MODEL, "-t", str(TEMPERATURE),
    ]
    t0 = time.monotonic()
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=TIMEOUT_S)
    duration_s = time.monotonic() - t0
    if proc.returncode != 0:
        raise SystemExit(
            f"drafter exited {proc.returncode} for corpus={corpus}:\n{proc.stderr}"
        )
    return Draft(proc.stdout.strip(), proc.stderr.strip(), duration_s)


def write_draft(out_dir: Path, eval_case: Eval, corpus: str, result: Draft) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "input-prompt.txt").write_text(eval_case.prompt, encoding="utf-8")
    (out_dir / "output.md").write_text(wrap_markdown(result.text), encoding="utf-8")

    meta = {
        "backend": "typhoon",
        "config": "draft",
        "mode": "typhoon-draft",
        "eval_id": eval_case.id,
        "eval_name": eval_case.name,
        "register": eval_case.register,
        "corpus_category": corpus,
        "model": MODEL,
        "temperature": TEMPERATURE,
        "exemplars": EXEMPLARS,
        "duration_s": round(result.duration_s, 2),
        "drafter_stderr": result.stderr,
        "signals": asdict(mechanical_signals(result.text)),
    }
    (out_dir / "meta.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def main() -> None:
    iteration = next_iteration_dir()
    ran: list[str] = []
    skipped: list[str] = []

    for eval_case in load_evals():
        corpus = EVAL_REGISTER_TO_CORPUS.get(eval_case.register)
        if corpus is None:
            skipped.append(f"{eval_case.name} (register {eval_case.register!r} — no corpus)")
            continue
        print(f"drafting {eval_case.name} (register={eval_case.register} -> corpus={corpus}) ...")
        result = draft(eval_case.prompt, corpus)
        write_draft(iteration / eval_case.name / "typhoon" / "draft", eval_case, corpus, result)
        ran.append(eval_case.name)

    print(f"\niteration: {iteration}")
    print(f"drafted ({len(ran)}): {', '.join(ran)}")
    if skipped:
        print(f"skipped ({len(skipped)}): {'; '.join(skipped)}")


if __name__ == "__main__":
    main()
