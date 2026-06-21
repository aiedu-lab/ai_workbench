# Agent Architecture

## BACKGROUND
What are assistants? What are agents? How each of the agentic 
components (LLM, MCP, Skills) fit the agents. Specifically 
the concept of SKILLS and MCP.

## CONTEXT
Correct my current understanding of "assistants and agents" 
per the section below. Please amend or enhance as appropriate 
while answering follow on questions.

## CONSTRATINTS
Explain simply with as little jargon with concrete examples 
(rather than abstract buzzwords) to illustrate the use cases. 
Use diagrams to visually illustrate where appropriate.
Generate answers to each question succinctly within an 
average of 400 words and in 2-3 paragraphs.

## OUTPUT
Generate the content in markdown (md) format. Use ascii art 
or a format that fits in markdown. If some topic is left 
unaddressed, annotate the topic with a comment so that we 
can deep dive.  Add a short reference URL section at the end.

---

## QUESTIONS

### MCP
SWAGGER APIs were created for machine readability? Then why did 
we need MCP? Is it that the "knowhow" of the API is also added 
to MCP which is not mandated in swagger? Does it come with 
example usage as well?

### SKILLS 
Skills are also called as "knowhow"? What do we really mean? 
I understand progressing disclosure and all the jargon 
associated with how we can only send description in context, etc. 
But what is the real utility of SKILL? Is it that SKILLS has 
description, what is does in plain english along with example 
usage that makes is a cookbook recipe? 

### AGENT

#### AGENT LOOP
Agents execute in a loop ("agent loop"), request/respond LLM, 
call Tools as appropriate,  gather the response of the tool, 
update context, and submit the tool result to the LLM. 
In this loop, when and how are skills triggered or activated. 
Typically Skills can package an accompanying software 
script/code.  

#### AGENT ORCHESTRATION
When does agent ochestration come into the picture, what is
the "agent orchestration loop", and is this loop same as the
"agent loop"?

#### AGENT MEMORY
Is it fair to assume that the long term memory is embedded in 
the LLM, whereas the short term memory is embedded in the **context** 
of an agent? How should we conceptualize the memory?

#### SECURITY
One way to attack an agent is to "poison" its context. Context 
can be poisoned via user prompts or content that is retrieved via
MCP/Tool calls? Is this a fair way to conceptualize "context 
poisoning"? 

##### CONTEXT OVERSIGHT
One mitigation to "context oversight" is "prompt oversight". That
is catch the issue when the context is submitted to the LLM as 
prompt in the "agent orchestration loop" by submitting the prompt
the prompt to the "judge LLM". Is this the "agent loop" or 
"agent orchestration loop?". 

If one were to design a security solution where we are not in the
way of developers, where can we insert the "judge LLM" functionality?
For example, could this functionality be in the LLM Gateway?

Do we also need to intercept all inputs to the agent: LLM request
response, MCP request response, other agents/users request to 
the calls to the agent? Or is it sufficient to just be in the
calls between the agent and the LLM (LLM Gateway). 

What would be an example of a benefit where we are intermediating
and examining the calls to the MCP (MCP Gateway) as well?

##### CODE EXECUTION
Similarly, the LLM itself may also respond with code that 
agent needs to run. Thus agents also need a way to "run" 
the accompanying code from LLM or Skill? How Is it realized 
via another Tool (code runner) or it is an intrinsic 
capability of the agent? 

### LLM
LLM is the brain and agent is the muscle/executor of whatever the brain suggests. Where does the logic reside, which  triggers the execution of the appropriate Skill? Does that "trigger" mechanism live in agents or in the LLM?

---

# Concept: Assistants and Agents

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

---

## 🔌 MCP (Model Context Protocol)

### Why MCP over Swagger/OpenAPI?

Swagger (OpenAPI) was designed to make web endpoints machine-readable for traditional deterministic software. It explicitly maps HTTP methods, paths, and tight JSON schemas. However, passing raw OpenAPI specifications directly into an LLM context window creates immense bloat and lacks behavioral semantics.

The **Model Context Protocol (MCP)** standardizes how an application client exposes data and capabilities to an LLM securely through an open protocol. Rather than forcing the LLM application to parse hundreds of unique REST dialects, MCP establishes an explicit, two-way client-server architecture split into three core primitives: **Prompts** (templated instructions), **Resources** (static/dynamic text data like files or logs), and **Tools** (executable actions).

