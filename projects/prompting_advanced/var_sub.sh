#!/usr/bin/env bash

SITUATION="I am a student with \$500 saved."
QUESTION="Should I buy a used gaming laptop or invest the \$500?"
CONSTRAINTS="Consider: immediate utility, long-term value, opportunity cost, liquidity, age-appropriate risk."
OUTPUT="Prioritized ordered list of choice. Each explained in 3 lines or less with: price, reasons, description."

PROMPT="Context:
$SITUATION

Task:
$QUESTION

Reasoning:
Think step by step. List each assumption and inference explicitly.

Constraints:
$CONSTRAINTS

Output:
Numbered reasoning steps → Final answer
$OUTPUT
"

claude -p "$PROMPT"
