#!/usr/bin/env bash
# build_mindmap.sh — convert a book file/URL to a mindmap HTML.
# Usage: ./build_mindmap.sh <book_url_or_file> [output.html]
#
# Creates a tmp/ working directory next to the output file,
# converts the input to plain text (detailed-notes.md), then
# runs piper.sh from that directory.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

# ── Argument parsing ────────────────────────────────────────────
if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <book_url_or_file> [output_file]" >&2
  exit 1
fi

INPUT="$1"
OUTPUT="${2:-./mindmap.html}"

# Resolve output to an absolute path so the copy at the end works
OUTPUT="$(mkdir -p "$(dirname "$OUTPUT")" && \
  realpath "$(dirname "$OUTPUT")")/$(basename "$OUTPUT")"

# ── Validation: extension ───────────────────────────────────────
EXT="${INPUT##*.}"
EXT="${EXT,,}"   # lowercase
case "$EXT" in
  pdf|html|htm|txt|md) ;;
  *)
    echo "Error: unsupported extension '.$EXT'." >&2
    echo "  Supported: pdf html htm txt md" >&2
    exit 1
    ;;
esac

# ── Validation: existence ───────────────────────────────────────
if [[ "$INPUT" =~ ^https?:// ]]; then
  if ! curl -fsS --head "$INPUT" > /dev/null 2>&1; then
    echo "Error: URL not reachable: $INPUT" >&2
    exit 1
  fi
else
  if [[ ! -f "$INPUT" ]]; then
    echo "Error: file not found: $INPUT" >&2
    exit 1
  fi
  INPUT="$(realpath "$INPUT")"
fi

# ── Create tmp working directory next to output ─────────────────
OUTPUT_DIR="$(dirname "$OUTPUT")"
WORK_DIR="$OUTPUT_DIR/.tmp"
mkdir -p "$WORK_DIR"

NOTES_FILE="$WORK_DIR/detailed-notes.md"

# ── Convert input to plain text ─────────────────────────────────
echo "[build] Converting input to plain text..."
case "$EXT" in
  pdf)
    if ! command -v pdftotext &> /dev/null; then
      echo "Error: pdftotext not found." >&2
      echo "  Install: sudo apt install poppler-utils" >&2
      exit 1
    fi
    pdftotext "$INPUT" "$NOTES_FILE"
    ;;
  html|htm)
    if ! command -v html2text &> /dev/null; then
      echo "Error: html2text not found." >&2
      echo "  Install: sudo apt install html2text" >&2
      exit 1
    fi
    if [[ "$INPUT" =~ ^https?:// ]]; then
      curl -fsSL "$INPUT" | html2text > "$NOTES_FILE"
    else
      html2text "$INPUT" > "$NOTES_FILE"
    fi
    ;;
  txt|md)
    cp "$INPUT" "$NOTES_FILE"
    ;;
esac
echo "[build] Notes written to $NOTES_FILE"

# ── Run the agent pipeline ──────────────────────────────────────
"$SCRIPT_DIR/piper.sh" "$WORK_DIR"

# ── Copy final HTML to requested output path ────────────────────
cp "$WORK_DIR/mindmap.html" "$OUTPUT"
echo "[build] Mindmap saved: $OUTPUT"
