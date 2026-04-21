# Multi Agent Workflow on Laptop - The AI Team

## Objective

Learn how to **combine multiple AI agents** so each does what it’s best at—like a team.

---

## Concepts

### 1. What is a Multi-Agent Workflow?

In the world of AI, a "Generalist" tries to do everything, such as a 
student trying to write, edit, and design a whole yearbook alone. 
A Multi-Agent Workflow is a "Specialist" approach. You break a big 
job into smaller tasks and give each task to the AI "agent" best 
suited for it.

**The Big Idea**: Instead of asking one AI to "Build a house," you ask:
* One to "Draw the blueprints" 
* Another to "List the materials" 
* Third to "Check for safety."

---

### Analogy

Think of a **school group project**:

* One student → writes content
* One student → checks grammar
* One student → creates slides

One student may be good at writing, but not at creating slides.
👉 Better than one student doing everything which takes more time 
and may be poorly done.  

---

### Why use multiple agents?

Each tool has strengths:

| Agent                      | Strength                        |
| -------------------------- | ------------------------------- |
| Claude Code                | Writing & fixing code           |
| Claude CoWork              | Working with files & automation |
| Web tools (Lovable)        | Building UI quickly             |
| Chat (Gemini)              | Thinking, planning              |

---

### When NOT to use multi-agent

Multi-agent systems are cool, but add work and cost. Avoid this for:
* Simple tasks - simple email, math probllem, rename few files
* Beginners just starting
* Small scripts or quick answers

❌ Overengineering example:
> Using 3 agents to rename files

---

## Exercise 1: The Bug-Squash pipeline - “Code -> Review -> Fix” Workflow

### Objective
Learn how to use multiple agents together:
- Claude Code → write code
- Codex (OpenAI) → review code
- Claude Code → fix code

---

### Goal
Use a "Team" to write, critique, and fix code. We use human to oversee 
and two different AI "personalities" to ensure the code is good.

- The Author: Claude Code writes code
- The Critic: OpenAI Codex reviews code
- The Overseer: Human validates review feedback
- The Author: Claude Code fixes code
---

#### The Author: Claude Code writes code

Generate code 
```bash
# Task: Create a python script to sort files in a folder by type.
CODE_PROMPT="Write a Python script that 
  - moves files into folders based on the month they were created
  - do not delete files
  - output ONLY raw Python code. 
  - do NOT output markdown, fences, or backticks
  - do NOT output explanation or introduction
"
claude -p "$CODE_PROMPT" > organizer.gen.py
```

Sanitize code if not clean
```bash
# Remove any lines with markdown backticks
sed '/^```/d' organizer.gen.py > organizer.py
```

#### The Critic: OpenAI Codex reviews Code

```bash
MODEL="gpt-4.1"
REVIEW_PROMPT="Review the code in organizer.py.
  - find bugs
  - improve safety
  - suggest improvements
  - suggest better structure
  - find 3 ways this script could fail (disk full, file locked, etc)

=== CODE (organizer.py) ===
$(cat organizer.py)
"
codex exec --model "$MODEL" "$REVIEW_PROMPT" > organizer.review.md
```

#### The Author: Claude Code fixes code

```bash
FIX_PROMPT="Fix python script below based on code review.
  - Do not rewrite everything
  - Only fix identified issues
  - Keep it simple
  - output ONLY raw Python code. 
  - do NOT output markdown, fences, or backticks
  - do NOT output explanation or introduction

=== CODE (organizer.py) ===
$(cat organizer.py)

=== REVIEW (organizer.review.md) ===
$(cat organizer.review.md)
"
claude -p "$FIX_PROMPT" > organizer.fixed.py
```
4. Accept Fix if appropriate (Human)
* examine diff
```bash
diff organizer.py organizer.fixed.py
```
* if diff is appropriate, accept the fix
```bash
mv organizer.fixed.py organizer.py
```

### Tokenomics
* Review 1-2 times, avoid loop review
* Keep files small
* Avoid reviewing entire repos
* Avoid reviewing more than few files and few 100 lines of code

### Rules
* Do NOT skip review step
* Do NOT blindly accept fixes
* Always compare before vs after

---

## Exercise 2: “Mini Data Pipeline”

Goal:

* Download simple data
* Clean it
* Analyze it
* Build a simple web page to visualize the data

Using **"few" (2–3) agents**

### Execution

0. Define the Plan (Chat Agent)

```bash
Ask: 

Create a simple plan to:
1. Get public data (e.g., stock prices)
2. Clean the data
3. Analyze it
4. Build a simple web page to visualize the data

