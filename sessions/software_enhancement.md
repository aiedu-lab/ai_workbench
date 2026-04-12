# Software Enhancement

The below steps are guidelines for any software enhancement 
initiative.

## Enhancement Steps: Explore → Plan → Code → Commit

**Never** ask Claude Code to modify existing code without 
first understanding it. 
The pattern that works:

```bash
# Step 1: Explore only — no edits yet
claude "
Read through files in [project_directory] and explain what each 
file does.
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

## Legacy to Modern Code

In this initiative, the business logic remains same but the software is 
upgraded to leverage "better" programming language frameworks. 
Examples include migrating from:
* PHP to python or python 2.x to 3.x for better constructs and 
ecosystem.
* python to Go for stronger typing and/or concurrency support.

### Migration Workflow

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

## Modifying Hybrid Code: Manually Written + AI Generated

In this scenario, the business logic is modified. Examples include
* Code refactoring so as to decouple configuration (hard code) from 
the code logic or decouple data/prompt from the code logic. 
* Code maintenance so as to fix bugs and cleanup or retire old code.
* Code adaptation so as to use "better" modules or libraries, for improved 
performance, cipher, etc. 

### Modification Workflow

When a codebase mixes hand-written and AI-generated code, use these
rules to keep it coherent:

**Mark sections in comments:**

```html
<!-- MANUAL: core layout — do not regenerate -->
<header>...</header>

<!-- AI-GENERATED: Phase 1 Step 2 (plan_history.md) -->
<ul id="history"></ul>
```

**Fence sections in CLAUDE.md:**

```markdown
## Do NOT Touch
- The <header> block in files — manually maintained

## Safe to Modify
- The #history section and its CSS
- JavaScript functions prefixed with `ai_`
```

**One plan.md per feature:**

```
[project directory]
  plan.md             ← original app
  plan_history.md     ← history feature
  plan_validation.md  ← input validation
  [directories files ...]
  CLAUDE.md
```

**Always diff before accepting:**

```bash
git diff [file]
git add -p    # stage interactively, hunk by hunk
```

---

### Enhancing Tests

TODO ADD: 
What are the broard types of test enhancements. 
What are the steps to follow and prompt templates that help enhance test cases for each category below?

Test types:
* Unit Tests
* Solution Tests
* CI Smoke Tests
* Benchmark Tests

### Enhancing Manifest

TODO ADD: 
What are the broard types of manifest enhancements 
What are the steps to follow and prompt templates that help enhance manifest for each type?
