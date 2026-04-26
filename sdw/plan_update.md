# Plan: Phase 14 — Improve Setup, Skills, and RAG

## Section Identified

**File:** `sdw/prompt_history.md`, lines 415–510
**Heading:** `## Improve Setup Skill RAG`

**Key contents (five task areas):**
1. **Student Development System Setup** — create `sessions/development_system.md`; add it to README.md after Instructor Preflight row
2. **Move tool setup files** — `tools/github.md`, `tools/vscode.md`, `tools/provider_cost_control.md` → `tools/dev_system/`; migrate student-facing laptop setup content from `sessions/instructor.md` Section 4
3. **GitHub SSH Setup** — expand `tools/dev_system/github.md` with account + SSH key instructions; add GitHub SSH key generation and `.ssh/config` entry to `labsetup.py`; add GitHub SSH + git identity checks to `preflight_check.py`
4. **macOS Dev Container** — replace Parallels VM section in `tools/VM/setup.md` with Dev Container (VSCode + Docker Desktop); add platform overview to `sessions/instructor.md`
5. **Skills/RAG/Embeddings reinforcement** — add Skills callback in `sessions/client_agent.md`; add "Why Not Traditional RAG?" callout + cross-reference in `sessions/llm_wiki.md`; add local embedding stretch goal (`nomic-embed-text`) to `sessions/ai_local.md`
6. **Consistency check** — cross-file link audit across all modified files

---

## Context

Phase 14 implements `sdw/prompt_history.md §## Improve Setup Skill RAG`
(lines 415–510). Phase 12 (the current highest phase) left `tools/dev_system/`
as an empty directory; Phase 14 populates it. This phase also closes two
conceptual gaps: (a) students had no dedicated session for laptop setup, and
(b) Skills/Embeddings/RAG concepts introduced in Advanced Prompting were
never referenced in later sessions.

**Current state of key files:**

| File | Status |
|------|--------|
| `tools/dev_system/` | EXISTS — empty |
| `tools/github.md` | EXISTS — source for move |
| `tools/vscode.md` | EXISTS — source for move |
| `tools/provider_cost_control.md` | EXISTS — source for move |
| `sessions/development_system.md` | DOES NOT EXIST |
| `tools/VM/setup.md` | EXISTS — Windows (WSL2) + macOS (Parallels) |
| `sessions/instructor.md` | EXISTS — 8 sections; Section 4 = Student Laptop Preflight |
| `projects/group_meetup/labsetup.py` | EXISTS — SSH key/config pattern from Phase 12 |
| `projects/group_meetup/preflight_check.py` | EXISTS — PASS/FAIL check pattern from Phase 12 |

---

## Execution Steps

### Phase 14.1 — Student Development System Session

**Target files:** `sessions/development_system.md` (NEW), `README.md`

**Step 14.1.1 — Create `sessions/development_system.md`**

Six sections (cross-references only — no duplicated content):

- **Section 0 — Platform Overview:** table showing Win11→WSL2 and
  macOS→Dev Container both connecting to VSCode; shared SSH to `ai-lab`
- **Section 1 — VM / Container Setup:** link to `tools/VM/setup.md`
- **Section 2 — VSCode Setup:** link to `tools/dev_system/vscode.md`
- **Section 3 — GitHub Account and SSH Setup:** link to `tools/dev_system/github.md`
- **Section 4 — LLM Provider Setup:** links to `tools/claude/cloud.md`
  and `tools/dev_system/provider_cost_control.md`
- **Section 5 — Run Lab Setup Script:** two-step workflow commands:
  ```bash
  export DISCORD_WEBHOOK_URL="<paste from #meetup-notifications>"
  python3 projects/group_meetup/labsetup.py
  python3 projects/group_meetup/preflight_check.py
  ```

Validation:
```bash
python3 -c "
from pathlib import Path
t = Path('sessions/development_system.md').read_text()
for s in ['Section 0', 'tools/dev_system/', 'labsetup.py', 'preflight_check.py']:
    assert s in t, f'Missing: {s}'
print('PASS')
"
```

**Step 14.1.2 — Add `development_system.md` row to `README.md` agenda**

