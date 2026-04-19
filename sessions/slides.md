
## Slides

### Objective
Learn how to use AI to create compelling communication and storytelling artifacts:
- slides
- structured narratives
- visual storytelling

### Tools
- [Gamma](https://gamma.app) — AI presentation tool

### Setup

#### Install / Start
- Gamma is browser-based — no local install required.
- Navigate to [gamma.app](https://gamma.app) and sign in with Google
  or your email.
- First-time users: create a free account (no credit card needed).
- **Login verification:** confirm you can reach your Gamma dashboard
  before the exercise begins.

#### Student / Team Discount
- Students with a `.edu` email: apply for free Pro access at
  `gamma.app/education`.
- Teams: one shared Pro workspace is sufficient for classroom demos.

#### Guardrails
- Do not enter personal data, student names, or private school
  information into prompts.
- Treat all AI-generated content as a draft — verify facts before
  presenting.
- Gamma stores decks in the cloud; avoid uploading sensitive material.

#### Tokenomics
- Gamma uses an internal credit system (not API tokens).
- Free tier: ~400 AI credits/month — sufficient for 2–3 full decks.
- To conserve credits: iterate on one deck rather than regenerating
  from scratch; prefer **Edit** over **Regenerate**.

### Concept
Prompting for communication:
- clarity > verbosity
- structure > raw ideas

### Demo (Instructor-Led)

The instructor builds the AI Education Lab pitch deck live in Gamma.
Students watch AI generate the deck in real time — that IS the demo.

- Prompt plan: [`projects/slides/demo/plan.md`](../projects/slides/demo/plan.md)
- Time: 10 min generate + 5 min edit iteration
- Key moment: show **Edit** (not Regenerate) to change one bullet —
  demonstrates cost-efficient iteration

### Exercise A — "How AI Agents Work" (Individual)

```bash
Explain "How AI agents work"
```

#### Prompt
- [Poor Prompt](../prompts/poor.md###Slides####Basic)
  - messy structure
  - too verbose
  - inconsistent slides
- [Improved Prompt](../prompts/poor.md###Slides####Improved)
  - easier to understand
  - improves story telling
- [Structured Prompt](../prompts/best.md###Slides####Better)
  - scoped  → clean 5-slide deck
  - constrained → clear structure
  - simple domain → understandable explanation
- [Failure Injected Prompt](../prompts/failures.md###Slides)
  - Give vague prompt → observe poor structure
  - Inundate data → slides become cluttered & violates "one idea per slide"
  - Over-specify → observe rigidity

#### Validation
After generating your deck, verify each item before moving on:
- [ ] Exactly 5 slides generated (no more, no fewer)
- [ ] Each slide has exactly one central idea
- [ ] Title slide states the topic clearly
- [ ] No slide exceeds 3 bullet points
- [ ] Spot-checked 2 factual claims — no hallucinations found
- [ ] Visual theme is consistent across all slides
- [ ] You can explain every slide in your own words without reading it

### Exercise B — Group Meetup Organizer Pitch Deck (toy version 0)

**Audience:** a student club committee deciding whether to adopt
this system.

**Your task:** build a stakeholder pitch deck in Gamma for the
Group Meetup Organizer. Use this structure:

| Slide | Title | Content |
|-------|-------|---------|
| 1 | The Problem | Group coordination is painful — threads, no-shows, venue chaos |
| 2 | The Solution | Three steps: Poll → Select → Notify via Discord |
| 3 | How It Works | Poller asks each member; Selector picks best date + venue; Notifier sends Discord message |
| 4 | What Success Looks Like | One message in Discord: date, venue, attendees — done |
| 5 | What We Need From You | Approve the system so we can build it next session |

**Constraints:**
- Exactly 5 slides, one idea per slide, max 3 bullets per slide
- No code, no implementation details — concept only
- The Notifier sends a Discord message (not email, not calendar)

> **Gap statement:** We have a pitch. We have no working system.
> In the Web Site session we build a first version of the UI —
> and see exactly what is still missing.

### Reflection
  - What made the good version better?
  - Which constraint mattered most?
  - Where did AI overcomplicate?

### Output
- [Plan](../projects/slides/plan.md)
- [Notes](../learnings/session_notes/slides.md)
