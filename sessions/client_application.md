# Application on Laptop

## Tools & Setup
* [Claude Desktop](../tools/claude/desktop.md)
* [IDE - VSCode](https://code.visualstudio.com/)
* [Python in VSCode](https://code.visualstudio.com/docs/languages/python)

## Exercise - Event Organizer

We'll create a simple event organizer application that can be used to organize 
social events among friends. 

[Sample Draft Plan](../plans/draft/event_organizer.md) is a starting template 
of a plan. Use Claude Desktop (Chat) to build the plan. 
* Add important sections to the plan, such as the Email API structure
  so that the agent can send emails to the members of the event. 
* Make the plan more concrete, specific, failure-proof to edge cases, ...

Follow the below-mentioned **Planning → Execution → Reflection** sequence 
for executing the plan. 

1. Planning

* **Intent → Plan → Fortify → Validate → Iterate**
* Planning Tool: Claude Desktop (Chat)

2. Execution

* **Plan: Analyze → Update prompt → Iterate**
* IDE Tool: VSCode IDE
* Agent Tool: Claude Desktop (Code)

3. Fortify
* Push agent to reveal and identify potential failure scenarios 
* Cross question agent to justify the plan and its reasoning
* Intentionally give the agent conflicting instructions to see how 
it handles the conflict.
```bash
Initiate rescheduling when anyone cancels. 
Never reschedule once everyone agrees.
```

4. Validate & Iterate
* Use Claude Desktop (Chat) to validate and improve the plan if needed.

5. Save on completion
* Push to Github branch
* Submit Pull Request from branch to mainline

## Guardrails & Tokenomics

* Reference [⚠️ Guardrails - CLI Agents](../tools/provider_cost_control.md#cli-agents)
* Reference [💰 Cost Control - API](../tools/provider_cost_control.md#pay-per-use)

## Output

* [Plan](../projects/client_app/plan.md)
* [Notes](../learnings/session_notes/client_app.md)