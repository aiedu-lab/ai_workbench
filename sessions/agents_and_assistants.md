# Concept: Agents and AI assistants

## 🎯 Objective

Distinguish an **AI assistant** — the application you open and talk
to — from an **AI agent** — the component inside it that actually
gets work done by looping with an LLM and its tools.

---

## 🧠 The Core Concepts

### What is an AI assistant?

An assistant is a complete application: potentially a user-facing
interface, one or many LLM(s), Tool(s) with permissions, Knowhow(s)
(aka skills), and a *master agent* that does the work and spawns
additional agents on demand.

Examples: Claude Desktop, Claude CLI, Antigravity, Claude.ai, Codex.

### What is an AI agent?

An agent operates on a **subset of resources** it has been granted
within the assistant. It interacts with an LLM, which may ask the
agent to call a Tool or invoke a Knowhow; the Tool's response or
the Knowhow's effect is fed back to the LLM. This loop continues
until the LLM decides the job is done.

```text
Agent → LLM → "call Tool X" / "invoke Knowhow Y"
          ↑                │
          └──── result ────┘
   ...repeats until the LLM says the job is done
```

### How an assistant and its agents fit together

The assistant is the container; agents are what run inside it:

```text
Assistant (e.g. Claude Desktop, Claude CLI, Codex)
├── LLM(s)
├── Tool(s)     — with granted permissions
├── Knowhow(s)  — skills an agent can invoke
└── Master agent
    └── spawns sub-agents on demand, each scoped to a
        subset of the assistant's resources
```

You will build and run both layers later in the lab:
[Exercise: Create/Run Agent App](client_agent.md) (single agent),
[Exercise: Multi-Agent Workflows](client_multiagent.md) (master
agent spawning sub-agents), and
[Exercise: Run Multi-Agent Workflows on Server](server_multiagent.md)
(durable multi-agent systems).

## References

* [Agents and AI assistants](https://drive.google.com/file/d/1hucHQ0QpD3mWeIofVjgvl2m4Nnej52Nm/view)
</content>
