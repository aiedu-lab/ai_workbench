# Claude Code Guardrails

## Scope Rules

- Only operate inside this repository
- Do NOT access:
  - ~/Downloads
  - ~/
  - system directories

## Prompt Constraint (MANDATORY)

Always include:

"Only read and modify files inside this project directory.
Do not access parent directories or external folders."

## File Constraints

- Prefer working in:
  - /projects/
  - /src/

- Avoid:
  - node_modules/
  - large datasets

## Execution Discipline

- Always explain plan before execution
- Limit retries to 3 attempts
- Stop if behavior is unclear
