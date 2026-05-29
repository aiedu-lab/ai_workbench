#!/usr/bin/env python3
"""
main.py — CLI entry point for Tower of Hanoi.

Usage examples:
    python3 src/main.py
    python3 src/main.py --number-discs 4
    python3 src/main.py --no-step-by-step --step-file ./solution.md
    python3 src/main.py --number-discs 5 --no-step-by-step
"""

import argparse
import sys
from orchestrator import Orchestrator


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Tower of Hanoi solver",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--number-discs",
        type=int,
        default=3,
        metavar="N",
        help="Number of discs (must be ≥ 1)",
    )
    parser.add_argument(
        "--step-by-step",
        default=True,
        action=argparse.BooleanOptionalAction,   # enables --no-step-by-step
        help="Pause and display each step interactively",
    )
    parser.add_argument(
        "--step-file",
        type=str,
        default="./steps_filename.md",
        metavar="PATH",
        help="Markdown file where all steps are written",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.number_discs < 1:
        raise SystemExit("Error: --number-discs must be a positive integer.")

    orchestrator = Orchestrator(
        num_discs=args.number_discs,
        step_by_step=args.step_by_step,
        step_file=args.step_file,
    )
    orchestrator.run()


if __name__ == "__main__":
    sys.exit(main())
