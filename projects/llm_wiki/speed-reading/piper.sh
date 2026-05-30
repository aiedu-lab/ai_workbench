#!/usr/bin/env bash
# piper.sh — convert a book file/URL to an HTML mindmap.
#
# This script IS the pipeline orchestrator described in:
#   agents/piper-pipeline-orchestrator.md
# It implements the coordination doctrine defined there:
# task scope locking, agent sequencing, retry policy, and
# independent final verification via Sentinel.
#
# 5-phase pipeline: sanitizer → setup → converter → seth → leo
# Each phase echoes [phase-name] progress to stdout.
# Use --from-phase to resume after a partial run.
#
# Usage: ./piper.sh [OPTIONS] <input> [output.html]
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
AGENT_DIR="$SCRIPT_DIR/agents"

# ── Phase: Argument Sanitizer ────────────────────────────────────

FROM_PHASE=""
INPUT=""
OUTPUT="./mindmap.html"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --help)
      cat <<'HELP'
Usage: piper.sh [OPTIONS] <input> [output.html]

Convert a book file or URL to a self-contained HTML mindmap.

OPTIONS
  --help              Show this help and exit.
  --from-phase <name> Skip phases before <name>; checks that
                      required artifacts from prior phases
                      exist before proceeding.

PHASES (run in order)
  sanitizer   Parse args, validate input, resolve paths.
  setup       Verify CLI tools (pdftotext, html2text).
  converter   Convert input → <book>-detailed-notes.md.
  seth        Run Seth agent → <book>-mindmap-content.json.
  leo         Run Leo+Quinn agents → <book>-mindmap.html.

INPUTS  pdf  html  htm  txt  md  (file or https:// URL)

DEFAULT output: ./mindmap.html

Intermediate files are written to <output-dir>/.tmp/ with the
book filename as prefix (e.g. TheComingWave-detailed-notes.md).

EXAMPLES
  ./piper.sh TheComingWave.pdf
  ./piper.sh book.pdf out/mindmap.html
  ./piper.sh --from-phase leo book.pdf out/mindmap.html
HELP
      exit 0
      ;;
    --from-phase)
      [[ $# -ge 2 ]] || {
        echo "Error: --from-phase requires an argument" >&2
        exit 1
      }
      FROM_PHASE="$2"; shift 2 ;;
    -*)
      echo "Error: unknown option '$1'" >&2
      echo "Run: $0 --help" >&2
      exit 1 ;;
    *)
      if [[ -z "$INPUT" ]]; then INPUT="$1"
      elif [[ "$OUTPUT" == "./mindmap.html" ]]; then OUTPUT="$1"
      else
        echo "Error: unexpected argument '$1'" >&2
        exit 1
      fi
      shift ;;
  esac
done

if [[ -z "$INPUT" ]]; then
  echo "Error: input file or URL is required." >&2
  echo "Run: $0 --help" >&2
  exit 1
fi

# Map phase name → numeric index for skip comparisons
case "${FROM_PHASE:-sanitizer}" in
  sanitizer) FROM_IDX=0 ;;
  setup)     FROM_IDX=1 ;;
  converter) FROM_IDX=2 ;;
  seth)      FROM_IDX=3 ;;
  leo)       FROM_IDX=4 ;;
  *)
    echo "Error: unknown phase '$FROM_PHASE'." >&2
    echo "  Valid phases: sanitizer setup converter seth leo" >&2
    exit 1 ;;
esac

# Detect + validate extension
EXT="${INPUT##*.}"
EXT="${EXT,,}"
case "$EXT" in
  pdf|html|htm|txt|md) ;;
  *)
    echo "Error: unsupported extension '.$EXT'." >&2
    echo "  Supported: pdf html htm txt md" >&2
    exit 1 ;;
esac

# Validate input existence / URL reachability
if [[ "$INPUT" =~ ^https?:// ]]; then
  if ! curl -fsS --head "$INPUT" > /dev/null 2>&1; then
    echo "Error: URL not reachable: $INPUT" >&2
    exit 1
  fi
else
  [[ -f "$INPUT" ]] || {
    echo "Error: file not found: $INPUT" >&2
    exit 1
  }
  INPUT="$(realpath "$INPUT")"
fi

# Derive book name (basename without extension) for file prefix
BOOK_NAME="$(basename "$INPUT")"
BOOK_NAME="${BOOK_NAME%.*}"

# Resolve output to an absolute path
OUTPUT="$(mkdir -p "$(dirname "$OUTPUT")" && \
  realpath "$(dirname "$OUTPUT")")/$(basename "$OUTPUT")"
OUTPUT_DIR="$(dirname "$OUTPUT")"
WORK_DIR="$OUTPUT_DIR/.tmp"

# Intermediate file paths (book-name prefixed, inside .tmp/)
NOTES_FILE="$WORK_DIR/$BOOK_NAME-detailed-notes.md"
CONTENT_JSON="$WORK_DIR/$BOOK_NAME-mindmap-content.json"
HTML_FILE="$WORK_DIR/$BOOK_NAME-mindmap.html"

echo "[sanitizer] Input:  $INPUT"
echo "[sanitizer] Output: $OUTPUT"
[[ -n "$FROM_PHASE" ]] && \
  echo "[sanitizer] Resuming from phase: $FROM_PHASE"

# ── Phase: Utility Setup ─────────────────────────────────────────

if [[ $FROM_IDX -le 1 ]]; then
  echo "[setup] Checking required tools..."
  case "$EXT" in
    pdf)
      command -v pdftotext &>/dev/null || {
        echo "Error: pdftotext not found." >&2
        echo "  Install: sudo apt install poppler-utils" >&2
        exit 1
      } ;;
    html|htm)
      command -v html2text &>/dev/null || {
        echo "Error: html2text not found." >&2
        echo "  Install: sudo apt install html2text" >&2
        exit 1
      } ;;
  esac
  mkdir -p "$WORK_DIR"
  echo "[setup] Tools OK. Work dir: $WORK_DIR"
