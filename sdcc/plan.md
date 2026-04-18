# Plan: Group Meetup Organizer — Progressive Exercise Arc

TL;DR
This plan consolidates the seemingly disparate exercises across sessions 
into **one progressive project** — the `Group Meetup Organizer` — 
that grows in sophistication, features, and deployment scope as 
students advance through the lab. The same project appears
in every session from Planning through Multi-Agent Workflows. Earlier
sessions use deliberately incomplete toy versions so that students
feel the gap — and understand why SDD and agents are needed — before
building the full application. Execute one step at a time.

---

## Project Description (canonical — replaces the draft plan)

### What this is

A **one-shot meetup coordinator** for a fixed group. Given a list of
members, available dates, and venue options, it:

1. Polls each member: "Are you free? What venue do you prefer?"
2. Selects the venue that the most free members prefer
3. Notifies the group via a Discord message

That is the complete application. It runs once per meetup. A human
(the organizer) triggers it when they want to schedule a meetup.

### What this is NOT

* Not a recurring scheduler or cron job
* Not a SaaS product with user registration or authentication
* Not a multi-tenant system with events, subscriptions, or regions
* Not an email sender or calendar invite system
* Not a cancellation or rescheduling workflow

These are real product features that would be built on top of this
architecture. They are not part of the lab.

### Why one-shot is the right scope

The Poller → Selector → Notifier architecture is identical whether
you run the system once or a hundred times. A recurring scheduler
is just a cron job wrapping the same three steps. Teaching the
one-shot version teaches everything architecturally important, and
a student can complete it in a single lab session.

### The complete data model (simple)

**config.yaml** — the only configuration interface. Set by the
instructor before the lab; students receive it ready to use.

```yaml
group: "Thursday Study Squad"
members:
  - name: "Alice"
  - name: "Bob"
  - name: "Carol"
  - name: "David"
options:
  dates:
    - "Thu Apr 24 7pm"
    - "Thu May 1 7pm"
    - "Thu May 8 7pm"
  venues:
    - "Library Room A"
    - "Coffee Lab on Castro"
    - "Online / Video Call"
```

**responses.json** — written by the Poller, read by the Selector.

```json
{
  "Alice":  {"available": true,  "venue": "Library Room A"},
  "Bob":    {"available": true,  "venue": "Coffee Lab on Castro"},
  "Carol":  {"available": false, "venue": null},
  "David":  {"available": true,  "venue": "Library Room A"}
}
```

**decision.json** — written by the Selector, read by the Notifier.

```json
{
  "date": "Thu Apr 24 7pm",
  "venue": "Library Room A",
  "attendees": ["Alice", "Bob", "David"]
}
```

### Selection logic (simple majority, no ties)

The Selector picks:
- Date: the date where the most members are available
- Venue: the venue preferred by the most available members
- Tie-breaking: alphabetical order (deterministic, no randomness)
- Cancelled: if zero members are available, write
  `{"cancelled": true}` to `decision.json` and the Notifier
  sends a cancellation message

### The three scripts (non-agentic version)

```
python poller.py    # reads config.yaml, collects responses,
                    # writes responses.json
python selector.py  # reads responses.json, picks date + venue,
                    # writes decision.json
python notifier.py  # reads decision.json, POSTs to Discord webhook
```

---

## Scope Decisions (locked)

### 1. One fixed group, fixed members

Members are defined in `config.yaml`. The application never adds,
removes, or authenticates members. The instructor sets up
`config.yaml` before the lab; students do not edit it.

### 2. Discord channel pre-provisioned by instructor

The instructor creates the Discord server, channel, and webhook URL
before the lab. Students receive `DISCORD_WEBHOOK_URL` as an
environment variable. The application never creates or manages
channels.

### 3. Shared store is flat files in the non-agentic version

No database until the agentic versions, where persistent state earns
its complexity. In the non-agentic version: two JSON files.

### 4. Stack grows only when complexity earns it

| Version | Stack | Why the stack is this size |
|---|---|---|
| Toy (Gamma) | Slides only | No code needed |
| Toy (Lovable) | HTML form, no backend | UI concept only |
| Non-agentic (SDD) | Python + flat files | Architecture visible, zero framework noise |
| Single-agent (OpenClaw) | Python + FastAPI + MongoDB | Agent needs HTTP interface + persistent state |
| Multi-agent (OpenClaw) | Python + FastAPI + MongoDB | Multiple agents share one store |
| Temporal (laptop) | + Temporal | Durable orchestration requires real persistence |
| Docker (server) | All above in containers | Deployment adds container layer only |

---

## Notification Platform Decision (locked)

