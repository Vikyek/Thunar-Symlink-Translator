#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BIN_DIR="${HOME}/.local/bin"

echo "=== Installing Thunar-Symlink-Translator ==="

mkdir -p "${BIN_DIR}"
install -Dm755 "${SCRIPT_DIR}/cli.py" "${BIN_DIR}/thunar-symlink-translator"

echo "Installed thunar-symlink-translator to ${BIN_DIR}/thunar-symlink-translator"
echo "Configure Thunar Custom Action command: thunar-symlink-translator %F"
