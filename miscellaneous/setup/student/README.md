# Lab Environment Setup

**This directory is lab infrastructure, not an exercise.** Students
run these scripts to provision their environment; there is no
`plan.md` here and nothing in this directory is meant to be solved
or submitted.

## Reference
* [Dev Workbench setup](../sessions/dev_workbench.md)

## Contents
* `labsetup.py` — idempotent, OS-aware lab environment setup script
* `preflight_check.py` — pre-lab environment validation
* `config.yaml` / `labenv.yaml` — lab environment configuration
* `poller.py` / `selector.py` / `notifier.py` — Group Meetup
  Organizer pipeline components used by the multi-agent exercises
  in `projects/client_multiagent/` and `projects/server_multiagent/`

## Usage
Complete the [Setup Prerequisites](../prerequisites.md) first. Then
run from the repo root; the wrappers in `miscellaneous/setup/` build
the `.venv` these scripts need and then run them:
```bash
export DISCORD_WEBHOOK_URL="<paste from #meetup-notifications>"
bash miscellaneous/setup/install.sh    # runs labsetup.py
bash miscellaneous/setup/validate.sh   # runs preflight_check.py
```
