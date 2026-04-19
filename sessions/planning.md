# Planning

## Tools
- Claude Desktop (Code)

---

## Concepts
- Spec-first thinking
- plan.md is "master blueprint" 
- contract between humans and AI

---

## Exercise

**Project: Group Meetup Organizer**

> One group. One meetup. Three steps: poll, select, notify.
> The instructor sets up the group config before the lab.
> You write the code that runs those three steps.

Your task: read 
[`plans/draft/event_organizer.md`](../plans/draft/event_organizer.md)
and produce a `plan.md` for the Group Meetup Organizer. Focus on:
- What the three components do (concept level — no code)
- What data flows between them
- What success looks like for each component

> You will return to this project in every remaining session —
> first as a pitch deck, then as a toy web site, then as three
> Python scripts, then as an agentic system, then deployed on
> a server.
---

## Process Workflow
- **Planning → Execute → Reflect**
- **Planning** 
  - **Intent → Plan → Fortify → Validate → Iterate**
  - Intent: Humans collaboratively agree on what to build
  - Plan: AI and human collaboratively drafts a plan
  - Fortify: Both manually and by querying agent
    - Examine edge cases
    - Push agent to reveal and identify potential failure scenarios 
      eg “List 3 potential failure points”
    - Cross question agent whether it can identify plan assumptions 
    - Push agent to think step by step and reason about the plan
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
- [Project Spec](../plans/draft/event_organizer.md)

---

## Output
- [Plan](../projects/client_app/plan.md)
- [Notes](../learnings/session_notes/planning.md)
