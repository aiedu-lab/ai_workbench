# CLAUDE.md

## Do NOT Touch
- The <header> section in index.html — manually maintained
- Any file outside this directory

## Safe to Modify
- The #history section and its CSS
- JavaScript functions prefixed with `ai_`

## Incremental Change Protocol
1. Always read the existing file before proposing changes
2. Propose a diff, do not overwrite
3. Add a comment citing which plan.md step generated the change
