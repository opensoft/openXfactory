#!/usr/bin/env bash
# Enforce update policy at the execution boundary after worker env scrubbing.
set -euo pipefail
export DISABLE_UPDATES=1
export DISABLE_AUTOUPDATER=1
launcher_dir="$(cd -- "$(dirname -- "$0")" && pwd -P)"
exec "$launcher_dir/../node_modules/@anthropic-ai/claude-code-linux-x64/claude" "$@"
