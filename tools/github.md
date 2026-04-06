# GitHub (15 mins)

## Objective
Learn how to save, track, and share your work safely

---

## Tools
- GitHub

---

## Concept
GitHub is like:
- Google Docs version history
- + backup
- + collaboration

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
