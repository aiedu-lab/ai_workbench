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

## Summary

| Question | Short Answer |
|---|---|
| When does Claude spawn agents? | When the Task tool is available and Claude reasons that parallel subtasks would help |
| How do agents coordinate? | Through the parent's context window — no direct agent-to-agent communication |
| Does the SDK handle RBAC? | No — you implement access control above the SDK layer |
| Does the SDK manage sessions? | No — you maintain the history array and persist it yourself |
| What does the Agent SDK add? | The agentic loop (tool call → execute → feed result back → repeat) so you do not implement it yourself |
