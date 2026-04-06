#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  review_code.sh --input INPUT_FILE [--output OUTPUT_FILE] [--model MODEL]

Options:
  --input     Input file to review (required)
  --output    Output markdown file (default: /tmp/review.md)
  --model     OpenAI model to use (default: gpt-4.1)
  -h, --help  Show this help
EOF
}

die() {
  echo "Error: $*" >&2
  exit 1
}

INPUT_FILE=""
OUTPUT_FILE="/tmp/review.md"
MODEL="gpt-4.1"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --input)
      [[ $# -ge 2 ]] || die "--input requires a value"
      [[ -n "${2:-}" && "${2:-}" != --* ]] || die "--input requires a value"
      INPUT_FILE="$2"
      shift 2
      ;;
    --output)
      [[ $# -ge 2 ]] || die "--output requires a value"
      [[ -n "${2:-}" && "${2:-}" != --* ]] || die "--output requires a value"
      OUTPUT_FILE="$2"
      shift 2
      ;;
    --model)
      [[ $# -ge 2 ]] || die "--model requires a value"
      [[ -n "${2:-}" && "${2:-}" != --* ]] || die "--model requires a value"
      MODEL="$2"
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

[[ -n "$INPUT_FILE" ]] || die "--input is required"
[[ -f "$INPUT_FILE" ]] || die "file not found: $INPUT_FILE"
[[ -r "$INPUT_FILE" ]] || die "file not readable: $INPUT_FILE"

OUTDIR="$(dirname -- "$OUTPUT_FILE")"
[[ -d "$OUTDIR" ]] || die "output directory not found: $OUTDIR"
[[ -w "$OUTDIR" ]] || die "output directory not writable: $OUTDIR"

tmp_output="$(mktemp)" || die "failed to create temporary output file"
tmp_prompt="$(mktemp)" || {
  rm -f "$tmp_output"
  die "failed to create temporary prompt file"
}
trap 'rm -f "$tmp_output" "$tmp_prompt"' EXIT

cat > "$tmp_prompt" <<EOF
Review the following code:

$(cat "$INPUT_FILE")

Rules:
- find bugs
- improve safety
- suggest improvements
- suggest better structure

Output:
Structured markdown review with sections:
- Issues
- Suggestions
- Improved Snippets
EOF

if ! openai responses.create -m "$MODEL" -i "$(cat "$tmp_prompt")" > "$tmp_output"; then
  die "openai review failed"
fi

mv -- "$tmp_output" "$OUTPUT_FILE"
trap - EXIT
echo "Review written to $OUTPUT_FILE"