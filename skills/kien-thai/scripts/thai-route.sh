#!/usr/bin/env bash
# Route a Thai-prose request to the best available drafter, then hand off to audit.
#
# The decision "is a Thai-native model reachable? draft with it : draft with
# kien-thai" is encoded here so it runs deterministically instead of relying on
# an agent to follow prose. The audit step (kode-thai) stays agent-driven — it
# is LLM judgment over the kien-thai frames, not a scriptable transform.
#
# Usage:   thai-route.sh <register> "<prompt>"
#   register  corpus category for few-shot conditioning (marketing, tech-writing,
#             bank-longform, newspaper-feature, translation, scholarly) — or "-"
#             for none.
#
# Exit:  0  native draft on stdout; audit it next with kode-thai
#        3  no native model — draft with kien-thai directly (the skill stands alone)
set -euo pipefail

here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
draft="$here/thai-native-draft.py"

register="${1:-}"
prompt="${2:-}"
if [[ -z "$prompt" ]]; then
  echo "usage: thai-route.sh <register|-> \"<prompt>\"" >&2
  exit 2
fi

reg_args=()
[[ "$register" != "-" && -n "$register" ]] && reg_args=(--register "$register")

if ! python3 "$draft" --check >/dev/null 2>&1; then
  echo "thai-route: no Thai-native model — draft with kien-thai directly." >&2
  exit 3
fi

python3 "$draft" "${reg_args[@]+"${reg_args[@]}"}" "$prompt"
echo "thai-route: native draft above. Next: audit with kode-thai (loop kien-thai to convergence)." >&2