Insert immediately after the `instructor.md` row:
```
| [**Development System Setup**](sessions/development_system.md) | Before lab | [VM/WSL2/DevContainer](tools/VM/setup.md), [VSCode](tools/dev_system/vscode.md), [GitHub](tools/dev_system/github.md) | 30 mins |
```

Validation: `grep -n "development_system" README.md` — one match,
immediately below the `instructor.md` row.

---

### Phase 14.2 — Migrate Tool Files to `tools/dev_system/`

**Target files:**
- `tools/github.md` → `tools/dev_system/github.md`
- `tools/vscode.md` → `tools/dev_system/vscode.md`
- `tools/provider_cost_control.md` → `tools/dev_system/provider_cost_control.md`
- All files with inbound links to the old paths

**Step 14.2.1 — Move `tools/github.md` → `tools/dev_system/github.md`**
```bash
git mv tools/github.md tools/dev_system/github.md
```

**Step 14.2.2 — Move `tools/vscode.md` → `tools/dev_system/vscode.md`**
```bash
git mv tools/vscode.md tools/dev_system/vscode.md
```

**Step 14.2.3 — Move `tools/provider_cost_control.md` → `tools/dev_system/provider_cost_control.md`**
```bash
git mv tools/provider_cost_control.md tools/dev_system/provider_cost_control.md
```

**Step 14.2.4 — Fix all inbound links broken by the moves**

Files to update (known references):

| File | Old prefix | New prefix |
|------|-----------|------------|
| `sessions/client_application.md` | `../tools/provider_cost_control.md` | `../tools/dev_system/provider_cost_control.md` |
| `sessions/server_multiagent.md` | `../tools/provider_cost_control.md` | `../tools/dev_system/provider_cost_control.md` |
| `sessions/web_site.md` | `../tools/provider_cost_control.md` | `../tools/dev_system/provider_cost_control.md` |
| `tools/claude/cli.md` | `../provider_cost_control.md` | `../dev_system/provider_cost_control.md` |
| `tools/openai/codex_cli.md` | `../provider_cost_control.md` | `../dev_system/provider_cost_control.md` |
| `tools/openclaw/cli.md` | `../provider_cost_control.md` | `../dev_system/provider_cost_control.md` |
| Any file referencing `tools/github.md` or `tools/vscode.md` | update to `tools/dev_system/` path |

Validation — zero old-path references remain:
```bash
grep -rn "tools/github\.md\|tools/vscode\.md\|tools/provider_cost_control\.md" \
  sessions/ tools/ README.md
# expected: no output
```

**Step 14.2.5 — Move student-facing setup content from `sessions/instructor.md` Section 4 to `sessions/development_system.md`**

- Move Win11+WSL2 and macOS platform setup blocks into
  `sessions/development_system.md` Sections 1–2
- Replace moved content in `instructor.md` Section 4 with:
  > "Students complete platform and tool setup independently using
  > [Development System Setup](development_system.md) before the
  > lab day. This section covers the instructor's validation gate only."
- Keep `preflight_check.py` run instruction + "Every item must show PASS"
  in Section 4 — that is the instructor validation step, not student content.

Validation:
```bash
grep -c "development_system" sessions/instructor.md  # >= 1
grep -c "wsl --status" sessions/development_system.md  # 1
```

---

### Phase 14.3 — GitHub SSH Setup

**Target files:** `tools/dev_system/github.md`,
`projects/group_meetup/labenv.yaml`,
`projects/group_meetup/labsetup.py`,
`projects/group_meetup/preflight_check.py`

**Step 14.3.1 — Expand `tools/dev_system/github.md` with Account + SSH Setup**

Add two new top-level sections before the existing content:

**## Account Setup**
- Create account at `github.com/signup`; verify email
- Install `gh` CLI (if not already covered); `gh auth login`

**## SSH Key Setup for GitHub**
- Key naming: `~/.ssh/{username}_id_ed25519_github`
  (parallel to lab key `~/.ssh/{username}_id_ed25519`)
- Generation command (if not using `labsetup.py`):
  ```bash
  ssh-keygen -t ed25519 -f ~/.ssh/$(whoami)_id_ed25519_github -N "" -C "$(whoami)@github"
  ```
- Upload via `gh`: `gh ssh-key add ~/.ssh/$(whoami)_id_ed25519_github.pub --title "$(whoami)-lab-key"`
- `.ssh/config` entry (written by `labsetup.py`):
  ```
  Host github.com
    HostName github.com
    User     git
    IdentityFile ~/.ssh/<username>_id_ed25519_github
  ```
