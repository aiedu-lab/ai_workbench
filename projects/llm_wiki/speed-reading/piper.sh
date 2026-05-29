#!/usr/bin/env bash
# piper.sh — multi-agent mindmap pipeline orchestrator.
# Usage: ./piper.sh <detailed_notes_file> [output.html]
#
# Runs Seth → Leo → Quinn in sequence.
# If Quinn outputs NOT APPROVED, retries Leo → Quinn up to 3 times.
set -euo pipefail

AGENT_DIR="$(dirname "$0")/agents"
SCRIPT_DIR="$(dirname "$0")"

# ── Argument parsing ────────────────────────────────────────────
if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <detailed_notes_file> [output.html]" >&2
  exit 1
fi

NOTES_FILE="$1"
OUTPUT="${2:-mindmap.html}"

if [[ ! -f "$NOTES_FILE" ]]; then
  echo "Error: notes file not found: $NOTES_FILE" >&2
  exit 1
fi

# ── Temp files ──────────────────────────────────────────────────
CONTENT_JSON="$(mktemp /tmp/mindmap_content_XXXXXX.json)"
QA_REPORT="$(mktemp /tmp/mindmap_qa_XXXXXX.md)"
trap 'rm -f "$CONTENT_JSON" "$QA_REPORT"' EXIT

# ── Step 1: Seth — synthesise notes → JSON ──────────────────────
echo "[piper] Step 1: Seth — synthesising content..."
claude --print \
  "Read the detailed notes below and synthesise them into a
mindmap content structure. Output valid JSON matching the
mindmap-content template.

$(cat "$NOTES_FILE")" \
  --system-prompt-file \
  "$AGENT_DIR/seth-content-synthesizer.md" \
  > "$CONTENT_JSON"

if [[ $? -ne 0 ]]; then
  echo "[piper] Seth failed — aborting pipeline." >&2
  exit 1
fi
echo "[piper] Seth complete."

# ── Steps 2+3: Leo → Quinn with retry ──────────────────────────
MAX_RETRIES=3
attempt=0

while true; do
  attempt=$(( attempt + 1 ))

  # Step 2: Leo — render JSON → HTML
  echo "[piper] Step 2 (attempt $attempt): Leo — rendering HTML..."
  claude --print \
    "Read the mindmap JSON below and render it as a
self-contained mindmap HTML file.

$(cat "$CONTENT_JSON")" \
    --system-prompt-file \
    "$AGENT_DIR/leo-layout-engineer.md" \
    > "$OUTPUT"

  if [[ $? -ne 0 ]]; then
    echo "[piper] Leo failed — aborting pipeline." >&2
    exit 1
  fi
  echo "[piper] Leo complete."

  # Step 3: Quinn — QA review of HTML
  echo "[piper] Step 3 (attempt $attempt): Quinn — reviewing..."
  quinn_output="$(claude --print \
    "Review the mindmap HTML below and report any issues.
Output NOT APPROVED if the mindmap fails quality checks.

$(cat "$OUTPUT")" \
    --system-prompt-file \
    "$AGENT_DIR/quinn-qa-reviewer.md")"

  if [[ $? -ne 0 ]]; then
    echo "[piper] Quinn failed — aborting pipeline." >&2
    exit 1
  fi

  if echo "$quinn_output" | grep -q "NOT APPROVED"; then
    echo "[piper] Quinn: NOT APPROVED (attempt $attempt)."
    if [[ $attempt -ge $MAX_RETRIES ]]; then
      echo "[piper] Max retries ($MAX_RETRIES) reached — aborting." >&2
      echo "$quinn_output" >&2
      exit 1
    fi
    echo "[piper] Retrying Leo + Quinn..."
    continue
  fi

  echo "[piper] Quinn: APPROVED."
  break
done

echo "[piper] Pipeline complete. Output: $OUTPUT"
