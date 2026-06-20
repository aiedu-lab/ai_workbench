# Advanced Prompting Exercise

Solution workspace for the Smart Rewrite Assistant (CoT-as-skill)
exercise.

## Exercise
* [Exercise](../../sessions/prompting_advanced.md)

## Artifacts
* `prompt.md` — the reusable prompt skill/template
* `template.txt` / `data.json` — template and runtime substitution data
* `var_sub.sh` / `run.py` — scripts that merge template and data
* `cot_prompt.py` — Chain-of-Thought prompt driver

## Operating Protocol
Ask the agent to read this directory's `plan.md` (if present) and
execute it per the repo root CLAUDE.md operating protocol (Plan
Update Protocol, one step per turn, commit after each step).

## Submit
Commit and push your solution to your feature branch
(`feature/from_$GITHUB_USERNAME`) after completing the exercise.