- Validation: `ssh -T git@github.com` → `Hi <username>! You've successfully authenticated...`

**Step 14.3.2 — Add `GITHUB_USERNAME` to `projects/group_meetup/labenv.yaml`**
```yaml
# GitHub username for SSH key upload and git operations.
GITHUB_USERNAME: "<your-github-username>"
```
Same placeholder-detection pattern as `DOCKER_SERVER_ID`.

**Step 14.3.3 — Add GitHub SSH setup to `projects/group_meetup/labsetup.py`**

New constants (follow existing lab-SSH naming exactly):
```python
GITHUB_KEYS = ("GITHUB_USERNAME",)
GITHUB_HOST_ALIAS = "github.com"
GITHUB_SSH_KEY = SSH_DIR / f"{_USERNAME}_id_ed25519_github"
```

New functions (identical signature pattern to Phase 12 functions):
- `_generate_github_ssh_key()` — idempotent (skip if `GITHUB_SSH_KEY.exists()`)
- `_write_github_ssh_config(env)` — idempotent (scan for `Host github.com`; skip if found)
- `_validate_github_ssh()` — WARN (not exit): check `"successfully authenticated"` in
  `stderr` of `ssh git@github.com` (GitHub always exits 1 even on success; string check is correct)

Wire into `main()`: guarded by `github_real` flag (all `GITHUB_KEYS` are non-placeholder).

Validation:
```bash
python3 -c "
import ast, pathlib
src = pathlib.Path('projects/group_meetup/labsetup.py').read_text()
fns = {n.name for n in ast.walk(ast.parse(src)) if isinstance(n, ast.FunctionDef)}
req = {'_generate_github_ssh_key', '_write_github_ssh_config', '_validate_github_ssh'}
print('PASS' if not req - fns else f'FAIL: {req - fns}')
"
```

**Step 14.3.4 — Add GitHub SSH + git identity checks to `projects/group_meetup/preflight_check.py`**

New constant:
```python
GITHUB_SSH_KEY = Path.home() / ".ssh" / f"{getpass.getuser()}_id_ed25519_github"
```

New check functions:
- `check_github_ssh_key()` — assert `GITHUB_SSH_KEY.exists()`
- `check_github_ssh()` — run `ssh -o BatchMode=yes -o ConnectTimeout=10 git@github.com`;
  success = `"successfully authenticated"` in `result.stderr`
- `check_git_identity()` — assert `git config --global user.name` and
  `git config --global user.email` are both non-empty

Wire into `main()` after existing SSH checks.

Validation:
```bash
python3 -c "
import ast, pathlib
src = pathlib.Path('projects/group_meetup/preflight_check.py').read_text()
fns = {n.name for n in ast.walk(ast.parse(src)) if isinstance(n, ast.FunctionDef)}
req = {'check_github_ssh_key', 'check_github_ssh', 'check_git_identity'}
print('PASS' if not req - fns else f'FAIL: {req - fns}')
"
```

---

### Phase 14.4 — macOS Dev Container Setup

**Target files:** `tools/VM/setup.md`, `sessions/instructor.md`

**Step 14.4.1 — Replace macOS Parallels section in `tools/VM/setup.md` with Dev Container**

Replace the entire `## macOS` section (full replacement, not additive).

New `## macOS — Dev Container` section covers:
- **Why Dev Containers:** zero licence cost; Ubuntu env identical to
  lab server; no VM disk allocation; VSCode-native (same Remote extension pattern as WSL2)
- **Requirements:** macOS 13+, Docker Desktop (free for personal/educational use),
  VSCode with Dev Containers extension
- **Installation:** install Docker Desktop, verify `docker --version`;
  install VSCode Dev Containers extension; clone repo; open in VSCode →
  "Reopen in Container" prompt (or `Cmd+Shift+P`)
- **`devcontainer.json`** (to be committed at `.devcontainer/devcontainer.json`):
  ```json
  {
    "image": "mcr.microsoft.com/devcontainers/python:3.12-bullseye",
    "features": {
      "ghcr.io/devcontainers/features/git:1": {},
      "ghcr.io/devcontainers/features/node:1": {"version": "lts"}
    },
    "postCreateCommand": "pip install requests pyyaml"
  }
  ```
