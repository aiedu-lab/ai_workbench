# GitHub and Git

## Objective
Learn how to save, track, and share your work safely

---

## Tools
- GitHub
- Git

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
# admin:public_key is required for labsetup.py to upload your
# SSH key via `gh ssh-key add`
gh auth login -s admin:public_key  # GitHub.com → HTTPS → browser
gh auth status  # must exit 0 before continuing

# Already authenticated without admin:public_key? Run instead:
gh auth refresh -h github.com -s admin:public_key
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
`setup/labsetup.py`.

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
export GITHUB_USERNAME=`gh api user -q .login`
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

## Cheat Sheet

Quick-reference commands for collaborating across sessions — with
human peers and AI agents alike.

**Inspect history** — see what happened, in order, across all
branches:

```bash
git log --oneline --graph --decorate --all -10
```

**Create or switch to your personal branch off `main`** — run once
per session; `git branch --list` tells you whether it already
exists:

```bash
git switch main && git pull
git branch --list fix/from_$GITHUB_USERNAME \
  | grep -q . && git switch fix/from_$GITHUB_USERNAME \
  || git switch -c fix/from_$GITHUB_USERNAME main
```

**Compare your branch against `main`** — see what you have that
`main` doesn't, and vice versa:

```bash
git log --oneline --graph --decorate --left-right \
  fix/from_$GITHUB_USERNAME...main
```

**Push, pull, merge, rebase** — keep your branch synced with
`main`:

```bash
git push                # publish your commits to origin
git pull                # fetch + merge latest from your branch
git merge main          # bring main's changes into your branch
git rebase main         # replay your commits on top of main
```

**Create a pull request** — once your branch is ready for review:

```bash
gh pr create --base main --head fix/from_$GITHUB_USERNAME
```

---

## Output
- At least 1 commit per participant
- Clear commit messages
- [Notes](../learnings/session_notes/github.md)
