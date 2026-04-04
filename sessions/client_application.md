## Client Application

### Setup
- Install Claude Code (API mode)
- Set $5 spend cap
- cd into repo directory
- set up key, validate key, start claude cleanly
```bash
export ANTHROPIC_API_KEY='substitute-with-your-key'
bash tools/claude/check_env.sh
claude logout # ensure no subscription usage
claude
```

### Exercise
- Build local app using agent loop:
  - Prompt → Run → Error → Fix

### Safety
- Kill switch (`Ctrl + C`)
- Limit file scope

### Output
- [Plan](../projects/client_app/plan.md)
- [Notes](../learnings/session_notes/client_app.md)