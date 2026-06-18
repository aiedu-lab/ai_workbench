# Claude Agents and Claude SDK

---

## How Claude Spawns and Coordinates Agents

### The Single-Agent Default

When you run `claude` and type a prompt, by default Claude runs as a
single agent. It receives your message, thinks, calls tools (Bash, Read,
Write, etc.) one at a time, and replies. This is a loop:

```
User prompt
→ Claude thinks (LLM inference)
→ Claude calls a tool (e.g. Bash: "run pytest")
→ Tool result returned to Claude
→ Claude thinks again
→ Claude calls another tool or produces a final answer
→ Repeat until done or max-turns reached
```

Each cycle of this loop is one "turn." The `--max-turns 10` flag caps
how many loops are allowed. Each loop costs tokens (input + output) and
wall-clock time.

---

### When Claude Spawns Multiple Agents

Claude spawns subagents when the task is explicitly parallelizable and
you have given it the right tools and permissions. The decision is made
by the LLM itself — Claude reasons about whether subtasks are
independent and whether parallelizing them would be faster.

The trigger mechanisms are:

**1. The `Task` tool**

Claude Code has a built-in tool called `Task`. When Claude calls it,
it spawns a new independent Claude subprocess with its own context
window, its own tool permissions, and a specific subtask description.
The parent waits for the child to return a result, then continues.

```
Parent Claude
├── calls Task("analyze security in auth.py")  → Child Agent 1
├── calls Task("find edge cases in api.py")    → Child Agent 2
└── calls Task("check CLAUDE.md compliance")   → Child Agent 3
     ↓ all run in parallel ↓
Parent collects results, synthesizes final review
```

**2. The `/code-review` plugin architecture**

The official code-review plugin launches exactly 4-5 specialized agents
in parallel using this pattern. Each agent has a different system prompt
(different specialization) but shares the same diff as input. This
reduces the chance that one blind spot affects all findings.

**3. Explicit prompt instruction**

If your prompt says "spawn 3 agents to check X, Y, and Z in parallel,"
Claude will attempt to do this using the Task tool if it is available
in its tool list.

---

### What Controls Whether 1 or N Agents Are Spawned

| Factor | Effect |
|---|---|
| `Task` tool in allowed tools | Required for subagents — without it, no spawning |
| `--max-turns` cap | Each subagent consumes turns from the parent's budget |
| Prompt instruction | Explicit "in parallel" instruction increases likelihood |
| Task complexity | Claude autonomously decides if parallelism helps |
| `permissionMode` setting | `acceptEdits` or `bypassPermissions` needed for agents to act |
| Token cost awareness | Claude avoids spawning agents for trivial tasks |

