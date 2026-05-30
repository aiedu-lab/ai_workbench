#!/usr/bin/env python3
"""piper.py — Piper orchestrator entry point.

Piper converts any book file or URL to a self-contained
HTML mindmap using a four-agent AI pipeline:

  Seth (synthesizer) → Leo (renderer) → Quinn (QA)
                                       → Sentinel (final gate)

This script IS the pipeline orchestrator described in:
  agents/piper-pipeline-orchestrator.md

It implements the coordination doctrine defined there:
task scope locking, agent sequencing, retry policy (up to 3),
and independent final verification via Sentinel.

Waterfall progress display (printed at each phase transition):

Phase                                          Function               Artifact
─────                                          ────────               ────────
[✓] sanitizer                                  arg parser             n/a
└─ [✓] setup                                   tool checker           n/a
     └─ [✓] converter                          note taker             .tmp/<book>-detailed-notes.md
          └─ [✓] Seth                          synthesizer            .tmp/<book>-mindmap-content.json
               └─ [⟳] validator               loop until success
                    |  Leo · Quinn · Sentinel  (attempt 2 of 3)
                    └─ [⟳] Leo                map creator            .tmp/<book>-mindmap.html
                         └─ [ ] Quinn          QA reviewer            qa
                              └─ [ ] Sentinel  final gate             qa

Module layout (src/):
  piper.py        — this file; CLI entry point + argument parsing
  orchestrator.py — Piper class; all five pipeline phases
  display.py      — PhaseDisplay class; 3-column waterfall renderer
  spinner.py      — Spinner class; animated stderr progress indicator

Usage: python3 src/piper.py [OPTIONS]
"""
import argparse
import sys

from orchestrator import Piper, _PHASE_MAP

_HELP_TEXT = """\
Usage: piper.py [OPTIONS]

Convert a book file or URL to a self-contained HTML mindmap.

OPTIONS
  --help                Show this help and exit.
  --input  <path|url>   Book file or URL (required).
                        Supported: pdf html htm txt md
  --output <path>       Output HTML path (default: ./mindmap.html).
  --from-phase <name>   Skip phases before <name>; verifies that
                        prior-phase artifacts exist first.
  --log-dir <dir>       Write per-agent stdout to <dir>/<agent>.log
                        in real time. Waterfall display is unaffected.
                        Use: tail -f <dir>/leo.log to track progress.

PHASES (run in order)
  sanitizer           Parse args, validate input, resolve paths.
  setup               Verify CLI tools (pdftotext, html2text).
  converter           Convert input → <book>-detailed-notes.md.
  seth                Seth agent → <book>-mindmap-content.json.
  validator-loop|leo  Start the full Leo+Quinn+Sentinel loop.
                      Both names are identical — use either.
                      Retries Leo when Quinn or Sentinel rejects.
  quinn               Resume from Quinn; skip Leo (HTML must exist).
  sentinel            Resume from Sentinel; skip Leo+Quinn.

Intermediate files are written to <output-dir>/.tmp/ with the
book filename as prefix (e.g. TheComingWave-detailed-notes.md).

EXAMPLES
  # Full run from scratch with agent logging
  python3 src/piper.py \\
    --input  examples/TheComingWave.pdf \\
    --output examples/TheComingWave-mindmap.html \\
    --log-dir examples

  # In a second terminal, monitor Leo's progress
  tail -f examples/leo.log

  # Resume from validator-loop (Seth already wrote JSON)
  python3 src/piper.py \\
    --from-phase validator-loop \\
    --input  examples/TheComingWave.pdf \\
    --output examples/TheComingWave-mindmap.html \\
    --log-dir examples

  # Resume from Quinn (Leo's HTML exists, ran out of tokens)
  python3 src/piper.py \\
    --from-phase quinn \\
    --input  examples/TheComingWave.pdf \\
    --output examples/TheComingWave-mindmap.html

  # Resume from Sentinel (Leo+Quinn already done)
  python3 src/piper.py \\
    --from-phase sentinel \\
    --input  examples/TheComingWave.pdf \\
    --output examples/TheComingWave-mindmap.html
"""


def main() -> int:
  """Parse arguments and run the Piper pipeline."""
  parser = argparse.ArgumentParser(
    prog="piper.py", add_help=False,
    description=(
      "Convert a book file or URL to a self-contained"
      " HTML mindmap."
    ),
  )
  parser.add_argument("--help", action="store_true")
  parser.add_argument("--input", metavar="<path|url>")
  parser.add_argument(
    "--output", metavar="<path>", default="./mindmap.html"
  )
  parser.add_argument(
    "--from-phase", metavar="<name>",
    default="sanitizer", dest="from_phase",
  )
  parser.add_argument(
    "--log-dir", metavar="<dir>",
    default=None, dest="log_dir",
    help="Directory for per-agent log files.",
  )
  args = parser.parse_args()

  if args.help:
    print(_HELP_TEXT, end="")
    return 0
  if not args.input:
    print(
      "Error: input file or URL is required.\n"
      "Run: piper.py --help",
      file=sys.stderr,
    )
    return 1
  if args.from_phase not in _PHASE_MAP:
    valid = " ".join(sorted(set(_PHASE_MAP)))
    print(
      f"Error: unknown phase '{args.from_phase}'.\n"
      f"  Valid: {valid}",
      file=sys.stderr,
    )
    return 1

  return Piper(
    args.input, args.output, args.from_phase,
    log_dir=args.log_dir,
  ).run()


if __name__ == "__main__":
  sys.exit(main())
