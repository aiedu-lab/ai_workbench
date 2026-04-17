# Concept: Spec Driven Development (SDD)

## 🎯 Objective
Learn how to build software by writing the "instructions" before writing
the code. Spec Driven Development (SDD) teaches AI agents exactly what
to build, how to build it, and in what order.

## 🧠 The Core Artifacts

### 1. `CLAUDE.md` (The Operating Protocol)
This is the rulebook for your AI. Instead of relying on legacy
environment files or repetitive prompting, we put the essence of our
coding standards here.
* **What it does:** Tells the agent what languages to use, how to
  format code, and what tools to run.
* **Example Rule:**
```markdown
Always write tests before implementing the logic.
Use Vite for the frontend.
```

### 2. `plan.md` (The Blueprint)
The step-by-step checklist. AI agents get confused if you ask for an
entire app at once. `plan.md` breaks the project into manageable,
verifiable phases.

## 🔑 Key Takeaway
You are the *architect*. The AI is the *typist*. If the code fails,
the bug is usually in your `plan.md` or `CLAUDE.md`, not the AI's
execution.

## 🏃 Exercise
For the hands-on SDD project, see
[Exercise: Create Group Meetup Organizer using SDD](client_application.md).
