#!/usr/bin/env bash
# piper.sh — multi-agent mindmap pipeline orchestrator.
# Usage: ./piper.sh <work_dir>
#
# work_dir must contain detailed-notes.md.
# Agents cd to work_dir so Claude's file tools stay within
# the allowed working directory.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
AGENT_DIR="$SCRIPT_DIR/agents"

# ── Argument parsing ────────────────────────────────────────────
if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <work_dir>" >&2
  exit 1
fi

WORK_DIR="$(realpath "$1")"

if [[ ! -f "$WORK_DIR/detailed-notes.md" ]]; then
  echo "Error: $WORK_DIR/detailed-notes.md not found" >&2
  exit 1
fi

# cd so Claude file tools stay within the allowed directory
cd "$WORK_DIR"

# ── Step 1: Seth — synthesise notes → JSON ──────────────────────
echo "[piper] Step 1: Seth — synthesising content..."
claude --print \
  "Synthesize $WORK_DIR/detailed-notes.md \
into $WORK_DIR/mindmap-content.json" \
  --system-prompt-file "$AGENT_DIR/seth-content-synthesizer.md"

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
    "Render $WORK_DIR/mindmap-content.json \
into $WORK_DIR/mindmap.html" \
    --system-prompt-file "$AGENT_DIR/leo-layout-engineer.md"

  if [[ $? -ne 0 ]]; then
    echo "[piper] Leo failed — aborting pipeline." >&2
    exit 1
  fi
  echo "[piper] Leo complete."

  # Step 3: Quinn — QA review; output captured to detect NOT APPROVED
  echo "[piper] Step 3 (attempt $attempt): Quinn — reviewing..."
  quinn_output="$(claude --print \
    "Review $WORK_DIR/mindmap.html for quality issues." \
    --system-prompt-file "$AGENT_DIR/quinn-qa-reviewer.md")"

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

echo "[piper] Pipeline complete. Output: $WORK_DIR/mindmap.html"
