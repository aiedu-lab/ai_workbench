# CLAUDE.md — AI Workbench

> **Purpose:** This file is read by Claude Code at the start of every
> session. It encodes project-wide operating protocol, guardrails,
> style rules, and commit conventions. Keep this file concise
> (target 150–200 lines). Move project-specific detail to
> subdirectory `CLAUDE.md` files, not here.

---

## PROJECT OVERVIEW

This repository is the **AI Workbench** — a structured curriculum
teaching AI tools and prompting techniques to high school and university
students. It contains session plans, exercises, web projects, CLI
scripts, and multi-agent workflows.

**Repository root layout:**

```
ai_workbench/
  sessions/          # Lesson markdown files
  projects/          # Hands-on student projects
    web_site/        # Lovable & Claude Code web exercises
    client_*/        # Local app & workflow exercises
    server_*/        # Server-side exercises
  plans/             # Plan files (canonical + drafts)
  sdw/               # Specification Driven Workbench
    plan.md          # Creates contents for the lab and each session
  tools/             # Tool configuration guides
  learnings/         # Session notes and retrospectives
  docs/archive/      # Completed phase archives
```

---

## BEHAVIORAL INVARIANTS

These rules apply in every session without exception. Claude must
follow them even if the user prompt does not mention them.

### 1. Explore Before Acting

Before modifying any existing file, read and summarize it first:

```
Read [file]. Explain what it does. Do NOT write any file yet.
```

Never assume the contents of a file. Always verify.

### 2. Plan Before Coding or Creating Content

For any change touching more than one file or one function, produce a
written plan first. Use Plan Mode:

```
Propose a step-by-step plan. Do not write ANY code until I approve.
```

### 3. One Step at a Time

Execute the plan one step per session turn. After each step:

1. Show the diff
2. Wait for explicit human approval before proceeding

### 4. Commit Protocol

Every completed step must be committed before the next step begins.

**Commit message format:**

```
<type>: Phase X: Step Y - <summary of changes>
```

**Conventional commit prefixes:**

| Prefix | Use |
|---|---|
| `feat:` | New feature or capability |
| `fix:` | Bug fix |
| `style:` | Formatting, whitespace, no logic change |
| `refactor:` | Code restructure, no behavior change |
| `test:` | Adding or updating tests |
| `chore:` | Build, config, tooling, docs update |
| `docs:` | Documentation only |

**Example:**

```bash
git commit -m "feat: Phase 1: Step 2 - add history list to index.html"
```

### 5. Update Plan, Tag, and Push

After each committed step, mark it COMPLETED in `plan.md`, then:

```bash
git add plan.md
git commit -m "chore: Phase X: Step Y - mark step completed in plan.md"
git tag -a vX.Y-<brief-summary>-step-completed \
    -m "Completed Phase X Step Y: <summary>"
git push origin <output-branch> --tags
```

Tags use the format: `vX.Y-brief-summary-step-completed`
Example: `v1.2-add-history-list-step-completed`

### 6. Branching and Merging

NEVER make changes in the main branch - main remains locked. 
NEVER create a `Pull Request` (PR), perform `Code Reviews`, or 
`merge` the branch to main.

All the below decisions are manual:
* generate a pull request (PR) of the branch
* trigger a code review request to agent and follow up content edits
* merge of the branch to main or any other branch
* creation of a branch

### 7. Never Touch These

Unless explicitly instructed by the user:

* `docs/archive/` — read-only; never modify archived phases
* `plan.md` — only update to mark steps COMPLETED or add new steps;
  never delete existing history
* Files outside the current working directory for a task
* `.env` files, secrets, API keys — never read or write these

### 8. Safety Rules

* **NEVER** hardcode API keys, passwords, or tokens in any file
* **NEVER** use `rm -rf` without explicit user confirmation
* **NEVER** push directly to `main` — always use a feature branch
* **NEVER** run destructive bash commands silently; show the command
  and wait for approval
* **ALWAYS** run the validation command listed in the task's plan
  step before declaring the step complete

---

## DOCUMENTATION

### Focus on WHY, not WHAT

Comments and docstrings must explain architecture and business logic,
not restate the code:

```python
# BAD: iterates over the list
for item in items:

# GOOD: process in insertion order so history displays chronologically;
# localStorage not used — page reload intentionally clears history
# to keep the demo stateless and avoid privacy concerns
for item in items:
```

