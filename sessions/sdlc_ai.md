# Concept & Exercise: AI Across the SDLC

## 🎯 Objective
Writing code is only about 30% of software engineering. The rest of the 
Software Development Life Cycle (SDLC) involves testing, reviewing, 
deploying, and maintaining. This session explores how AI agents can 
automate the surrounding infrastructure.

## 🔄 Beyond Code Generation

### 1. Advanced Testing Strategies
* **Unit Testing:** Agents can read a function and generate tests 
for edge cases (null inputs, boundary limits).
* **Smoke Tests:** Quick scripts to ping APIs after deployment to 
ensure nothing caught fire.

### 2. Code Review & Auditing
* **Automated PR Reviews:** Having an AI automatically scan 
Pull Requests for logic flaws and security vulnerabilities 
before a human ever looks at it.

### 3. CI/CD (Continuous Integration / Continuous Deployment)
* **Writing Pipelines:** You can ask an agent, 
*"Write a GitHub Actions YAML file that runs my Pytests."*
* **Debugging Pipelines:** Pasting failed Action logs to an 
agent often yields the exact line that needs fixing.

---

## ⚖️ The Great Debate: IDE vs. Desktop/CLI Agents

**The Intelligent IDE (e.g., Cursor, GitHub Copilot)**
* **Best for:** Micro-edits, inline code generation, writing 
functions within a single file.

**The CLI / Desktop Agent (e.g., Claude Code)**
* **Best for:** Macro-tasks, repo-wide refactoring, orchestration, 
and SDLC infrastructure.

---

## 🏃‍♂️ The Exercise: Full SDLC Automation

In this exercise, we will build a tiny application - 
a **Website Health Monitor**—and use the Claude CLI 
to walk through every stage of the SDLC.

### Phase 1: Planning & Coding (Development)
1. **The Spec:** Open your terminal and start Claude CLI (`claude`).
2. **The Prompt:** 
```bash
Create a python script called `monitor.py` that accepts a URL. 
It should ping the URL and print 'UP' if the status is 200, 
and 'DOWN' otherwise.
```
3. **Action:** Let Claude generate and save the file.

### Phase 2: Test Generation (QA)
1. **The Prompt:** 
```bash
Read `monitor.py`. Generate a `pytest` file named `test_monitor.py`. 
Include tests for a successful 200 response, a 404 response, and 
a server timeout.
```
2. **Action:** Run `pytest` to ensure the tests pass. 
Note Claude CLI can do this for you.

### Phase 3: The CI/CD Pipeline (DevOps)
1. **The Prompt:** 
```bash
Create a GitHub Actions workflow in `.github/workflows/test.yml`. 
It should trigger on every push, set up Python, install pytest, 
and run `test_monitor.py
```
2. **Action:** Claude will generate the YAML file to automate 
your testing.

### Phase 4: AI Code Review (Peer Review)
*Now we tie it into our GitHub workflow!*
1. **Commit:** Push code to a new branch `git checkout -b feat/monitor`
2. **PR:** Open a Pull Request on GitHub.
3. **Review:** Add a comment on your PR: `@claude review` 
4. **Action:** Watch as the AI assumes the role of a Senior Developer, 
providing inline feedback on your code based on the GitHub Action 
we set up in previous labs.

## Key Takeaway
You just acted as a Product Manager, QA Engineer, DevOps Engineer, and 
Lead Reviewer, all orchestrated through an AI CLI.
