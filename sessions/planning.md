# Planning

## Tools
- Claude Code

---

## Concepts
- Spec-first thinking
- plan.md is "master blueprint" 
- contract between humans and AI

---

## Exercise
```bash
Build a social event organizer application
```
---

## Process Workflow
- **Planning → Execute → Reflect**
- **Planning** 
  - **Intent → Plan → Fortify → Validate → Iterate**
  - Intent: Humans collaboratively agree on what to build
  - Plan: AI and human collaboratively drafts a plan
  - Fortify: Both manually and by querying agent
    - Examine edge cases
    - Push agent to reveal and identify potential failure scenarios eg “List 3 potential failure points”
    - Cross question agent to justify the plan and its reasoning
  - Validate: Cross check AI understood the plan
  - Iterate: Humans review and refine the plan
- **Execute**: AI executes the plan
- **Reflect**
  - **Verify → Fix → Re-execute**
  - Verify: cross check AI output is appropriate
  - Fix: if output is not appropriate, refine the plan
  - Re-execute: AI re-executes the planning step

---

## Golden Rule

If the code breaks or agent fails:
- the plan is wrong
- do not fix the code or agent 
- fix the plan. 
- retest code or retry agent

---

## Key Practices
- Highlight-to-prompt iteration

---

## Tokenomics
- Batching
  - Avoid: freestyle prompting as stream of consciouness
  - Avoid: repeated small and incremental edits 
  - Collate: prompt changes collected into few prompt
  - Use plan.md file or copy and paste plan file into prompt when tool does not natively accept plan files

---

## How - We - Work

### 1. Plan First
- Always create or refine `plan.md` before coding

### 2. Prompt with Structure
Use:
- Context
- Task
- Constraints
- Output format

### 3. Execute Carefully
- Run agents in controlled scope
- Avoid large directories

### 4. Reflect
- What failed?
- Why?
- How did we fix it?

---

## References
- [Draft Plan](project.md)

---

## Output
- [Plan](../projects/client_app/plan.md)
- [Notes](../learnings/session_notes/planning.md)