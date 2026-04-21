# Instructor Preflight Checklist

Complete every step and its validation before students arrive.
Time required: approximately 60 minutes.

> **Class ID convention:** choose a short unique identifier for
> this class run (e.g. `2026-spring`, `2026-fall-hs`). Replace
> every occurrence of `<CLASS_ID>` below with your chosen value.
> This prevents name collisions when the same instructor runs
> multiple cohorts.

---

## Section 1 — Collect Student Roster (5 min)

Before provisioning anything, collect one row per student in a
local roster file (never committed — contains personal info):

| Full name   | GitHub username | Discord username | Laptop OS   | Admin? | Server acct? |
|-------------|-----------------|------------------|-------------|--------|--------------|
| Alice Smith | `alicesmith`    | `@alice`         | Win11+WSL2  | yes    | yes          |
| Bob Jones   | `bobjones42`    | `@bob`           | macOS 14    | yes    | yes          |

**GitHub username** — validate each one resolves:

```bash
# Replace USERNAME with each student's handle
curl -s https://api.github.com/users/USERNAME \
  | python3 -c "import sys,json; d=json.load(sys.stdin); \
    print('OK:', d['login']) if 'login' in d \
    else print('NOT FOUND')"
```

**Discord username** — new-format handles are `@username` (no
discriminator). Old-format: `username#1234`. Confirm each student
has a Discord account before inviting (Section 2).

**Laptop OS** — accept only `Win11+WSL2` or `macOS 13+`. Students
on older OS versions must upgrade before the lab.

**Admin/sudo** — required for tool installation (Section 4).
Students without admin access cannot complete the exercises.

**Server account** — required for Phase 6 Docker deployment.
Provision in Section 3; mark this column `yes` after that step.

---

## Section 2 — Discord Server Setup and Student Invite (15 min)

Reference: https://support.discord.com/hc/en-us/articles/204849977

- Choose your `<CLASS_ID>` (e.g. `2026-spring`)
- Create a new Discord server named `meetup-lab-<CLASS_ID>`
  > export DISCORD_SERVER="meetup-lab-2026-spring"
  - Server Settings → Overview → Server Name
  - Do NOT reuse a previous class server — name collisions corrupt
    webhook URLs from prior runs
- Create a text channel `#meetup-notifications` inside the server
- Invite each student by Discord username:
  - Server Settings → Invites → Create Invite (no expiry)
  - Or: right-click `#meetup-notifications` → Invite People
  - Send the invite link to each student via a shared doc or
    class chat before the lab day
- Confirm every student has joined and can read
  `#meetup-notifications`:
  - Each student posts a test message: "ready: <their name>"
  - Do not proceed until all students appear in the member list
- Create the webhook (only after all students have joined):
  - Channel Settings → Integrations → Webhooks → New Webhook
  - Name: `Meetup Bot`
  - Copy the webhook URL — and export as `DISCORD_WEBHOOK_URL`
  > **SECRET:** Never commit this URL to any file. The
  > validation step below posts it directly to
  > `#meetup-notifications`. Students join the channel to
  > retrieve it — the channel membership IS the access control.
  > See Section 6 for the student-side export step.
- Validation:

```bash
python3 -c "
import requests, os
url = os.environ['DISCORD_WEBHOOK_URL']
msg = (
  '🔑 Lab DISCORD_WEBHOOK_URL — see Section 6):\n'
  + url
)
r = requests.post(url, json={'content': msg})
print('OK' if r.status_code == 204 else f'FAIL: {r.status_code}')
"
```

Expected: `OK` and a message containing the webhook URL appears
in `#meetup-notifications`, visible only to students who joined.
Students retrieve it from there in Section 6.

---

## Section 3 — Shared Server Provisioning (15 min)

The server is used in Phase 6 (Docker deployment). Provision it
before the lab — students cannot do this themselves.

**Server requirements:**
- OS: Ubuntu 22.04 LTS (recommended) or 24.04
- Reachable from student laptops (public IP or VPN-accessible)
- Inbound ports open: 22 (SSH), 8080 (Temporal UI), 8088 (app)
- Outbound internet access (to pull Docker images, reach Discord)

> **labenv.yaml:** Record the server hostname as `DOCKER_SERVER`
> in `projects/group_meetup/labenv.yaml` so students load it
> automatically via `labsetup.py` (see Section 6).

**Provision the shared account:**

```bash
# On the server (as root or a user with sudo)
sudo useradd -m -s /bin/bash labuser
sudo usermod -aG docker labuser

# Pre-install required tools
sudo apt-get update
sudo apt-get install -y docker.io docker-compose-v2 git python3 pip

# Pre-clone the lab repo
sudo -u labuser git clone \
  https://github.com/<ORG>/ai_education_lab \
  /home/labuser/ai_education_lab
```