**Discord via Webhook. No alternatives.**

| Platform | Setup cost | Auth complexity | Lab-viable? |
|---|---|---|---|
| Email (SMTP) | Medium | App passwords, spam filters, delivery lag | ⚠️ Borderline |
| WhatsApp (Twilio) | High | Meta Business Account, WABA, template approval | ❌ No |
| Discord Bot | Medium | Developer Portal, bot token, Intents, async | ⚠️ Borderline |
| **Discord Webhook** | **Minimal** | **No token, no bot, just a URL** | **✅ Yes** |

The full Notifier in the non-agentic version:

```python
# notifier.py
import requests, json, os

decision = json.load(open("decision.json"))
if decision.get("cancelled"):
  msg = "❌ **Meetup cancelled** — not enough members available."
else:
  attendees = ", ".join(decision["attendees"])
  msg = (
    f"📅 **Meetup confirmed!**\n"
    f"**Date:** {decision['date']}\n"
    f"**Venue:** {decision['venue']}\n"
    f"**Attending:** {attendees}"
  )

requests.post(os.environ["DISCORD_WEBHOOK_URL"], json={"content": msg})
print("Notification sent.")
```

Pluggability note (appears once, in the SDD session):
> The Notifier is a pluggable component. Swapping Discord for email
> (SendGrid), SMS (Twilio), or Slack (Slack webhooks) requires
> changing only `notifier.py`. The Poller and Selector are unaffected.

---

## Architecture Arc

```
Session: Planning
└── Concept only — no code, plan the app in plain language
  └── Output: plan.md for the Group Meetup Organizer

Session: Create Presentation (Gamma)
└── Demo: AI Education Lab pitch deck (5 slides, instructor-led)
└── Exercise: Group Meetup Organizer pitch deck (toy version 0)
  └── No functionality — stakeholder presentation only
  └── Gap: "We have a pitch but no working product."

Session: Create/Run Web Site (Lovable)
└── Demo: Hello World on Lovable (unchanged)
└── Exercise: Group Meetup Organizer poll UI (toy version 1)
  └── Real UI, fake backend — hardcoded result, no webhook call
  └── Gap: "The UI exists but the app is not real yet."

Session: Client Application / SDD
└── Demo: Hello World via SDD plan + Claude Code (unchanged)
└── Exercise: Group Meetup Organizer — non-agentic version
  └── Three Python scripts + two JSON files + config.yaml
  └── Real Discord webhook notification
  └── No web framework, no database

Session: Client Workflow Automation (OpenClaw)
└── Demo: File organization (CoWork + OpenClaw, unchanged)
└── Exercise A: Single-agent (OpenClaw) — one agent, three steps
└── Exercise B: Multi-agent (OpenClaw) — one agent per component
└── Note: CoWork guardrails vs OpenClaw permissions model

Session: Multi-Agent Workflows
└── Exercise A: Three agents + Temporal on laptop
└── Exercise B: Deploy to server via Docker
```

---

## Phase -1: INSTRUCTOR PREFLIGHT

**Target file:** `sessions/instructor.md` (new file)

**Purpose:** Everything an instructor must complete *before* students
arrive. Any CS graduate can run this checklist independently. Each
step includes a validation test so the instructor knows it worked.

