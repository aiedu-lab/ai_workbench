# VSCode

## Setup
* [VSCode](https://code.visualstudio.com/download)
  - During install, check "Add to PATH"
  - After install, open VSCode and install:
* [Remote-WSL Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl) (Microsoft) - if using WSL
* [Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) (Microsoft)
* [Claude Code Extension](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code) (Anthropic)

## Validation
* Open VSCode and connect to Remote-WSL
* Open a folder in WSL
* Open a terminal in VSCode
* Run: `claude --version`
* Check that Claude is working

## Guardrails
* If using WAL, always work inside WSL directory `~/` rather than 
  Windows paths `/mnt/c/...` as cross-filesystem I/O is significantly 
  slower and may cause permission issues.