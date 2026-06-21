# Temporal CLI

## Install

### Download
```bash
curl -sSf https://temporal.download/cli.sh | sh
```

### Add temporal to PATH
```bash
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### Start temporal server
```bash
# Starts a local dev server with UI at http://localhost:8233
temporal server start-dev
```

### Validate 

* Installation
```bash
temporal version
```
* Temporal Server Running
  * Open `http://localhost:8233` — success if the Temporal UI loads and
    shows an empty workflow list - OR - 
  * `curl http://localhost:8233` responds.

---

## Python SDK Setup

### Install the SDK
```bash
pip install temporalio
```

### Connect to the local server
```python
import asyncio
from temporalio.client import Client

async def main():
  # Connects to local dev server on default gRPC port 7233
  client = await Client.connect("localhost:7233")
  return client

client = asyncio.run(main())
```

### Define an activity (one agent = one activity)
```python
from temporalio import activity

# Each activity maps to one OpenClaw agent call.
# Scope it to exactly one external API.
@activity.defn
async def poll_members(event_id: str) -> list[str]:
  # Call OpenClaw Poller agent here
  ...

@activity.defn
async def select_venue(responses: list[str]) -> str:
  # Call OpenClaw Selector agent here
  ...

@activity.defn
async def notify_members(venue: str) -> None:
  # Call OpenClaw Notifier agent here
  ...
```

### Define a workflow (orchestrates the activities)
```python
from datetime import timedelta
from temporalio import workflow
from temporalio.common import RetryPolicy

@workflow.defn
class MeetupWorkflow:
  @workflow.run
  async def run(self, event_id: str) -> None:
    # Temporal retries each activity on failure automatically.
    # Start with the poll, then select, then notify.
    responses = await workflow.execute_activity(
      poll_members,
      event_id,
      start_to_close_timeout=timedelta(minutes=5),
    )
    venue = await workflow.execute_activity(
      select_venue,
      responses,
      start_to_close_timeout=timedelta(minutes=2),
    )
    await workflow.execute_activity(
      notify_members,
      venue,
      start_to_close_timeout=timedelta(minutes=2),
    )
```

### Run a worker (registers workflow + activities with Temporal)
```python
import asyncio
from temporalio.client import Client
from temporalio.worker import Worker

async def main():
  client = await Client.connect("localhost:7233")
  worker = Worker(
    client,
    task_queue="meetup-queue",
    workflows=[MeetupWorkflow],
    activities=[poll_members, select_venue, notify_members],
  )
  await worker.run()

asyncio.run(main())
```

### Start a workflow (trigger from CLI or code)
```bash
temporal workflow start \
  --task-queue meetup-queue \
  --type MeetupWorkflow \
  --input '"event-001"'
```

---

## Documentation
* [Temporal - Workflow Orchestrator](https://temporal.io)
* [Temporal Python SDK](https://docs.temporal.io/develop/python)
* [Temporal CLI reference](https://docs.temporal.io/cli)
