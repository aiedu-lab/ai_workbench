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
# Task: Create a  script to sort files in a folder by type.
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

## Key Insight

> “The problem is not solved by more AI
> It is solved by better coordination.”

---

## Tokenomics (Save Cost)

* Do planning in Chat (cheaper)
* Use agents only for execution
* Avoid repeating the same task
* Keep files small
* Avoid agents looping and retrying e.g review each other

---

## When to Use Multi-Agent

Use when:

* Task has clear stages (collect → clean → analyze)
* Different tools have clear strengths
* Output needs validation

---

## When NOT to Use

Avoid when:

* Task is simple
* One agent can handle it
* You don’t yet understand the workflow

---

## References

* Session: Prompting Basics
* Session: Plan-first Thinking
* Claude Code Documentation
* Internal repo `/prompts/`

---

## Final Rule

> “Start with one agent.
> Only add more agents when you clearly see the need.”

---
