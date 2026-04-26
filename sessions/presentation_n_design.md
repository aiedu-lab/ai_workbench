
## Presentation & Design

### Objective

Learn how to use AI to create compelling communication and visual
artifacts — from structured slide decks to interactive UI mockups:
- slides and structured narratives
- visual storytelling with Gamma
- interactive UI prototypes and branded decks with Claude Design

### Tools

- [Gamma](https://gamma.app) — AI presentation tool (content
  structure from prompts)
- [Claude Design](https://claude.ai/design) — visual design engine
  (interactive UI mockups and branded decks; requires Claude Pro)

### Setup

#### Gamma — Install / Start

- Gamma is browser-based — no local install required.
- Navigate to [gamma.app](https://gamma.app) and sign in with Google
  or your email.
- First-time users: create a free account (no credit card needed).
- **Login verification:** confirm you can reach your Gamma dashboard
  before the exercise begins.

#### Gamma — Student / Team Discount

- Students with a `.edu` email: apply for free Pro access at
  `gamma.app/education`.
- Teams: one shared Pro workspace is sufficient for classroom demos.

#### Gamma — Guardrails

- Do not enter personal data, student names, or private school
  information into prompts.
- Treat all AI-generated content as a draft — verify facts before
  presenting.
- Gamma stores decks in the cloud; avoid uploading sensitive material.

#### Gamma — Tokenomics

- Gamma uses an internal credit system (not API tokens).
- Free tier: ~400 AI credits/month — sufficient for 2–3 full decks.
- To conserve credits: iterate on one deck rather than regenerating
  from scratch; prefer **Edit** over **Regenerate**.

#### Claude Design — Setup

- Claude Design runs at [claude.ai/design](https://claude.ai/design)
  — no local install required.
- Requires a **Claude Pro** subscription (or Claude Max).
- Sign in with your claude.ai account — see
  [Claude Cloud Setup](../tools/claude/cloud.md).
- **Login verification:** confirm you can open a new project at
  `claude.ai/design` before the exercise begins.

### Concept: Prompting for Communication (Gamma)

Prompting for slides and narratives:
- clarity > verbosity
- structure > raw ideas

### Concept: What Is Claude Design?

In previous sessions, AI returned text and code. Claude Design is
different — it returns **rendered, interactive visual artifacts**
powered by Claude Opus 4.7:

- **For developers:** functional frontend prototypes — buttons that
  click, sliders that move — ready to hand off to a codebase via
  **Send to Claude Code**.
- **For presenters:** formatted, multi-slide pitch decks (HTML, PPTX,
  or Canva exports) generated from a plain-language outline.

**Specification Driven Presentation (SDP):** Gamma and Claude Design
are both prompt-driven. The spec is your outline or brief; the AI
generates the artifact. They differ in output:

> Gamma = content structure. Claude Design = visual design.
> A polished production presentation benefits from both.

### Demo (Instructor-Led)

The instructor builds the AI Workbench pitch deck live in Gamma.
Students watch AI generate the deck in real time — that IS the demo.

- Prompt plan: [`projects/slides/demo/plan.md`](../projects/slides/demo/plan.md)
- Time: 10 min generate + 5 min edit iteration
- Key moment: show **Edit** (not Regenerate) to change one bullet —
  demonstrates cost-efficient iteration

### Exercise A — "How AI Agents Work" (Individual, Gamma)

```markdown
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
  - scoped → clean 5-slide deck
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

### Exercise B — Group Meetup Organizer Pitch Deck (toy version 0, Gamma)

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

### Exercise C — Interactive UI Prototype (Claude Design)

**Scenario:** you have written backend logic for a physics
calculator and need a beautiful interface.

#### Step 1: Generate the mockup

Go to [claude.ai/design](https://claude.ai/design) and start a new
project. Use this prompt:

```markdown
Scenario: I need a mobile app UI prototype for a high school physics
tool called 'Newton's Apple'. The main screen should have:
1. A clean, dark-mode aesthetic with neon green accents.
2. Three interactive input sliders for Mass (kg), Acceleration (m/s²),
   and Time (s).
3. A large, stylized 'Calculate Force' button.
4. A display area for the result that updates dynamically.

Make the layout modern, with plenty of whitespace, and ensure the
UI feels tactile.
```

#### Step 2: Refine with point-and-edit

1. Click the **Calculate Force** button in the generated preview.
2. Prompt: `Make this button look like a glowing 3D pill.`
3. Test the sliders — they are interactive in the preview.

#### Step 3: Handoff to code

Click **Send to Claude Code** — this packages the HTML/CSS/JS so
the Claude Code CLI can inject it directly into a Git repo.

#### Validation

- [ ] Prototype renders with dark-mode aesthetic and neon accents
- [ ] Three sliders are present and interactive
- [ ] Point-and-edit refinement changed the button style
- [ ] **Send to Claude Code** option is visible in the export menu

### Exercise D — Branded Pitch Deck (Claude Design)

**Scenario:** pitch Newton's Apple to a panel of judges in 10 min.

#### Step 1: Build the skeleton first

Never ask AI to "make a presentation" all at once. Outline first:

```markdown
I need a 5-slide pitch deck for my app 'Newton's Apple'. The
audience is a high school science department. Outline the 5 slides
first.
```

#### Step 2: Generate the full deck

Once Claude provides the outline:

```markdown
Perfect. Now build the full deck. Use a bold, high-contrast design:
dark navy backgrounds, white text, and orange accents. Add a subtle
fade transition between the slides. On the 'Market' slide, include
an animated donut chart showing student engagement.
```

#### Step 3: Export

The output is a browser-based interactive presentation.

1. Click the **Export** menu.
2. Choose **Canva** (add custom graphics) or **PPTX** (PowerPoint).

#### Validation

- [ ] 5-slide deck generated from the outline
- [ ] Dark navy + white + orange design applied
- [ ] Animated donut chart appears on the Market slide
- [ ] Export to PPTX or Canva succeeds

### Key Takeaways (Claude Design)

1. **Design systems matter:** Claude Design can ingest a brand
   document and apply those colors and fonts to everything it builds.
2. **Interactive over static:** always request interactive components
   (charts, sliders) rather than static images.
3. **The AI assembly line:** Claude Design for the *look*; Claude
   Code for the *logic*.

### Reflection

- What made the structured Gamma prompt better than the vague one?
- Which constraint mattered most in Exercise B?
- When would you use Claude Design instead of Gamma?
- Where did AI overcomplicate — and how did you fix it?

### Output

- [Plan](../projects/slides/plan.md)
- [Notes](../learnings/session_notes/presentation_n_design.md)

---

## What Is Missing → Web Site Session

The pitch deck describes the system but builds nothing. The next
session creates a real UI in Lovable — a poll form and a result
page — and makes explicit what a working backend would need to do.

**Next session:** [Create/Run Web Site](web_site.md)
