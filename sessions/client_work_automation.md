# Workflow Automation on Laptop

## Tools

* [Claude Desktop (CoWork)](../tools/claude/desktop.md)

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
* [Notes](../learnings/session_notes/client_work_automation.md)

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

Open `plans/draft/event_organizer.md`. The component contract is
unchanged — the agent must produce the same `responses.json`,
`decision.json`, and Discord notification as the scripts did.

### Step 1 — SDD Loop

**Spec prompt (paste into Claude Code):**

```
Context: plans/draft/event_organizer.md — Component Contract table.
Task: Build a single Claude Code agent (agent_meetup.py) that
  executes all three steps in sequence:
  1. Poll each member (read config.yaml, write responses.json)
  2. Select date/venue (read responses.json, write decision.json)
  3. Notify Discord (read decision.json, POST DISCORD_WEBHOOK_URL)
Constraints:
- Same input/output files as the three-script version
- Agent must present a plan before executing any step
- No step executes if the previous step failed
Output: agent_meetup.py
```

### Validation

- [ ] `agent_meetup.py` presents a plan before polling begins
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