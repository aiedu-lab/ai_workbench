# Web Site on Server

## Tools

* [Lovable](https://lovable.dev/) — AI website builder (login verified)
* [Claude Code CLI (API mode)](https://docs.claude.com/code/) — AI coding
  assistant via terminal
* [Claude Code VSCode Extension](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)
  — AI coding assistant inside IDE
* [Claude Desktop (Code)](https://claude.com/download) — AI coding assistant
  via desktop app

---

## Activities

* Demo: Lovable
* Demo: Claude Code CLI (API mode)
* Exercise: Build a web site using Lovable and Claude Code

---

## Demo

### Lovable

* Review [plan.md](https://github.com/asarcar/aiedulabhelloworld/blob/main/plan.md)
* Use [Lovable](https://app.lovable.dev/dashboard) to execute plan
* Reference web site: [Hello, World!](https://hello-aiedu.lovable.app/)

### Use Cases

* **Program Updates** — Dynamic and on-demand reporting
  * Pull data from varied sources — JIRA/GitHub (eng), Asana (product),
    Confluence (docs) or via Glean-MCP (cross-org), etc.
  * Extract data from program spreadsheets (Excel, Google Sheets, MS Project),
    project status reports (internal wiki, slides, emails), etc.
  * Present program status, risks, dependencies in a structured format to
    various levels of stakeholders — execs, VPs, managers, etc.
* **Internal Announcements**
* **Marketing** — PR, blogs
* **Education** — course delivery, testing, etc.

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

## Installing Claude Code

### Prerequisites

```bash
# Verify Node.js version (18+ required)
node --version

# Verify npm
npm --version
```

If Node.js is not installed, download from [nodejs.org](https://nodejs.org)
(choose LTS). Windows users must use WSL2.

### Step 1 — Install the CLI globally

```bash
npm install -g @anthropic-ai/claude-code
```

Verify:

```bash
claude --version
```

### Step 2 — Authenticate

```bash
claude
```

On first launch, Claude Code opens a browser for OAuth login using your
Anthropic account. Alternatively, for API key access:

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
```

### Step 3 — Install the VSCode Extension

1. Open VSCode
2. Press `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (Mac) to open
   Extensions
3. Search for **"Claude Code"** — install the extension published by
   **Anthropic** (2M+ installs, verified publisher)
4. Restart VSCode if prompted

Once installed:

* Click the **Spark (⚡) icon** in the left Activity Bar to open the
  Claude Code sidebar
* The same icon appears in the top-right Editor Toolbar when a file is open
* Inline diffs appear in real time — use **Accept / Reject** buttons per change
* Open multiple conversations in separate tabs via the Sessions list

To keep the sidebar open across restarts, add to your VSCode `settings.json`:

```json
{
  "auto-run-command.rules": [
    {
      "condition": "always",
      "command": "claude-vscode.sidebar.open"
    }
  ]
}
```

Or set a keyboard shortcut: `Cmd+Shift+I` (Mac) / `Ctrl+Shift+I` (Windows).

### Step 4 — Confirm the integrated terminal works

In VSCode's integrated terminal (`Ctrl+\``):

```bash
claude -p "say hello" 
```

You should see a response. The CLI and the extension share the same
authentication and settings.

---

## When to Use CLI vs VSCode Extension vs Desktop

| Project Type | Recommended Route | Why |
|---|---|---|
| **Simple** — single file, quick fix, scripted output | **CLI** | Fastest; pipe output directly; scriptable |
| **Medium** — multi-file feature, incremental changes | **VSCode Extension** | Inline diffs, accept/reject per change, file navigation sidebar |
| **Complex** — large refactor, migration, multi-agent | **VSCode Extension + CLI** | Extension for review; CLI for automation, hooks, and scripting |
| **Non-technical user, rapid prototype** | **Claude Desktop (Chat)** | No terminal required; conversational interface |
| **CI/CD pipeline / automation** | **CLI with `-p` flag** | Non-interactive, scriptable, redirect-friendly |

**Rule of thumb:**

* Writing a new file from a prompt → **CLI**
* Reviewing and editing existing code → **VSCode Extension**
* Planning a large change before executing → **Desktop (Chat)** or
  Extension Plan Mode (`Shift+Tab` twice)

---

## Exercise: Build a Web Site

Agree on a project with your team, for example:

```bash
Intent: Build a web site for students that know basic programming
        to learn about AI.
```

Then plan and execute using Claude Desktop or Claude Code.

### Hands-On Steps

**Step 1 — Write a plan:**

```bash
# In your project directory
cat > plan.md << 'EOF'
# Hello World App Plan

## Task
Create a minimal static webpage demonstrating a Hello World app.

## Files
- index.html only

## Features
- Display "Hello, World!" on load
- Textbox for a name + Submit button
- Submitting changes display to "Hello, <name>!"
- Empty submit reverts to "Hello, World!"

## Constraints
- No frameworks — plain HTML, CSS, JS only
- Single index.html file
- Add WHY comments on non-obvious blocks
- All code in this directory only

## Output
Output only raw file contents of index.html — no explanation, no fences.
EOF
```

**Step 2 — Generate with Claude Code:**

```bash
claude -p "$(cat plan.md)" --allowedTools "Write" > /dev/null
```

**Step 3 — Validate:**

```bash
head -1 index.html   # must be <!DOCTYPE html>
python3 -m http.server 8888
# open http://localhost:8888
```

**Step 4 — Incremental change (add name history):**

```bash
PROMPT="Add a scrollable history list below the submit button in index.html.
- Keep all changes inside index.html only
- Append each submitted name to a <ul id='history'> element
- Style consistently with existing look
- Add a comment explaining WHY history is stored in-memory not localStorage
Output only the modified file."

claude -p "$PROMPT" --allowedTools "Write" > /dev/null
```

Review the diff before accepting:

```bash
git diff index.html
```

**Step 5 — Validate the change:**

Refresh `http://localhost:8888`, submit several names, verify history appears.

---

## Key Takeaways

* Compare "writing code" vs "managing specs"
* How to handle incremental changes?
* Areas where "generated" content is poor?

---

## Code Migration and Working on Existing Code

### The Core Principle: Explore → Plan → Code → Commit

Never ask Claude Code to modify existing code without first understanding it.
The pattern that works:

```bash
# Step 1: Explore only — no edits yet
claude "Read through index.html and explain what each section does.
Do NOT write any code yet."

# Step 2: Plan
claude "Based on your analysis, propose a step-by-step plan to add
input validation. List each file change needed."

# Step 3: Execute one step at a time
claude -p "Execute only Step 1 of the plan." --allowedTools "Write" > /dev/null

# Step 4: Review diff and commit before next step
git diff
git add -p
git commit -m "step 1: add input validation skeleton"
```

### Legacy to Modern: Migration Workflow

Claude Code can modernize old codebases systematically. The proven approach
is the **Strangler Fig Pattern** — replace pieces incrementally while keeping
the system running:

```bash
# Phase 1: Understand what you have
claude "Analyze this codebase. Document:
1. What each file does
2. All dependencies between files
3. Any hardcoded values that should be config
4. Any patterns that are outdated or unsafe
Do NOT change anything yet."

# Phase 2: Generate a migration plan
claude "Based on the analysis, create a phased migration plan.
Phase 1: Add test harness around critical paths
Phase 2: Extract config from hardcoded values
Phase 3: Replace [legacy pattern] with [modern equivalent]
For each phase, list exact file-level changes and rollback steps."

# Phase 3: Execute phase by phase with validation
claude -p "Execute Phase 1 only. 
Create test files that verify current behavior before any changes."
--allowedTools "Write,Bash" > /dev/null

# Run tests to establish baseline
python3 -m pytest tests/

# Phase 4: Execute next phase, re-run tests, commit
```

### Hybrid Code: Manually Written + AI Generated

When a codebase is partially hand-written and partially AI-generated via
`CLAUDE.md` and `plan.md`, use these rules to keep it coherent:

**Rule 1 — Mark sections clearly in comments:**

```html
<!-- === MANUAL: core layout — do not regenerate === -->
<header>...</header>

<!-- === AI-GENERATED: history feature v2 — see plan_history.md === -->
<ul id="history">...</ul>
```

**Rule 2 — Use CLAUDE.md to fence what Claude can and cannot touch:**

```markdown
# CLAUDE.md

## Do NOT Touch
- The <header> section in index.html — manually maintained
- Any file outside this directory

## Safe to Modify
- The #history section and its CSS
- JavaScript functions prefixed with `ai_`

## Incremental Change Protocol
1. Always read the existing file before proposing changes
2. Propose a diff, do not overwrite
3. Add a comment citing which plan.md step generated the change
```

**Rule 3 — One plan.md per feature, not one monolithic plan:**

```
projects/web_site/hello_world_claudeCLI/
  plan.md                  ← original app
  plan_history.md          ← history feature
  plan_validation.md       ← input validation
  index.html
  CLAUDE.md
```

Each plan.md targets specific sections. Claude reads CLAUDE.md first, so
it knows not to touch other sections.

**Rule 4 — Always diff before accepting:**

```bash
# In VSCode Extension: use inline Accept/Reject per change
# In CLI: always check git diff before committing
git diff index.html
git add -p    # stage interactively, hunk by hunk
```

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
PROMPT="Add a scrollable history list below the submit button in index.html.
- Keep all changes inside index.html only
- Append each submitted name to a <ul id='history'> element
- Style to match existing look
- Add a comment explaining WHY history is stored in-memory not localStorage
Output only the modified file."

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

## Additional Benefits of Claude Code: CLAUDE.md Guardrails

`CLAUDE.md` is a markdown file in the project root that Claude Code reads
automatically at the start of every session. It acts as persistent operating
instructions — a "project README for the AI agent." Reference
[CLAUDE.md for hello_world_app](../projects/web_site/hello_world_claudeCLI/CLAUDE.md).

**Example CLAUDE.md for this project:**

```markdown
# CLAUDE.md — Hello World App

## Project Rules
- Single file app: ALL code must stay in index.html
- No frameworks, no external libraries, no CDN imports
- Do not create files outside this directory

## Coding Standards
- Add WHY comments on every non-obvious block
- Use semantic HTML (label, section, etc.)
- CSS variables for all colors

## Do NOT Touch
- plan.md
- The <header> block — manually maintained
- Any file outside projects/web_site/hello_world_claudeCLI/

## Safe to Modify
- The #history section and its CSS
- JavaScript functions prefixed with ai_

## Test Command
python3 -m http.server 8888  # then open http://localhost:8888
```

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

```markdown
## Safety Rules
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

### Claude Code pricing paths (April 2026)

| Path | Cost | Best for |
|---|---|---|
| Free tier | $0 | Try it out, very light use |
| Pro (monthly) | $20/month | Students, moderate use |
| Pro (annual) | $17/month ($200/year) | Save 15% vs monthly |
| Max 5x | $100/month | Daily heavy use |
| Max 20x | $200/month | Power users, large codebases |
| API pay-as-you-go | $3/$15 per MTok (Sonnet 4.6) | Scripting, occasional use |

**Model cost comparison (API):**

| Model | Input | Output | Best use |
|---|---|---|---|
| Haiku 4.5 | $1/MTok | $5/MTok | Simple lookups, subagents |
| Sonnet 4.6 | $3/MTok | $15/MTok | Most coding tasks (default) |
| Opus 4.6 | $5/MTok | $25/MTok | Complex multi-file work only |

### Student and education discounts

* **Anthropic Education Plan** — Free Claude Pro access for students, faculty,
  and staff at partner universities (includes Northeastern, LSE, and others).
  Check with your institution's IT department or student services.
  If enrolled: sign in at `claude.ai` with your school email — access is
  automatic if your university has a partnership.
* **Annual billing** — 15% savings vs monthly ($200/year vs $240/year for Pro)
* **Promotional credits** — Anthropic occasionally offers credits when new
  models launch; monitor `claude.ai` Settings → Usage for active offers
* **No individual student discount codes exist** — any coupon codes on
  third-party sites are fake; Anthropic's help center confirms this explicitly

### Top 8 cost-saving practices

1. **Use Sonnet for 80% of tasks** — reserve Opus only for complex
   multi-file architecture decisions
2. **Use `/clear` between unrelated tasks** — accumulated context wastes
   tokens and degrades output quality
3. **Use Plan Mode first** (`Shift+Tab` twice in Extension, or ask Claude to
   plan before coding) — prevents expensive re-dos
4. **Keep CLAUDE.md concise** (100–200 lines max) — it is loaded every
   session; bloated CLAUDE.md burns tokens before a single line is written
5. **Batch small changes into one prompt** — one session with 5 changes
   costs far less than 5 separate sessions
6. **Use `-p` flag for scripts** — non-interactive mode exits after one
   response; no idle session overhead
7. **Prompt cache reuse** — for repeated large-context tasks, caching
   cuts input costs by up to 90% automatically
8. **Set `--max-turns`** in automated scripts — prevents runaway agent
   loops from burning tokens

### Cost sanity check for the lab

A typical student session building the Hello World app:

* Single file generation: ~5,000 tokens ≈ $0.015 at Sonnet rates
* Incremental change + review: ~3,000 tokens ≈ $0.009
* Full exercise end-to-end: well under $0.10

For the lab exercises, API pay-as-you-go is the most economical path for
students who are not heavy daily users.

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
* [Plan Draft for Event Organizer](../plans/draft/event_organizer.md)

---

## Output

* [Plan](https://github.com/asarcar/aiedulabhelloworld/blob/main/plan.md)
* [Notes](../learnings/session_notes/web_site.md)
