#!/usr/bin/env bash
# CI-only, lifecycle-free install. No global packages or developer profiles.
set -euo pipefail

case "$(uname -s):$(uname -m)" in
  Linux:x86_64) ;;
  *) echo "Pinned worker binary requires the declared Linux x64 runner." >&2; exit 2 ;;
esac

source_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
install_dir="$(mktemp -d "${RUNNER_TEMP:?RUNNER_TEMP must name the CI scratch root}/doc-health-worker.XXXXXX")"
cp -- "$source_dir/package.json" "$source_dir/package-lock.json" "$install_dir/"
npm ci --prefix "$install_dir" --ignore-scripts --no-audit --no-fund

binary_dir="$install_dir/node_modules/@anthropic-ai/claude-code-linux-x64"
binary="$binary_dir/claude"
test -f "$binary" && test -x "$binary" && test ! -L "$binary"
expected="$(node -e 'const fs = require("fs"); const p = JSON.parse(fs.readFileSync(process.argv[1], "utf8")); process.stdout.write(p.dependencies["@anthropic-ai/claude-code-linux-x64"]);' "$source_dir/package.json")"
mkdir -m 700 "$install_dir/version-home"
# Version acceptance has no inherited provider credentials or active profile.
actual="$(timeout 20 env -i PATH="$PATH" HOME="$install_dir/version-home" \
  CLAUDE_CONFIG_DIR="$install_dir/version-home" DISABLE_AUTOUPDATER=1 \
  CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1 "$binary" --version)"
case "$actual" in
  "$expected"|"$expected "*) ;;
  *) echo "Pinned worker binary version mismatch." >&2; exit 2 ;;
esac

if [ -n "${GITHUB_PATH:-}" ]; then
  printf '%s\n' "$binary_dir" >> "$GITHUB_PATH"
fi
printf 'Verified locked worker CLI: %s\n' "$actual"
printf 'Worker binary directory: %s\n' "$binary_dir"