- [ ] **Step -1.1: Create the `sessions/instructor.md` file**

  The file must contain the following sections, in order:

  **Header:**
  ```
  # Instructor Preflight Checklist
  Complete every step and its validation before students arrive.
  Time required: approximately 30 minutes.
  ```

  **Section 1 — Discord Setup (10 min)**
  - Create a Discord server named `meetup-lab` (or use an existing one)
  - Create a text channel `#meetup-notifications`
  - Open Channel Settings → Integrations → Webhooks → New Webhook
  - Name the webhook `Meetup Bot`
  - Copy the webhook URL — this is `DISCORD_WEBHOOK_URL`
  - Validation:
    ```bash
    export DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/..."
    python -c "
    import requests, os
    r = requests.post(os.environ['DISCORD_WEBHOOK_URL'],
                      json={'content': '✅ Instructor preflight test'})
    print('OK' if r.status_code == 204 else f'FAIL: {r.status_code}')
    "
    ```
    Expected: `OK` and a message appears in `#meetup-notifications`.

  **Section 2 — Create `config.yaml` for the lab group (5 min)**
  - Replace the member names with the actual students attending
  - Replace venue options with locally relevant options
  - Save as `config.yaml` in the project directory
  - Template:
    ```yaml
    group: "Thursday Study Squad"
    members:
      - name: "Alice"    # replace with actual student names
      - name: "Bob"
      - name: "Carol"
      - name: "David"
    options:
      dates:
        - "Thu Apr 24 7pm"   # replace with upcoming Thursdays
        - "Thu May 1 7pm"
        - "Thu May 8 7pm"
      venues:
        - "Library Room A"   # replace with local venues
        - "Coffee Lab"
        - "Online / Video Call"
    ```
  - Validation: `python -c "import yaml; print(yaml.safe_load(open('config.yaml')))"` — no errors.

  **Section 3 — Create `.env.example` for students (2 min)**
  - Create `.env.example` in the project root:
    ```
    DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/REPLACE_ME
    ```
  - Do NOT commit the real URL — `.env` must be in `.gitignore`
  - Share the real URL with students verbally or via a shared doc

  **Section 4 — Verify Python environment (5 min)**
  - Ensure Python 3.10+ is installed: `python --version`
  - Install dependencies: `pip install requests pyyaml`
  - Validation: `python -c "import requests, yaml; print('OK')`

  **Section 5 — Run the non-agentic version end-to-end (10 min)**
  - This is the full smoke test. Run all three scripts in sequence
    using the `config.yaml` you just created:
    ```bash
    python poller.py    # enter responses for each member manually
    python selector.py  # check decision.json output
    python notifier.py  # confirm Discord message arrives
    ```
  - Expected: `#meetup-notifications` receives a message like:
    ```
    📅 Meetup confirmed!
    Date: Thu Apr 24 7pm
    Venue: Library Room A
    Attending: Alice, Bob, David
    ```
  - If this works, the lab is ready.

  **Section 6 — README.md agenda reference**
  - Confirm `README.md` lists `sessions/instructor.md` as the
    first entry, before Planning, with label "Instructor Preflight"
  - Students should not need to read this file, but it must be
    discoverable if they are teaching the lab themselves

- [ ] **Step -1.2: Add `sessions/instructor.md` to `README.md` agenda**
  - Add as the first row, before all session rows:

    ```markdown
    | [**Instructor Preflight**](sessions/instructor.md) | Before lab | Discord, config.yaml, Python env | 30 mins |
    ```

---

## Phase 0: VALIDATE AND LOCK THE PROJECT SPEC

**Target file:** `plans/draft/event_organizer.md`

- [ ] **Step 0.1: Audit current `event_organizer.md`**
  - Read the file end to end
  - The current draft describes a full SaaS product (recurring
    events, self-onboarding, region rotation, cancellation flows,
    garbage collection). Flag everything that exceeds the one-shot
    scope defined in the Project Description above.
  - Do NOT edit yet — produce a written audit listing what to
    keep, what to remove, and what to add

- [ ] **Step 0.2: Rewrite `event_organizer.md` to correct scope**
  - Keep: project description, the three-component model, the data
    model (config.yaml / responses.json / decision.json), the
    session arc mapping
  - Remove: recurring scheduling, self-onboarding, member
    subscription management, region/city rotation, calendar invites,
    cancellation workflow, garbage collection, ConsensusThreshold
    dropdown, DeleteAfterWeeks — all of these
  - Add: the simplified selection logic (simple majority,
    alphabetical tie-breaking, cancellation if zero available)
  - Add: the scope decisions section (verbatim from this plan)
  - Add: instructor setup steps (Discord pre-provisioning)
  - Add: notification platform decision and rationale
  - Constraint: readable in under 5 minutes; answers "what are we
    building and why" — not "how"; no feature that cannot be
    implemented in a 90-minute lab session

- [ ] **Step 0.3: Lock the three-component contract**
  - Poller: input `config.yaml` → output `responses.json`
  - Selector: input `responses.json` → output `decision.json`
  - Notifier: input `decision.json` + `DISCORD_WEBHOOK_URL` →
    output Discord message
  - Contract must be identical in every session file

---

## Phase 1: PLANNING SESSION — VALIDATE WORDING

**Target file:** `sessions/planning.md`

- [ ] **Step 1.1: Audit `sessions/planning.md`**
  - Confirm the exercise references the `Group Meetup Organizer`
  - Confirm framing is concept-only (no code, no framework specifics)
  - Confirm it points to `plans/draft/event_organizer.md`
  - Flag any wording from the over-specified draft (recurring events,
    self-onboarding, cancellation) — remove it

- [ ] **Step 1.2: Update `sessions/planning.md` if needed**
  - Exercise: name the project, describe it as a one-shot coordinator,
    state the three components at concept level, ask students to
    produce a plan (not code)
  - Scope statement to include:
    > "One group. One meetup. Three steps: poll, select, notify.
    > The instructor sets up the group config before the lab.
    > You write the code that runs those three steps."
  - Add the full forward reference arc:
    > "You will return to this project in every remaining session —
    > first as a pitch deck, then as a toy web site, then as three
    > Python scripts, then as an agentic system, then deployed on
    > a server."

