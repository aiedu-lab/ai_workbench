# OpenClaw CLI

## Setup
Detects  OS, installs Node (if needed), installs OpenClaw, and launches onboarding.
```bash
curl -fsSL https://openclaw.ai/install.sh | bash
```

## Guardrails

* OpenClaw executes whatever APIs are available in your machine. Hence, the safest
  approach is to use it in a Virtual Machine or Docker container with highly 
  restricted network and external API access needed to complete its task.

## Tokenomics
OpenClaw is eager to do its job and greedy in token execution. Intermediate 
access between OpenClaw to LLM provider via a proxy to monitor, track and 
control token usage.
* Reference [💰 Cost Control - API](../provider_cost_control.md#pay-per-use)

## Documentation

[Claude Code (CLI)](https://code.claude.com/docs)