else
  echo "[setup] Skipping (resuming from '$FROM_PHASE')."
  mkdir -p "$WORK_DIR"
fi

# ── Phase: File Converter ────────────────────────────────────────

if [[ $FROM_IDX -le 2 ]]; then
  echo "[converter] Converting input to plain text..."
  case "$EXT" in
    pdf)
      pdftotext "$INPUT" "$NOTES_FILE" ;;
    html|htm)
      if [[ "$INPUT" =~ ^https?:// ]]; then
        curl -fsSL "$INPUT" | html2text > "$NOTES_FILE"
      else
        html2text "$INPUT" > "$NOTES_FILE"
      fi ;;
    txt|md)
      cp "$INPUT" "$NOTES_FILE" ;;
  esac
  echo "[converter] Notes: $NOTES_FILE"
else
  echo "[converter] Skipping (resuming from '$FROM_PHASE')."
  [[ -f "$NOTES_FILE" ]] || {
    echo "Error: $NOTES_FILE not found for resume." >&2
    exit 1
  }
fi

# cd so Claude file tools stay within the allowed directory
cd "$WORK_DIR"

# ── Phase: Seth Synthesizer ──────────────────────────────────────

if [[ $FROM_IDX -le 3 ]]; then
  echo "[seth] Synthesising content into JSON..."
  claude --print \
    "Synthesize $NOTES_FILE into $CONTENT_JSON" \
    --system-prompt-file \
    "$AGENT_DIR/seth-content-synthesizer.md"
  [[ $? -eq 0 ]] || {
    echo "[seth] Failed — aborting." >&2; exit 1
  }
  echo "[seth] Content JSON: $CONTENT_JSON"
else
  echo "[seth] Skipping (resuming from '$FROM_PHASE')."
  [[ -f "$CONTENT_JSON" ]] || {
    echo "Error: $CONTENT_JSON not found for resume." >&2
    echo "  Re-run without --from-phase leo to regenerate." >&2
    exit 1
  }
fi

# ── Phase: Leo Renderer + Quinn Validator + Sentinel Guard ──────

MAX_RETRIES=3
attempt=0

while true; do
  attempt=$(( attempt + 1 ))

  echo "[leo] Rendering HTML (attempt $attempt)..."
  claude --print \
    "Render $CONTENT_JSON into $HTML_FILE" \
    --system-prompt-file \
    "$AGENT_DIR/leo-layout-engineer.md"
  [[ $? -eq 0 ]] || {
    echo "[leo] Failed — aborting." >&2; exit 1
  }
  echo "[leo] HTML: $HTML_FILE"

  echo "[quinn] Reviewing HTML (attempt $attempt)..."
  quinn_out="$(claude --print \
    "Review $HTML_FILE for quality issues." \
    --system-prompt-file \
    "$AGENT_DIR/quinn-qa-reviewer.md")"
  [[ $? -eq 0 ]] || {
    echo "[quinn] Failed — aborting." >&2; exit 1
  }

  if echo "$quinn_out" | grep -q "NOT APPROVED"; then
    echo "[quinn] NOT APPROVED (attempt $attempt)."
    if [[ $attempt -ge $MAX_RETRIES ]]; then
      echo "[quinn] Max retries ($MAX_RETRIES) reached." >&2
      echo "$quinn_out" >&2
      exit 1
    fi
    echo "[quinn] Retrying Leo + Quinn + Sentinel..."
    continue
  fi
  echo "[quinn] APPROVED."

  # Sentinel independently verifies Quinn's approval —
  # overrules if it finds failures Quinn missed.
  echo "[sentinel] Final verification (attempt $attempt)..."
  sentinel_out="$(claude --print \
    "Final verification of $HTML_FILE. Quinn approved. \
Independently verify — overrule if you see any failure." \
    --system-prompt-file \
    "$AGENT_DIR/sentinel-final-guardian.md")"
  [[ $? -eq 0 ]] || {
    echo "[sentinel] Failed — aborting." >&2; exit 1
  }

  if echo "$sentinel_out" | grep -q "NOT APPROVED"; then
    echo "[sentinel] NOT APPROVED (attempt $attempt)."
    if [[ $attempt -ge $MAX_RETRIES ]]; then
      echo "[sentinel] Max retries ($MAX_RETRIES) reached." >&2
      echo "$sentinel_out" >&2
      exit 1
    fi
    echo "[sentinel] Overruling Quinn — retrying Leo..."
    continue
  fi

  echo "[sentinel] APPROVED."
  break
done

# ── Copy final HTML to requested output path ─────────────────────

cp "$HTML_FILE" "$OUTPUT"
echo "[done] Mindmap saved: $OUTPUT"
