# VSCode

## Setup
* [VSCode](https://code.visualstudio.com/download)
  - During install, check "Add to PATH"
  - After install, open VSCode and install:
* [Remote-WSL Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl) (Microsoft) - if using WSL
* [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) (Microsoft)
* [Claude Code Extension](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code) (Anthropic)
* [GitHub Extension](https://code.visualstudio.com/docs/sourcecontrol/github)

## Validation
* Change Directory to Your WS: Open a folder in WSL
* Open VSCode: and connect to Remote-WSL `code .`
* Check Claude
  * Works on command line? Run: `claude --version`
  * Claude Extension Works? chat `just act as a conversational agent as "say Hello"
  * GitHub Works on command line? Run `git branch --all` shows you are on a branch
  * GitHub Extension Works? `git pull`, `git push`, etc. works on the branch
## Guardrails
* If using WAL, always work inside WSL directory `~/` rather than 
  Windows paths `/mnt/c/...` as cross-filesystem I/O is significantly 
  slower and may cause permission issues.
