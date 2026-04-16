# AI Education Lab

## Objective
A hands-on, community-driven program to learn about agentic solutions, 
such as AI tools, AI driven workflows, etc. through exercises. 
The program is structured as a series of sessions, each focusing on a 
specific tool or concept with the objective to learn how agents work 
for various use cases, such as coding, automation, etc. using:
* Prompting
* Planning (plan.md)
* Agent execution
* Reflection and debugging

## 📅 Agenda

| Topic of Lesson | Lesson Duration | Tool | Tool Duration |
| :--- | :---: | :--- | :---: |
| [**Introduction**](sessions/introduction.md) | 30 mins |  |  |
| [**Concept: Basic Prompting Techniques**](sessions/prompting_basics.md) | 30 mins | [Browser Chat](https://gemini.google.com) |  |
| [**Exercise: Problem Solving**](sessions/problem_solving.md) | 45 mins | [Browser Chat](https://gemini.google.com) |  |
| [**Concept: Planning**](sessions/planning.md) | 45 mins | [Claude Desktop (Chat)](tools/claude/desktop.md) | 15 mins  |
| [**Exercise: Create Presentation**](sessions/slides.md) | 45 mins | [Gamma](https://gamma.app/), [GitHub](tools/github.md) | 15 mins |
| [**Exercise: Create/Run Web Site on Laptop/Lovable**](sessions/web_site.md) | 60 mins | [Lovable.dev](https://lovable.ai), [Claude Code (CLI)](tools/claude/cli.md) | 15 mins |
| [**Concept: Spec Driven Development (SDD)**](sessions/sdd_basics.md) | 45 mins | | |
| [**Exercise: SDD - Group Meetup Organizer**](sessions/client_application.md) | 45 mins | [Claude Code (Pro)](tools/claude/desktop.md), [VSCode](https://code.visualstudio.com/) | 15 mins |
| [**Exercise: Create/Run Workflows on Laptop**](sessions/client_work_automation.md) | 75 mins | [Claude CoWork](tools/claude/desktop.md) | 15 mins |
| [**Exercise: Create/Run Multi-Agent Workflows on Laptop**](sessions/client_multiagent.md) | 60 mins | [Claude Code (CLI)](tools/claude/cli.md), [OpenAI Codex (CLI)](tools/openai/codex_cli.md) | 15 mins |
| [**Concept: Advanced Prompting Techniques**](sessions/prompting_advanced.md) | 60 mins | [Claude Chat](tools/claude/desktop.md) |  |
| [**Concept: Code Review**](sessions/code_review.md) | 30 mins | [Claude Code (Pro)](tools/claude/desktop.md), [VSCode](https://code.visualstudio.com/) |  |
| [**Concept: AI Across the SDLC**](sessions/sdlc_ai.md) | 45 mins | [Claude Code (CLI)](tools/claude/cli.md), GitHub Actions |  |
| [**Exercise: Run Applications on Server**](sessions/server_application.md) | 60 mins | [OpenClaw](tools/openclaw/cli.md) | 15 mins | 15 mins |
| [**Exercise: Run Multi-Agent Workflows on Server**](sessions/server_multiagent.md) | 60 mins | [Temporal](https://temporal.io/) | 15 mins |
| [**Concept: Software Enhancement**](sessions/software_enhancement.md) | 30 mins | [Claude Code (Pro)](tools/claude/desktop.md), [VSCode](https://code.visualstudio.com/) |  |
| [**Future Advancements**](sessions/future_advancements.md) | 30 mins |  |  |
| [**Recap**](sessions/recap.md) | 30 mins |  |  |

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

## 🤝 Contribution Guidelines
After each session:
1. Add/update:
   * `plan.md`
   * prompts (best + failures)
   * learnings
2. Commit to a separate branch:
```bash
git add .
git commit -m "Session X updates"
git push
```
3. Submit for Pull Request for merging into main branch
---

## 🙌 Credits
Inspired by practical AI learning approaches and community collaboration.
