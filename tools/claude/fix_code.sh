#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  fix_code.sh --output-file OUTPUT_FILE [--review-file REVIEW_MARKDOWN_FILE]

Options:
  --output-file   Output file to write fixed code (required)
  --review-file   Input review markdown file (default: /tmp/review.md)
  -h, --help      Show this help
EOF
}

die() {
  echo "Error: $*" >&2
  exit 1
}

REVIEW_MARKDOWN_FILE="/tmp/review.md"
OUTPUT_FILE=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --output-file)
      [[ $# -ge 2 ]] || die "--output-file requires a value"
      [[ -n "${2:-}" && "${2:-}" != --* ]] || die "--output-file requires a value"
      OUTPUT_FILE="$2"
      shift 2
      ;;
    --review-file)
      [[ $# -ge 2 ]] || die "--review-file requires a value"
      [[ -n "${2:-}" && "${2:-}" != --* ]] || die "--review-file requires a value"
      REVIEW_MARKDOWN_FILE="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    --)
      shift
      [[ $# -eq 0 ]] || die "Unexpected positional arguments: $*"
      break
      ;;
    *)
      die "Unknown option: $1"
      ;;
  esac
done

[[ -n "$OUTPUT_FILE" ]] || die "--output-file is required"
[[ -e "$REVIEW_MARKDOWN_FILE" ]] || die "file not found: $REVIEW_MARKDOWN_FILE"
[[ -r "$REVIEW_MARKDOWN_FILE" ]] || die "file not readable: $REVIEW_MARKDOWN_FILE"

OUTDIR="$(dirname -- "$OUTPUT_FILE")"
[[ -d "$OUTDIR" ]] || die "output directory not found: $OUTDIR"
[[ -w "$OUTDIR" ]] || die "output directory not writable: $OUTDIR"

tmp_output="$(mktemp)" || die "failed to create temp file"
trap 'rm -f "$tmp_output"' EXIT

if ! claude -p <<EOF > "$tmp_output"
Improve the code using the feedback below:

$(cat "$REVIEW_MARKDOWN_FILE")

Rules:
- Do not rewrite everything
- Only fix issues
- Keep it simple
EOF
then
  die "claude review failed"
fi

mv -- "$tmp_output" "$OUTPUT_FILE"
trap - EXIT
echo "Fixed code for '$REVIEW_MARKDOWN_FILE' written to '$OUTPUT_FILE'"