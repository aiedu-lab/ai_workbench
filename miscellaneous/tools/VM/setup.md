# Virtual Machine (VM) Setup

## Windows

**WSL (Windows Subsystem for Linux)** lets you run a full Linux
environment directly on Windows — no separate VM software, no dual
boot. WSL2 uses a real Linux kernel inside a lightweight managed VM,
giving you a native Ubuntu terminal, file system, and networking
alongside your Windows desktop.

### Why WSL

- **Native Linux toolchain** — Python, Git, Docker, and Claude Code
  behave identically to a Linux server; no path or line-ending issues.
- **Zero licence cost** — built into Windows 11 and Windows 10 (2004+);
  no third-party VM licence required.
- **VSCode integration** — the Remote-WSL extension opens any folder
  inside WSL as if it were a local project; the terminal, debugger,
  and extensions all run on Linux.
- **Docker Desktop compatibility** — Docker Desktop for Windows uses
  the WSL2 backend; containers run with near-native performance.
- **Fast startup** — WSL2 starts in seconds; no boot sequence.

### Installation

**Requirements:** Windows 11 (recommended) or Windows 10 version 2004+
with admin rights.

```bash
# 1. Open PowerShell as Administrator and run:
wsl --install

# This installs WSL2 + Ubuntu (latest LTS) in one step.
# Reboot when prompted.

# 2. After reboot, Ubuntu opens automatically to finish setup.
#    Create a UNIX username and password when prompted.

# 3. Verify WSL2 is the default:
wsl --status          # Default Version: 2

# 4. Verify Ubuntu is running:
wsl -l -v             # Ubuntu  Running  2
```

If Ubuntu does not appear after reboot, install it explicitly:

```bash
wsl --install -d Ubuntu-22.04
```

#### Create a Linux VM

WSL2 creates and manages the VM automatically — there is no manual
disk or CPU allocation. The VM starts when you open a WSL terminal
and suspends when all terminals close.

To adjust resource limits, create `%USERPROFILE%\.wslconfig`:

```ini
[wsl2]
memory=8GB
processors=4
swap=2GB
```

Apply the new limits:

```bash
wsl --shutdown     # stops all WSL VMs
wsl                # restarts with new limits
```

Verify resources inside Ubuntu:

```bash
nproc              # CPU cores available
free -h            # RAM and swap
df -h /            # disk space
```

Recommended minimums for this lab: 8 GB RAM, 4 cores, 40 GB disk.

#### Suggested workflow

1. Install WSL2 + Ubuntu-22.04 (steps above).
2. Open VS Code on Windows; install the **Remote - WSL** extension.
3. From the Ubuntu terminal:
   ```bash
   code .           # opens VS Code connected to WSL
   ```
4. Install Python, Git, and lab tools inside Ubuntu (not on Windows):
   ```bash
   sudo apt-get update
   sudo apt-get install -y python3 python3-pip git

   # Claude Code: use the native installer (matches
   # miscellaneous/tools/claude/cli.md) — npm package deprecated
   curl -fsSL https://claude.ai/install.sh | bash
   ```
5. Keep all project files under `~/` (inside WSL), not under
   `/mnt/c/` — WSL I/O on Windows-mounted drives is significantly
   slower.
6. Use `git` inside Ubuntu for all commits; the Windows Git client
   can cause line-ending conflicts with the lab repo.
7. Use snapshots sparingly — WSL2 does not have built-in snapshot
   support; commit frequently to Git instead.

## macOS — Dev Container

**Dev Containers** give macOS students the same Ubuntu environment
as WSL2 on Windows — zero licence cost, no disk allocation, and
native VSCode integration via the same Remote extension pattern.

### Why Dev Containers

- **Zero licence cost** — Docker Desktop is free for personal and
  educational use; no third-party VM licence required.
- **Identical Ubuntu environment** — the container image matches
  the lab server OS; behaviour is the same as WSL2.
- **VSCode-native** — the Dev Containers extension mirrors the
  Remote-WSL workflow exactly; students switch platforms with one
  command change.
- **No disk allocation** — Docker manages storage automatically;
  no fixed-size VM disk to provision.

### Requirements

- macOS 13 (Ventura) or later
- Docker Desktop (free for personal/educational use)
- VSCode with the **Dev Containers** extension

### Installation

1. Install **Docker Desktop** from `docker.com/products/docker-desktop`.
   After install, verify:

```bash
docker --version   # e.g. Docker version 27.x.x
```

2. Install the **Dev Containers** extension in VSCode
   (`ms-vscode-remote.remote-containers`).

3. Clone the lab repo (if not already cloned):

```bash
git clone https://github.com/aiedu-lab/ai_workbench.git
cd ai_workbench
```

4. Run `python3 miscellaneous/setup/student/labsetup.py` once —
on macOS it copies
[devcontainer.json](devcontainer/devcontainer.json) and
[Dockerfile](devcontainer/Dockerfile) from
`miscellaneous/tools/VM/devcontainer/`
(the canonical source) into `.devcontainer/`; on Windows/WSL or
native Linux it removes `.devcontainer/` if present, since the lab
environment is already native there.

5. Open the repo in VSCode:
- For the first time VSCode will detect `.devcontainer/devcontainer.json`
and `.devcontainer/Dockerfile` — a **Create Container** prompt
will appear - click it to create a linux container.
- For subsequent times, a **"Reopen in Container"** prompt will appear — 
click it, or use `Cmd+Shift+P` → **Dev Containers: Reopen in Container**.
- Container creation honors the following:
  - Ubuntu LTS image target is built per the `devcontainer.json`. 
  - `$USER` is provisioned when the container is built - the container's
    primary user matches host username instead of the image default `vscode`.
  - `${localEnv:USER}` is substituted from the host macOS shell's
  - python3.12 and pyyaml is installed 

#### Suggested workflow

1. Install Docker Desktop and verify `docker --version`.
2. Open the lab repo in VSCode → "Reopen in Container".
3. All lab work happens in the Dev Container terminal — Python,
   Git, and SSH behave identically to the lab server.
4. Resource limits (Docker Desktop → Settings → Resources):
   RAM: 8 GB minimum, CPUs: 4 minimum.
5. Use `git` inside the container for all commits.

## Notes for instructors

- Standardize on one Linux distro (Ubuntu LTS version) for the whole class.
- Provide a prebuilt setup guide with exact package versions.
- Encourage everyone to keep the work in Git repo.
- Provide a base VM image to reduce setup time.

## Best practice

For an introduction class, keep the VM lightweight and consistent.  
The goal is to make the environment feel predictable so everyone 
can focus on agent design, prompt workflows, and debugging rather 
than VM configuration.
