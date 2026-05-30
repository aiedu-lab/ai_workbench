# AI Workbench

## Objective
A hands-on, community-driven program to learn about generative AI solutions, 
such as agentic AI applications, AI driven workflows and intelligence, 
etc. through exercises. 
The program is structured as a series of sessions, each focusing on a 
specific tool or concept with the objective to learn how agents work 
for various use cases, such as coding, automation, etc. using:
* Prompting
* Planning (plan.md)
* Agent execution
* Reflection and debugging

## 🌐 Motivation

Generative AI is reshaping every industry. This table shows
how AI-native approaches are transforming — not just
improving — the way work gets done:

| Domain | Legacy | AI Native | Objective | Transformation |
| :--- | :--- | :--- | :--- | :--- |
| Internet Search | Google keyword ranking | ChatGPT / Claude | How to best prepare for Multivariable Calculus | Knowledge fully reasoned, correlated, and synthesised — not a list of keyword matches |
| Photography | Photoshop manual editing | Midjourney / Adobe Firefly | Make our event photos look professional | Describe the result in words; AI handles composition, lighting, and style |
| Software Development | IDE + Stack Overflow | Claude Code / Cursor | Ship quality software faster | Coding agents generate, test, and debug code end-to-end across the entire codebase |
| Manufacturing Planning | ERP + spreadsheets | Hadrian / Machina Labs | Optimise production scheduling for custom parts | AI reads CAD files, programs CNC machines, and schedules jobs autonomously |
| Customer Relationships | Salesforce CRM manual entry | Auracell | Sell more with less manual tracking | Automated pipeline management and customer records updated from conversation context |
| Conversational Intelligence | Gong call recording + analytics | 1mind | Close the deal with this customer | Real-time AI agent offers live intelligence and suggested responses, not just post-call analysis |
| Running a Company | Human-in-the-loop for every decision | [Autonomous AI orgs](https://x.com/benln/status/2054546806516654263) | Scale operations without scaling headcount | AI agents own workflows end-to-end; humans set goals and review exceptions |

The sessions in this workbench are designed to give you
hands-on experience with the tools that make AI-native
approaches possible.

---

## 🔧 Specification Driven Workbench (SDW)

This repository is a **Specification Driven Workbench (SDW)**: all
content changes flow from a written specification, never from direct
edits. The specification plan (`sdw/plan.md`) is the single source
of truth — it is append-only, never rewritten. AI executes each
plan step under instructor review; the resulting content, plan
entries, and prompt history are committed together, creating a full
audit trail from intent to implementation.

> **In short:** prompt → plan → execute → review → commit.
> No content is created outside the plan.

---

## 📅 Agenda

| Topic of Lesson | Description | Lesson Duration | Tool | Tool Duration |
| :--- | :--- | :---: | :--- | :---: |
| [**Introduction**](sessions/introduction.md) | Orient to the course arc, tools, and the Group Meetup Organizer project thread. | 30 mins | [Claude Chat](tools/claude/desktop.md) |  |
| [**Development Workbench Setup**](sessions/dev_workbench.md) | Install and verify WSL2/Dev Container, VSCode, and GitHub before lab day. | Before lab | [VM/WSL2/DevContainer](tools/VM/setup.md), [VSCode](tools/dev_workbench/vscode.md), [GitHub](tools/dev_workbench/github.md), [Claude](tools/claude/cloud.md), [Claude Code](tools/dev_workbench/vscode.md) | 30 mins |
| [**Concept: Basic Prompting Techniques**](sessions/prompting_basics.md) | Learn the vocabulary and mental models for directing AI effectively. | 30 mins | [Browser Chat](https://gemini.google.com) |  |
| [**Exercise: Problem Solving**](sessions/problem_solving.md) | Apply prompting to real problems and build a structured AI feedback loop. | 45 mins | [Browser Chat](https://gemini.google.com) |  |
| [**Concept: Planning**](sessions/planning.md) | Draft, critique, and refine plans with AI — the foundation of spec-driven work. | 45 mins | [Claude Desktop (Chat)](tools/claude/desktop.md) | 15 mins |
| [**Exercise: Presentation & Design**](sessions/presentation_n_design.md) | Generate slide decks and visual designs with AI in minutes. | 60 mins | [Gamma](https://gamma.app/), [Claude Design](https://claude.ai/design) | 15 mins |
| [**Exercise: Create/Run Web Site on Laptop/Lovable**](sessions/web_site.md) | Build and deploy a working web page using AI code generation. | 60 mins | [Lovable.dev](https://lovable.ai), [Claude Code (CLI)](tools/claude/cli.md) | 15 mins |
| [**Concept: Advanced Prompting Techniques**](sessions/prompting_advanced.md) | Master skills, few-shot examples, chain-of-thought, RAG, and agent patterns. | 90 mins | [Claude Chat](tools/claude/desktop.md) |  |
| [**Concept: Human Driven Development**](sessions/hdd.md) | Human conceptualizes plan; AI executes detail. High-confidence pattern for high-penalty domains. | 30 mins | [Claude Code (CLI)](tools/claude/cli.md) | |
| [**Exercise: Embeddings Visualization**](sessions/embedding.md) | Visualize word vectors: map, cluster, concept direction, similarity, and nearest-neighbor context with GloVe. | 40 mins | Python, GloVe | 10 mins |
| [**Concept: Spec Driven Development (SDD)**](sessions/sdd_basics.md) | Write a specification first, then let AI generate matching code reliably. | 45 mins | [Claude Code (CLI)](tools/claude/cli.md) | |
| [**Exercise: Create Group Meetup Organizer using SDD, App runs on Laptop**](sessions/client_application.md) | Implement the Poller → Selector → Notifier pipeline with AI-generated code. | 45 mins | [Claude Code (Pro)](tools/claude/desktop.md), [VSCode](https://code.visualstudio.com/) | 15 mins |
| [**Concept: Code Review**](sessions/code_review.md) | Use AI to catch bugs, enforce style, and explain unfamiliar code. | 30 mins | [Claude Code (Pro)](tools/claude/desktop.md), [VSCode](https://code.visualstudio.com/) |  |
| [**Concept: AI Across the SDLC**](sessions/sdlc_ai.md) | See how AI integrates across the entire software development lifecycle. | 45 mins | [Claude Code (CLI)](tools/claude/cli.md), GitHub Actions |  |
| [**Exercise: Create/Run Agent App on Laptop**](sessions/client_agent.md) | Build a single-agent CoWork workflow that plans and executes file tasks. | 75 mins | [Claude CoWork](tools/claude/desktop.md) | 15 mins |
| [**Exercise: Create/Run Multi-Agent Workflows on Laptop**](sessions/client_multiagent.md) | Coordinate specialized agents for problems no single agent handles reliably. | 60 mins | [Claude Code (CLI)](tools/claude/cli.md), [OpenAI Codex (CLI)](tools/openai/codex_cli.md) | 15 mins |
| [**Exercise: Run Multi-Agent Workflows on Server**](sessions/server_multiagent.md) | Deploy a durable multi-agent system using Temporal on a shared server. | 60 mins | [OpenClaw](tools/openclaw/cli.md), [Temporal](tools/temporal/cli.md) | 15 mins |
| [**Concept: Solution Architecture**](sessions/solution.md) | Design full-stack AI solutions using patterns learned across the lab. | 45 mins | [Claude Chat](tools/claude/desktop.md), Python |  |
| [**Exercise: Personal Knowledge Management (LLM Wiki)**](sessions/llm_wiki.md) | Use an AI agent as librarian for a knowledge base that grows with each ingest. | 60 mins | [Obsidian](https://obsidian.md), [Claude Code (CLI)](tools/claude/cli.md) | 15 mins |
| [**Exercise: Applications on Pluggable Models**](sessions/pluggable_models.md) | Swap LLM providers without changing code — compare open-weight and closed models side by side. | 45 mins | [Groq](tools/groq/setup.md), [OpenRouter](tools/openrouter/openrouter.md), [Cline](tools/dev_workbench/cline.md) | 15 mins |
| [**Exercise: AI Local**](sessions/ai_local.md) | Run an LLM entirely offline for privacy, custom personas, and zero cloud cost. | 45 mins | [Ollama](tools/ollama/setup.md) | 15 mins |
| [**Future Advancements**](sessions/future_advancements.md) | Survey the AI frontier and what it means for the tools you just built. | 30 mins |  |  |
| [**Recap**](sessions/recap.md) | Reflect on what was built, what surprised you, and how to keep improving. | 30 mins |  |  |

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

ai-education-lab/
│
├── sessions/ # Session-wise exercises and materials
├── prompts/ # Prompt library (best, failures, templates)
├── projects/ # Generated apps and automation projects
├── plans/ # plan.md templates and canonical examples
├── learnings/ # Notes, reflections, and patterns
└── tools/ # Setup guides and guardrails

---

## 📚 What Goes Where

| Artifact          | Location                      |
|-------------------|-------------------------------|
| Best prompts      | `/prompts/best.md`            |
| Failed prompts    | `/prompts/failures.md`        |
| Project code      | `/projects/<project>/`        |
| Plan frameworks   | `/plans/`                     |
| Session notes     | `/learnings/session-notes/`   |

---

## 🧑‍🏫 Instructor Guidelines

Execute [**Instructor Preflight**](sessions/instructor.md) before starting 
the workbench lab sessions and check off on setting up the student roster, 
discord server, docker server, student laptops, etc.

---

## 🤝 Contribution Guidelines

### Workbench Update Workflow

All content changes must follow this sequence in strict order:

1. **Specify** — append the new prompt to
   `sdw/prompt_history.md`. The prompt directs AI to extend
   `sdw/plan.md` with new phases or steps; never edit plan.md
   directly.
2. **Plan** — AI appends the new phase/steps to `sdw/plan.md`.
   Both files are append-only and serve as the system of record.
3. **Execute** — AI executes each plan step one at a time under
   reviewer approval, following `CLAUDE.md` operating protocol.
4. **Commit** — commit `prompt_history.md`, `plan.md`, and the
   generated content together on a feature branch. Annotate every
   AI-generated section:
   ```text
   <!-- AI-GENERATED [provider:model]: Phase X Step Y -->
   ```
5. **PR & Review** — submit a pull request to `main`. The PR
   description must include:
   * `provider:model` used to append changes to `sdw/plan.md`
   * `provider:model` used to execute the plan and generate content
   * Link to the executed section in `sdw/plan.md`
   Maintainers run AI-assisted style checks (80-col, 2-space
   indent) then review content before approving the merge.

> **No direct content edits.** All changes originate in
> `sdw/prompt_history.md` and flow through `sdw/plan.md`.

### SDW Skills

Two project-scoped Claude Code slash-command skills live in
`.claude/commands/` and are available in any Claude Code session
opened in this repo.

| Skill | Invocation | Purpose |
|---|---|---|
| `/replan` | `/replan` or `/replan <section>` | Run the full Specify→Plan→Approve→Execute cycle. Without argument, targets the last `## [ ]` section in `sdw/prompt_history.md`. With argument, targets the named section. |
| `/plan-step` | `/plan-step [draft]` | Generate or validate a single plan step against the CONTEXT/ACTION/CONSTRAINTS/OUTPUT/TEST template before appending it to `sdw/plan.md`. |

**Examples:**
```
/replan                  # auto-targets last unprocessed section
/replan Skillify         # targets ## Skillify in prompt_history.md
/plan-step               # interactive — prompts for each field
/plan-step add pristine/ to README layout
```

`/plan-step` is applied internally by `/replan` when generating
each step — no separate invocation needed during a replan cycle.
> Contributors may not commit directly to `main`.

---

## 🙌 Credits
Inspired by practical AI learning approaches and community collaboration.
