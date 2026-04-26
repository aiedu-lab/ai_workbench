# Application on Laptop

## Tools

* [Claude Desktop](../tools/claude/desktop.md)
* [IDE - VSCode](https://code.visualstudio.com/)
* [Python in VSCode](https://code.visualstudio.com/docs/languages/python)

---

## Demo — Hello World via SDD

Before the exercise, the instructor runs a live SDD demo:

1. Write a one-paragraph spec for a "Hello World" CLI script
2. Generate a `plan.md` with Claude Desktop
3. Execute: `claude -p "$(cat plan.md)" --allowedTools "Write" > /dev/null`
4. Run the script and verify output

This shows the full SDD loop — spec → plan → generate → validate —
before students apply it to the real project.

---

## Exercise — Group Meetup Organizer (non-agentic version)

> This is the hands-on SDD exercise. Before starting, complete the
> [Concept: Spec Driven Development](sdd_basics.md) session.
> You are the *architect*; Claude Code is the *typist*.

In the Slides session you pitched a one-shot meetup coordinator.
In the Web Site session you built a toy UI with a fake Notifier.
This session builds the real system: three Python scripts that run,
with a Discord message you can see arrive in the channel the
instructor provisioned.

**Stack:** Python 3.10+ · flat files (`responses.json`,
`decision.json`) · `config.yaml`

No web framework. No database. Three scripts, run in sequence.

### Step 0 — Discord Setup

Your instructor already provisioned the Discord server and webhook.
Set the env var and verify it works:

```bash
# Your instructor provided this URL
export DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/..."

# One-line validation
python -c "
import requests, os
r = requests.post(os.environ['DISCORD_WEBHOOK_URL'],
                  json={'content': 'student setup test ✓'})
print('OK' if r.status_code == 204 else f'FAIL: {r.status_code}')
"
```

Expected: `OK` and your message appears in `#meetup-notifications`.

### Step 1 — Read the Spec

Open [`plans/specs/event_organizer.md`](../plans/specs/event_organizer.md).
Read the Component Contract and Data Model sections. You will
implement exactly those interfaces — nothing more.

### Step 2 — SDD Loop for Each Script

Repeat this loop for each of the three scripts:

```text
1. Write spec  → describe what the script does in plain language
2. Review spec → confirm inputs, outputs, edge cases
3. Generate    → claude -p "$(cat spec.md)" --allowedTools "Write" > /dev/null
4. Run         → python <script>.py
5. Validate    → check the output file matches the contract
6. Iterate     → if wrong, fix the spec and regenerate
```

**Poller spec** (inputs/outputs to capture in your spec):
- Read `config.yaml` — load members, dates, venues
- For each member: prompt availability (y/n) and venue preference
- Write `responses.json`

**Selector spec:**
- Read `responses.json`
- Pick date with most available members (alphabetical tie-break)
- Pick venue preferred by most available members (alphabetical tie-break)
- If zero available: write `{"cancelled": true}`
- Write `decision.json`

**Notifier spec:**
- Read `decision.json`
- If cancelled: POST cancellation message to `DISCORD_WEBHOOK_URL`
- Otherwise: POST date, venue, attendees to `DISCORD_WEBHOOK_URL`

### Step 3 — Full Validation Sequence

```bash
python poller.py    # enter responses for each member
# check responses.json is correct
python selector.py  # check decision.json
python notifier.py  # confirm Discord message arrives
```

Expected in `#meetup-notifications`:

```text
📅 Meetup confirmed!
Date: Thu Apr 24 7pm
Venue: Library Room A
Attending: Alice, Bob, David
```

### Pluggability note

> The Notifier is a pluggable component. Swapping Discord for email
> (SendGrid), SMS (Twilio), or Slack (Slack webhooks) requires
> changing only `notifier.py`. The Poller and Selector are unaffected.

### Reflection

- What would need to change to make this system agentic?
- Which script has the most edge cases? Did your spec cover them?

---

## Guardrails & Tokenomics

* Reference [⚠️ Guardrails - CLI Agents](../tools/provider_cost_control.md#cli-agents)
* Reference [💰 Cost Control - API](../tools/provider_cost_control.md#pay-per-use)

---

## Output

* [Project Spec](../plans/specs/event_organizer.md)
* [Notes](../learnings/session_notes/client_app.md)

---

## What Is Missing → Agent Session

The three scripts run sequentially and hold no state. A crash
between scripts loses partial work with no way to retry from
the right point. The next session wraps all three steps in a
single Claude Code agent — one process that plans, executes,
and reports errors at each step.

**Next session:** [Create/Run Agent App](client_agent.md)
