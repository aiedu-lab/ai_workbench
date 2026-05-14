# SDW Replan Skill

Execute the full Specification Driven Workbench (SDW) replan
cycle — orient, generate, approve, execute, commit.

## Invocation

```
/replan [section-name]
```

- **No argument:** scan `sdw/prompt_history.md` for the last
  `## [ ]` heading and use that as the target section.
- **With argument** (e.g. `/replan Skillify`): target the
  section whose `##` heading contains `$ARGUMENTS`, regardless
  of its `[ ]` / `[x]` state.

## Steps

### 1. Orient

Before reading any file, call the `EnterPlanMode` tool so
that phase-step generation and approval happen in plan mode.

Read these files in order:

1. `CLAUDE.md` — operating protocol and step template.
2. `sdw/plan.md` — scan all `## Phase N` headings; the new
   phase is the highest N found + 1.
3. `sdw/prompt_history.md`:
   - **No argument:** find the last `## <Title>` heading whose
     immediately following line is `[ ] Status` 
     (the most recently added unprocessed section). Use that
     section as the target.
   - **With argument:** find the section whose heading contains
     `$ARGUMENTS`.
   Note the section title and its line range.

State before proceeding:
```
Target section : ## <title> (lines X–Y of prompt_history.md)
New phase      : Phase N+1
```

### 2. Generate Phase Steps

For each distinct deliverable in the target section, produce one
step using the format defined in `.claude/commands/plan-step.md`.
Apply the plan-step self-check to every step before writing it.

The **final step** of every phase must be a "Mark complete" step
that:
- Changes `[ ] Status` → `[x] Status` on the line after
  `## <title>` in `sdb/prompt_history.md`
- Appends the full Phase N+1 block to `sdw/plan.md`. Each
  step in the appended block must follow the plan-step
  template exactly — including the `[ ] Status` line after
  the step heading — using a condensed (one-paragraph) body
  per field rather than multi-line.
- Commits all changed files and tags
  `vN+1.K-<brief-summary>-step-completed`.

### 3. Present for Approval

Output the full Phase N+1 block as readable markdown.
Do **not** write any file yet.

End with:
```
Proposed Phase N+1 — awaiting approval.
Reply "Approve" to execute step by step.
```

### 4. Execute (after approval)

Execute one step per turn following CLAUDE.md §One Step at a Time:

1. Make only the changes described in the current step.
2. Run the VERIFY command; confirm it passes.
3. Commit per CLAUDE.md §Commit Protocol.
4. Wait for explicit approval before the next step.

After the final step, run the verification suite:
```bash
# Target section marked complete
grep -A1 "^## <title>" sdb/prompt_history.md | grep "^\[ \] Status"
# → 0 matches

# No remaining unprocessed sections before this one
grep -A1 "^## " sdb/prompt_history.md \
  | grep -B1 "^\[ \] Status" | grep "^## " | tail -1

# Tag pushed
git tag | grep "v<N+1>\."
```
