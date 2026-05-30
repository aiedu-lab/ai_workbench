#!/usr/bin/env bash
# piper.sh — Piper orchestrator: book file/URL → HTML mindmap.
#
# This script IS the pipeline orchestrator described in:
#   agents/piper-pipeline-orchestrator.md
# It implements the coordination doctrine defined there:
# task scope locking, agent sequencing, retry policy, and
# independent final verification via Sentinel.
#
# Waterfall progress display (printed at each phase transition):
#
# Phase                                           Function                Artifact
# ─────                                           ────────                ────────
# [✓] sanitizer                                  arg parser              n/a
# └─ [✓] setup                                   tool checker            n/a
#      └─ [✓] converter                          note taker              .tmp/<book>-detailed-notes.md
#           └─ [✓] Seth                          synthesizer             .tmp/<book>-mindmap-content.json
#                └─ [⟳] validator                loop until success
#                     |  Leo · Quinn · Sentinel  (attempt 2 of 3)
#                     └─ [⟳] Leo                 map creator             .tmp/<book>-mindmap.html
#                          └─ [ ] Quinn           QA reviewer             qa
#                               └─ [ ] Sentinel   final gate              qa
#
# Usage: ./piper.sh [OPTIONS] <input> [output.html]
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
AGENT_DIR="$SCRIPT_DIR/agents"

# ── Waterfall activity display ───────────────────────────────────
# 5 main-phase states (0=sanitizer 1=setup 2=converter 3=seth 4=validator)
# 3 validator sub-step states (0=leo 1=quinn 2=sentinel)
# States: pending | active | done | skip
_PH_ST=(pending pending pending pending pending)
_VL_ST=(pending pending pending)
_VL_ATTEMPT=0   # current attempt number
_VL_MAX=0       # max retries set before entering the loop

# Tree-prefix per display level (5-char indentation step):
#   L0=sanitizer  L1=setup    L2=converter  L3=Seth
#   L4=validator  L5=Leo      L6=Quinn      L7=Sentinel
_PFX=(
  ""
  "└─ "
  "     └─ "
  "          └─ "
  "               └─ "
  "                    └─ "
  "                         └─ "
  "                              └─ "
)
# Connector printed between validator and Leo rows
# (aligned with Leo's └─ prefix, uses | instead of └─)
_VL_CONN="                    |  "

_mark() {   # emit status symbol for a given state
  case "$1" in
    done)   printf "[✓]" ;;
    active) printf "[⟳]" ;;
    skip)   printf "[~]" ;;
    *)      printf "[ ]" ;;
  esac
}

# Build the left (phase-tree) column string for a row.
# Args: level  state  display-name
_ptree() {
  printf "%s%s %s" "${_PFX[$1]}" "$(_mark "$2")" "$3"
}

# Print the full 3-column waterfall to stdout.
# Columns: Phase (45) · Function (22) · Artifact
_waterfall() {
  local B="${BOOK_NAME:-<book>}"
  printf "\n"
  printf "%-45s  %-22s  %s\n" "Phase" "Function" "Artifact"
  printf "%-45s  %-22s  %s\n" \
    "─────────────────────────────────────────────" \
    "──────────────────────" \
    "──────────────────────────────────"

  printf "%-45s  %-22s  %s\n" \
    "$(_ptree 0 "${_PH_ST[0]}" "sanitizer")" \
    "arg parser" "n/a"
  printf "%-45s  %-22s  %s\n" \
    "$(_ptree 1 "${_PH_ST[1]}" "setup")" \
    "tool checker" "n/a"
  printf "%-45s  %-22s  %s\n" \
    "$(_ptree 2 "${_PH_ST[2]}" "converter")" \
    "note taker" ".tmp/$B-detailed-notes.md"
  printf "%-45s  %-22s  %s\n" \
    "$(_ptree 3 "${_PH_ST[3]}" "Seth")" \
    "synthesizer" ".tmp/$B-mindmap-content.json"

  # validator row (no artifact)
  printf "%-45s  %-22s\n" \
    "$(_ptree 4 "${_PH_ST[4]}" "validator")" \
    "loop until success"

  # connector: shows what is looping and current attempt
  local conn_sfx=""
  [[ $_VL_ATTEMPT -gt 0 ]] && \
    conn_sfx="  (attempt $_VL_ATTEMPT of $_VL_MAX)"
  printf "%sLeo · Quinn · Sentinel%s\n" "$_VL_CONN" "$conn_sfx"

  printf "%-45s  %-22s  %s\n" \
    "$(_ptree 5 "${_VL_ST[0]}" "Leo")" \
    "map creator" ".tmp/$B-mindmap.html"
  printf "%-45s  %-22s  %s\n" \
    "$(_ptree 6 "${_VL_ST[1]}" "Quinn")" \
    "QA reviewer" "qa"
  printf "%-45s  %-22s  %s\n" \
    "$(_ptree 7 "${_VL_ST[2]}" "Sentinel")" \
    "final gate" "qa"
  printf "\n"
}