- **Suggested workflow:** all lab work in Dev Container terminal;
  SSH keys generated inside container; resource limits: 8 GB RAM, 4 CPUs in
  Docker Desktop → Settings → Resources

Validation:
```bash
grep -c "Dev Container" tools/VM/setup.md  # >= 3
grep -c "Parallels" tools/VM/setup.md      # 0
```

**Step 14.4.2 — Update `sessions/instructor.md` Section 0 Parallels reference**

Change the section 0 reference line from:
> "full instructions for Windows (WSL2) and macOS (Parallels) VMs"

To:
> "full instructions for Windows (WSL2) and macOS (Dev Container) environments"

**Step 14.4.3 — Add Platform Architecture overview to `sessions/instructor.md`**

Add new Section 8 at the end of the file:

**## Section 8 — Student Platform Architecture**

Table:

| Layer | Win11 | macOS |
|-------|-------|-------|
| Frontend | VSCode native | VSCode native |
| Dev environment | WSL2 Ubuntu | Dev Container Ubuntu |
| Server access | SSH → ai-lab | SSH → ai-lab (identical) |

Framing note:
> "Students on Win11 use VSCode → Remote-WSL → Ubuntu. Students on macOS
> use VSCode → Dev Containers → Ubuntu. Both produce an identical Ubuntu
> shell. The Docker server (Section 3) is accessed via SSH from both."

Validation:
```bash
grep -c "Parallels" sessions/instructor.md  # 0
grep -c "Section 8" sessions/instructor.md  # 1
```

---

### Phase 14.5 — Skills and RAG Reinforcement

**Target files:** `sessions/client_agent.md`, `sessions/llm_wiki.md`, `sessions/ai_local.md`

**Step 14.5.1 — Add Skills callback to `sessions/client_agent.md` Exercise A**

After the Exercise A "Prompt Draft" block, add a **"Turn the Prompt into a Skill"** subsection:

