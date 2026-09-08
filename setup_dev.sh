#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
if ! command -v uv >/dev/null 2>&1; then
  echo "Install uv, then rerun: bash setup_dev.sh" >&2
  exit 1
fi
uv sync --locked --python 3.12
