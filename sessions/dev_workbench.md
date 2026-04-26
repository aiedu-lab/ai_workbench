# AI Development Workbench: Platform & Workflow Guidelines

## Objective

Provide a **simple, consistent, and low-friction development environment** 
for learners to learn AI tooling, while allowing enough flexibility for 
experimentation.

---

# 1. Core Principle

> **VS Code is your interface. Your code runs in a Linux environment.**

Students should not initially worry about:

* containers
* virtual machines
* kernels

They should focus on:

* writing code
* running commands
* using AI tools

---

# 2. Standardized Development Framework

## macOS Setup (Primary Recommendation)

### Architecture

```
[ macOS ]
   └── VS Code (UI)
         └── Dev Container (Linux runtime)
```

### Components

* VS Code installed on macOS
* Docker Desktop or Colima
* Dev Containers (`.devcontainer.json`)
* Linux environment inside container

---

## Windows 11 Setup

### Architecture

```
[ Windows ]
   └── VS Code (UI)
         └── WSL (Linux runtime)
```

### Components

* VS Code installed on Windows
* WSL (Ubuntu recommended)
* Linux environment inside WSL

---

## Key Insight

| Concept           | macOS         | Windows |
| ----------------- | ------------- | ------- |
| Linux environment | Dev Container | WSL     |
| VS Code location  | Host          | Host    |
| Code execution    | Linux         | Linux   |

> From a student perspective, both environments behave the same.

---

# 3. Claude + AI Tooling Integration

### Recommended Setup

* Claude Desktop → installed on host (macOS / Windows)
* VS Code → primary IDE
* Claude VS Code plugin → installed in VS Code
* Code execution → Linux environment (container or WSL)

---

## Mental Model

| Component               | Runs Where              |
| ----------------------- | ----------------------- |
| VS Code UI              | Host OS                 |
| Claude Desktop          | Host OS                 |
| Claude plugin           | VS Code                 |
| Python / Node / AI code | Linux (WSL / container) |

---

# 4. Learner Rules (Critical)

## Rule 1 — Single Environment

> **Your code runs in ONE place: the Linux environment.**

Do NOT mix:

* macOS tools + container tools
* Windows tools + WSL tools

---

## Rule 2 — Use the Right Terminal

> **Use a terminal connected to your project environment.**

Recommended:

* VS Code integrated terminal

Advanced (optional):

* External terminal attached to WSL/container

---

## Rule 3 — Install Tools in the Right Place

Install inside Linux:

* Python
* Node.js
* pip / npm packages
* AI frameworks

Install on host:

* VS Code
* Claude Desktop
* Docker / WSL

---

## Rule 4 — Keep Files in Linux

Always work in:

* WSL: `/home/...`
* Dev Container: `/workspaces/...`

Avoid:

* Windows `C:\` paths
* macOS `/Users/...` for project code

---

## Rule 5 — If Things Break

> **Rebuild the environment instead of debugging endlessly.**

* Dev Containers → “Rebuild Container”
* WSL → restart or recreate environment

---

# 5. Workflow (What Learners Actually Do)

## Step 1 — Open Project

* macOS → “Reopen in Container”
* Windows → “Open in WSL”

---

## Step 2 — Use Terminal

```
python
pip install <package>
npm install
```

Same commands across both platforms.

---

## Step 3 — Develop + Use AI Tools

* Edit code in VS Code
* Use Claude plugin for assistance
* Run code in terminal

---

# 6. Common Pitfalls

## Pitfall 1 — Installing Tools in Wrong Place

Symptom:

* “Command not found”
* “Package not installed”

Cause:

* Installed on host instead of Linux

---

## Pitfall 2 — Mixed File Systems

Symptom:

* Code not visible
* Performance issues

Cause:

* Working outside Linux environment

---

## Pitfall 3 — Multiple Terminals

Symptom:

* Different results in different terminals

Cause:

* Using:

  * system terminal
  * VS Code terminal
  * WSL/container inconsistently

---

# 7. General Learning Strategy

## Phase 1 (Beginner)

* Do NOT bog down into:

  * containers
  * WSL internals
  * virtualization

Focus on:

* “Run this command”
* “Write this code”

---

## Phase 2 (Intermediate)

Introduction to:

* “This is actually Linux”
* File system structure
* Basic environment concepts

---

## Phase 3 (Advanced)

Understand:

* Containers vs WSL
* Reproducibility
* Dev environments
* AI agent workflows

---

# 8. Why This Framework Works

* Consistent across Mac and Windows
* Minimizes setup complexity
* Reduces environment-related failures
* Scales from beginner → advanced workflows
* Compatible with modern AI tooling

---

# 9. Bottom Line

* macOS → Dev Containers
* Windows → WSL
* VS Code → always the interface
* Linux → always the execution environment

> Keep the model simple. Hide complexity early. Reveal it only when needed.

---