# ── Spinner ──────────────────────────────────────────────────────
# Animates on stderr during every active agent call so the user
# sees live progress. Stderr keeps spinner separate from waterfall.
_SPIN_CHARS='/-\|'
_SPIN_PID=""

_spin_start() {
  local label="$1"
  (
    local i=0
    while true; do
      local c="${_SPIN_CHARS:$((i % 4)):1}"
      printf "  [%s] %s\r" "$c" "$label" >&2
      sleep 0.15
      i=$(( i + 1 ))   # avoid (( i++ )) exit-code 1 when i=0
    done
  ) &
  _SPIN_PID=$!
}

_spin_stop() {
  if [[ -n "${_SPIN_PID:-}" ]]; then
    kill "$_SPIN_PID" 2>/dev/null || true
    wait "$_SPIN_PID" 2>/dev/null || true
    _SPIN_PID=""
    printf "%-70s\r" "" >&2
  fi
}

trap '_spin_stop' EXIT

# ── Phase: Argument Sanitizer ────────────────────────────────────

_PH_ST[0]="active"

FROM_PHASE=""
INPUT=""
OUTPUT="./mindmap.html"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --help)
      cat <<'HELP'
Usage: piper.sh [OPTIONS] --input <book> [--output <mindmap.html>]

Convert a book file or URL to a self-contained HTML mindmap.

OPTIONS
  --help                Show this help and exit.
  --input  <path|url>   Book file or URL (required).
                        Supported: pdf html htm txt md
  --output <path>       Output HTML path (default: ./mindmap.html).
  --from-phase <name>   Skip phases before <name>; verifies that
                        prior-phase artifacts exist first.

PHASES (run in order)
  sanitizer      Parse args, validate input, resolve paths.
  setup          Verify CLI tools (pdftotext, html2text).
  converter      Convert input → <book>-detailed-notes.md.
  seth           Seth agent → <book>-mindmap-content.json.
  validator-loop Leo+Quinn+Sentinel → <book>-mindmap.html.
                 Retries Leo when Quinn or Sentinel rejects.

Intermediate files are written to <output-dir>/.tmp/ with the
book filename as prefix (e.g. TheComingWave-detailed-notes.md).

EXAMPLES
  # Full run from scratch
  ./piper.sh \
    --input  example/TheComingWave.pdf \
    --output example/TheComingWave_mindmap.html

  # Resume from validator-loop (Seth already wrote JSON)
  ./piper.sh \
    --from-phase validator-loop \
    --input  example/TheComingWave.pdf \
    --output example/TheComingWave_mindmap.html
HELP
      exit 0
      ;;
    --input)
      [[ $# -ge 2 ]] || {
        echo "Error: --input requires an argument" >&2; exit 1
      }
      INPUT="$2"; shift 2 ;;
    --output)
      [[ $# -ge 2 ]] || {
        echo "Error: --output requires an argument" >&2; exit 1
      }
      OUTPUT="$2"; shift 2 ;;
    --from-phase)
      [[ $# -ge 2 ]] || {
        echo "Error: --from-phase requires an argument" >&2
        exit 1
      }
      FROM_PHASE="$2"; shift 2 ;;
    *)
      echo "Error: unknown argument '$1'" >&2
      echo "Run: $0 --help" >&2
      exit 1 ;;
  esac
done

if [[ -z "$INPUT" ]]; then
  echo "Error: input file or URL is required." >&2
  echo "Run: $0 --help" >&2; exit 1
fi

