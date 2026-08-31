# <img src="miscellaneous/docs/images/aiedu-lab.png" alt="aiedu-lab" width="32" valign="middle"> AI Workbench

## Objective
A hands-on, community-driven program to learn about generative AI solutions, 
such as agentic AI applications, AI driven workflows and intelligence, 
etc. through exercises. 
The program is structured as a series of sessions, each focusing on a 
specific tool or concept.

> **Companion Repository:** [LA Workbench](https://github.com/aiedu-lab/la_workbench)
> is an independent Linear Algebra curriculum that pairs well with
> this lab. Its NumPy/PyTorch exercises build the math intuition —
> vectors, matrices, transformations — that powers the embeddings,
> inference, and training concepts exercised here.

---

## 📅 Agenda

| Topic of Lesson | Description | Lesson Duration | Tool | Tool Duration |
| :--- | :--- | :---: | :--- | :---: |
| [**Why learn GenAI?**](sessions/motivation.md) | Understand why generative AI matters and what the AI Computer shift means for builders. | 30 mins | [Claude Chat](miscellaneous/tools/claude/desktop.md) | |
| [**Introduction**](sessions/introduction.md) | Orient to the course arc, tools, and the Group Meetup Organizer project thread. | 30 mins | [Claude Chat](miscellaneous/tools/claude/desktop.md) |  |
| [**Development Workbench Setup**](sessions/dev_workbench.md) | Install and verify WSL2/Dev Container, VSCode, and GitHub before lab day. | Before lab | [VM/WSL2/DevContainer](miscellaneous/tools/VM/setup.md), [VSCode](miscellaneous/tools/dev_workbench/vscode.md), [GitHub](miscellaneous/tools/dev_workbench/github_and_git.md), [Claude](miscellaneous/tools/claude/cloud.md), [Claude Code](miscellaneous/tools/dev_workbench/vscode.md) | 30 mins |
| [**Concept: Basic Prompting Techniques**](sessions/prompting_basics.md) | Learn the vocabulary and mental models for directing AI effectively. | 30 mins | [Browser Chat](https://gemini.google.com) |  |
| [**Exercise: Problem Solving**](sessions/problem_solving.md) | Apply prompting to real problems and build a structured AI feedback loop. | 45 mins | [Browser Chat](https://gemini.google.com) |  |
| [**Concept: Planning**](sessions/planning.md) | Draft, critique, and refine plans with AI — the foundation of spec-driven work. | 45 mins | [Claude Desktop (Chat)](miscellaneous/tools/claude/desktop.md) | 15 mins |
| [**Exercise: Presentation & Design**](sessions/presentation_n_design.md) | Generate slide decks and visual designs with AI in minutes. | 60 mins | [Gamma](https://gamma.app/), [Claude Design](https://claude.ai/design) | 15 mins |
| [**Exercise: Create/Run Web Site on Laptop/Lovable**](sessions/web_site.md) | Build and deploy a working web page using AI code generation. | 60 mins | [Lovable.dev](https://lovable.ai), [Claude Code (CLI)](miscellaneous/tools/claude/cli.md) | 15 mins |
| [**Concept: Advanced Prompting Techniques**](sessions/prompting_advanced.md) | Master skills, few-shot examples, chain-of-thought, RAG, and agent patterns. | 90 mins | [Claude Chat](miscellaneous/tools/claude/desktop.md) |  |
| [**Concept: Human Driven Development**](sessions/hdd.md) | Human conceptualizes plan; AI executes detail. High-confidence pattern for high-penalty domains. | 30 mins | [Claude Code (CLI)](miscellaneous/tools/claude/cli.md) | |
| [**Exercise: Embeddings Visualization**](sessions/embedding.md) | Visualize word vectors: map, cluster, concept direction, similarity, and nearest-neighbor context with GloVe. | 40 mins | Python, GloVe | 10 mins |
| [**Concept: Assistant Family, Assistant, and Agent**](sessions/assistant-family_assistant_and_agent.md) | See how an AI assistant (Claude Desktop, CLI, Codex) hosts agents that loop with an LLM and its tools to get work done. | 30 mins | [Claude Chat](miscellaneous/tools/claude/desktop.md) |  |
| [**Concept: Spec Driven Development (SDD)**](sessions/sdd_basics.md) | Write a specification first, then let AI generate matching code reliably. | 45 mins | [Claude Code (CLI)](miscellaneous/tools/claude/cli.md) | |
| [**Exercise: Create Group Meetup Organizer using SDD, App runs on Laptop**](sessions/client_application.md) | Implement the Poller → Selector → Notifier pipeline with AI-generated code. | 45 mins | [Claude Code (Pro)](miscellaneous/tools/claude/desktop.md), [VSCode](https://code.visualstudio.com/) | 15 mins |
| [**Concept: Code Review**](sessions/code_review.md) | Use AI to catch bugs, enforce style, and explain unfamiliar code. | 30 mins | [Claude Code (Pro)](miscellaneous/tools/claude/desktop.md), [VSCode](https://code.visualstudio.com/) |  |
| [**Concept: AI Across the SDLC**](sessions/sdlc_ai.md) | See how AI integrates across the entire software development lifecycle. | 45 mins | [Claude Code (CLI)](miscellaneous/tools/claude/cli.md), GitHub Actions |  |
| [**Exercise: Create/Run Agent App on Laptop**](sessions/client_agent.md) | Build a single-agent CoWork workflow that plans and executes file tasks. | 75 mins | [Claude CoWork](miscellaneous/tools/claude/desktop.md) | 15 mins |
| [**Exercise: Create/Run Multi-Agent Workflows on Laptop**](sessions/client_multiagent.md) | Coordinate specialized agents for problems no single agent handles reliably. | 60 mins | [Claude Code (CLI)](miscellaneous/tools/claude/cli.md), [OpenAI Codex (CLI)](miscellaneous/tools/openai/codex_cli.md) | 15 mins |
| [**Exercise: Run Multi-Agent Workflows on Server**](sessions/server_multiagent.md) | Deploy a durable multi-agent system using Temporal on a shared server. | 60 mins | [OpenClaw](miscellaneous/tools/openclaw/cli.md), [Temporal](miscellaneous/tools/temporal/cli.md) | 15 mins |
| [**Concept: Solution Architecture**](sessions/solution.md) | Design full-stack AI solutions using patterns learned across the lab. | 45 mins | [Claude Chat](miscellaneous/tools/claude/desktop.md), Python |  |
| [**Exercise: Personal Knowledge Management (LLM Wiki)**](sessions/llm_wiki.md) | Use an AI agent as librarian for a knowledge base that grows with each ingest. | 60 mins | [Obsidian](https://obsidian.md), [Claude Code (CLI)](miscellaneous/tools/claude/cli.md) | 15 mins |
| [**Exercise: Applications on Pluggable Models**](sessions/pluggable_models.md) | Swap LLM providers without changing code — compare open-weight and closed models side by side. | 45 mins | [Groq](miscellaneous/tools/groq/setup.md), [OpenRouter](miscellaneous/tools/openrouter/openrouter.md), [Cline](miscellaneous/tools/dev_workbench/cline.md) | 15 mins |
| [**Concept: Model Serving Stack**](sessions/model_serving_stack.md) | See the layers between your prompt and a model's reply — agent harness, provider, foundation model — and compare cloud, free-CLI, and local-Ollama stacks. | 30 mins | | |
| [**Concept: AI Local**](sessions/ai_local_model.md) | Local open-weight models, the agent harnesses that drive them, and how Ollama serves them. | 30 mins | | |
| [**Exercise: AI Local**](sessions/ai_local.md) | Run an LLM entirely offline for privacy, custom personas, and zero cloud cost. | 45 mins | [Ollama](miscellaneous/tools/ollama/setup.md) | 15 mins |
| [**Future Advancements**](sessions/future_advancements.md) | Survey the AI frontier and what it means for the tools you just built. | 30 mins |  |  |
| [**Recap**](sessions/recap.md) | Reflect on what was built, what surprised you, and how to keep improving. | 30 mins |  |  |

---

## 🔁 Student Workflow

* Go through the sessions serially — do not jump ahead.
* Complete the [Development Workbench Setup](sessions/dev_workbench.md)
  once, before lab day.
* Join the class Discord channel for live sessions and coordination
  with the instructor and your peers.

For each session:

1. **Branch** — pull and merge the latest `origin/main` into local
   `main`, then create your personal branch off `main` if it does
   not exist yet, or switch to it and merge in the latest `main`.
2. **Grok** the session's Concept section.
3. **Design, develop, and test** the Exercise section's solution
   with the appropriate AI tools, inside the matching
   `projects/<project>/` subfolder.
4. **Commit and tag** the changes on your branch.
5. **Push** the validated branch to `origin`.
6. **Submit a pull request** to merge your branch into `main`.
7. **Notify** the instructor on Discord that you completed the
   session, and ask for PR feedback.

See [GitHub and
Git](miscellaneous/tools/dev_workbench/github_and_git.md) for the
exact commands behind each step.

---

## 📤 Submitting Exercise Solutions

Once you've completed an exercise or a set of exercises, submit it 
so it becomes a durable record of your work.

1. Ensure you've the latest mainline branch:
   `git switch main && git pull origin main`
2. Create (or Switch to) a branch off of main where you'll make the changes:
   `git switch --create solutions-branch 2>/dev/null || git switch solutions-branch`
3. Create projects/<project-name>/solutions/<github-userid>/ —
   <project-name> is the matching project subfolder for the session
   (e.g. projects/embedding/), and <github-userid> is any one member's
   GitHub user id if you worked in a group. Inside it, add:
   * solution.md — copy [solution_template.md](
       miscellaneous/reporting/solution_template.md
     ) and fill in each section. Keep the `# Solution: <Title>`
     heading and section names exactly as given; the completion
     report depends on them to label and credit your work.
   * your file(s):
     * requirements.in (or equivalent) for any extra installs
     * all source files

   `labsetup.py` wires up a pre-commit hook that validates
   solution.md automatically, rejecting the commit if the heading
   or Contributors section is missing or malformed.
3. If you have spent a lot of time and submitting multiple solutions,
   then prior to pushing your solution to origin please ensure you've
   the latest version or origin/main: `git rebase origin/main`
4. Push your changes to origin: `git push origin solutions-branch`
5. Open a pull request named `projects/<project-name>/solutions/<github-userid>`.
6. Once the maintainer approves and merges your PR,
   [`.github/workflows/report.yml`](.github/workflows/report.yml)
   automatically regenerates [`summary_report.md`](
   miscellaneous/reporting/summary_report.md) (the whole class's
   completion record) and each contributor's own
   `miscellaneous/reporting/for_each_student/<github-userid>-report.md`
   — no manual step needed.

---

## 🧭 Tools

| Platform | Application | Tools |
| :--- | :---: | :---: |
| Browser | Chat | OpenAI, Gemini, Claude Chat | 
| Browser | SaaS | Lovable.dev, Gamma |
| Client | Desktop Application | Claude Chat, Code, CoWork |
| Server | Server Application | OpenClaw, Claude |

---

## 📁 Repository Structure

```text
ai_workbench/
├── sessions/                    # Lesson exercises & materials
├── projects/                    # Generated apps & automation
└── miscellaneous/
    ├── software_defined_workbench/  # SDW plan + history
    ├── setup/
    │   ├── student/              # Student lab setup scripts
    │   └── instructor/           # Instructor preflight/roster
    ├── tools/                    # Setup guides and guardrails
    ├── plans/                    # plan.md templates + canonical
    ├── learnings/                # Notes, reflections, patterns
    ├── prompts/                  # Prompt library (best/failures)
    ├── docs/                     # Brand assets, archived phases
    ├── experimental/             # Draft sessions not promoted
    └── tests/                    # Repo-level smoke tests
```

---

## 📚 What Goes Where

| Artifact          | Location                                   |
|-------------------|---------------------------------------------|
| Project code      | `/projects/<project>/`                       |
| Session notes     | `/miscellaneous/learnings/session-notes/`    |
| Student setup     | `/miscellaneous/setup/student/`              |
| Instructor setup  | `/miscellaneous/setup/instructor/`           |

---

## 🧑‍🏫 Instructor Guidelines

Execute [**Instructor Preflight**](
miscellaneous/setup/instructor/instructor.md) before starting 
the workbench lab sessions and check off on setting up the student roster, 
discord server, docker server, student laptops, etc.

---

## 🤝 Contribution Guidelines

### 🔧 Specification Driven Workbench (SDW)

This repository is a **Specification Driven Workbench (SDW)**: all
content changes flow from a written specification, never from
direct edits. `SDW_DIR` below means
`miscellaneous/software_defined_workbench`; its `SDW_DIR/plan.md`
is the single source of truth — it is append-only, never
rewritten. AI executes each plan step under
instructor review; the resulting content, plan entries, and
prompt history are committed together, creating a full audit
trail from intent to implementation.

> **In short:** prompt → plan → execute → review → commit.
> No content is created outside the plan.

### Workbench Update Workflow

All content changes must follow this sequence in strict order:

1. **Specify** — append the new prompt to
   `SDW_DIR/prompt_history.md`. The prompt directs AI to extend
   `SDW_DIR/plan.md` with new phases or steps; never edit
   plan.md directly.
2. **Plan** — AI appends the new phase/steps to
   `SDW_DIR/plan.md`. Both files are append-only and serve as
   the system of record.
3. **Execute** — AI executes each plan step one at a time under
   reviewer approval, following `AGENTS.md` operating protocol.
4. **Commit** — commit `prompt_history.md`, `plan.md`, and the
   generated content together on a feature branch. Annotate every
   AI-generated section:
   ```text
   <!-- AI-GENERATED [provider:model]: Phase X Step Y -->
   ```
5. **PR & Review** — submit a pull request to `main`. The PR
   description must include:
   * `provider:model` used to append changes to
     `SDW_DIR/plan.md`
   * `provider:model` used to execute the plan and generate content
   * Link to the executed section in `SDW_DIR/plan.md`
   Maintainers run AI-assisted style checks (80-col, 2-space
   indent) then review content before approving the merge.

> **No direct content edits.** All changes originate in
> `SDW_DIR/prompt_history.md` and flow through `SDW_DIR/plan.md`.

### SDW Skills

Two project-scoped Claude Code slash-command skills live in
`.claude/commands/` and are available in any Claude Code session
opened in this repo.

| Skill | Invocation | Purpose |
|---|---|---|
| `/replan` | `/replan` or `/replan <section>` | Run the full Specify→Plan→Approve→Execute cycle. Without argument, targets the last `## [ ]` section in `SDW_DIR/prompt_history.md`. With argument, targets the named section. |
| `/plan-step` | `/plan-step [draft]` | Generate or validate a single plan step against the CONTEXT/ACTION/CONSTRAINTS/OUTPUT/TEST template before appending it to `SDW_DIR/plan.md`. |

**Examples:**
```
/replan                  # auto-targets last unprocessed section
/replan Skillify         # targets ## Skillify in prompt_history.md
/plan-step               # interactive — prompts for each field
/plan-step add pristine/ to README layout
```

`/plan-step` is applied internally by `/replan` when generating
each step — no separate invocation needed during a replan cycle.

> **Note:** "Instructor" (see 🧑‍🏫 Instructor Guidelines above) is
> an *education* role describing how you use this course.
> "Contributor", "Maintainer", and "Admin" below are *GitHub* roles
> describing your repo permissions — an instructor is often also a
> GitHub admin, but doesn't have to be, and the two are independent.
>
> Contributors may not commit directly to `main`. Write-access
> contributors (instructors) do **not** need a separate reviewer to
> merge their own PR — a PR is required, but zero additional
> approvals are needed. See
> [contributor.md](miscellaneous/setup/contributor/contributor.md)
> for the `gh` commands to submit a pull request and validate your
> contributor access.

---

## 🧭 Maintainer Guidelines

Reviewing and merging pull requests is a maintainer's job. See
[maintainer.md](miscellaneous/setup/maintainer/maintainer.md) for
the full `gh` command reference.

---

## 🛠️ Admin Guidelines

Repo hygiene (branch protection, CODEOWNERS, CI secrets) and
collaborator-role management are admin tasks. See
[admin.md](miscellaneous/setup/admin/admin.md) for the full `gh`
command reference.

---

## Agent Conventions

This repo uses a two-layer model so loading it in any AI coding
tool gives consistent, non-duplicated context.

### Layer 1 — Universal (`.agent/`)

Provider-agnostic content that every compliant tool can read:

| Construct | Path | Invocation | Read by |
|---|---|---|---|
| Rule | `.agent/rules/*.md` | Automatic | All (see Layer 2) |
| Skill | `.agent/skills/<n>/SKILL.md` | `/name` or auto | All (see Layer 2) |
| Workflow | `.agent/workflows/*.md` | Explicit trigger | Antigravity native |

**Rules in this repo:**
- `always-line-length.md` — 79-char limit, Python/Markdown
- `git-output-rules.md` — always use `--no-pager --no-ext-diff`

### Layer 2 — Provider loaders (thin wrappers)

Each tool reads its own loader file, which references Layer 1:

| Tool | Loader file | Notes |
|---|---|---|
| Codex CLI | `AGENTS.md` | Full protocol; step 0 reads `.agent/rules/` |
| Claude Code | `CLAUDE.md` | Symlink → `AGENTS.md` (zero duplication) |
| Antigravity | `AGENTS.md` + `.agent/` | Reads both natively |
| Cursor | `.cursor/rules/*.mdc` | **Not yet wired** |
| Windsurf | `.windsurfrules` | **Not yet wired** |
| GitHub Copilot | `.github/copilot-instructions.md` | **Not yet wired** |

### Claude Code-only skills

Project skills in `.claude/commands/` use Claude Code-specific
tools (plan mode, SDW protocol) and are not portable:

| Skill | Purpose |
|---|---|
| `/replan` | Full Specify→Plan→Approve→Execute cycle |
| `/plan-step` | Generate/validate a single plan.md step |
| `/proc-article` | Knowledge ingestion pipeline |

`.claude/skills/` (loaded by name, not slash commands):

| Skill | Purpose |
|---|---|
| `pr_submit_plugin` | 7-step gated PR submit chain: branch/tree hook → build+test+container-tests (stub) → `bazel run //:pr_check` (act) → `bazel run //:submit_pr` → confirm hook. Bazel-based, mirroring `aim`. |
| `pr_merge_plugin` | 3-step gated PR merge chain: wait-for-checks hook → `bazel run //:merge_pr` → confirm-merged hook. |
| `model_modernizer` | Reports current model vs. latest; recommends, never auto-switches. |

`tools/scripts/repo_utils/` also has `check_pr.py`/`approve_pr.py`/
`merge_pr.py`, run via bazel (`bazel run //:check_pr -- <PR#>`,
etc.) — this repo now has a minimal bazel scaffold (mirroring
`aim`'s "no real code yet, full bazel scaffold anyway" pattern) so
these no longer run as bare `python3` scripts.

#### PR Workflow Plugins — Example Usage

| Script | Purpose | Example |
|---|---|---|
| `check_pr` | Read-only: reports state/checks/review-decision, exits 0 only if the PR looks mergeable right now | `bazel run //:check_pr -- <PR#>` |
| `submit_pr` | Pushes the current branch and opens a PR | `bazel run //:submit_pr -- --title "..." --body "..." --base main --draft` |
| `approve_pr` | Approves a PR (never your own -- GitHub rejects self-approval) | `bazel run //:approve_pr -- <PR#> --body "..."` |
| `merge_pr` | Merges a PR only after confirming checks passed and any required review is satisfied (retries with `--admin` when review is required but exempt via branch protection) | `bazel run //:merge_pr -- <PR#> --method squash --delete-branch` |

Preferred entry points: `/check_pr <PR#>` and `/check_prs`
(read-only), `/pr_submit` (drafts the title/body from the
branch's actual content, then runs the submit chain),
`/pr_approve` (MAINTAIN/ADMIN only), and `/pr_merge` (WRITE+,
gated on checks passing and review
satisfied/not-required/admin-exempt) -- see
`.claude/commands/{check_pr,check_prs,pr_submit,pr_approve,
pr_merge}.md` for each one's exact scope.

`pr_check.py` passes `act` `--reuse` (keep the job container
between runs instead of removing it) to avoid a container-removal
timeout on Docker Desktop's WSL2 backend -- see `pr_check.py`'s
own comment. Run `docker container prune` occasionally to
reclaim the containers this leaves behind. If the WSL2/Docker
flakiness itself is blocking you (or you know a change doesn't
need a full local act run -- docs/skill-only, say), `touch
.pr_check_skip` at the repo root to skip `act` entirely (exit 0
immediately, no Docker call at all); `rm .pr_check_skip` to
re-enable. Git-ignored, local-machine-only, and only skips the
local act simulation -- real GitHub Actions CI still runs
pr-validation.yaml on every actual push/PR regardless. All 5
repos, including ITDev, support this the same way.

**Cross-repo consistency:** this tooling is intentionally duplicated
(not symlinked) across every sister repo -- ITDev, aim, personal,
ai_workbench, la_workbench. Any change here must be ported to the
same path in every other repo; see each script's own "Sync note".

---

## 🙌 Credits
Inspired by practical AI learning approaches and community collaboration.
