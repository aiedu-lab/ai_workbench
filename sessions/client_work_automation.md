# Workflow Automation on Laptop

## Rules
* Be VERY Cautious - Build heavy guardrails by SETTING RULES
  * NO execution before plan approval
* ASK Agent to explain/justify the plan
  * CROSS QUESTION specific choices made 

## Tools & Setup

* [Claude Desktop (CoWork)](../tools/claude/desktop.md)
* Test with a test folder before using on real data
```bash
# Create a test directory
mkdir -p test_dir
cd test_dir

# Create dummy files of different types and sizes
truncate -s 1K very_small_file_tom.txt 
truncate -s 1K very_small_file_alice.pdf 
truncate -s 2K small_file_susan.jpg 
truncate -s 2K small_file_charlie.mp4 
truncate -s 4K medium_file_bob.pdf 
truncate -s 4K medium_file_lisa.jpg 
truncate -s 8K large_file_harry.txt 
truncate -s 8K large_file_david.mp4
```
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