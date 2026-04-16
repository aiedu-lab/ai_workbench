# Workflow Automation on Laptop

## Tools & Setup

* [Claude Desktop (CoWork)](../tools/claude/desktop.md)
* Test with a test folder before using on real data.
  [create test_dir](../tests/test_dir.sh) to create the folder.
* Grant folder access in `OS Settings` to move/edit files.
* **Login verification:** confirm CoWork is reachable in Claude
  Desktop before the exercise begins.

## Setup

### Student / Team Discount
* Students: check `claude.ai/pricing` for current education
  promotions; a Claude Pro plan includes CoWork.
* Teams: Claude Team plan provides a shared workspace — one seat
  is sufficient for classroom demos.

### Guardrails
* Always test on `test_dir` first — never run on a real folder
  until the test run is clean.
* No execution before plan approval — the agent must present the
  full step-by-step plan before any file is moved.
* Ask the agent to explain every decision; cross-question any
  choice that is not immediately obvious.
* Never grant write access to folders outside the exercise
  directory.

### Tokenomics
* CoWork consumes Pro / Team plan tokens — long, iterative
  automations cost more.
* Keep prompts focused; a narrow task (one folder, one rule) uses
  far fewer tokens than a broad one.
* Iterate on the test folder; only run on real data once the
  prompt is stable.

## Exercise

* Intent: Organize files in folder - group by file type

* Process: **Intent → Plan → Fortify → Validate → Iterate**
  * **Plan: Analyze → Update prompt → Iterate**

* Prompt Draft
```bash
You are a helpful assistant.
Context: I want to organize a given folder.
Task: Propose a safe and reversible plan.
Constraints:
- Do not delete files
- Do not change original files
- Group by file type
- Ask before execution

Output: Step-by-step checklist
```

## Reflection
* Shift focus from "writing code" to "writing guardrailed specs."
* What did the AI get wrong? How did we fix it?
* What did we miss? How can we improve the prompt?

## Documentation
* [CoWork](https://support.claude.com/en/articles/13345190-get-started-with-cowork)

## Output
* [Plan](../projects/client_automation/plan.md)
* [Notes](../learnings/session_notes/client_work_automation.md)