> "The File Organizer prompt has the `Context/Task/Constraints/Output`
> structure from [Advanced Prompting — §1 Skills](prompting_advanced.md#1-skills-reusable-prompts).
> Save it as `file-organizer-skill` in `projects/skill.md` so you can
> reuse it across sessions with a single invocation."

Add a Reflection bullet:
> "How does `file-organizer-skill` compare to `professional-rewrite-skill`
> from Advanced Prompting? What makes a prompt worth naming as a skill?"

Validation:
```bash
grep -c "file-organizer-skill" sessions/client_agent.md    # >= 2
grep -c "prompting_advanced" sessions/client_agent.md      # 1
```

**Step 14.5.2 — Reinforce LLM Wiki vs RAG in `sessions/llm_wiki.md`**

Immediately after the existing "The Core Concept" bullet block, add a
callout box:

> **Why not just build a RAG pipeline?**
> Traditional RAG (covered in [Advanced Prompting — §8 Embeddings & RAG](prompting_advanced.md#embeddings--retrieval-augmented-generation-rag))
> requires chunking documents, generating embeddings, a vector database,
> and retrieval code. The LLM Wiki skips all of that: the LLM organizes
> knowledge into human-readable, diff-able, Obsidian-navigable markdown.
> For a personal knowledge base the LLM Wiki is simpler and more
> maintainable. RAG remains the right choice when your corpus exceeds
> what a prompt context window can hold and you need at-scale retrieval.

Validation:
```bash
grep -c "prompting_advanced" sessions/llm_wiki.md    # >= 1
grep -c "Traditional RAG" sessions/llm_wiki.md        # >= 2
```

**Step 14.5.3 — Add local embedding stretch goal to `sessions/ai_local.md`**

Add after the existing "Stretch Goal — Connect to the Main Project" section,
titled **"Stretch Goal B — Semantic Similarity with Local Embeddings"**:

```bash
ollama pull nomic-embed-text
```

5-line Python demo (uses only `ollama` + `numpy`; same sentence pair as
Advanced Prompting §8 for conceptual continuity):
```python
import ollama, numpy as np

def embed(text): return ollama.embeddings(model="nomic-embed-text", prompt=text)["embedding"]

a, b, c = map(np.array, [
  embed("The meeting is at 3pm"),
  embed("What time is my next event?"),
  embed("I enjoy hiking on weekends"),
])
def cosine(x, y): return float(np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y)))
print(f"related:   {cosine(a, b):.2f}")   # ~0.6–0.8
print(f"unrelated: {cosine(a, c):.2f}")   # ~0.1–0.2
```

Reflection:
> "This is the same cosine similarity from
> [Advanced Prompting — §8](prompting_advanced.md#embeddings--retrieval-augmented-generation-rag),
> but running entirely offline. How does local embedding quality compare?"

Validation:
```bash
grep -c "nomic-embed-text" sessions/ai_local.md     # >= 2
grep -c "prompting_advanced" sessions/ai_local.md   # 1
```

---

### Phase 14.6 — Consistency Check for Phase 14

- [ ] **Step 14.6.1:** README.md — `development_system.md` row present,
  positioned immediately after `instructor.md` row

- [ ] **Step 14.6.2:** `tools/dev_system/` contains exactly three files:
  `github.md`, `vscode.md`, `provider_cost_control.md`; original
  `tools/github.md`, `tools/vscode.md`, `tools/provider_cost_control.md`
  no longer exist

- [ ] **Step 14.6.3:** Zero broken references to old tool paths:
  ```bash
  grep -rn "tools/github\.md\|tools/vscode\.md\|tools/provider_cost_control\.md" \
    sessions/ tools/ README.md  # no output
  ```

- [ ] **Step 14.6.4:** `tools/VM/setup.md` — "Parallels" count = 0;
  "Dev Container" count >= 3

- [ ] **Step 14.6.5:** `sessions/instructor.md` — "Parallels" count = 0;
  Section 8 present; Section 4 redirects to `development_system.md`

- [ ] **Step 14.6.6:** `tools/dev_system/github.md` — contains
  `id_ed25519_github`, `gh ssh-key add`, `ssh -T git@github.com`

- [ ] **Step 14.6.7:** `labsetup.py` contains all three GitHub SSH functions;
  `preflight_check.py` contains all three GitHub checks

- [ ] **Step 14.6.8:** `sessions/client_agent.md` contains
  `file-organizer-skill` and back-reference to `prompting_advanced.md`

- [ ] **Step 14.6.9:** `sessions/llm_wiki.md` contains "Why Not Traditional
  RAG?" callout and forward reference to `prompting_advanced.md`

- [ ] **Step 14.6.10:** `sessions/ai_local.md` contains `nomic-embed-text`
  and reference to `prompting_advanced.md`

- [ ] **Step 14.6.11:** All code blocks in new/modified files are tagged
  (bash, python, json, text, etc.) — zero untagged opening fences

---

## Critical Files Modified

| File | Change |
|------|--------|
| `sessions/development_system.md` | CREATE |
| `README.md` | ADD development_system row |
| `tools/github.md` → `tools/dev_system/github.md` | MOVE + expand GitHub SSH |
| `tools/vscode.md` → `tools/dev_system/vscode.md` | MOVE |
| `tools/provider_cost_control.md` → `tools/dev_system/provider_cost_control.md` | MOVE |
| `sessions/instructor.md` | UPDATE Section 0, Section 4; ADD Section 8 |
| `tools/VM/setup.md` | REPLACE macOS Parallels → Dev Container |
| `projects/group_meetup/labenv.yaml` | ADD GITHUB_USERNAME |
| `projects/group_meetup/labsetup.py` | ADD GitHub SSH key/config/validate |
| `projects/group_meetup/preflight_check.py` | ADD GitHub SSH + git identity checks |
| `sessions/client_agent.md` | ADD Skills callback |
| `sessions/llm_wiki.md` | ADD RAG callout + prompting_advanced link |
| `sessions/ai_local.md` | ADD local embedding stretch goal |

---

## Execution Protocol

Follow CLAUDE.md conventions:
- One step per turn; show diff; wait for approval before next step
- Commit each step: `feat: Phase 14: Step 14.X.Y - <summary>`
- Mark completed in `sdw/plan.md` with chore commit after each step
- Tag: `git tag -a v14.X-<brief>-step-completed`
- All code blocks in new files must be tagged (bash/python/json/text)
- sdw/plan.v2.md will be created first (as a standalone preview of Phase 14),
  then its content merged into sdw/plan.md as the authoritative record