### Comment requirements

* Every non-obvious block: one WHY comment
* Every function/method: one-line docstring stating purpose and any
  non-obvious contract (e.g., side effects, ordering assumptions)
* Every AI-generated section: annotate with the plan step that
  generated it:

```html
<!-- AI-GENERATED: Phase 1 Step 2 (plan_history.md) -->
```

### Manually maintained sections

Mark hand-written sections so Claude does not regenerate them:

```html
<!-- MANUAL: core layout — do not regenerate -->
```

---

## STYLE & HYGIENE (STRICT)

### Indentation

Use exactly **2 spaces**. Never hard tabs. This applies to all file
types: HTML, CSS, JS, Python, Markdown, YAML, shell scripts.

### Line length

Maximum **80 columns**. Wrap code and comments precisely. Long strings
and URLs are exempt if wrapping would break them.

```python
# BAD (92 chars):
def organize_files(source_dir: Path, dry_run: bool, verbose: bool) -> None:

# GOOD (wrapped at 80):
def organize_files(
  source_dir: Path,
  dry_run: bool,
  verbose: bool,
) -> None:
```

### Diff consistency

Indentation of surrounding context in all diffs must match the 2-space
and 80-column rules. Never produce a diff with mixed indentation.

### File hygiene

* No trailing whitespace
* Single blank line at end of file
* No commented-out dead code — delete it or leave it; add a WHY
  comment if the deletion needs explanation

### Modern Language Constructs
* Python: Use 3.12+ features (`list[]`, `dict[]`, `|` for
  Union). Never use `typing.List` or `typing.Dict`.
* General: Always prefer latest stable language features.

---

## SESSION REHYDRATION

At the start of every new session, Claude must orient itself by
reading these files in order before taking any action:

1. `CLAUDE.md` (this file) — operating protocol
2. `sdw/plan.md` - plan to create content for the lab
3. `projects/[project_directory]/plan.md` — current phase, active step, 
   last completed step
4. The specific file(s) targeted by the active step

Then state:

```
Currently on: Phase X, Step Y — [step title]
Last completed: Phase X, Step Y-1 — [step title]
Next action: [one sentence]
```

Do not proceed without this orientation if `plan.md` exists.

### TOKEN & CONTEXT EFFICIENCY

* **Diffs Only:** Never rewrite existing files in full.
  Always use diff/search-replace blocks.
* **Strict Scope:** Only read files within the active service
  directory. Never traverse `.tmp/`, `.venv/`, `.gemini/`, 
  `__pycache__/`, `bazel-*/` or `external/`.
* **Concise:** Zero filler. Direct technical execution only.
* **Context Audit:** Drop idle files from context regularly.
  Re-read only when directly needed.


| Context level | Action |
|---|---|
| 0–60% | Work freely |
| 60–80% | Finish current step, commit, use `/compact` |
| 80–90% | Commit immediately, use `/clear`, rehydrate |
| 90%+ | Stop. Commit what exists. Start a fresh session. |

Use `/clear` between unrelated tasks. Accumulated context from a
previous task wastes tokens and degrades output on the next task.

---

## COMMON COMMANDS

```bash
# Run local web server for web projects
python3 -m http.server 8888

# Generate a file from a plan (suppress console output)
claude -p "$(cat plan.md)" --allowedTools "Write" > /dev/null

# Check what changed before committing
git diff
git add -p   # interactive hunk-by-hunk staging

# Tag a completed step
git tag -a v1.2-add-history-step-completed \
    -m "Completed Phase 1 Step 2: add history list"
git push origin feature/my-branch --tags
```

---

## PROJECT-SPECIFIC NOTES

* **Content** creation plan lives in `sdw/plan.md`.
* **Projects** live in `projects/[project directory]/`. 
  Each sub-project has its own `CLAUDE.md` with file-level fencing rules.
* **Plan template** follows the phased template in
  `plans/canonical/phased_template.md`.
* **Plans** live in `projects/[project directory]/`. 
  Each sub-project has its own `plan.md`
* **Session notes** go in `learnings/session_notes/` — one file per
  session.
* **Tokenomics:** Use Sonnet for 80%+ of tasks. Reserve Opus only for
  complex multi-file architecture decisions.