```text
+------------------+         MCP          +-------------------+
|  Agent Client    |<====================>|    MCP Server     |
| (e.g., CLI/App)  |   (JSON-RPC over     | (File System, Git,|
+--------+---------+    Stdio / HTTP)     |  Database, Cloud) |
         |                                +---------+---------+
         | (Context / Tools)                        |
         v                                          v
+--------+---------+                      +---------+---------+
|    LLM Engine    |                      | Core System Infra |
+------------------+                      +-------------------+

```

### Does it include "Knowhow" and examples?

Yes. MCP allows tools and resources to explicitly define metadata, structural hints, and text descriptions tailored for LLM reasoning. While it does not *strictly mandate* few-shot example usage inside the basic schema definition, developers regularly bake semantic "knowhow"—including expected usage patterns, constraints, and execution examples—directly into the descriptive fields or via the **Prompts API** primitive. This minimizes the prompt engineering footprint required to make a tool safely usable by the LLM.

---

## 🛠️ SKILLS (Knowhow)

### What is the real utility of a Skill?

Think of a **Tool** as a atomic primitive command line or API endpoint (e.g., `read_file()` or `execute_bash()`). A **Skill** (or Knowhow) is a composite, higher-level capability or structured "cookbook recipe." It wraps raw tool execution with context, operational boundaries, specific workflows, and few-shot examples that guide the LLM on *how and when* to act.

The real utility of a Skill is **context minimization and cognitive alignment**. Instead of stuffing thousands of lines of documentation or full operating manuals into the active prompt window upfront, you expose only the high-level Skill signature. When that Skill is active, it brings along its own tailored runtime execution logic, standardizing how the LLM solves complex, multi-step domain problems.

```text
┌────────────────────────────────────────────────────────┐
│ SKILL: Triage Security Vulnerability                   │
│  ├─ Plain-English Intent: "Run when CVE is detected"  │
│  ├─ Few-Shot Examples: [Pattern A -> Fix B]           │
│  └─ Execution Chain:                                   │
│       1. Tool Call: run_scanner()                      │
│       2. Tool Call: parse_ast()                        │
└────────────────────────────────────────────────────────┘

```

For instance, a raw tool lets an LLM execute a generic database query. A security *Skill* encapsulates the exact operational playbook required to perform a compliance audit on that database, bundling the plain-English intent, validation logic, and example inputs together.

---

## 🤖 AGENT

### Agent Loop vs. Agent Orchestration Loop

#### The Agent Loop

The **Agent Loop** is the atomic, low-level execution cycle of a single agent. It operates as a continuous state machine:

```text
      ┌─── Submit Prompt ───> [ LLM Engine ]
      │                            │
      │                     Evaluates State &
[ Agent Context ]            Emits Tool Call
      ^                            │
      │                            v
      └─── Update Context ─── [ Tool Executor ]

```

#### The Agent Orchestration Loop

The **Agent Orchestration Loop** operates one abstraction layer above. It is the managerial engine that coordinates *multi-agent* systems. It handles task decomposition, structural routing between specialized sub-agents, global state synchronization, and conflict resolution when individual agents hit roadblocks.

```text
               ┌─── Delegate Task ───> [ Agent A (Frontend) ]
               │
[ Orchestrator ] ─── Sync Global State
               │
               └─── Delegate Task ───> [ Agent B (SecOps) ]

```

They are distinct tiers: the Agent Loop manages the relationship between an LLM and its local primitives, while the Orchestration Loop manages the relationships and handoffs between multiple standalone agents.

### When and how are Skills triggered in the loop?

The semantic decision to activate a Skill belongs entirely to the LLM, but the execution mechanism is handled by the agent framework.

1. The agent passes a list of available Skill descriptions into the context.
2. The LLM evaluates the user goal, realizes a Skill fits the intent, and emits a structured request to invoke it.
3. The Agent Loop intercepts this request, unpacks the software script or sub-steps bound to that Skill, routes the inputs through the necessary underlying tools, and feeds the compiled result back into the context.

---

## 🧠 AGENT MEMORY

Your conceptual model is largely accurate, but modern systems split agent memory into three distinct tiers:

