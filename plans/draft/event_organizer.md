# Group Meetup Organizer — Project Spec

## What This Is

A **one-shot meetup coordinator** for a fixed group. Given a list of
members, available dates, and venue options, it:

1. Polls each member: "Are you free? What venue do you prefer?"
2. Selects the venue that the most free members prefer
3. Notifies the group via a Discord message

The application runs once per meetup. A human (the organizer)
triggers it when they want to schedule a meetup.

## What This Is NOT

- Not a recurring scheduler or cron job
- Not a SaaS product with user registration or authentication
- Not a multi-tenant system with events, subscriptions, or regions
- Not an email sender or calendar invite system
- Not a cancellation or rescheduling workflow

These are real product features that would be built on top of this
architecture. They are not part of the lab.

---

## Data Model

**`config.yaml`** — the only configuration interface. Set by the
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

**`responses.json`** — written by the Poller, read by the Selector.

```json
{
  "Alice":  {"available": true,  "venue": "Library Room A"},
  "Bob":    {"available": true,  "venue": "Coffee Lab on Castro"},
  "Carol":  {"available": false, "venue": null},
  "David":  {"available": true,  "venue": "Library Room A"}
}
```

**`decision.json`** — written by the Selector, read by the Notifier.

```json
{
  "date": "Thu Apr 24 7pm",
  "venue": "Library Room A",
  "attendees": ["Alice", "Bob", "David"]
}
```

---

## Selection Logic

- **Date:** the date where the most members are available
- **Venue:** the venue preferred by the most available members
- **Tie-breaking:** alphabetical order (deterministic, no randomness)
- **Cancelled:** if zero members are available, write
  `{"cancelled": true}` to `decision.json`; the Notifier sends a
  cancellation message

---

## The Three Scripts

```
python poller.py    # reads config.yaml, collects responses,
                    # writes responses.json
python selector.py  # reads responses.json, picks date + venue,
                    # writes decision.json
python notifier.py  # reads decision.json, POSTs to Discord webhook
```

---

## Scope Decisions (Locked)

| Decision | Choice | Reason |
|----------|--------|--------|
| Group size | Fixed, from `config.yaml` | No auth needed; instructor sets roster |
| Notification | Discord webhook only | Minimal setup — no token, no bot, just a URL |
| Storage | Flat files (non-agentic) | Architecture visible, zero framework noise |
| Stack growth | Only when complexity earns it | See session arc below |

---

## Notification Platform

**Discord via Webhook. No alternatives.**

| Platform | Setup cost | Lab-viable? |
|----------|------------|-------------|
| Email (SMTP) | Medium — app passwords, spam filters | ⚠️ Borderline |
| WhatsApp (Twilio) | High — WABA, template approval | ❌ No |
| Discord Bot | Medium — token, Intents, async | ⚠️ Borderline |
| **Discord Webhook** | **Minimal — just a URL** | **✅ Yes** |

The Notifier is a pluggable component. Swapping Discord for email
(SendGrid), SMS (Twilio), or Slack (Slack webhooks) requires
changing only `notifier.py`. The Poller and Selector are unaffected.

---

## Session Arc

| Session | Version | What it demonstrates |
|---------|---------|----------------------|
| Planning | Concept only | Plan the app in plain language |
| Slides (Gamma) | Pitch deck (toy v0) | Stakeholder presentation — no code |
| Web Site (Lovable) | Poll UI (toy v1) | Real UI, fake backend, hardcoded result |
| Client Application | 3 Python scripts | Real system — real Discord notification |
| Client Workflow | Single agent (OpenClaw) | One agent runs all three steps |
| Multi-Agent | 3 agents + Temporal | Durable, retryable pipeline |
| Server Deploy | Docker stack | Deployed on a real server |

Each version is visibly incomplete; the gap is named explicitly so
students understand why the next session's technology is needed.
