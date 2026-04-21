# Client Agent Application - runs on Laptop

## Tools

* [Claude Desktop (CoWork, Code)](../tools/claude/desktop.md)
* [OpenClaw](../tools/openclaw/cli.md)

## Setup

### Verify Tools
* Test with a test folder before using on real data.
  [create test_dir](../tests/test_dir.sh) to create the folder.
* Grant folder access in `OS Settings` to move/edit files.
* **Login verification:** confirm CoWork is reachable in Claude
  Desktop before the exercise begins.

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

## Exercise A — File Organizer (CoWork)

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

### Validation
After completing the exercise, verify each item before moving on:
- [ ] Agent presented a written plan before moving any files
- [ ] You read and approved the plan explicitly before execution
- [ ] First run used `test_dir`, not a real folder
- [ ] No original files were deleted
- [ ] Files are grouped by type as intended
- [ ] You can explain why the agent made each grouping decision
- [ ] You identified at least one edge case the agent did not handle

## Reflection
* Shift focus from "writing code" to "writing guardrailed specs."
* What did the AI get wrong? How did we fix it?
* What did we miss? How can we improve the prompt?

## Documentation
* [CoWork](https://support.claude.com/en/articles/13345190-get-started-with-cowork)

## Output
* [Plan](../projects/client_automation/plan.md)
* [Notes](../learnings/session_notes/client_agent.md)

---

## Exercise B — Group Meetup Organizer: Single-Agent Version

**Previous version:** Phase 4 produced three scripts run in
sequence (`poller.py → selector.py → notifier.py`). Each was a
standalone program. This exercise replaces all three with one
Claude Code agent.

**Stack upgrade:** Scripts hold no state — a crash loses nothing.
Agents are long-running; a crash mid-run risks losing partial
work. FastAPI exposes an HTTP interface so the agent's progress
can be inspected. MongoDB persists response data between restarts
so no work is lost if the agent is interrupted.

### Step 0 — Reuse the Spec

Open `plans/specs/event_organizer.md`. The component contract is
unchanged — the agent must produce the same `responses.json`,
`decision.json`, and Discord notification as the scripts did.

### Step 1 — SDD Loop

**Spec prompt (paste into Claude Code):**

> Claude Code is the agent here — it reads your spec, plans its
> work, and generates code. `agent_meetup.py` is the output, a
> plain Python script, not an agent itself.

```
Show me a step-by-step plan and wait for my approval before
writing any code or running any command.

Context: plans/specs/event_organizer.md — Component Contract table.
Task: Generate agent_meetup.py — a Python script that runs
  all three steps in sequence:
  1. Poll each member (read config.yaml, write responses.json)
  2. Select date/venue (read responses.json, write decision.json)
  3. Notify Discord (read decision.json, POST DISCORD_WEBHOOK_URL)
Constraints on the generated script:
- Same input/output files as the three-script version
- Exit with a clear error if any step fails; do not proceed
Output: agent_meetup.py
```

### Validation

- [ ] Claude Code showed a plan and you approved it before any
  code was written
- [ ] `responses.json` matches the format from Phase 4 scripts
- [ ] `decision.json` written before notifier step fires
- [ ] Discord `#meetup-notifications` receives the same message
  as Phase 4 (`📅 Meetup confirmed! ...`)
- [ ] Stopping agent after Step 1 leaves `responses.json`
  intact; re-running picks up from Step 2

### Reflection

- What did the agent do that three separate scripts could not?
- What happens if the agent crashes between Step 2 and Step 3?
  How would you detect and recover?

---

## Exercise C — Group Meetup Organizer: Multi-Agent Version

Three specialized agents replace the single agent. Shared state
via MongoDB ensures no agent can skip ahead or corrupt another's
output.

| Agent | Input | Output |
|-------|-------|--------|
| Poller Agent | `config.yaml` | MongoDB `responses` collection |
| Selector Agent | MongoDB `responses` | MongoDB `decision` doc |
| Notifier Agent | MongoDB `decision` | Discord message |

### Step 0 — Understand the Failure Mode

Kill `agent_meetup.py` with Ctrl-C while it is midway through
polling. Observe: `responses.json` may be partially written.
That is the problem MongoDB solves — each agent writes
atomically; a crash leaves the collection intact.

### Step 1 — SDD Loop

**Spec prompt:**

> As before, Claude Code is the agent — it plans and generates
> the three Python scripts. Each script is a standalone program,
> not an agent itself.

```
Show me a step-by-step plan and wait for my approval before
writing any code or running any command.

Context: plans/specs/event_organizer.md — Component Contract.
Task: Generate three Python scripts:
  - poller_agent.py: reads config.yaml, stores responses
    in MongoDB collection `responses`
  - selector_agent.py: reads `responses`, writes decision
    doc to MongoDB collection `decision`
  - notifier_agent.py: reads `decision` doc, POSTs to
    DISCORD_WEBHOOK_URL
Constraints on the generated scripts:
- Each script must verify its input data exists; exit with
  a clear error if not
- MongoDB: mongodb://localhost:27017, db: meetup
Output: Three runnable Python scripts
```

### Failure Injection

1. Run `poller_agent.py` — let it complete
2. Run `selector_agent.py` — kill with Ctrl-C immediately
3. Run `notifier_agent.py`

**Expected:** Notifier detects no completed `decision` doc and
exits with an error — it must NOT send a Discord message.

**If Notifier fires:** the agents are not enforcing ordering.
Fix the spec and regenerate.

### Validation

- [ ] Poller Agent writes to MongoDB, not a flat file
- [ ] Selector Agent refuses to run if `responses` collection
  is empty or incomplete
- [ ] Notifier Agent refuses to run if no `decision` doc exists
- [ ] Failure injection: killing Selector prevents Notifier
  from firing
- [ ] Full run produces the same Discord message as Phase 4

### Reflection

- What coordination problem did we create by splitting into
  three agents?
- What happens if two Poller Agents run simultaneously?
- How would you guarantee exactly-once execution?
  (This seeds Phase 6: Temporal.)

---

## What Is Missing → Phase 6

Each agent is independent. There is no coordinator that:
- Retries a failed agent automatically
- Prevents duplicate runs across parallel invocations
- Reports workflow progress to a human

That coordinator is Temporal. Phase 6 wraps the three agents in
a durable Temporal workflow and deploys the entire stack to a
shared server via Docker.

**Next session:** [Multi-Agent Workflows](client_multiagent.md)

## References
- [Specification Driven Development](sdd_basics.md)
