# Virtual Machine (VM) Setup

## Windows

**WSL**

## Why WSL

### Installation

#### Create a Linux VM

#### Suggested workflow

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
