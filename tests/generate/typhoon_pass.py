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
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from lib import (  # noqa: E402
    EVAL_REGISTER_TO_CORPUS,
    ROOT,
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


def draft(prompt: str, corpus: str) -> tuple[str, str, float]:
    """Return (text, stderr, duration_s) from one drafter invocation."""
    cmd = [
        sys.executable, str(DRAFTER), prompt,
        "-r", corpus, "-n", str(EXEMPLARS),
        "-m", MODEL, "-t", str(TEMPERATURE),
    ]
    t0 = time.monotonic()
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=TIMEOUT_S)
    dur = time.monotonic() - t0
    if proc.returncode != 0:
        raise SystemExit(
            f"drafter exited {proc.returncode} for corpus={corpus}:\n{proc.stderr}"
        )
    return proc.stdout.strip(), proc.stderr.strip(), dur


def main() -> None:
    iteration = next_iteration_dir()
    skipped: list[str] = []
    ran: list[str] = []
    for ev in load_evals():
        corpus = EVAL_REGISTER_TO_CORPUS.get(ev.register)
        if corpus is None:
            skipped.append(f"{ev.name} (register {ev.register!r} — no corpus)")
            continue
        print(f"drafting {ev.name} (register={ev.register} -> corpus={corpus}) ...")
        text, stderr, dur = draft(ev.prompt, corpus)
        out_dir = iteration / ev.name / "typhoon" / "draft"
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / "input-prompt.txt").write_text(ev.prompt, encoding="utf-8")
        (out_dir / "output.md").write_text(wrap_markdown(text), encoding="utf-8")
        (out_dir / "meta.json").write_text(
            json.dumps(
                {
                    "backend": "typhoon",
                    "config": "draft",
                    "mode": "typhoon-draft",
                    "eval_id": ev.id,
                    "eval_name": ev.name,
                    "register": ev.register,
                    "corpus_category": corpus,
                    "model": MODEL,
                    "temperature": TEMPERATURE,
                    "exemplars": EXEMPLARS,
                    "duration_s": round(dur, 2),
                    "drafter_stderr": stderr,
                    "signals": mechanical_signals(text),
                },
                ensure_ascii=False,
                indent=2,
            ),
            encoding="utf-8",
        )
        ran.append(ev.name)

    print(f"\niteration: {iteration}")
    print(f"drafted ({len(ran)}): {', '.join(ran)}")
    if skipped:
        print(f"skipped ({len(skipped)}): {'; '.join(skipped)}")


if __name__ == "__main__":
    main()
