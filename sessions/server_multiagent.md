# Multi-Agent Workflow on Server

## Tools

* [OpenClaw CLI](../tools/openclaw/cli.md) — agent executor
* [Temporal CLI](../tools/temporal/cli.md) — workflow orchestrator

## Setup

### Verify Tools

**OpenClaw:**
```bash
openclaw --version    # prints installed version
openclaw help         # lists available commands
```
Success: version number printed; command list appears without errors.

**Temporal (local dev mode):**
```bash
temporal version            # prints installed version
temporal server start-dev   # starts Temporal on localhost:8233
```
Open `http://localhost:8233` — success if the Temporal UI loads and
shows an empty workflow list.

### Student / Team Discount
* Temporal Cloud: free trial available at `temporal.io/cloud`.
* OpenClaw: billed via your AI provider API key — no separate plan.
* Anthropic student credits: $50 free API credits via
  [Student Builder Application](https://www.anthropic.com/api/student-builder-application).

### Guardrails
* Run OpenClaw inside a VM or Docker container with restricted
  network access — it executes any API available in its environment.
* Scope each agent to exactly one external API.
* Require human approval before any step that touches external
  systems (email, calendar, payment).
* Reference [⚠️ OpenClaw Guardrails](../tools/openclaw/cli.md#guardrails).

### Tokenomics
* Token cost multiplies with each agent hop — keep workflows
  shallow and agent prompts narrow.
* Use an API proxy between OpenClaw and your LLM provider to
  monitor and cap spend.
* Reference [💰 Cost Control](../tools/provider_cost_control.md#pay-per-use)
  and [OpenClaw Tokenomics](../tools/openclaw/cli.md#tokenomics).

## CoWork vs OpenClaw

Use this table when deciding which tool to use for local laptop work:

| Aspect | Claude CoWork | OpenClaw |
|---|---|---|
| Runs on | Laptop (desktop app) | Laptop or server |
| Interface | GUI (Claude Desktop) | CLI / Docker |
| Best for | File / folder tasks | API-driven workflows |
| Token billing | Pro / Team plan | Pay-per-use (API key) |
| Runs unattended | No — human in the loop | Yes |
| Guardrail approach | Plan approval in chat | VM / Docker isolation |
| Scales to server | No | Yes |

**Use CoWork when:** the task is file/folder-centric, a human stays
in the loop, and you are running locally on a Pro or Team plan.

**Use OpenClaw when:** the task is API-driven, needs to run
unattended, targets a server or Docker container, or requires
fine-grained token cost control.

## Concept

A multi-agent workflow decomposes a complex task into specialized
agents — each with a single responsibility — and orchestrates them
so a failure in one agent can be retried without restarting the
entire pipeline.

Key properties:
* **Decomposition:** each agent owns one step (poll, select, notify)
* **Orchestration:** Temporal sequences agents and handles retries
* **Isolation:** agents run in containers with scoped API access
* **Observability:** Temporal UI shows real-time workflow state

## Exercise — Group Meetup Organizer Pipeline

Three-agent pipeline using the
[Group Meetup Organizer spec](../plans/draft/event_organizer.md):

| Agent | Responsibility |
|---|---|
| Poller | Sends availability poll; collects member responses |
| Selector | Picks venue based on majority preference |
| Notifier | Sends confirmation email with venue and time |

Work through the phases in order. Phases 3 and 4 are stretch goals.

### Phase 1 — Single Agent on Laptop
Build one OpenClaw agent that performs all three steps sequentially:
poll → select → notify. Goal: validate agent setup and domain logic
before introducing decomposition.

### Phase 2 — Three Agents on Laptop
Split into three separate OpenClaw agents called in sequence from a
Python script. Goal: test each agent independently before composing
the pipeline.

### Phase 3 — Three Agents + Temporal on Laptop (Stretch)
Wire the three agents into a Temporal workflow with `temporal server
start-dev` running locally. Goal: experience orchestration and
retry — simulate a Selector failure and observe Temporal retry it
automatically.

### Phase 4 — Deploy to Server in Docker (Stretch)
Package the Phase 3 workflow in a Docker container and deploy to a
server. Goal: production-grade deployment with full container
isolation.

### Validation
After completing your phase, verify each item:
- [ ] Phase 1: agent completed poll → select → notify without errors
- [ ] Phase 2: each agent was tested in isolation before composition
- [ ] Phase 2: pipeline produced the correct notification output
- [ ] Phase 3: Temporal UI shows all workflow steps as succeeded
- [ ] Phase 3: you simulated an agent failure and observed retry
- [ ] No agent was granted access beyond its one required API
- [ ] You can explain what Temporal does if Notifier fails after
      Selector has already succeeded

## Reflection
* Which phase was hardest to debug? Why?
* What would break if agents were not isolated from each other?
* When would you choose Temporal over a simple Python script?

## Output
* [Plan](../projects/server_multiagent/plan.md)
* [Notes](../learnings/session_notes/server_multiagent.md)
