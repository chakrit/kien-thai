"""Ask a Thai-native model to name scholarly works on the Thai language.

Not a pytest module — a one-off probe:

    nice -n 19 uv run python tests/probe_thai_authorities.py

Why. Rules in this repo need provenance, and the corpus covers *prose voice*, not
*language scholarship*. chakrit's proposal (2026-07-26): ask a Thai-trained model
which Thai-language scholarly works it knows, so rule provenance can lean on Thai
authorities instead of English style manuals — my own prior on "what a style guide
says" is the least trustworthy thing I produce here.

The safe form, and the only one used. **Name candidate authorities; never quote their
rulings.** A title is checkable — a wrong one is obviously wrong. A remembered ruling
from an 8B is fluent, confidently attributed, and possibly invented, which is the same
surface-plausible failure this repo exists to catch. Everything returned is a
*candidate* for verification, never provenance.

Scholarly, not school. School grammars teach prescriptive simplification, which is
plausibly part of the over-formal skew the skill fights; seeding provenance from them
would import the bias.

Asked in English on purpose: no Thai is authored by Claude anywhere in this repo.
Titles come back in Thai regardless.
"""

from __future__ import annotations

import json
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from lib import ROOT  # noqa: E402

API = "http://localhost:11434/api/generate"
MODEL = "scb10x/llama3.1-typhoon2-8b-instruct"
TIMEOUT_S = 300

PROMPT = """List scholarly and academic works about the THAI LANGUAGE itself \
— its grammar, syntax, usage, style, or linguistics.

Requirements:
- Scholarly/academic works only. EXCLUDE school textbooks (แบบเรียน) and \
exam-preparation books.
- Give the title in Thai, the author's name, and the approximate era or year.
- Include the publisher or institution if you know it.
- Only list works you are actually confident exist. It is much better to list \
five works you are sure about than twenty you are guessing at.
- For each one, add a short note on what aspect of Thai it covers.

Format each entry on its own line as:
TITLE | AUTHOR | YEAR/ERA | PUBLISHER | WHAT IT COVERS
"""


def ask(prompt: str) -> str:
    """POST to the ollama HTTP API with stream disabled.

    Never shell out to `ollama run` — the CLI leaks its streaming re-render into
    redirected output (duplicated fragments, chars dropped mid-UTF-8), which
    silently corrupts Thai. See docs/vendor/model-backends.md.
    """
    payload = json.dumps(
        {"model": MODEL, "prompt": prompt, "stream": False}
    ).encode("utf-8")
    req = urllib.request.Request(
        API, data=payload, headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=TIMEOUT_S) as resp:
        return json.loads(resp.read().decode("utf-8")).get("response", "")


def main() -> int:
    text = ask(PROMPT)
    out = ROOT / "workspace" / "probes" / "thai-authorities.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    header = (
        "<!-- Typhoon-2 8B output. UNVERIFIED CANDIDATES — every title needs\n"
        "     checking before it is cited as provenance anywhere. -->\n\n"
        "# Candidate Thai-language scholarly authorities\n\n"
    )
    out.write_text(header + text.strip() + "\n", encoding="utf-8")
    print(text.strip())
    print(f"\nwrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
