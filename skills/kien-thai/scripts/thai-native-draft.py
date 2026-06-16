#!/usr/bin/env python3
"""Draft Thai prose with a Thai-native model (Typhoon-2 by default) via ollama.

Why this exists: the "machine-sounding Thai" the kien-thai skill fights is
largely an artifact of English-centric base models. A Thai-pretrained model
(Typhoon, SEA-LION, OpenThaiGPT) carries the native distribution in its
weights, so drafting with one and auditing with kien-thai beats drafting with
kien-thai alone. The frames do not go away — they become the audit layer
(kode-thai loop) over a native-drafted base. See README.md in this directory.

CAVEAT (load-bearing, from the 2026-06-09 probe): capture output via the HTTP
API with stream=false, NEVER `ollama run`. The CLI leaks its streaming
re-render into redirected output — duplicated line fragments and chars dropped
mid-UTF-8. This script uses the API for exactly that reason.

The script never fabricates Thai. Few-shot conditioning is pulled live from the
repo's vetted corpus/ (the canonical native-Thai source); the system prompt is
English meta-instruction only.

Exit codes:
  0  draft printed to stdout
  2  usage / argument error
  3  no Thai-native model reachable — caller should fall back to kien-thai
"""

import argparse
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

DEFAULT_MODEL = "scb10x/llama3.1-typhoon2-8b-instruct"
DEFAULT_HOST = "http://localhost:11434"

SYSTEM = (
    "You are a native Thai writer. Write Thai that reads like a real Thai "
    "author, not translated-from-English prose. Avoid over-formal and "
    "over-polite defaults, calqued sentence shapes, period-spam, and stock "
    "AI connectives. Match the voice of the reference passages when given. "
    "Output only the Thai prose — no preamble, no translation, no notes."
)


def repo_root() -> Path:
    # scripts/ -> kien-thai/ -> skills/ -> repo root
    return Path(__file__).resolve().parents[3]


def strip_frontmatter(text: str) -> str:
    """Return the body after a leading `---`-delimited YAML frontmatter block."""
    if not text.startswith("---"):
        return text.strip()
    parts = text.split("---", 2)
    return parts[2].strip() if len(parts) == 3 else text.strip()


def load_exemplars(register: str, limit: int) -> list[str]:
    """Pull up to `limit` vetted native snippets from corpus/curated/<register>/."""
    cat_dir = repo_root() / "corpus" / "curated" / register
    if not cat_dir.is_dir():
        avail = ", ".join(
            sorted(p.name for p in (repo_root() / "corpus" / "curated").iterdir())
            if (repo_root() / "corpus" / "curated").is_dir()
            else []
        )
        print(
            f"warning: no corpus category '{register}' "
            f"(available: {avail or 'none'}); drafting without few-shot exemplars",
            file=sys.stderr,
        )
        return []
    bodies = [strip_frontmatter(p.read_text(encoding="utf-8")) for p in sorted(cat_dir.glob("*.md"))]
    return [b for b in bodies if b][:limit]


def build_prompt(task: str, exemplars: list[str]) -> str:
    if not exemplars:
        return task
    refs = "\n\n".join(f"ตัวอย่างงานเขียนอ้างอิง:\n{e}" for e in exemplars)
    return f"{refs}\n\nเขียนตามแนวเสียงของตัวอย่างข้างบน\n\n{task}"


def call_ollama(host: str, model: str, prompt: str, temperature: float) -> str:
    body = json.dumps(
        {
            "model": model,
            "system": SYSTEM,
            "prompt": prompt,
            "stream": False,  # load-bearing — see module docstring
            "options": {"temperature": temperature},
        }
    ).encode("utf-8")
    req = urllib.request.Request(
        f"{host}/api/generate",
        data=body,
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            return json.loads(resp.read())["response"]
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", "replace")
        if e.code == 404:
            _exit3(f"model '{model}' not pulled on {host} — `ollama pull {model}`")
        sys.exit(f"ollama HTTP {e.code}: {detail}")
    except urllib.error.URLError as e:
        _exit3(f"no ollama at {host} ({e.reason}) — start it with `ollama serve`")


def _exit3(msg: str) -> None:
    print(f"thai-native-draft: {msg}", file=sys.stderr)
    raise SystemExit(3)


def check_model(host: str, model: str) -> None:
    """Report whether `model` is available; exit 0 if yes, 3 if not (caller branches)."""
    try:
        with urllib.request.urlopen(f"{host}/api/tags", timeout=10) as resp:
            names = [m["name"] for m in json.loads(resp.read()).get("models", [])]
    except urllib.error.URLError as e:
        _exit3(f"no ollama at {host} ({e.reason})")
    if any(n == model or n.split(":")[0] == model for n in names):
        print(f"available: {model} on {host}")
        raise SystemExit(0)
    _exit3(f"model '{model}' not pulled on {host} — `ollama pull {model}`")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("prompt", nargs="?", help="task prompt; omit to read from stdin")
    ap.add_argument("-r", "--register", help="corpus category for few-shot conditioning (e.g. marketing, tech-writing)")
    ap.add_argument("-n", "--exemplars", type=int, default=3, help="max few-shot exemplars (default 3)")
    ap.add_argument("-m", "--model", default=DEFAULT_MODEL, help=f"ollama model (default {DEFAULT_MODEL})")
    ap.add_argument("--host", default=DEFAULT_HOST, help=f"ollama host (default {DEFAULT_HOST})")
    ap.add_argument("-t", "--temperature", type=float, default=0.8)
    ap.add_argument("--check", action="store_true", help="report model availability and exit (0 yes, 3 no)")
    args = ap.parse_args()

    if args.check:
        check_model(args.host, args.model)

    task = args.prompt if args.prompt is not None else sys.stdin.read().strip()
    if not task:
        ap.error("empty prompt")

    exemplars = load_exemplars(args.register, args.exemplars) if args.register else []
    prompt = build_prompt(task, exemplars)
    print(call_ollama(args.host, args.model, prompt, args.temperature))


if __name__ == "__main__":
    main()
