# Web Site

## Tools

* [Lovable (SaaS)](https://lovable.dev/) - AI website builder (login verified)

Reference links includes set up and installation instructions:
* [Claude Code CLI (API mode)](../tools/claude/cli.md) - AI coding assistant:
* [Claude Desktop (Code)](../tools/claude/desktop.md) - AI coding assistant

---

## Activities
* Demo: Lovable (SaaS)
* Demo: Claude Code CLI (API mode)
* Exercise: Build a web site using Lovable and Claude Code

---

## Demo

### Lovable

* Review [plan.md](https://github.com/asarcar/aiedulabhelloworld/blob/main/plan.md)
* Use [Lovable](https://app.lovable.dev/dashboard) to execute plan.
* Reference web site: [Hello, World!](https://hello-aiedu.lovable.app/)

### Use cases
* **Program Updates** - Dynamic and on-demand reporting
  * Pull data from varied sources - JIRA/GitHub (eng), Asana (product), 
    Confluence (docs) or via Glean-MCP (cross-org), etc.
  * Extract data from program spread sheets (excel, google sheets, MS project plan), 
    project status reports (internal wiki, slides, emails), etc.
  * Present program status, risks, dependencies, etc. in a structured format to 
    various level of stake holders - execs, VPs, managers, etc.
* **Internal Announcements**
* **Marketing** - PR, blogs
* **Education** - course delivery, testing, etc.

---

### Claude Code CLI (API mode)

* Review [plan.md](../projects/web_site/hello_world_claudeCLI/plan.md)
* Change to project subdirectory:

```bash
export REPO_ROOT=...
cd $REPO_ROOT/projects/web_site/hello_world_claudeCLI
```

* Use Claude Code CLI to execute plan:

```bash
# Discard console output — Claude writes the file directly
claude -p "$(cat plan.md)" --allowedTools "Write" > /dev/null
```

* Start local web service to preview:

```bash
python3 -m http.server 8888
```

* Validate: open `http://localhost:8888` in browser

---

## Exercise: Build a Web Site

Agree on a project with your team, for example:

```bash
Intent: Build a web site for students that know basic programming
        to learn about AI.
```

Then plan and execute using Claude Desktop or Claude Code.

### Hands-On Steps

1. Write a plan:
[plan.md](../projects/web_site/hello_world_claudeCLI/plan.md)

2. Generate with Claude Code:

```bash
claude -p "$(cat plan.md)" --allowedTools "Write" > /dev/null
```

3. Validate:

```bash
head -1 index.html   # must be <!DOCTYPE html>
python3 -m http.server 8888
# open http://localhost:8888, submit names, verify page
```

---

## Exercise B — Group Meetup Organizer Poll UI (toy version 1)

Build a poll UI for the Group Meetup Organizer in Lovable. This is
a toy version — real UI, fake backend.

### What to build

**Poll form:**
- Member name (text input)
- 3 date checkboxes (use dates from `config.yaml`)
- Venue preference (radio buttons: Library Room A, Coffee Lab, Online)
- Submit button

**Result page (hardcoded — no real logic):**
- Display: "📅 Meetup confirmed! Thu Apr 24 7pm — Library Room A"
- Display: "✓ Notification sent to Discord"
- No actual webhook call — this is display only

### Lovable prompt

```
Build a one-page meetup poll app.

Page 1 — Poll form:
- Text input: "Your name"
- 3 checkboxes: "Thu Apr 24 7pm", "Thu May 1 7pm", "Thu May 8 7pm"
- Radio buttons: "Library Room A", "Coffee Lab", "Online / Video Call"
- Submit button: "Submit Response"

Page 2 — Result (shown after submit, hardcoded):
- Heading: "📅 Meetup confirmed!"
- Line: "Date: Thu Apr 24 7pm"
- Line: "Venue: Library Room A"
- Line: "✓ Notification sent to Discord"

Constraint: no backend, no database, no API calls.
Style: clean, mobile-friendly.
```

### Explicit omissions (state these to students)

- No Selector algorithm — the result is hardcoded
- No Discord webhook call — "✓ Notification sent" is a lie
- No persistence — data disappears on refresh

> **Gap statement:** The Selector has no logic. The Notifier sends
> nothing. Data disappears on refresh. We have a UI but not an
> application. In the Client Application session we build the real
> system — three Python scripts that actually run.

---

## Key Takeaways

* Compare "writing code" vs "managing specs"
* Areas where "generated" content is poor?

---

## Reflection: Claude Code vs Lovable — Deep Comparison

### Incremental Changes: History Textbox Example

**The scenario:** Add a history textbox that shows previously submitted names.

#### Lovable approach

* Type the request in chat:

```bash
Add a scrollable history box below the submit button
that lists all previously entered names
```

* Lovable generates the change, live-previews it instantly in the browser
* No terminal, no file management, no manual browser refresh
* **Aesthetic control:** High — Lovable applies consistent styling from the
  existing design system automatically
* **Test/validation:** None built-in — Lovable has no test runner; you eyeball
  the live preview
* **Time to working UI:** ~30 seconds
* **Risk:** You cannot easily constrain what Lovable touches — it may
  rewrite surrounding components

#### Claude Code CLI approach

```bash
PROMPT="
Add a scrollable history list below the submit button in index.html.
- Keep all changes inside index.html only
- Append each submitted name to a <ul id='history'> element
- Style to match existing look
- Add a comment explaining WHY history is stored in-memory not localStorage
Output only the modified file.
"

claude -p "$PROMPT" --allowedTools "Write" > /dev/null
```

* Full control over exactly which files are touched
* Can mandate comments, naming conventions, coding style via the prompt
* Test by running `python3 -m http.server 8888` and opening browser
* Can add automated tests in the same prompt: *"also write test_index.js
  that validates the history appends correctly"*
* **Time to working UI:** ~1–2 minutes
* **Aesthetic control:** Depends on how explicit your prompt is — lower
  out-of-the-box than Lovable

#### Verdict

| Dimension | Lovable | Claude Code |
|---|---|---|
| Speed to working UI | ✅ Faster (seconds) | Slower (minutes) |
| Aesthetic consistency | ✅ Automatic | Requires explicit prompts |
| File/scope control | ❌ Opaque | ✅ Precise |
| Test generation | ❌ None built-in | ✅ Can generate in same pass |
| Validation | Visual only | ✅ Can run automated tests |
| Code transparency | ❌ Hidden | ✅ Full visibility |
| Incremental diff review | ❌ Hard | ✅ `diff` / `git diff` |
| Legacy migration | ❌ Not supported | ✅ Explore-Plan-Code-Commit |
| Hybrid code ownership | ❌ Opaque | ✅ CLAUDE.md fences sections |

**For simple visual changes:** Lovable wins on speed.
**For changes that need testing, constraints, code review, or migration:**
Claude Code wins.

---

### Additional Benefits of Claude Code: CLAUDE.md Guardrails

`CLAUDE.md` is a markdown file in the project root that Claude Code reads
automatically at the start of every session. It acts as persistent operating
instructions — a "project README for the AI agent."

[Example CLAUDE.md for hello_world_app](../projects/web_site/hello_world_claudeCLI/CLAUDE.md).

**Why this matters vs Lovable:**

* Lovable has no equivalent — its instructions live only in the chat and
  reset between sessions
* CLAUDE.md persists across every session, every team member, every CI run
* Can encode security rules (e.g., *"never hardcode API keys"*), architecture
  decisions, and "do not touch" zones
* Can be version-controlled alongside code — the guardrails evolve with
  the project
* Can include hooks for deterministic enforcement (e.g., block `rm -rf`,
  auto-run lint after every file write)

**Safety guardrails to add to any CLAUDE.md:**

## Safety Rules
```bash
- NEVER hardcode API keys, passwords, or secrets
- NEVER use rm -rf without explicit confirmation
- NEVER push directly to main branch
- ALWAYS add a WHY comment when deleting code
- ALWAYS run tests before declaring a task complete
```

---

## Lovable's SDLC Advantage — and the Claude Code Ecosystem Response

### What Lovable bundles out of the box

Lovable genuinely reduces SDLC burden beyond just code generation:

* **Hosting:** Built-in deployment at `*.lovable.app` — zero DevOps
* **Live preview:** Instant browser preview on every change
* **2-way GitHub sync:** Changes in Lovable push to GitHub; merges to main
  pull back automatically
* **No infrastructure management:** No server, no CI/CD pipeline to configure

This is a real advantage for non-engineers and rapid prototyping.

### Claude Code + ecosystem: matching Lovable's SDLC coverage

Claude Code is not alone — it has a growing ecosystem of companions that
together cover the full SDLC:

| SDLC Layer | Lovable | Claude Code Companion |
|---|---|---|
| Code generation | ✅ Built-in | ✅ Claude Code CLI |
| Hosting / deployment | ✅ lovable.app | **Vercel**, **Netlify**, **Railway** |
| CI/CD | ✅ Auto on merge | GitHub Actions (free) |
| Database | ✅ Supabase integration | **Supabase MCP**, Railway DB |
| Infrastructure mgmt | ✅ Zero-config | **Railway MCP** (natural language) |
| Preview deploys | ✅ Built-in | Vercel/Netlify PR previews |
| Monitoring | ❌ Limited | Vercel Analytics, DataDog |
| Security guardrails | ❌ None | CLAUDE.md + Hooks + Codacy MCP |
| Legacy migration | ❌ Not supported | ✅ Explore-Plan-Code-Commit |

**Key companions:**

* **Vercel** — `git push` → auto-deploy. Free tier, instant preview URLs per
  PR. Best for static/Next.js apps. Claude Code has a Vercel MCP plugin.
* **Netlify** — Similar to Vercel. Claude Code, Codex, and Gemini agents are
  accessible directly from the Netlify dashboard. Free tier available.
* **Railway** — Full-stack including databases (Postgres, Redis). Has a
  dedicated Claude Code plugin and MCP server:

```bash
claude mcp add railway-mcp-server -- npx -y @railway/mcp-server
```

  Then ask Claude: *"deploy this to Railway and check the logs"* — it handles
  the entire deploy workflow in natural language.

* **Supabase MCP** — Claude Code can read/write your database, run migrations,
  and manage auth directly from the terminal session.
* **GitHub Actions** — Free CI/CD. Claude Code can generate the workflow YAML.
  Standard pattern: push to branch → run tests → deploy to Vercel on merge.

### Summary: Which to choose?

| Scenario | Recommendation |
|---|---|
| Non-engineer, rapid prototype, no DevOps | **Lovable** |
| Engineer, need code control, testing, security | **Claude Code** |
| Want UI speed + code control | **Both** — Lovable for design, Claude Code for logic |
| Production app needing CI/CD, monitoring | **Claude Code + Vercel/Railway** |
| Teaching best practices (comments, tests, git) | **Claude Code** — full visibility |
| Legacy migration or hybrid codebase | **Claude Code only** |

**The honest comparison:** Lovable wins on *time to first demo*. Claude Code
wins on *long-term maintainability, testability, and control*. For an AI
Education Lab context, Claude Code is the better teaching tool because students
see and own every line of code — nothing is hidden behind a chat interface.

---

## Tokenomics and Cost Control

For Lovable (SaaS), reference the student programs for cost control:
* [Lovable Student Discount](https://lovable.dev/students)
  * “Learner” 50% Discount: for Pro subscription at $12.50/month. 

For Claude and any LLM-Provider API calls, reference the links below
for cost control:
* [Claude Cost Control](../tools/claude/cost_control.md)
* [Provider Cost Control](../tools/provider_cost_control.md)

---

## References

* [Lovable vs Replit](https://lovable.dev/guides/lovable-vs-replit-platform-comparison)
* [Anthropic Console (API Key & Limits)](https://platform.claude.com/)
* [Claude Code CLI Documentation](https://docs.claude.com/code/)
* [Claude Code Quickstart Guide](https://docs.claude.com/code/quickstart)
* [Claude Code VSCode Extension](https://code.claude.com/docs/en/vs-code)
* [Claude Code Common Workflows](https://code.claude.com/docs/en/common-workflows)
* [Claude Pricing](https://claude.com/pricing)
* [Anthropic Education Program](https://www.anthropic.com/education)
* [Plan Draft for Event Organizer](../plans/specs/event_organizer.md)

---

## Output
* [Plan](https://github.com/asarcar/aiedulabhelloworld/blob/main/plan.md)
* [Notes](../learnings/session_notes/web_site.md)

---

## What Is Missing → Client Application Session

The UI exists but the backend is hardcoded — the Discord webhook
is never called and no data is written. The next session replaces
the fake backend with three real Python scripts using SDD: a
Poller that collects responses, a Selector that picks the best
date and venue, and a Notifier that fires a real Discord message.

**Next session:** [Client Application / SDD](client_application.md)