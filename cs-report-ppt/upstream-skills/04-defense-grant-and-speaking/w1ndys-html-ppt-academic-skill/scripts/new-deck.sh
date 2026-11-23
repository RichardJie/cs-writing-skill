#!/usr/bin/env bash
set -euo pipefail

NAME="${1:-my-defense}"
TEMPLATE="${2:-thesis-defense}"
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC_DIR="$ROOT_DIR/templates/full-decks/$TEMPLATE"
DEST_DIR="$ROOT_DIR/examples/$NAME"

if [ ! -d "$SRC_DIR" ]; then
  printf 'Template not found: %s\n' "$TEMPLATE" >&2
  exit 1
fi

if [ -e "$DEST_DIR" ]; then
  printf 'Destination already exists: examples/%s\n' "$NAME" >&2
  exit 1
fi

mkdir -p "$DEST_DIR"
cp -R "$SRC_DIR/"* "$DEST_DIR/"

python3 - "$DEST_DIR/index.html" <<'PY'
from pathlib import Path
import sys

path = Path(sys.argv[1])
text = path.read_text(encoding="utf-8")
text = text.replace("../../../assets/", "../../assets/")
path.write_text(text, encoding="utf-8")
PY

printf 'Created examples/%s from %s\n' "$NAME" "$TEMPLATE"
