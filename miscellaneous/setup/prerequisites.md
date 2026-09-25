# Setup Prerequisites

<!-- AI-GENERATED [anthropic:claude-opus-5-5]: Phase 50 Step 50.10
     (plan.md) -->

Complete every row below **before** running
`bash miscellaneous/setup/install.sh`. The installer checks the rows
marked **yes** first and stops, changing nothing, until they are done.
Each row links to the guide with the full steps.

| # | Prerequisite | Who | How | Checked by `install.sh` |
|---|---|---|---|---|
| 1 | Linux shell: WSL2 Ubuntu 24.04 (Windows) or the Dev Container (macOS) | Both | [VM Setup Guide](../tools/VM/setup.md) | no |
| 2 | Python 3.12 or newer (Ubuntu 24.04 ships 3.12) | Both | `python3 -V` | yes |
| 3 | Your sudo password (apt packages, Ollama) | Both | account created in step 1 | no |
| 4 | git installed with a global name and email | Both | [Git Identity Setup](../tools/dev_workbench/github_and_git.md#git-identity-setup) | yes |
| 5 | GitHub account, `gh` installed, `gh auth login -s admin:public_key` | Both | [Account Setup](../tools/dev_workbench/github_and_git.md#account-setup) | yes |
| 6 | This repo cloned; run commands from its root | Both | `git clone https://github.com/aiedu-lab/ai_workbench.git` | implicit |
| 7 | Joined the class Discord and exported the webhook: `export DISCORD_WEBHOOK_URL="<from #meetup-notifications>"` | Both | [Discord setup](instructor/instructor.md#section-2--discord-server-setup-and-student-invite-15-min) | yes |
| 8 | Discord server and webhook created, real `labenv.yaml` values (including the server host key `DOCKER_SERVER_HOST_KEY`), lab server provisioned | Instructor | [Instructor Preflight](instructor/instructor.md) | no |

## After install

These steps come after `install.sh` and need a person, so the
installer cannot do them:

* **Log in to Claude Code:** run `claude` once and follow the prompt
  ([Claude Code CLI](../tools/claude/cli.md)). `install.sh` installs
  the CLI but never logs in for you.
* **Lab-server SSH:** `install.sh` posts your public key to
  `#meetup-notifications`; the lab-server SSH check in
  `validate.sh` passes once the instructor installs it.

Then run `bash miscellaneous/setup/validate.sh` — every check must
show **PASS**.
