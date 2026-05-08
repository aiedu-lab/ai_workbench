# SDW Plan Step Skill

Generate or validate a single `sdw/plan.md` step that strictly
conforms to the CLAUDE.md §Plan Update Protocol five-field template.

## Invocation

```
/plan-step [draft description]
```

- **No argument:** enter interactive mode — the skill prompts for
  each field in turn.
- **With argument** (e.g. `/plan-step add pristine/ to README`):
  use `$ARGUMENTS` as the step intent and derive all five fields,
  then present the formatted block for review.

This skill is also applied internally by `/replan` when generating
each step — you do not need to invoke it separately during a replan
cycle.

## Template

Every step must contain all five fields. Missing or vague fields
are rejected.

```
### Step N.K: <step name>

[ ] Status

CONTEXT: <one sentence describing what exists before this step>
ACTION: <exact files, functions, or APIs to change — no vague
        verbs like "implement" or "handle">
CONSTRAINTS: <what NOT to touch; explicit scope limits>
OUTPUT: <concrete artifacts — file names, content, interface
        signatures>
TEST: <exact shell command with expected output>
```

The `[ ] Status` line is flipped to `[x] Status` when the step
is executed, providing an at-a-glance execution tracker inside
`sdw/plan.md`.

## Self-Check (apply before accepting any step)

- [ ] CONTEXT is a single sentence.
- [ ] ACTION names specific files or functions — zero vague verbs.
- [ ] CONSTRAINTS explicitly lists what is out of scope.
- [ ] OUTPUT lists concrete file names or interface signatures.
- [ ] TEST is a runnable shell command with the expected result
      stated.

If any field fails the check, ask for clarification rather than
guessing. Do not append a step that fails the self-check.

## Output

Present the formatted step as a fenced markdown block ready to
copy-paste into `sdw/plan.md`. Do not append to any file unless
the user explicitly confirms.
