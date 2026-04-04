## Planning

### Tools
- Claude Code

### Concepts
- Spec-first thinking: plan.md is "master blueprint" and contract between humans and AI

### Exercise
```bash
Build a social event organizer application
```

### Process
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
- **Insight**: if agent fails, do NOT fix the code manually, fix the plan and have the agent retry

### Key Practices
- Highlight-to-prompt iteration

### Tokenomics
- Batching
  - Avoid: freestyle prompting as stream of consciouness
  - Avoid: repeated small and incremental edits 
  - Collate: prompt changes collected into few prompt
  - Use plan.md file or copy and paste plan file into prompt when tool does not natively accept plan files


### References
- [Draft Plan](project.md)

### Output
- [Plan](../projects/client_app/plan.md)
- [Notes](../learnings/session_notes/planning.md)