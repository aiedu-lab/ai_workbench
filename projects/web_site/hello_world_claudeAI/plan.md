# Project Plan: Hello World App Claude AI

> **Maintenance Rule:** When a Phase is 100% complete, move its
> detailed steps to `docs/archive/phase_X.md` and replace it here
> with a one-line summary. Keep this file under 150 lines of active
> content — it is loaded into every Claude Code session and a bloated
> plan wastes context tokens.

---

## 🟢 Phase 1: Hello World Web App

*Status: In Progress | Target: 2026-05-01*

* [ ] **Step 1.1: Generate base app**
  * Context: Single-file index.html static webpage as a simple Hello World App
  * Implementation: `projects/web_site/hello_world_claudeai/index.html`
  * [ ] Display "Hello, World!" on load
  * [ ] A textbox where the user can type any name
  * [ ] A Submit button that changes the display to "Hello, <name>!"
  * [ ] If the textbox is empty when Submit is pressed, revert to "Hello, World!"
  * Validation: `python3 -m http.server 8888` → open
    `http://localhost:8888`, verify "Hello, World!" displays
  * Commit: `feat: Phase 1: Step 1 - generate base hello world app`
  * Tag: `v1.1-base-app-step-completed`

* [] **Step 1.2: Add name history feature**
  * Context: Scrollable history list of submitted names; in-memory
    only (no localStorage) — see `plan_history.md`
  * [ ] Scaffold `<ul id="history">` element in HTML
  * [ ] Wire submit handler to append to history list
  * [ ] Add WHY comment explaining in-memory choice
  * Validation: Submit 3 names, verify all 3 appear in history list
  * Commit: `feat: Phase 1: Step 2 - add name history list`
  * Tag: `v1.2-history-list-step-completed`

* [ ] **Step 1.3: Input validation**
  * Context: Empty submit should revert to "Hello, World!"; names
    with only whitespace treated as empty
  * Validation: Submit empty, submit spaces-only, verify revert
  * Commit: `fix: Phase 1: Step 3 - add input validation`
  * Tag: `v1.3-input-validation-step-completed`

* [ ] **Step 1.4: CLAUDE.md and guardrails**
  * Context: Add project-level `CLAUDE.md` fencing the header block
    and documenting the in-memory decision
  * Validation: Read `CLAUDE.md`, confirm fencing is correct
  * Commit: `chore: Phase 1: Step 4 - add project CLAUDE.md`
  * Tag: `v1.4-claude-md-step-completed`


---

## 🟡 Phase 2: Multi-Agent Code Review Pipeline

*Status: Proposed*

* [ ] **Step 2.1: Claude Code generates organizer script**
  * Produce `organizer.py` from prompt — file sorter by creation month
* [ ] **Step 2.2: Codex reviews the script**
  * `codex exec` reviews for bugs, safety, failure modes
  * Output: `review_organizer.md`
* [ ] **Step 2.3: Claude Code applies fixes**
  * Read review, apply targeted fixes only, produce `organizer.v2.py`
* [ ] **Step 2.4: Human diff review and acceptance**
  * `diff organizer.py organizer.v2.py` → accept if appropriate

---

## ⚪ Phase 2: Server Deployment

*Status: Backlog*

* Deploy web app to Railway or Vercel via CLI
* Set up GitHub Actions CI/CD pipeline
* Add monitoring and preview deploy per PR

---

##  Constraints
* No frameworks — plain HTML, CSS, and JS only
* Everything in a single index.html file
* Add self-describing comments explaining the WHY behind each decision
* Do not generate any files outside the current directory

---

## Output
Output only the raw file contents of index.html with no explanation,
no markdown fences, no preamble.

---

## 📁 Archived Phases

* [x] **Phase 0: Repository Setup** (See `docs/archive/phase_0.md`)
  * Created org `aiedu-lab`, transferred repo, set branch protection
  * Reconnected Lovable after transfer

---

## Session Rehydration Checklist

> Claude: read this block at the start of every session before acting.

```
Currently on  : Phase __, Step __ — [step title]
Last completed: Phase __, Step __ — [step title]
Last tag      : v__.__-[summary]-step-completed
Next action   : [one sentence]
```

Fill in the blanks from the checkboxes above, then confirm with the
user before proceeding.