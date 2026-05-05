# GitHub

## Objective
Learn how to save, track, and share your work safely

---

## Tools
- GitHub

---

## Concept
GitHub is like:
* Google Docs version history
* + backup
* + collaboration

---

## Account Setup

1. Create an account at `github.com/signup` and verify your email.

2. Install the `gh` CLI inside Ubuntu (WSL2 or Dev Container):

```bash
# Add official keyring
curl -fsSL \
  https://cli.github.com/packages/githubcli-archive-keyring.gpg \
  | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
sudo chmod go+r \
  /usr/share/keyrings/githubcli-archive-keyring.gpg

# Add repo to sources
echo "deb [arch=$(dpkg --print-architecture) \
  signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] \
  https://cli.github.com/packages stable main" \
  | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null

# Install
sudo apt update && sudo apt install gh -y
```

3. Authenticate - **required before running `labsetup.py`**:

```bash
gh auth login   # choose GitHub.com → HTTPS → browser
gh auth status  # must exit 0 before continuing
```

---

## Git Identity Setup

Set your name and email so every commit is attributed to you:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Replace `"Your Name"` and `"you@example.com"` with your
actual name and GitHub-registered email address.

---

## SSH Key Setup for GitHub

Keys are named `~/.ssh/<username>_id_ed25519_github` — parallel
to the lab server key `~/.ssh/<username>_id_ed25519` from
`projects/group_meetup/labsetup.py`.

**Generate** (skip if `labsetup.py` has already done this):

```bash
ssh-keygen -t ed25519 \
  -f ~/.ssh/$(whoami)_id_ed25519_github \
  -N "" -C "$(whoami)@github"
```

**Upload** the public key to GitHub:

```bash
gh ssh-key add ~/.ssh/$(whoami)_id_ed25519_github.pub \
  --title "$(whoami)-lab-key"
```

**`~/.ssh/config` entry** (written automatically by `labsetup.py`):

```text
Host github.com
  HostName     github.com
  User         git
  IdentityFile ~/.ssh/<username>_id_ed25519_github
```

**Validate:**

```bash
ssh -T git@github.com
# Expected: Hi <username>! You've successfully authenticated...
```

---

## Set Up VSCode
* Install extension': 
  * [GitHub Pull Requests VSCode Extension](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github)
* Sign in to GitHub in VScode: 
  * Click GitHub icon in the sidebar and "Sign In"

## Set Up Command Line

See [Account Setup](#account-setup) for `gh` CLI installation.

* Verify `gh` is installed and authenticated:

```bash
gh --version
gh auth status
```
---

## Activity (Hands-on)
### GitHub Web
- Open your repo
  - Go to your GitHub repository in browser
  - Edit README.md
  - Add: "GitHub Web section completed"
  - Click: Commit changes 
- Understand commit
  - Commit = save point
  - Message = what changed
- Examples of commit message:
  - Good: "Add GitHub Web section completed"
  - Bad: "update"

### Git Command Line (Local)

**Step 1 — Clone `ai_workbench` into your workspace:**

```bash
export GITHUB_USERNAME="<your_github_username>"
# Set MY_WORKSPACE to your preferred directory.
# Example: ~/ws/sw — choose any path you like.
export MY_WORKSPACE=~/ws/sw
mkdir -p $MY_WORKSPACE
cd $MY_WORKSPACE
git clone git@github.com:aiedu-lab/ai_workbench.git
cd ai_workbench
```

**Step 2 — Create your personal branch off `main`:**

```bash
# All your exercises will live on this branch
git checkout main
git pull
git checkout -b feature/from_$GITHUB_USERNAME
```

**Step 3 — Push branch to origin and set upstream:**

```bash
git push --set-upstream origin feature/from_$GITHUB_USERNAME
```

**Validate — confirm branch is visible on GitHub:**

```bash
gh browse --branch feature/from_$GITHUB_USERNAME
# Opens the branch URL in your browser.
# Confirm it appears under Code → Branches.
```

- Pull latest changes from your branch at any time:

```bash
git pull
```

- Check status before and after edits:

```bash
git status
```

- Commit and push changes:

```bash
git add <file>
git commit -m "feat: <what you changed>"
git push
```
---

### Reflection
- What changed after commit?
- Can you go back to old version?
- Why is this safer than local files?

---

## Output
- At least 1 commit per participant
- Clear commit messages
- [Notes](../learnings/session_notes/github.md)
