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
  no Parallels or VirtualBox licence required.
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

```
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
   npm install -g @anthropic-ai/claude-code
   ```
5. Keep all project files under `~/` (inside WSL), not under
   `/mnt/c/` — WSL I/O on Windows-mounted drives is significantly
   slower.
6. Use `git` inside Ubuntu for all commits; the Windows Git client
   can cause line-ending conflicts with the lab repo.
7. Use snapshots sparingly — WSL2 does not have built-in snapshot
   support; commit frequently to Git instead.

## macOS

**Parallels Desktop** is the most convenient and beginner-friendly option. 
It provides the smoothest setup, strong macOS integration, and the least 
friction for students.

### Why Parallels Desktop

- Easiest for beginners.
- Strong integration with macOS.
- Good performance on Apple Silicon Macs.
- Better suited for classroom use than more technical VM tools.

### Installation

1. Download **Parallels Desktop** from the official Parallels website.
2. Open the installer and follow the prompts.
3. Approve any macOS permission requests.
4. Launch Parallels Desktop after installation.

#### Create a Linux VM

1. Open Parallels Desktop.
2. Click **+** to create a new virtual machine.
3. Choose **Install Windows or another OS from a DVD or image file**.
4. Select Ubuntu ISO - noble 24.04 LTS or later.
5. Allocate resources:
   - CPU: 6 cores - `nproc`
   - RAM: 16 GB, SWAP 4GB - `free -h`
   - Disk: 64 GB - `df -h`
6. Start the VM and complete the Linux installation.
7. Install Parallels Tools when prompted.

#### Suggested workflow

1. Install Parallels Desktop.
2. Install Ubuntu inside the VM.
3. Install Python, Git, and VS Code inside the VM or use shared folders from macOS.
4. Set up Claude-based workflows and your OpenClaw tooling inside the Linux environment.
5. Use snapshots or restore points before major experiments.

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
