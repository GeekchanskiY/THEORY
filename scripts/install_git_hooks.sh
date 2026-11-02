#!/bin/sh
# Install repo git hooks without changing git config.
set -e
repo_root="$(cd "$(dirname "$0")/.." && pwd)"
mkdir -p "$repo_root/.git/hooks"
cp "$repo_root/.githooks/pre-commit" "$repo_root/.git/hooks/pre-commit"
chmod +x "$repo_root/.git/hooks/pre-commit"
echo "Installed $repo_root/.git/hooks/pre-commit"
