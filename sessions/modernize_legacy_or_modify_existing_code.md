# Code Migration 

Code migration involves steps to 
modernize legacy or modify existing code.

## The Core Principle: Explore → Plan → Code → Commit

**Never** ask Claude Code to modify existing code without 
first understanding it. 
The pattern that works:

```bash
# Step 1: Explore only — no edits yet
claude "
Read through index.html and explain what each section does.
Do NOT write any code yet.
"

# Step 2: Plan
claude "
Based on your analysis, propose a step-by-step plan to add
input validation. List each file change needed.
"

# Step 3: Execute one step at a time
claude -p "Execute only Step 1 of the plan." --allowedTools "Write" > /dev/null

# Step 4: Review diff and commit before next step
git diff
git add -p
git commit -m "step 1: add input validation skeleton"
```

---

## Legacy to Modern: Migration Workflow

Claude Code can modernize old codebases systematically. 
The proven approach is the **Strangler Fig Pattern** — 
replace pieces incrementally while keeping the system running:

```bash
# Phase 1: Understand what you have
claude "
Analyze this codebase. Document:
1. What each file does
2. All dependencies between files
3. Any hardcoded values that should be config
4. Any patterns that are outdated or unsafe
Do NOT change anything yet.
"

# Phase 2: Generate a migration plan
claude "
Based on the analysis, create a phased migration plan.
Phase 1: Add test harness around critical paths
Phase 2: Extract config from hardcoded values
Phase 3: Replace [legacy pattern] with [modern equivalent]
For each phase, list exact file-level changes and rollback steps.
"

# Phase 3: Execute phase by phase with validation
claude -p "
Execute Phase 1 only. 
Create test files that verify current behavior before any changes.
" --allowedTools "Write,Bash" > /dev/null

# Run tests to establish baseline
python3 -m pytest tests/

# Phase 4: Execute next phase, re-run tests, commit
```
---

## Hybrid Code: Manually Written + AI Generated

When a codebase is partially hand-written and partially AI-generated via
`CLAUDE.md` and `plan.md`, use these rules to keep it coherent:

1. Rule 1 — Mark sections clearly in comments:

```html
<!-- === MANUAL: core layout — do not regenerate === -->
<header>...</header>

<!-- === AI-GENERATED: history feature v2 — see plan_history.md === -->
<ul id="history">...</ul>
```

2. Rule 2 — Use CLAUDE.md to fence what Claude can and cannot touch: reference
[Claude.md](../projects/modernize_legacy_or_modify_existing_code/CLAUDE.md)

3. Rule 3 — One plan.md per feature, not one monolithic plan:

```
projects/web_site/hello_world_claudeCLI/
  plan.md                  ← original app
  plan_history.md          ← history feature
  plan_validation.md       ← input validation
  index.html
  CLAUDE.md
```

Each plan.md targets specific sections. Claude reads CLAUDE.md first, so
it knows not to touch other sections.

4. Rule 4 — Always diff before accepting:**

```bash
# In VSCode Extension: use inline Accept/Reject per change
# In CLI: always check git diff before committing
git diff index.html
git add -p    # stage interactively, hunk by hunk
```