# Map phase name → numeric index for skip comparisons.
case "${FROM_PHASE:-sanitizer}" in
  sanitizer)      FROM_IDX=0 ;;
  setup)          FROM_IDX=1 ;;
  converter)      FROM_IDX=2 ;;
  seth)           FROM_IDX=3 ;;
  validator-loop) FROM_IDX=4 ;;
  leo)            FROM_IDX=4 ;;   # alias for validator-loop
  *)
    echo "Error: unknown phase '$FROM_PHASE'." >&2
    echo "  Valid: sanitizer setup converter seth validator-loop" >&2
    exit 1 ;;
esac

# Detect + validate extension.
EXT="${INPUT##*.}"
EXT="${EXT,,}"
case "$EXT" in
  pdf|html|htm|txt|md) ;;
  *)
    echo "Error: unsupported extension '.$EXT'." >&2
    echo "  Supported: pdf html htm txt md" >&2
    exit 1 ;;
esac

# Validate input existence / URL reachability.
if [[ "$INPUT" =~ ^https?:// ]]; then
  curl -fsS --head "$INPUT" > /dev/null 2>&1 || {
    echo "Error: URL not reachable: $INPUT" >&2; exit 1
  }
else
  [[ -f "$INPUT" ]] || {
    echo "Error: file not found: $INPUT" >&2; exit 1
  }
  INPUT="$(realpath "$INPUT")"
fi

# Derive book name (basename without extension) for file prefix.
BOOK_NAME="$(basename "$INPUT")"
BOOK_NAME="${BOOK_NAME%.*}"

# Resolve output to an absolute path.
OUTPUT="$(mkdir -p "$(dirname "$OUTPUT")" && \
  realpath "$(dirname "$OUTPUT")")/$(basename "$OUTPUT")"
OUTPUT_DIR="$(dirname "$OUTPUT")"
WORK_DIR="$OUTPUT_DIR/.tmp"

# Intermediate file paths (book-name prefixed, inside .tmp/).
NOTES_FILE="$WORK_DIR/$BOOK_NAME-detailed-notes.md"
CONTENT_JSON="$WORK_DIR/$BOOK_NAME-mindmap-content.json"
HTML_FILE="$WORK_DIR/$BOOK_NAME-mindmap.html"

# Mark sanitizer done; pre-mark phases before FROM_IDX as skip.
_PH_ST[0]="done"
_idx=1
while [[ $_idx -lt $FROM_IDX ]]; do
  _PH_ST[$_idx]="skip"
  _idx=$(( _idx + 1 ))
done
_waterfall

# ── Phase: Utility Setup ─────────────────────────────────────────

if [[ $FROM_IDX -le 1 ]]; then
  _PH_ST[1]="active"
  _waterfall
  _spin_start "Checking required CLI tools..."
  case "$EXT" in
    pdf)
      command -v pdftotext &>/dev/null || {
        _spin_stop
        echo "Error: pdftotext not found." >&2
        echo "  Install: sudo apt install poppler-utils" >&2
        exit 1
      } ;;
    html|htm)
      command -v html2text &>/dev/null || {
        _spin_stop
        echo "Error: html2text not found." >&2
        echo "  Install: sudo apt install html2text" >&2
        exit 1
      } ;;
  esac
  mkdir -p "$WORK_DIR"
  _spin_stop
  _PH_ST[1]="done"
else
  mkdir -p "$WORK_DIR"
fi

# ── Phase: File Converter ────────────────────────────────────────

