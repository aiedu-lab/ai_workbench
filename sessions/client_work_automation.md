# Workflow Automation on Laptop

## Rules
* Be VERY Cautious - Build heavy guardrails by SETTING RULES
  * NO execution before plan approval
* ASK Agent to explain/justify the plan
  * CROSS QUESTION specific choices made 

## Tools & Setup

* [Claude Desktop (CoWork)](../tools/claude/desktop.md)
* Test with a test folder before using on real data. 
  [create test_dir](../tests/test_dir.sh) to create the folder.
* Grant folder access in `OS Settings` to move/edit files

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