# CLAUDE.md

## Project Rules
- Single file app: ALL code must stay in index.html
- No frameworks, no external libraries, no CDN imports
- Do not create files outside this directory

## Coding Standards
- Add WHY comments on every non-obvious block
- Use semantic HTML (label, section, etc.)
- CSS variables for all colors

## Do NOT Touch
- plan.md
- The <header> section in index.html — manually maintained
- Any file outside projects/web_site/hello_world_claudeCLI/

## Safe to Modify
- The #history section and its CSS
- JavaScript functions prefixed with `ai_`

## Incremental Change Protocol
1. Always read the existing file before proposing changes
2. Propose a diff, do not overwrite
3. Add a comment citing which plan.md step generated the change

## Test Command
python3 -m http.server 8888  # then open http://localhost:8888