---

## Phase 2: SLIDES SESSION — GAMMA PRESENTATIONS

**Target file:** `sessions/slides.md`

- [ ] **Step 2.1: Audit `sessions/slides.md`**
  - Confirm the session has a demo section and an exercise section
  - Confirm any reference to the organizer is scoped as one-shot
    (not recurring, not SaaS)

- [ ] **Step 2.2: Confirm or add Demo (AI Education Lab deck)**
  - 5-slide deck, instructor builds it live in Gamma:
    1. Who runs the lab and who attends
    2. Why the lab exists
    3. What the exercises are (the progressive arc)
    4. How to contribute to the lab
    5. Call to action

- [ ] **Step 2.3: Add `Group Meetup Organizer` exercise (toy version 0)**
  - Frame: "Build a stakeholder pitch deck. Audience: a student
    club committee deciding whether to adopt this system."
  - Slide content: problem, three-component solution at concept
    level (poll → select → Discord notification), what success
    looks like
  - Gap statement:
    > "We have a pitch. We have no working system. In the Web Site
    > session we build a first version of the UI — and see exactly
    > what is still missing."
  - No implementation details of any kind

- [ ] **Step 2.4: Confirm Gamma install/start instructions present**

---

## Phase 3: WEB SITE SESSION — LOVABLE TOY UI (TOY VERSION 1)

**Target file:** `sessions/web_site.md`

- [ ] **Step 3.1: Audit `sessions/web_site.md`**
  - Hello World demo and Exercise A must remain intact
  - Confirm `Group Meetup Organizer` exercise does not exist yet
    (or confirm it is scoped as toy version only)

- [ ] **Step 3.2: Add `Group Meetup Organizer` toy UI exercise (Exercise B)**
  - Position: after Exercise A
  - What to build in Lovable:
    - Poll form: member name, 3 date checkboxes, venue preference
    - Submit button
    - Result page: hardcoded date + venue, "✓ Notification sent
      to Discord" (display only — no webhook call)
  - Explicit omissions (state in the exercise):
    - No Selector algorithm
    - No Discord webhook call
    - No persistence
  - Gap statement:
    > "The Selector has no logic. The Notifier sends nothing.
    > Data disappears on refresh. We have a UI but not an
    > application. In the Client Application session we build
    > the real system."

- [ ] **Step 3.3: Confirm session structure:**
  1. Demo: Hello World (Lovable vs Claude Code CLI)
  2. Exercise A: Hello World with Claude Code
  3. Exercise B: Group Meetup Organizer toy UI (new)

---

## Phase 4: CLIENT APPLICATION SESSION — NON-AGENTIC VERSION

**Target file:** `sessions/client_application.md`

**Key point:** The non-agentic version is **three Python scripts and
two JSON files**. No web framework, no database. Students run each
script in sequence in the terminal.

- [ ] **Step 4.1: Audit `sessions/client_application.md`**
  - If the exercise specifies React + FastAPI + MongoDB: update to
    pure Python + flat files for the non-agentic version. The full
    web stack moves to Phase 5 where agents earn it.
  - The Hello World SDD demo must remain intact

- [ ] **Step 4.2: Add opening backward reference**
  - Open with:
    > "In the Slides session you pitched a one-shot meetup
    > coordinator. In the Web Site session you built a toy UI
    > with a fake Notifier. This session builds the real system:
    > three Python scripts that run, with a Discord message you
    > can see arrive in the channel the instructor provisioned."

- [ ] **Step 4.3: Add instructor-provisioned Discord setup block**
  - Students do not create the Discord channel — the instructor
    already did this (see `sessions/instructor.md`)
  - Students only need to set the env var and run the test:
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

- [ ] **Step 4.4: Write the exercise section**
  - SDD workflow for each of the three scripts:
    1. Write spec (Claude Code interviews you via plan.md)
    2. Review spec
    3. Generate: `claude -p "$(cat spec.md)" --allowedTools Write`
    4. Run and validate
    5. Iterate one component at a time
  - Validation sequence:
    1. `python poller.py` → enter responses for each member
    2. Check `responses.json` is correct
    3. `python selector.py` → check `decision.json`
    4. `python notifier.py` → confirm Discord message arrives
  - Pluggability note (appears here only)
  - Reflection: "What would need to change to make this agentic?"

- [ ] **Step 4.5: Confirm `sdd_basics.md` link resolves**

