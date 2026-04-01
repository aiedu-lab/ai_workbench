# AI Education Lab

A hands-on, community-driven program to learn AI tooling and coding agents through real-world exercises.

## 🎯 Objective

Enable participants to **“learn how to fish”** — not just use AI, but understand how to:
- Think in prompts
- Design plans (spec-first thinking)
- Debug AI outputs
- Manage AI agents effectively

---

## 🧠 Learning Philosophy

Each session follows a simple structure:

> **One Tool → One Concept → One Project → One Failure → One Reflection**

We emphasize:
- Planning over coding
- Debugging specs, not just code
- Learning from failures

---

## 🧰 Core Tools

- Primary Agent: Claude (Chat + Code)
- Web Tool: Replit / Lovable (select sessions)
- CLI Agent: Claude Code (API-based)

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

## 🧭 Claude Code Setup (API Mode Only) & Safe usage

### 1. Set API key:

```bash
export ANTHROPIC_API_KEY=...
```

### 2. Ensure no login session:

```bash
claude logout
```

### 3. Always run inside the repo

```bash
cd ai-education-lab
```

### 4. Verify environment


```bash
bash tools/claude/check_env.sh
claude
```

### 5. Constrain scope in prompts

Always include:

"Only read files in this project directory. Do not access external folders."

### 6. Avoid large directories

Never run on:

* ~/
* Downloads/
* node_modules/

### 7. Kill runaway processes

Press:

* Ctrl + C (Windows/Linux)
* Cmd + . (Mac)

---

## 🔐 Security: API Keys

- NEVER commit API keys to GitHub
- DO NOT store keys in any tracked file
- Use environment variables only:
  - macOS/Linux: `export ANTHROPIC_API_KEY=...`
  - Windows: `setx ANTHROPIC_API_KEY ...`

If a key is leaked:
- Revoke immediately
- Generate a new key

---

## ✍️ How We Work

### 1. Plan First
- Always create or refine `plan.md` before coding

### 2. Prompt with Structure
Use:
- Context
- Task
- Constraints
- Output format

### 3. Execute Carefully
- Run agents in controlled scope
- Avoid large directories

### 4. Reflect
- What failed?
- Why?
- How did we fix it?

---

## ⚠️ Guardrails

- Never run Claude Code on root directories
- Always constrain file scope (e.g., `src/`)
- Use a **Kill Switch** (`Ctrl + C`) for runaway agents
- Set API spend limits (e.g., $5)

---

## 💰 Tokenomics (Cost Awareness)

Two modes:
- **Subscription (Netflix)** → easy, less control
- **API (AWS)** → pay-per-use, precise, recommended for CLI

---

## 📚 What Goes Where

| Artifact | Location |
|--------|---------|
| Best prompts | `/prompts/best/` |
| Failed prompts | `/prompts/failures/` |
| Project code | `/projects/` |
| Plans (`plan.md`) | `/projects/<project>/` |
| Session notes | `/learnings/session-notes/` |

---

## 🤝 Contribution Guidelines

After each session:
1. Add/update:
   - `plan.md`
   - prompts (best + failures)
   - learnings
2. Commit:
```bash
git add .
git commit -m "Session X updates"
git push
```

---

## 🧩 Golden Rule

If the code breaks, the plan is wrong. Fix the plan, not the code.

---

## 🚀 Getting Started
Clone repo
Set up API key (for Claude Code sessions)
Join a group (Driver / Prompt / Observer)
Start Session 1

---

## 📖 Agenda

See: /sessions/agenda.md

---

## 🙌 Credits

Inspired by practical AI learning approaches and community collaboration.