The LLM reasons about this. It is not a deterministic rule. If Claude
determines that three subtasks are independent and the Task tool is
available, it will spawn three agents. If the task is sequential (step
2 depends on step 1's output), it will not parallelize.

---

### How Agents Coordinate

Subagents in Claude Code do not share memory or communicate directly.
Coordination happens through the parent:

```
Parent writes a task description → Child reads it from context
Child completes work → returns a text result to parent
Parent reads all child results → synthesizes in its own context
```

There is no shared state, no message passing between siblings, no
distributed coordination protocol. The parent's context window is the
coordination layer. This is why very large multi-agent tasks can
exhaust the parent's context window — it accumulates all child outputs.

Failures are handled by the parent noticing an error in the child's
return value and either retrying the Task call or adjusting its plan.
There is no automatic retry of failed subagents — Claude decides whether
to retry based on the error message in the result.

---

### Access Control in the Agent Hierarchy

Claude Code has a `permissionMode` that applies to all agents in a
session:

- **`default`**: Claude asks for approval before each Bash command and
  file write (what you see in interactive REPL)
- **`acceptEdits`**: Claude can write files without asking, but still
  asks before running Bash commands
- **`bypassPermissions`**: Claude can do everything without asking —
  used in CI/CD pipelines where no human is present

The `--allowedTools` flag whitelists specific commands so they do not
need approval:

```
--allowedTools 'Bash(gh pr diff*),Bash(gh api*),Write'
```

This means: allow any Bash command starting with `gh pr diff` or
`gh api`, and allow the Write tool — everything else requires approval.

Subagents inherit the parent's permission mode and allowed tools. There
is no per-agent RBAC — the access control is session-wide.

---

## Claude SDK

### What the SDK Is

The Claude SDK (`@anthropic-ai/sdk` for Node.js, `anthropic` for Python)
is a thin client library that wraps Anthropic's REST API. It handles:

- Connection management and retries
- Streaming responses
- Authentication header injection
- Request/response serialization

It is **not** a full agent framework. It gives you the raw building
blocks to call Claude, but orchestration, session management, and failure
handling are your responsibility.

The Claude Agent SDK (`@anthropic-ai/claude-agent-sdk`) is a separate,
higher-level library that wraps Claude Code's headless mode. This is
what the GitHub Actions workflow uses internally. It manages the full
agentic loop (tools, turns, streaming) without you having to implement
it yourself.

---

### Basic SDK Usage (Python)

```python
import anthropic

client = anthropic.Anthropic(api_key="sk-ant-api03-...")

# Single turn — simplest case
message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Explain division by zero in Python"}
    ]
)
print(message.content[0].text)
```

```python
# Multi-turn conversation — you manage history yourself
history = []

def chat(user_message):
    history.append({"role": "user", "content": user_message})
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=history
    )
    reply = response.content[0].text
    history.append({"role": "assistant", "content": reply})
    return reply

print(chat("What is 10 divided by 0 in Python?"))
print(chat("How do I guard against it?"))
```

---

### Tool Use via the SDK

The SDK supports giving Claude tools (functions it can call). You
define the tools, Claude decides when to call them, and you execute
them in your code:

```python
import anthropic, json

client = anthropic.Anthropic(api_key="sk-ant-api03-...")

tools = [
    {
        "name": "get_weather",
        "description": "Get current weather for a city",
        "input_schema": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "City name"}
            },
            "required": ["city"]
        }
    }
]

def get_weather(city):
    # Your actual implementation here
    return f"72°F and sunny in {city}"

messages = [{"role": "user", "content": "What is the weather in Tokyo?"}]

while True:
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        tools=tools,
        messages=messages
    )

    # If Claude wants to call a tool:
    if response.stop_reason == "tool_use":
        tool_call = next(b for b in response.content if b.type == "tool_use")
        result = get_weather(**tool_call.input)

        # Feed the result back to Claude
        messages.append({"role": "assistant", "content": response.content})
        messages.append({
            "role": "user",
            "content": [{
                "type": "tool_result",
                "tool_use_id": tool_call.id,
                "content": result
            }]
        })
    else:
        # Claude has a final answer
        print(response.content[0].text)
        break
```

---

### What the SDK Covers and Does Not Cover

| Capability | Basic SDK | Agent SDK | Notes |
|---|---|---|---|
| Single API call | ✅ | ✅ | |
| Streaming responses | ✅ | ✅ | |
| Tool use / function calling | ✅ | ✅ | You implement tool execution |
| Multi-turn conversation | ✅ | ✅ | You manage history array |
| Agentic loop (auto tool calls) | ❌ | ✅ | Agent SDK handles the loop |
| Session persistence across restarts | ❌ | ❌ | You implement (file/DB) |
| Token counting / budget tracking | ✅ | ✅ | Via `usage` field in response |
| Rate limit handling / retries | ✅ | ✅ | Built-in with backoff |
| Context window management | ❌ | ⚠️ Partial | You must truncate history |
| Subagent spawning / orchestration | ❌ | ⚠️ Partial | Via Task tool in prompts |
| RBAC / per-user permissions | ❌ | ❌ | You implement |
| Authentication (OAuth flow) | ❌ | ❌ | You provide the token/key |
| Failure recovery / checkpointing | ❌ | ❌ | You implement |
| Streaming tool results | ✅ | ✅ | |
| Prompt caching | ✅ | ✅ | Via cache-control headers |

---

### Token Visibility

The SDK returns token usage in every response:

```python
response = client.messages.create(...)
print(response.usage.input_tokens)    # tokens in your prompt
print(response.usage.output_tokens)   # tokens in Claude's reply
print(response.usage.cache_read_input_tokens)   # tokens served from cache
print(response.usage.cache_creation_input_tokens) # tokens written to cache
```

You can use this to build a cost tracker, enforce per-user budgets, or
alert when a session is approaching a token limit. The SDK does not do
this automatically — you build it from these numbers.

---

### Context Window Management — Your Responsibility

The SDK does not automatically truncate history. If your conversation
runs long, you will get a `context_window_exceeded` error. The patterns
to handle this:

**Sliding window** — drop oldest messages:
```python
MAX_TOKENS = 180_000  # stay under the 200k limit
while sum(len(m["content"]) for m in history) > MAX_TOKENS:
    history.pop(0)  # drop oldest
```

**Summarize and compress** — ask Claude to summarize old history:
```python
if len(history) > 20:
    summary = client.messages.create(
        model="claude-haiku-4-5-20251001",  # cheap model for summaries
        messages=[{
            "role": "user",
            "content": f"Summarize this conversation in 3 sentences: {history[:10]}"
        }],
        max_tokens=200
    ).content[0].text
    history = [{"role": "user", "content": f"Prior context: {summary}"}] + history[10:]
```

This is exactly what `/compact` does in the Claude Code REPL — it
calls Claude on the old history and replaces it with a summary.

---

### When to Use the SDK vs Claude Code CLI

| Use case | Recommended approach |
|---|---|
| Interactive coding assistant | Claude Code CLI (REPL) |
| CI/CD automation (PR review, tests) | `claude -p` or Agent SDK |
| Building a product on top of Claude | Basic SDK (you control everything) |
| Rapid prototyping with tools | Claude Code CLI or Agent SDK |
| Fine-grained RBAC, multi-tenant | Basic SDK (implement your own) |
| Teaching / classroom demos | Claude Code CLI |
| Production agent with checkpointing | Basic SDK + your persistence layer |

The rule of thumb: use Claude Code CLI when a human is in the loop.
Use the SDK when you are building something for other people to use.

---

## MCP: How External Tools Plug Into Claude Code

### What MCP Is

MCP stands for **Model Context Protocol**. It is an open standard
(published by Anthropic in late 2024) that defines how external tools
and data sources connect to AI agents. Think of it as USB-C for AI —
a single connector standard so that any tool can plug into any AI agent
that speaks the protocol, without custom integration work on either side.

Before MCP existed, if you wanted Claude to read your Google Drive, you
had to write custom code that called the Drive API and formatted the
results into Claude's prompt. Each integration was one-off. MCP
standardizes this: Google Drive publishes an MCP server, Claude Code
speaks the MCP client protocol, and they connect with no custom glue
code.

---

### The Three Components

```
┌─────────────────────┐        MCP Protocol         ┌──────────────────────┐
│   MCP Host          │ ◄──────────────────────────► │   MCP Server         │
│   (Claude Code)     │    JSON-RPC over stdio/SSE   │   (e.g. GitHub,      │
│                     │                              │    Gmail, Postgres)  │
│  - discovers tools  │                              │  - exposes tools     │
│  - calls tools      │                              │  - exposes resources │
│  - passes results   │                              │  - exposes prompts   │
│    back to Claude   │                              │                      │
└─────────────────────┘                              └──────────────────────┘
         │
         ▼
  Claude (LLM) decides
  when to call which tool
```

There are three things an MCP server can expose:

| Concept | What it is | Example |
|---|---|---|
| **Tools** | Functions Claude can call | `create_github_issue`, `send_email` |
| **Resources** | Data sources Claude can read | A file, a database row, a doc |
| **Prompts** | Reusable prompt templates | `/code-review` slash command |

---

### How MCP Servers Connect to Claude Code

There are two transport mechanisms:

**stdio (Standard Input/Output) — Local processes**

The MCP server runs as a child process on your machine. Claude Code
starts it, communicates with it over stdin/stdout using JSON-RPC
messages, and kills it when the session ends. This is used for local
tools — filesystem access, running scripts, local databases.

```bash
# Example: adding a local MCP server to Claude Code
claude mcp add my-database \
  -- python3 /path/to/my_db_server.py

# Claude Code stores this in ~/.claude.json:
# {
#   "mcpServers": {
#     "my-database": {
#       "command": "python3",
#       "args": ["/path/to/my_db_server.py"]
#     }
#   }
# }
```

**SSE (Server-Sent Events) — Remote servers over HTTP**

The MCP server runs somewhere on the internet. Claude Code connects
to a URL and keeps an HTTP connection open. Tool calls and responses
flow over this connection. This is used for cloud services — GitHub,
Gmail, Google Drive, Slack, etc.

```bash
# Example: adding a remote MCP server
claude mcp add github-mcp \
  --transport sse \
  --url https://mcp.github.com/sse

# Claude Code connects to this URL and discovers available tools
# automatically by calling the MCP "list_tools" endpoint
```

---

### What Happens When Claude Uses an MCP Tool

At session start, Claude Code sends a `tools/list` request to every
configured MCP server. Each server replies with its tool definitions
(name, description, input schema). Claude Code assembles all of these
into the list of tools it gives to Claude (the LLM) in its system
prompt.

When Claude decides to call an MCP tool, the flow is:

```
1. Claude (LLM) outputs a tool_use block:
   {
     "type": "tool_use",
     "name": "github_mcp__create_pull_request",
     "input": {"title": "fix: ...", "body": "...", "head": "..."}
   }

2. Claude Code receives this, identifies it as an MCP tool call
   (prefix "github_mcp__" maps to the "github-mcp" server)

3. Claude Code sends a tools/call request to the github-mcp server:
   {
     "method": "tools/call",
     "params": {
       "name": "create_pull_request",
       "arguments": {"title": "fix: ...", ...}
     }
   }

4. The MCP server executes the action (calls GitHub's API)
   and returns the result

5. Claude Code feeds the result back to Claude as a tool_result block

6. Claude continues its reasoning with the result in context
```

This is the same loop as the built-in Bash and Write tools — MCP just
extends the set of callable tools beyond what is built into Claude Code.

---

### Permission Model for MCP Tools

MCP tools go through the same permission gate as built-in tools. In
interactive REPL mode, Claude Code prompts you before calling any MCP
tool:

```
Claude wants to call: github_mcp__create_pull_request
  title: "fix: add input validation"
  body: "Resolves #22"
  head: "fix/demo-validation"

Allow? [y/n/always/never]
```

You can pre-approve specific MCP tools the same way you pre-approve
Bash commands:

```bash
claude --allowedTools "github_mcp__create_pull_request,github_mcp__list_prs"
```

Or in a workflow file:

```yaml
claude_args: "--allowedTools 'Bash(gh pr diff*),github_mcp__get_pull_request'"
```

In non-interactive mode (`-p` or GitHub Actions), you must pre-approve
tools via `--allowedTools` or `permissionMode: bypassPermissions` or
Claude will hit a permission denial — exactly what happened in your
GitHub Actions runs.

---

### Adding MCP Servers to Claude Code — Quick Reference

```bash
# Add a local (stdio) server:
claude mcp add <name> -- <command> [args...]

# Add a remote (SSE) server:
claude mcp add <name> --transport sse --url <url>

# Add with environment variables (e.g. for auth tokens):
claude mcp add github-mcp \
  --transport sse \
  --url https://mcp.github.com/sse \
  --env GITHUB_TOKEN=ghp_...

# List configured servers:
claude mcp list

# Remove a server:
claude mcp remove <name>

# Test a server is reachable:
claude mcp ping <name>
```

Config is stored in `~/.claude.json` under `mcpServers` (user scope)
or in `.claude.json` at the project root (project scope, shared with
the team).

---

### MCP vs Built-in Tools — When to Use Each

| Situation | Use |
|---|---|
| Running shell commands | Built-in `Bash` tool |
| Reading/writing local files | Built-in `Read` and `Write` tools |
| Calling GitHub API | `github-mcp` MCP server |
| Reading Gmail | `gmail-mcp` MCP server |
| Querying a database | Custom stdio MCP server |
| Browsing the web | Built-in `WebFetch` / `WebSearch` tools |
| Spawning subagents | Built-in `Task` tool (see below) |

MCP is for **external integrations**. Built-in tools handle **local
operations**. Both go through the same permission model and appear in
the same tool list that Claude sees.

---

### Building Your Own MCP Server

An MCP server is just a process that speaks JSON-RPC. The official
SDKs make this straightforward:

```python
# Minimal Python MCP server example
from mcp import FastMCP

mcp = FastMCP("my-tool-server")

@mcp.tool()
def check_code_quality(filepath: str) -> str:
    """Run flake8 on a Python file and return findings."""
    import subprocess
    result = subprocess.run(
        ["flake8", filepath],
        capture_output=True, text=True
    )
    return result.stdout or "No issues found"

if __name__ == "__main__":
    mcp.run()  # listens on stdio
```

```bash
# Register it with Claude Code:
claude mcp add code-quality -- python3 /path/to/my_server.py

# Now Claude can call check_code_quality() as a tool in any session
```

For the education lab, this pattern lets you build custom tools tailored
to your course — a tool that checks student code against your rubric,
a tool that queries your course database, a tool that validates a
specific project structure.

---

## The Task Tool and Local Bookkeeping

### Is the Task Tool Provided by Claude CLI?

Yes. `Task` is a **built-in tool** provided by the Claude Code binary
itself, not by any MCP server or plugin. When Claude Code starts a
session, it registers a fixed set of built-in tools and gives their
definitions to Claude (the LLM). The full list appears in the session
init log you saw earlier:

```json
"tools": [
  "Task",
  "Bash",
  "Read",
  "Write",
  "Edit",
  "Glob",
  "Grep",
  "WebFetch",
  "WebSearch",
  ...
]
```

`Task` is always in this list. It is implemented inside the Claude Code
Go/Node binary, not as an external process.

---

### What Happens Locally When Task Is Called

When Claude calls the `Task` tool, Claude Code (the parent process)
does the following — entirely locally, on your machine:

```
1. Claude Code receives the tool_use block from the LLM:
   {
     "type": "tool_use",
     "name": "Task",
     "input": {
       "description": "Check auth.py for security issues",
       "prompt": "You are a security reviewer. Read auth.py and ...",
       "allowedTools": ["Read", "Grep"]
     }
   }

2. Claude Code creates a new subprocess:
   - Spawns a new `claude` process (child)
   - Passes the child a fresh context window with ONLY:
     a. The task description as the user message
     b. The child's own system prompt (set by parent)
     c. The allowed tools list (scoped down from parent's list)
   - The child has NO memory of the parent's conversation

3. The child runs its own agentic loop:
   - Reads files, runs grep, analyses code
   - Produces a final text result
   - Exits

4. Claude Code captures the child's output and returns it to the
   parent Claude as a tool_result:
   {
     "type": "tool_result",
     "tool_use_id": "...",
     "content": "Found 2 security issues: ..."
   }

5. Parent Claude receives all child results, reasons over them,
   and produces a synthesized response
```

---

### The Local Bookkeeping Structures

Claude Code maintains the following in-memory structures for each
active Task invocation:

```
Session (parent)
├── session_id: UUID
├── context_window: [all messages so far]
├── active_tasks: [
│     {
│       task_id: UUID,
│       tool_use_id: "toolu_...",    ← links back to the tool call
│       description: "Check auth.py",
│       subprocess_pid: 12345,
│       allowed_tools: ["Read", "Grep"],
│       permission_mode: inherited from parent,
│       status: running | complete | failed,
│       result: null | "text output"
│     },
│     ...                            ← one entry per parallel task
│   ]
├── permission_mode: default | acceptEdits | bypassPermissions
└── allowed_tools: [...]             ← parent's approved tool list
```

Subagents run in separate processes with separate context windows.
They share nothing with each other. The parent's `active_tasks` array
is the only coordination structure — it tracks which subprocess maps
to which `tool_use_id` so the parent knows which result goes where
when children finish.

There is no shared memory segment, no message queue, no distributed
state. It is a simple parent/child process model with text as the
only communication channel.

---

### Tool Permissions Are Scoped Per Task

When the parent calls `Task`, it can restrict the child's tool access
below its own level:

```
Parent has: ["Task", "Bash", "Read", "Write", "Glob", "Grep"]

Child 1 (security review): ["Read", "Grep"]         ← read-only
Child 2 (fix a bug):       ["Read", "Write", "Edit"] ← can modify files
Child 3 (run tests):       ["Bash(pytest*)"]         ← only run tests
```

This scoping happens by Claude Code intercepting any tool call from a
child that is not in the child's allowed list and returning a permission
denial — the same mechanism that caused your `"This command requires
approval"` errors in the GitHub Actions logs.

The LLM (Claude the model) does not enforce permissions itself — it
just calls whatever tool it thinks is appropriate. Claude Code (the
binary wrapper) intercepts each tool call and checks it against the
allowed list before executing.

---

### Summary: Who Does What

| Component | Role |
|---|---|
| **Claude (LLM)** | Decides when to call Task, what prompt to give it, how many subagents to spawn, how to synthesize results |
| **Claude Code binary** | Spawns subprocesses, routes tool calls, enforces permissions, tracks active tasks, feeds results back |
| **MCP servers** | Provide additional tools beyond built-ins (GitHub, Gmail, custom tools) |
| **Built-in tools** | Bash, Read, Write, Task, Grep, Glob — implemented inside Claude Code binary |
| **Your prompt** | The only way to influence how many agents are spawned and what each one does |

The LLM reasons; Claude Code executes. Permissions and process
management are entirely in the Claude Code binary, not in the model.
This is why the same Claude model behaves differently with different
`permissionMode` settings — the model has no awareness of permissions,
only Claude Code does.

---

## Transport, SSE, and Streaming

---

### Why stdio for Local Tools Instead of HTTP/Loopback?

This is a good design question. The short answer is: **the protocol IS
the same (JSON-RPC 2.0) — only the transport layer differs**. MCP did
not make an inconsistent choice. It standardized the message format and
chose the most appropriate transport for each deployment context.

To understand why, separate the two layers:

```
Layer 1: Message format  →  JSON-RPC 2.0  (same everywhere in MCP)
Layer 2: Transport       →  stdio  (local)  OR  HTTP+SSE  (remote)
```

JSON-RPC 2.0 defines what a tool call message looks like:

```json
{ "jsonrpc": "2.0", "id": 1, "method": "tools/call",
  "params": { "name": "read_file", "arguments": { "path": "/tmp/x.py" } } }
```

This message format is identical whether it travels over a pipe or over
HTTP. MCP is the protocol. stdio and HTTP+SSE are the roads the protocol
drives on.

---

### Why stdio Was Chosen for Local Servers (Not HTTP/Loopback)

**Reason 1 — No port allocation needed**

Binding to a port, even on loopback (127.0.0.1), requires:
- Picking a port number that is not already in use
- OS permission to bind (ports below 1024 require root)
- Handling port conflicts if two MCP servers try the same port

With stdio, the OS hands you two pipes automatically when you fork a
child process. No negotiation, no conflicts, no cleanup.

**Reason 2 — Security is tighter**

A loopback socket can be connected to by *any other process on the same
machine*. If a local MCP server listens on 127.0.0.1:8765, any process
running as any user on that machine can send it tool calls — including
malicious code. You would need authentication (tokens, mTLS) even on
loopback.

A stdio pipe is kernel-enforced IPC: only the parent process (Claude
Code) and the child process (the MCP server) can read or write it.
No other process can intercept it. Security is free.

**Reason 3 — Process lifecycle is automatic**

With stdio: when Claude Code exits (or crashes), the OS closes the
pipes, the child process gets SIGPIPE, and it exits too. No orphaned
server processes.

With HTTP/loopback: if Claude Code exits, the MCP server keeps running,
listening on its port, consuming memory, possibly holding locks.
You need explicit cleanup logic.

**Reason 4 — No HTTP overhead for local calls**

A local tool call over HTTP requires:
- TCP handshake (even on loopback)
- HTTP request parsing
- HTTP response serialization
- Connection keep-alive management

Over stdio: it is a `write()` syscall and a `read()` syscall. For a
tool that runs hundreds of times per session (like `Read` or `Grep`),
this overhead adds up.

**Why HTTP+SSE IS the right choice for remote servers**

For a server running at `https://mcp.github.com`, you have no choice
but HTTP — you cannot share a pipe with a process on another machine.
HTTP also gives you TLS for encryption in transit, standard
authentication headers, and load balancing for free.

So the design is consistent: use the simplest transport that is
appropriate for the deployment distance. Local = stdio. Remote = HTTP.
Same JSON-RPC messages both ways.

---

### What Does SSE (Server-Sent Events) Actually Mean?

SSE is an HTTP feature that keeps a connection open so the server can
push data to the client at any time, without the client polling.

In a normal HTTP request:
```
Client: "GET /data"  →  Server processes  →  Server: "here is the data"
Connection closes.
```

In an SSE connection:
```
Client: "GET /events"  →  Server: "OK, connection open"
...time passes...
Server: "event: tools_changed\ndata: {...}\n\n"   ← pushed without request
...more time passes...
Server: "event: progress\ndata: {\"percent\": 42}\n\n"  ← pushed again
...connection stays open indefinitely...
```

The wire format is plain text, one event per double-newline:
```
event: content_block_delta
data: {"type":"content_block_delta","delta":{"type":"text_delta","text":"Hello"}}

event: content_block_delta
data: {"type":"content_block_delta","delta":{"type":"text_delta","text":" world"}}

event: message_stop
data: {"type":"message_stop"}

```

---

### Can the Server Asynchronously Push Tool List Changes?

Yes — this is explicitly designed into MCP. The spec defines a
notification called `notifications/tools/list_changed` that the server
pushes over the SSE channel when its tool list changes.

The full asynchronous notification flow in MCP's HTTP+SSE transport:

```
Claude Code (client)                    MCP Server (e.g. GitHub)
      │                                        │
      │── GET /sse ──────────────────────────► │  (SSE channel opens)
      │◄── 200 OK, connection open ────────────│
      │                                        │
      │── POST /messages ──────────────────────► │ (tool call - separate HTTP req)
      │◄── 202 Accepted ────────────────────── │
      │                                        │
      │◄── event: message ──────────────────── │ (result pushed over SSE)
      │    data: {"result": ...}               │
      │                                        │
      │  ...later, GitHub deploys a new tool...│
      │                                        │
      │◄── event: notification ─────────────── │ (pushed without any request)
      │    data: {"method":                    │
      │      "notifications/tools/list_changed"}│
      │                                        │
      │── POST /messages ──────────────────────► │ (Claude Code re-fetches tool list)
      │   {"method": "tools/list"}             │
```

Other notifications a server can push asynchronously:
- `notifications/resources/list_changed` — a file or resource changed
- `notifications/progress` — a long-running tool is X% complete
- `notifications/cancelled` — a tool execution was cancelled server-side

This is the key advantage of SSE over plain request/response HTTP: the
server has a channel to proactively inform the client about changes
without the client polling. For a code review tool, this means the MCP
server could push a notification when a background analysis finishes,
rather than having Claude Code poll every second asking "are you done yet?"

---

### What Does Streaming Mean? LLM vs MCP

Streaming means receiving data incrementally as it is produced, rather
than waiting for the entire result before receiving anything.

---

#### LLM Streaming

Without streaming, generating a 500-word response might take 10-15
seconds. The user sees nothing until the entire response is ready, then
it appears all at once.

With streaming, the LLM sends each token (roughly each word-piece) as
soon as it is computed. The user sees the response build up in real time,
word by word. This is what you see in the claude.ai chat interface and
in the Claude Code REPL — text appears as it is generated.

Under the hood, the Anthropic API sends SSE events. Each event carries
a small delta (a chunk of text or a partial tool call):

```
POST https://api.anthropic.com/v1/messages
Content-Type: application/json

{
  "model": "claude-sonnet-4-6",
  "max_tokens": 1024,
  "stream": true,
  "messages": [{"role": "user", "content": "Explain division by zero"}]
}
```

The response is a stream of SSE events:
```
event: message_start
data: {"type":"message_start","message":{"id":"msg_01...","model":"claude-sonnet-4-6",...}}

event: content_block_start
data: {"type":"content_block_start","index":0,"content_block":{"type":"text","text":""}}

event: content_block_delta
data: {"type":"content_block_delta","index":0,"delta":{"type":"text_delta","text":"Division"}}

event: content_block_delta
data: {"type":"content_block_delta","index":0,"delta":{"type":"text_delta","text":" by"}}

event: content_block_delta
data: {"type":"content_block_delta","index":0,"delta":{"type":"text_delta","text":" zero"}}

event: content_block_delta
data: {"type":"content_block_delta","index":0,"delta":{"type":"text_delta","text":" raises"}}

...

event: content_block_stop
data: {"type":"content_block_stop","index":0}

event: message_delta
data: {"type":"message_delta","delta":{"stop_reason":"end_turn"},"usage":{"output_tokens":312}}

event: message_stop
data: {"type":"message_stop"}
```

Each `content_block_delta` carries one small piece of text. You
assemble the full response by concatenating all the delta texts.

---

#### MCP Tool Call Streaming

MCP supports streaming for tool results through the `notifications/progress`
event. A tool that takes a long time (web scrape, large file analysis,
database query) can push incremental results rather than making the
client wait.

```
Claude Code → POST /messages → { "method": "tools/call", "params": { "name": "scrape_site" } }
MCP Server  → 202 Accepted

MCP Server  → SSE event: notification
              { "method": "notifications/progress",
                "params": { "progressToken": "abc", "progress": 10, "total": 100,
                            "message": "Fetched page 1 of 10" } }

MCP Server  → SSE event: notification
              { "method": "notifications/progress",
                "params": { "progressToken": "abc", "progress": 50, "total": 100,
                            "message": "Fetched page 5 of 10" } }

MCP Server  → SSE event: message  (final result)
              { "id": 1, "result": { "content": [{ "type": "text",
                                                   "text": "All 10 pages scraped..." }] } }
```

Claude Code can surface these progress events in the UI (the spinner
and percentage you sometimes see in the REPL during long tool calls).

---

### Concrete Python Code: LLM Streaming Without SDK

To show what the SDK saves you from, here is what streaming looks like
if you do it manually using only `requests`:

```python
import requests, json

response = requests.post(
    "https://api.anthropic.com/v1/messages",
    headers={
        "x-api-key": "sk-ant-api03-...",
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    },
    json={
        "model": "claude-sonnet-4-6",
        "max_tokens": 512,
        "stream": True,
        "messages": [{"role": "user", "content": "Say hi in 3 words"}]
    },
    stream=True
)

full_text = ""
input_tokens = 0
output_tokens = 0

for raw_line in response.iter_lines():
    if not raw_line:
        continue
    line = raw_line.decode("utf-8")

    if line.startswith("event:"):
        continue  # skip the event type line

    if line.startswith("data:"):
        payload = json.loads(line[6:])  # strip "data: "

        if payload["type"] == "content_block_delta":
            chunk = payload["delta"].get("text", "")
            full_text += chunk
            print(chunk, end="", flush=True)  # print as it arrives

        elif payload["type"] == "message_delta":
            output_tokens = payload.get("usage", {}).get("output_tokens", 0)

        elif payload["type"] == "message_start":
            input_tokens = payload["message"]["usage"]["input_tokens"]

print(f"\n\nTokens: {input_tokens} in, {output_tokens} out")
```

This works but requires you to:
- Know the SSE line format
- Know all the event type names
- Manually assemble deltas
- Handle tool_use blocks (which span multiple events and have their
  own delta type)
- Handle error events mid-stream
- Handle reconnection if the connection drops

---

### The Same Thing With the Claude SDK

```python
import anthropic

client = anthropic.Anthropic(api_key="sk-ant-api03-...")

# context manager handles connection, parsing, reassembly, cleanup
with client.messages.stream(
    model="claude-sonnet-4-6",
    max_tokens=512,
    messages=[{"role": "user", "content": "Say hi in 3 words"}]
) as stream:
    # text_stream: already assembled, yields complete words not raw deltas
    for chunk in stream.text_stream:
        print(chunk, end="", flush=True)

# After the stream, get the complete message with full usage stats:
final = stream.get_final_message()
print(f"\nTokens: {final.usage.input_tokens} in, {final.usage.output_tokens} out")
```

The SDK handles:
- Opening the streaming HTTP connection with correct headers
- Parsing raw SSE lines into structured event objects
- Assembling text deltas into a coherent stream
- Assembling tool_use blocks from their partial deltas
- Exposing `stream.text_stream`, `stream.input_json_stream` for tool inputs
- Collecting final usage stats
- Closing the connection on exit or exception

---

### Streaming With Tool Use (SDK Handles the Hard Part)

When Claude uses a tool during streaming, the tool call arrives as
partial deltas too. The input JSON for the tool call arrives character
by character. Without the SDK:

```
event: content_block_start
data: {"type":"content_block_start","index":0,
       "content_block":{"type":"tool_use","id":"toolu_01","name":"read_file","input":{}}}

event: content_block_delta
data: {"type":"content_block_delta","index":0,
       "delta":{"type":"input_json_delta","partial_json":"{\"pat"}}

event: content_block_delta
data: {"type":"content_block_delta","index":0,
       "delta":{"type":"input_json_delta","partial_json":"h\": \"/tm"}}

event: content_block_delta
data: {"type":"content_block_delta","index":0,
       "delta":{"type":"input_json_delta","partial_json":"p/x.py\"}"}}

event: content_block_stop
data: {"type":"content_block_stop","index":0}
```

You must concatenate `partial_json` across events and then parse the
assembled string as JSON to get the tool input. With the SDK:

```python
with client.messages.stream(...) as stream:
    # SDK fires this event when a complete tool call is ready:
    for event in stream:
        if event.type == "input_json":
            print(f"Tool input so far: {event.partial_json}")

    final = stream.get_final_message()
    for block in final.content:
        if block.type == "tool_use":
            print(f"Tool: {block.name}, Input: {block.input}")
            # block.input is already a parsed dict, not a raw string
```

---

### What the Agent SDK Adds on Top

The basic SDK handles one request/response pair, even if that pair is
streamed. The Agent SDK handles the full multi-turn agentic loop with
streaming at every step.

Without Agent SDK (you implement the loop):

```python
# You must implement this loop yourself:
messages = [{"role": "user", "content": prompt}]

while True:
    response = client.messages.create(model=..., messages=messages, tools=tools)

    if response.stop_reason == "tool_use":
        # extract tool calls
        # execute each tool
        # append results to messages
        # loop again
    else:
        break  # Claude has a final answer
```

With Agent SDK (the loop is built in):

```python
from anthropic.agents import run_agent

# SDK runs the loop, calls your tool functions, handles retries:
async for event in run_agent(
    model="claude-sonnet-4-6",
    tools=[my_tool_1, my_tool_2],
    prompt="Review the diff for PR #22"
):
    # Every step of the agent loop streams as an event:
    if event.type == "text":
        print(event.text, end="", flush=True)
    elif event.type == "tool_call":
        print(f"\n[Calling tool: {event.name}]")
    elif event.type == "tool_result":
        print(f"[Tool returned: {event.result[:80]}...]")
    elif event.type == "done":
        print(f"\nFinished. Turns: {event.num_turns}, Cost: ${event.cost:.4f}")
```

The Agent SDK heavy lifting:
- Runs the tool call → execute → feed result → repeat loop
- Streams every step as typed events you can render progressively
- Tracks turn count and enforces max_turns
- Handles permission denials from tools and surfaces them as events
- Aggregates total token usage and cost across all turns
- Manages the growing messages array (truncates if context fills)

---

### Summary Table

| Question | Answer |
|---|---|
| Why stdio for local MCP? | No port conflicts, tighter security (pipe vs socket), automatic lifecycle, lower overhead. JSON-RPC is the same either way. |
| Is JSON-RPC "instead of MCP"? | No — JSON-RPC IS the MCP message format. stdio and HTTP+SSE are just the transports. |
| What does SSE enable? | Server-to-client push without polling. Tool list changes, progress events, and results all arrive over the same open connection. |
| Can server push tool list changes? | Yes — `notifications/tools/list_changed` is a defined MCP notification. |
| What is LLM streaming? | Tokens arrive word-by-word as SSE events instead of all at once. You assemble deltas into full text. |
| What is MCP tool streaming? | Long-running tools push `notifications/progress` events while executing, instead of making the client wait silently. |
| What does the basic SDK provide for streaming? | Parses raw SSE events, assembles text and tool-input deltas, exposes simple iterators, handles errors and cleanup. |
| What does the Agent SDK add? | The full agentic loop — streaming every turn, tool call, result, and completion as typed events without you writing the loop. |

---

## Summary

| Question | Short Answer |
|---|---|
| When does Claude spawn agents? | When the Task tool is available and Claude reasons that parallel subtasks would help |
| How do agents coordinate? | Through the parent's context window — no direct agent-to-agent communication |
| Does the SDK handle RBAC? | No — you implement access control above the SDK layer |
| Does the SDK manage sessions? | No — you maintain the history array and persist it yourself |
| What does the Agent SDK add? | The agentic loop (tool call → execute → feed result back → repeat) so you do not implement it yourself |
