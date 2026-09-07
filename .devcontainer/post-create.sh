#!/usr/bin/env bash
set -euo pipefail
pip install --upgrade uv
uv sync --all-extras
uv run pre-commit install
npm install -g @anthropic-ai/claude-code
echo "Environment ready. Run 'make help'."