Keep it beginner friendly.
```

1. Data Collection (Claude CoWork)

Task: Download a simple dataset (CSV). 

Example prompt:
```bash
Find a small public dataset (CSV) about stocks.
Download it into this folder.
Do not download large files.
Explain what each column means.
```

2. Data Cleaning (Claude Code)

Task: Clean and structure the data

Example prompt:
```bash
Read the CSV file.
Clean missing values.
Rename columns clearly.
Save a new cleaned file.
Explain what you changed.
```

3. Analysis (Gemini)

Task: Generate insights

Example prompt:
```bash
Analyze the cleaned dataset.
Find 3 interesting insights.
Show simple statistics.
Explain in simple language.
```

4. SaaSify - scripted Visualization & Analysis (Lovable)

Example Prompt for Lovable:
```bash
1. A dropdown menu to select a stock symbol.
2. Push button named "Chart" to show a simple chart.
3. Push button named "Summary" to show a simple summary.
4. Keep it easy to understand.
```

---

## Reflection

### What worked?

* Breaking work into steps
* Assigning clear roles
* Reviewing before execution

---

### What breaks?

* Too many agents → confusion
* Poor handoff or lost context between agents
* Agents contradict - one says use python, another says use javascript
* Overcomplicating simple tasks

---

## Exercise 3 — Group Meetup Organizer: Temporal Orchestration

**Previous version:** Phase 5 Exercise C built three agents with
MongoDB shared state. The remaining problem: nothing prevents
Notifier from firing before Selector completes, or being invoked
twice if the coordinator crashes. Temporal solves this.

**What Temporal adds:** Each agent becomes an Activity inside a
durable Workflow. If SelectActivity crashes mid-run, Temporal
retries it automatically. NotifyActivity never fires until
SelectActivity succeeds — no coordination code needed in your
agents.

```
Temporal Workflow: MeetupWorkflow
  ├── PollActivity    (poll logic → responses to MongoDB)
  ├── SelectActivity  (select logic → decision to MongoDB)
  └── NotifyActivity  (notify logic → Discord webhook)
```

### Step 0 — Prerequisites

```bash
# macOS
brew install temporal
# Windows / WSL2
winget install Temporal

# Start Temporal dev server (keep running in a terminal)
temporal server start-dev
# UI: http://localhost:8080
```

### Step 1 — SDD Loop

> Claude Code generates the Temporal workflow. The three activity
> functions wrap your Phase 5 agent scripts.

```
Show me a step-by-step plan and wait for my approval before
writing any code or running any command.

Context: plans/specs/event_organizer.md — Component Contract.
Task: Generate a Temporal workflow (Python SDK) with three
  activities wrapping the Group Meetup Organizer agents:
  - PollActivity: poll logic (config.yaml → MongoDB responses)
  - SelectActivity: select logic (MongoDB responses → decision)
  - NotifyActivity: notify logic (decision → DISCORD_WEBHOOK_URL)
Constraints:
- SelectActivity must not start until PollActivity completes
- NotifyActivity must not start until SelectActivity completes
- Use temporalio Python SDK
- Temporal server: localhost:7233, MongoDB: localhost:27017
Output: workflow.py, worker.py, starter.py
```

### Failure Injection

1. `python worker.py` — start the worker
2. `python starter.py` — trigger MeetupWorkflow
3. Kill the worker with Ctrl-C while SelectActivity runs
4. `python worker.py` — restart the worker

**Expected:** Temporal replays from the last checkpoint.
SelectActivity re-runs; NotifyActivity fires only after it
succeeds. Verify sequence in the Temporal UI at
`http://localhost:8080`.

**If Notifier fires before Select completes:** ordering is not
enforced. Fix the spec and regenerate.

### Validation

- [ ] Temporal dev server running; UI at localhost:8080 visible
- [ ] `python starter.py` triggers MeetupWorkflow
- [ ] Temporal UI shows PollActivity → SelectActivity →
  NotifyActivity in order
- [ ] Failure injection: restarting worker resumes from
  SelectActivity; Notifier does not double-fire
- [ ] Discord `#meetup-notifications` receives the same message
  as Phase 4 and 5 runs

### Reflection

- What did Temporal give us that Phase 5 Exercise C could not?
- What is the cost of adding Temporal?
  (added infra, latency, operational complexity)
- When would you NOT use Temporal?

---

## What Is Missing → Server Session

The laptop Temporal workflow uses a dev server and local MongoDB.
For a real deployment:
- Temporal and MongoDB must be always-on services, not dev mode
- Multiple simultaneous poll submissions must be isolated
- Logs, retry history, and Discord notifications must be
  observable from a machine you are not sitting at

The next session deploys the complete stack — Temporal, MongoDB,
and all three worker containers — to a shared server via Docker
Compose, addressing each of these gaps.

**Next session:** [Multi-Agent Workflows on Server](server_multiagent.md)
