# Book Reader

---

## Setup

```text

▼ orchestratior (Piper) job: abc-123
    ├── seth-synthesizer agent-1 (Seth)
    |
    ├── leo-layout-engineer agent-2 (Leo)
    |
    └── quinn-qa-reviewer agent-3 (Quinn)

                FILE                    AGENT                           PROVIDER
                ────                    ─────                           ─────────
▼ orchestratior (Piper)
    |                                                          
    ├──────── detailed-notes.md ────────┐
    |                                   | 
    |                                   ▼                       
    |         mindmap-content.json ──── synthesizer ◄──────►  ┐
    |         |                                               |
    |         └─────────────────────────┐                     |
    |                                   ▼                     |   
    ├         mindmap.html ──────────  mapcreator   ◄──────►  | ◄────►  LLM (Anthropic)
    |         |                                               |
    |         └─────────────────────────┐                     |   
    |                                   ▼                     |   
    └────────────────────────────────► validator    ◄──────►  ┘
```

---

## Multiagents via Claude CLI

- **Orchestrator (Piper)** = a shell script that wires the pipeline, 
checks output validity, handles retries, sequences the
agent and triggers next agent. In this case, passing outputs as inputs to
the next agent. Piper is a shell script in this case.
* Each agent is a **separate Claude CLI process** with a scoped system prompt 
defining its role, input contract, and output contract. 
* Agents hand off work via local files — not via network calls to each other.

### Mechanisms

Key Arguments:
- **System prompt** = the agent's standing instructions (its "job description")
- **Input files** = the current task context
- **Output contract** = what type it must produce for the next agent
- **Output file** = what file it produces for the next agent

#### Orchestrator

The `piper` orchestrator is a shell script that simply waits for the 
process to exit, checks the exit code `$?`, and decides what to do 
next. This is standard OS process synchronization.
* Claude Code's `--system-print-file` flag or a `CLAUDE.md` file 
injects a system prompt.
* You run multiple Claude CLI processes, each with a different 
system prompt = different agent.
* Claude Code's `--print` makes Claude behave like any Unix command — it 
runs, produces output, and exits - a basis for sequential coordination:
```bash
claude --print "your task" \
  --system-prompt-file agents/seth.md < input.txt > output.txt
echo "Exit code: $?"   # 0 = success, non-zero = failure
```

#### Solution - Pulling it all together
Piper code example - from `ai-mindmap.md` / `README-mindmap-system.md` reference:

```bash
#!/bin/bash
# piper.sh — the orchestrator (plain shell, no LLM)

# Step 1: Run Agent-1 Seth — blocks here until Seth exits
  claude --print "Synthesize content from detailed-notes.md into mindmap-content.json"      \
         --system-prompt-file agents/seth-content-synthesizer.md                            \
         --output-format json                                                               \
         --output mindmap-content.json

if [ $? -ne 0 ]; then
  echo "Seth failed — aborting pipeline"; exit 1
fi

# Step 1: Check Seth's exit code — ONLY proceed if Seth succeeded
claude --print "Render mindmap-content.json into mindmap.html using mindmap-layout.json"    \
        --system-prompt-file agents/leo-layout-engineer.md                                  \
        --output mindmap.html

if [ $? -ne 0 ]; then
  echo "Leo failed — aborting pipeline"; exit 1
fi

# Step 3: Run Agent-3 Quinn — blocks until Quinn exits
claude -p "Review mindmap.html and report issues"                                           \
        --system-prompt-file agents/quinn-qa-reviewer.md                                    \
        --output qa-report.md

if [ $? -ne 0 ]; then
  echo "Quinn failed"; exit 1
fi

echo "Pipeline complete. Job: $JOB_ID"
```

---

