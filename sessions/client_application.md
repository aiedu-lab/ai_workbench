# Application on Laptop

## Tools & Setup
* [Claude Desktop](../tools/claude/desktop.md)
* [IDE - VSCode](https://code.visualstudio.com/)
* [Python in VSCode](https://code.visualstudio.com/docs/languages/python)

## Exercise - Group Meetup Organizer

> This is the hands-on SDD exercise. Before starting, complete the
> [Concept: Spec Driven Development](sdd_basics.md) session.
> You are the *architect*; Claude Code is the *typist*.

Build a web app that coordinates any recurring group meetup — a study
group, a social club, a community gathering — using email for
scheduling and consensus.

**Stack:** React + TypeScript (Vite) · FastAPI (Python) · MongoDB

[Sample Draft Plan](../plans/draft/event_organizer.md) is a starting
template. Use Claude Desktop (Chat) to refine it into your own
`plan.md`. Scope your execution to the **Implementation Checklist**
(Steps 1–4 in the draft); the full spec is aspirational context for
future iterations.
* Add important sections, such as the Email API structure so the
  agent can send notifications to members.
* Make the plan concrete, specific, and failure-proof to edge cases.

Follow the below-mentioned **Planning → Execution → Reflection** sequence 
for executing the plan. 

1. Planning

* **Intent → Plan → Fortify → Validate → Iterate**
* Planning Tool: Claude Desktop (Chat)

2. Execution

* **Plan: Analyze → Update prompt → Iterate**

3. Fortify
* Push agent to reveal and identify potential failure scenarios 
* Cross question agent to justify the plan and its reasoning
* Intentionally give the agent conflicting instructions to see how 
it handles the conflict.
```bash
Initiate rescheduling when anyone cancels. 
Never reschedule once everyone agrees.
```

4. Validate
* Validate the output.

5. Iterate
* Revisit Execution until the output is satisfactory.

### Save on completion
* Push to Github branch
* Submit Pull Request from branch to mainline

## Guardrails & Tokenomics

* Reference [⚠️ Guardrails - CLI Agents](../tools/provider_cost_control.md#cli-agents)
* Reference [💰 Cost Control - API](../tools/provider_cost_control.md#pay-per-use)

## Output

* [Plan](../projects/client_app/plan.md)
* [Notes](../learnings/session_notes/client_app.md)