---

## Phase 5: CLIENT WORKFLOW SESSION — AGENTIC VERSIONS

**Target file:** `sessions/client_work_automation.md`

**Stack upgrade note:** FastAPI + MongoDB are introduced here.
Agents need an HTTP interface (async poll responses) and state that
survives between restarts. Add one paragraph explaining this
transition before the exercise.

### Step 5A: Single-Agent Version

- [ ] **Step 5.1: Add single-agent exercise**
  - Opening: "You ran three scripts sequentially. Now one OpenClaw
    agent plans and executes all three steps."
  - Stack upgrade paragraph (as above)
  - Validation: Discord receives the same message as the non-agentic
    version — same output, new execution model
  - Reflection: "What did the agent do that the scripts could not?"

### Step 5B: Multi-Agent Version

- [ ] **Step 5.2: Add multi-agent exercise**
  - Three agents: Poller Agent, Selector Agent, Notifier Agent
  - Shared state via MongoDB
  - Failure injection: stop Selector Agent mid-run; Notifier must
    not fire
  - Reflection: "What coordination problem did we create?" (seeds
    Temporal)

- [ ] **Step 5.3: Add forward reference to multi-agent session**

---

## Phase 6: MULTI-AGENT WORKFLOWS SESSION — TEMPORAL + DOCKER

**Target file:** `sessions/client_multiagent.md`

### Step 6A: Three Agents + Temporal on Laptop

- [ ] **Step 6.1: Add Temporal orchestration exercise**
  - PollActivity → SelectActivity → NotifyActivity
  - NotifyActivity calls same Discord webhook — no change
  - Failure injection: kill SelectActivity, observe Temporal retry
  - Reflection: "What did Temporal give us that OpenClaw alone
    could not?"

### Step 6B: Deploy to Server via Docker

- [ ] **Step 6.2: Add Docker deployment exercise**
  - Five containers: poller, selector, notifier, temporal, mongo
  - `DISCORD_WEBHOOK_URL` injected via docker-compose.yml
  - Claude Code generates all Dockerfiles and docker-compose.yml
  - Validation: `docker compose up`, submit a poll, confirm Discord
    message arrives from the deployed stack

---

## Phase 7: FINAL REVIEW AND CONSISTENCY CHECK

**Target files:** All modified files plus `README.md`.

- [ ] **Step 7.1: Verify instructor.md is complete and accurate**
  - All six sections present with working validation commands
  - The smoke test (run all three scripts end-to-end) is the
    last step in the preflight checklist
  - `README.md` lists instructor.md as the first agenda entry

- [ ] **Step 7.2: Verify project description is consistent**
  - "One-shot meetup coordinator" appears in every session that
    describes the project — no session calls it recurring, SaaS,
    or multi-tenant
  - No session mentions self-onboarding, recurring scheduling,
    calendar invites, or cancellation flows

- [ ] **Step 7.3: Verify the arc is explicit end-to-end**
  - Every session states which version it builds and what was
    missing in the previous one
  - Every session (except the last) ends with a forward reference

- [ ] **Step 7.4: Verify notification platform is consistent**
  - Discord webhook in every session from Phase 4 onward
  - Pluggability note appears once only (Phase 4)

- [ ] **Step 7.5: Verify `README.md` agenda order:**
  0. Instructor Preflight (new, first row)
  1. Planning
  2. Slides / Gamma
  3. Web Site / Lovable
  4. Client Application / SDD
  5. Client Workflow Automation
  6. Multi-Agent Workflows

- [ ] **Step 7.6: Verify `event_organizer.md` is single source**
  - No session redefines the component contracts inline
  - No SaaS features survive in the spec

- [ ] **Step 7.7: Confirm all links resolve**
  - `grep -r "\[.*\](.*\.md)" sessions/ plans/` and spot-check

- [ ] **Step 7.8: Save completion note**

---

## Verification Criteria

* Any CS graduate can read `sessions/instructor.md` and run the
  preflight checklist without asking for help
* A student receives `config.yaml` and `DISCORD_WEBHOOK_URL` from
  the instructor and can run the non-agentic version in under 10
  minutes
* "One-shot meetup coordinator" — not "recurring SaaS product" —
  is the description every session uses
* The notification channel is the same Discord webhook from Phase 4
  through Phase 6 — no re-onboarding at any level
* Each toy version is visibly incomplete; the gap is named explicitly
* The stack grows exactly once (flat files → MongoDB at Phase 5)
  with a written explanation of why
* `event_organizer.md` answers "what and why"; session files answer
  "how and in what order"
* No session contains implementation details from a different scope