if [[ $FROM_IDX -le 2 ]]; then
  _PH_ST[2]="active"
  _waterfall
  _spin_start "Converting $(basename "$INPUT") to plain text..."
  case "$EXT" in
    pdf)   pdftotext "$INPUT" "$NOTES_FILE" ;;
    html|htm)
      if [[ "$INPUT" =~ ^https?:// ]]; then
        curl -fsSL "$INPUT" | html2text > "$NOTES_FILE"
      else
        html2text "$INPUT" > "$NOTES_FILE"
      fi ;;
    txt|md) cp "$INPUT" "$NOTES_FILE" ;;
  esac
  _spin_stop
  _PH_ST[2]="done"
else
  [[ -f "$NOTES_FILE" ]] || {
    echo "Error: $NOTES_FILE not found for resume." >&2
    exit 1
  }
fi

# cd so Claude file tools stay within the allowed directory.
cd "$WORK_DIR"

# ── Phase: Seth Synthesizer ──────────────────────────────────────
# Seth's stdout is captured so the spinner can animate freely.
# The JSON artifact is written by Seth's Write tool to CONTENT_JSON.

if [[ $FROM_IDX -le 3 ]]; then
  _PH_ST[3]="active"
  _waterfall
  _spin_start "Seth · synthesising concepts → mindmap JSON..."
  # shellcheck disable=SC2034
  _seth="$(claude --print \
    "Synthesize $NOTES_FILE into $CONTENT_JSON" \
    --permission-mode bypassPermissions \
    --system-prompt-file \
    "$AGENT_DIR/seth-content-synthesizer.md")" || {
    _spin_stop
    echo "Error: Seth failed — aborting." >&2; exit 1
  }
  _spin_stop
  [[ -f "$CONTENT_JSON" ]] || {
    echo "Error: Seth did not produce $CONTENT_JSON." >&2
    exit 1
  }
  _PH_ST[3]="done"
else
  [[ -f "$CONTENT_JSON" ]] || {
    echo "Error: $CONTENT_JSON not found for resume." >&2
    echo "  Re-run without --from-phase to regenerate." >&2
    exit 1
  }
fi

# ── Phase: Validator Loop (Leo → Quinn → Sentinel) ───────────────
# Leo renders; Quinn then Sentinel review independently.
# On rejection by either, Leo re-renders (up to VL_MAX retries).

_PH_ST[4]="active"
_VL_MAX=3
attempt=0

while true; do
  attempt=$(( attempt + 1 ))
  _VL_ATTEMPT=$attempt
  _VL_ST=(active pending pending)
  _waterfall

  _spin_start "Leo · rendering vis-network mindmap HTML..."
  # shellcheck disable=SC2034
  _leo="$(claude --print \
    "Render $CONTENT_JSON into $HTML_FILE" \
    --permission-mode bypassPermissions \
    --system-prompt-file \
    "$AGENT_DIR/leo-layout-engineer.md")" || {
    _spin_stop
    echo "Error: Leo failed — aborting." >&2; exit 1
  }
  _spin_stop

  _VL_ST=(done active pending)
  _waterfall

  _spin_start "Quinn · reviewing layout, hierarchy, content..."
  _quinn="$(claude --print \
    "Review $HTML_FILE for quality issues." \
    --permission-mode bypassPermissions \
    --system-prompt-file \
    "$AGENT_DIR/quinn-qa-reviewer.md")" || {
    _spin_stop
    echo "Error: Quinn failed — aborting." >&2; exit 1
  }
  _spin_stop

  if echo "$_quinn" | grep -q "NOT APPROVED"; then
    _VL_ST=(done skip skip)
    if [[ $attempt -ge $_VL_MAX ]]; then
      _PH_ST[4]="active"; _waterfall
      echo "Error: Quinn NOT APPROVED — max retries reached." >&2
      echo "$_quinn" >&2; exit 1
    fi
    _waterfall
    continue
  fi

  _VL_ST=(done done active)
  _waterfall

  _spin_start "Sentinel · final guard: spacing, completeness..."
  _sentinel="$(claude --print \
    "Final verification of $HTML_FILE. Quinn approved. \
Independently verify — overrule if you see any failure." \
    --permission-mode bypassPermissions \
    --system-prompt-file \
    "$AGENT_DIR/sentinel-final-guardian.md")" || {
    _spin_stop
    echo "Error: Sentinel failed — aborting." >&2; exit 1
  }
  _spin_stop

  if echo "$_sentinel" | grep -q "NOT APPROVED"; then
    _VL_ST=(done done skip)
    if [[ $attempt -ge $_VL_MAX ]]; then
      _PH_ST[4]="active"; _waterfall
      echo "Error: Sentinel NOT APPROVED — max retries." >&2
      echo "$_sentinel" >&2; exit 1
    fi
    _waterfall
    continue
  fi

  _VL_ST=(done done done)
  _PH_ST[4]="done"
  _waterfall
  break
done

# ── Copy final HTML to requested output path ─────────────────────

cp "$HTML_FILE" "$OUTPUT"
printf "[done] Mindmap saved: %s\n" "$OUTPUT"
