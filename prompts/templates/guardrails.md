# Guardrail Prompts (Mandatory)

## Scope Constraint

Only read and modify files inside this project directory.  
Do not access parent directories or external folders.

## File Constraints

- Ignore node_modules and large files  
- Do not scan entire filesystem  

## Execution Discipline

- Always explain plan before execution  
- Do not execute without approval  
- Limit retries to 3 attempts  

## Safety

- Do not delete files  
- Prefer reversible operations  