| Memory Tier | Architectural Realization | Operational Purpose |
| --- | --- | --- |
| **Long-Term** | Frozen LLM Weights | Deeply baked foundational knowledge, syntax, and reasoning capability gained during training/fine-tuning. |
| **Episodic / Mid-Term** | Vector/Graph Databases (RAG) | Historical context, logs of past interactions, and specialized corporate knowledge bases retrieved on-demand. |
| **Short-Term** | Dynamic Token Context Window | The active thread of conversation, short-lived tool execution results, and immediate variables. |

Conceptualize memory as an operating system: **Short-term memory** is your volatile RAM (fast, highly accessible, but strictly limited by the context window limit). **Mid-term memory** is your local solid-state drive (indexed via vector search, pulled into RAM only when needed). **Long-term memory** is the ROM firmware (completely unchangeable during runtime, guiding how the entire hardware processes logic).

---

## 🛡️ SECURITY

### Context Poisoning & Oversight

Indirect Prompt Injection—where an agent retrieves data via an MCP tool or external file that contains malicious hidden instructions—is exactly how "context poisoning" happens.

```text
[ Malicious Document ] ───> Via Tool Call ───> [ Agent Context Window ] ───> Poisons LLM Execution

```

#### Where to put the Judge LLM?

Evaluating the final compiled prompt via a "Judge LLM" sits at the edge of the **Agent Loop**, right before the payload hits the inference engine.

For an enterprise architecture that remains completely frictionless for developers, the ideal place to insert this security guardrail is an **LLM Gateway (Proxy)**. By putting the compliance and safety layer at the API gateway level, you intercept the raw requests and responses universally, regardless of what framework (LangChain, AutoGen, or custom Python agent loops) the developer runs locally.

```text
[ Developer Agent App ] <───> [ Secure LLM Gateway ] <───> [ Upstream LLM Provider ]
                                     │
                             (Judge LLM / Guard)

```

#### Is an LLM Gateway sufficient, or do we need an MCP Gateway?

While an LLM Gateway catches semantic manipulation (e.g., stopping the LLM from executing a destructive command), it is highly beneficial to deploy an **MCP Gateway** as well. Intermediating calls directly at the MCP layer provides structural isolation and behavioral defense:

* **Data Exfiltration Prevention:** You can inspect data payloads exiting an MCP environment to ensure sensitive records or PII do not leak to public LLM endpoints.
* **Blast Radius Restriction:** An MCP gateway can enforce zero-trust system access rules (e.g., blocking file writes or destructive bash operations on sensitive directories) *before* the command ever executes, bypassing an LLM's tendency to get tricked by clever jailbreaks.

### Code Execution: Tool vs. Intrinsic Capability

Code execution should **never** be realized as an unconstrained intrinsic capability of the agent runtime. It must always be decoupled and modeled explicitly as a sandboxed **Tool (Code Runner)**.

If the agent core executes LLM-generated code natively within its own process space, any context poisoning attack that compromises the LLM results in total system takeover. Isolating code execution inside a micro-container, WASM sandbox, or secure gRPC worker pool ensures that even if an agent is tricked into running a malicious script, the blast radius is strictly contained.

---

## 🧠 LLM vs. Agent Logic Split

The cognitive split maps directly to a **Brain vs. Muscle** paradigm:

* **The Trigger Mechanism (The Brain - LLM):** The intelligence to select, evaluate, and choose to activate a specific Skill resides entirely inside the **LLM**. The LLM reads the environment state, reasons over the descriptions, and decides *what* needs to happen.
* **The Routing Mechanism (The Muscle - Agent Framework):** The functional code that binds, sets up, and executes the code block or script attached to that Skill lives entirely in the **Agent infrastructure**.

The LLM issues the executive order; the agent framework handles the mechanical routing, parameter passing, sandboxing, and execution lifecycle.

---

## 🌐 References

* [Model Context Protocol (MCP) Specification](https://modelcontextprotocol.io/)
* [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
* [Dual LLM Pattern for Secure Tool Execution](https://www.anthropic.com/research/building-effective-agents)
* [Assistants and Agents](https://drive.google.com/file/d/1hucHQ0QpD3mWeIofVjgvl2m4Nnej52Nm/view)
</content>

