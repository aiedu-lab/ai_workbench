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

## Set Up VSCode
* Install extension': 
  * [GitHub Pull Requests VSCode Extension](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github)
* Sign in to GitHub in VScode: 
  * Click GitHub icon in the sidebar and "Sign In"

## Set Up Command Line
* Install `gh`:
```bash
# add official keyring:
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg

# add repo to sources
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null

# install package
sudo apt update
sudo apt install gh -y
``` 

* Verify installation of `gh`:
```bash
gh --version
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
- Clone repo if not already cloned
```bash
git clone <repo_url>
```
- Pull latest
```bash
git pull
```
- Edit README.md to add "git CLI section completed"
- Check status anytime to find what changed
```bash
# use especially 
#   when you change files 
#   before/after add, commit, push
git status
```
- "Commit" and "push" changes
```bash
git add .
git commit -m "Add GitHub Command Line section completed"
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