**Add each student's SSH public key:**

```bash
sudo -u labuser mkdir -p /home/labuser/.ssh
# Repeat for each student's public key:
echo "ssh-ed25519 AAAA... alice@laptop" \
  | sudo tee -a /home/labuser/.ssh/authorized_keys
sudo chmod 700 /home/labuser/.ssh
sudo chmod 600 /home/labuser/.ssh/authorized_keys
sudo chown -R labuser:labuser /home/labuser/.ssh
```

**Validation — run from each student laptop:**

```bash
ssh labuser@<SERVER_IP> docker ps
```

Expected: empty table header (no error). If any student gets
`Permission denied`, re-check their public key was added correctly.

Mark the `Server acct?` column `yes` in the roster (Section 1)
once every student passes this check.

---

## Section 4 — Student Laptop Preflight (10 min per student)

Students run this themselves before the lab. The instructor
validates by reviewing the output of `preflight_check.py`
(located at `projects/group_meetup/preflight_check.py`).

> **Note:** `preflight_check.py` is created in Phase 4 (Step 4.4).
> Run Phase 4 before distributing this script to students.

**Win11 + WSL2 setup:**

```bash
wsl --status          # Default Version: 2
wsl -l -v             # Ubuntu-22.04 must appear
# If missing:
wsl --install -d Ubuntu-22.04   # requires admin + reboot
```

**macOS setup:**

```bash
xcode-select --install
/bin/bash -c "$(curl -fsSL \
  https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python3 git
```

**Both platforms — required tools:**

```bash
# Python 3.10+
python3 --version           # must be >= 3.10

# Git identity
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# GitHub CLI
# Install: https://cli.github.com
gh auth login               # authenticate with GitHub account

# Claude Code CLI
npm install -g @anthropic-ai/claude-code
claude --version

# Python dependencies for the meetup project
pip install requests pyyaml
```

**Validation — run and share output with instructor:**

```bash
python3 projects/group_meetup/preflight_check.py
```

Every item must show `PASS` before the lab begins.

---

## Section 5 — Create config.yaml for the Lab Group (5 min)

Replace member names with the actual students from the roster
and venue options with locally relevant choices.

```yaml
group: "Thursday Study Squad"
members:
  - name: "Alice"    # replace with actual student names
  - name: "Bob"
  - name: "Carol"
  - name: "David"
options:
  dates:
    - "Thu Apr 24 7pm"   # replace with upcoming Thursdays
    - "Thu May 1 7pm"
    - "Thu May 8 7pm"
  venues:
    - "Library Room A"   # replace with local venues
    - "Coffee Lab"
    - "Online / Video Call"
```

> **labenv.yaml:** Also update `DISCORD_SERVER` in
> `projects/group_meetup/labenv.yaml` to match the server name
> set in Section 2 (e.g. `meetup-lab-2026-spring`).

Save as `config.yaml` in the project directory. Validation:

```bash
python3 -c "import yaml; print(yaml.safe_load(open('config.yaml')))"
```

No errors means the file is valid YAML.

---

## Section 6 — Create .env.example for Students (2 min)

Create `.env.example` in the project root to document the
required variable (placeholder only — never the real value):

```
# Retrieve the real URL from #meetup-notifications (Section 2)
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/REPLACE_ME
```

- Do NOT commit the real URL — `.env` must be in `.gitignore`
- Students retrieve the real URL from the pinned message in
  `#meetup-notifications` posted during Section 2 validation,
  then export it before running `labsetup.py`:

```bash
export DISCORD_WEBHOOK_URL="<paste URL from #meetup-notifications>"
python3 projects/group_meetup/labsetup.py
```

---

## Section 7 — Full End-to-End Smoke Test (10 min)

> **Prerequisite:** Complete Phase 4 (Step 4.6) first.
> That step creates `projects/group_meetup/` with `config.yaml`,
> `poller.py`, `selector.py`, `notifier.py`, and
> `preflight_check.py`. Do not run this section until all five
> files exist and Step 4.6 is marked complete.

Run all three scripts in sequence using the `config.yaml` from
`projects/group_meetup/`:

```bash
cd projects/group_meetup
python3 poller.py    # enter responses for each member manually
python3 selector.py  # check decision.json output
python3 notifier.py  # confirm Discord message arrives
```

Expected: `#meetup-notifications` in `meetup-lab-<CLASS_ID>`
receives a message like:

```
📅 Meetup confirmed!
Date: Thu Apr 24 7pm
Venue: Library Room A
Attending: Alice, Bob, David
```

If this works, the lab is ready. If not, check:
- `responses.json` — did `poller.py` write valid JSON?
- `decision.json` — did `selector.py` pick a date and venue?
- Discord channel — is `DISCORD_WEBHOOK_URL` exported correctly?
