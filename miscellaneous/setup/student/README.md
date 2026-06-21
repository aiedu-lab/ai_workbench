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
```bash
python3 setup/labsetup.py
python3 setup/preflight_check.py
```
