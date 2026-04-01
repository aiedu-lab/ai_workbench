# AI Education Lab Agenda

## Overview

A multi-session program to learn AI tooling and coding agents using:
- Prompting
- Planning (plan.md)
- Agent execution
- Reflection and debugging

---

## Session 1: Introduction (30 mins)

### Objective
Understand session structure and roles.

### Structure
**One Tool → One Concept → One Project → One Failure → One Reflection**

### Tool
- Claude Chat

### Activities
- Group formation (Driver / Prompt Engineer / Observer)
- Observer tracks hallucination drift

### Output
- Notes: `/learnings/session-notes/01_intro.md`

---

## Session 2: Prompting & Framework (45 mins)

### Concepts
- Prompts as software
- Prompt structure:
  - Context → Task → Constraints → Output
- Negative prompting

### Exercise
- Stock research demo
- Compare good vs bad prompts

### Output
- Notes: `/learnings/session-notes/02_prompting.md`

---

## Session 3: Plan, Plan, Plan (40 mins)

### Concepts
- Spec-first thinking
- plan.md as source of truth

### Exercise
- Event organizer app
- AI drafts plan → humans refine

### Key Practices
- Highlight-to-prompt iteration
- Failure injection:
  - “List 3 potential failure points”

### Output
- Plan: `/projects/client_app/plan.md`
- Notes: `/learnings/session-notes/03_planning.md`

---

## Session 4: AI Demo (60 mins)

### Tools
- Lovable (web)
- Claude Code (CLI)

### Activities
- Build app from plan.md
- Compare outputs

### Reflection
- Speed vs control vs transparency

---

## Session 5: Client Application (60 mins)

### Setup
- Install Claude Code (API mode)
- Set $5 spend cap
- cd into repo directory
- set up key, validate key, start claude cleanly
```bash
export ANTHROPIC_API_KEY='your-key'
bash tools/claude/check_env.sh
claude logout (ensure no subscription usage)
claude
```

### Exercise
- Build local app using agent loop:
  - Prompt → Run → Error → Fix

### Safety
- Kill switch (`Ctrl + C`)
- Limit file scope

### Output
- Code: `/projects/client_app/`
- Prompts: `/prompts/`
- Learnings: `/learnings/`

---

## Session 6: Work Automation (60 mins)

### Project
- Organize Downloads folder

### Rules
- No execution before plan approval
- No file deletion
- Explain approach first

### Output
- `/projects/client_automation/`

---

## Session 7: Server Application (60 mins)

### Project
- Flight tracker with notification

### Focus
- Extend plan-first thinking
- Compare agent approaches

### Pre-Check

- cd into repo directory
```bash
- bash tools/claude/check_env.sh # confirms API key is set
```

---

## Appendix

### Sample Project: Weekly Social Organizer

Includes:
- Intent
- Features
- Data schema
- Implementation checklist
- Technical blockers

---

## Master Rule

> If the code breaks, the plan is wrong. Fix the plan.
