# Code Review

## Objective

Learn how to integrate AI into the code review process — catching bugs,
security issues, and style violations **before** code reaches a human
reviewer or production. Understand the three levels of AI-assisted
review: local CLI, GitHub Actions, and managed multi-agent PR review.

---

## Concepts

### Why Code Review Matters

Code review is the last checkpoint before a bug ships. As AI tools like
Claude Code accelerate code generation (Anthropic reports 200% growth in
code output per engineer since 2024), review has become the new
bottleneck — many PRs get a quick skim instead of a deep read.

AI-assisted review flips the economics:

* Bugs found before commit: minutes to fix
* Bugs found after deployment: hours of debugging + incident response
* Bugs caught by AI review before human sees the PR: zero human review
  cycles wasted

The goal is **depth before speed** — catch the issues a skim misses.

### The Review Hierarchy

There are three places AI review can run, from cheapest to most thorough:

```
Level 1: Local (before commit)
  └── claude -p "review this diff" + git diff
  └── /code-review plugin (terminal, free with Claude Code)
  └── Cost: your API tokens, ~$0.01–0.05 per review

Level 2: GitHub Actions (on push / PR open, self-hosted)
  └── anthropics/claude-code-action (open source)
  └── @claude mention in PR comments triggers targeted review
  └── Cost: API tokens per run, ~$0.10–2.00 per review

Level 3: Managed Code Review (multi-agent, PR-level)
  └── Built into Claude Code Team/Enterprise
  └── 5 specialized agents in parallel, verification pass
  └── Inline comments on exact diff lines
  └── Cost: $15–25 per PR on average (Team/Enterprise only)
```

For the education lab: **Level 1** is the primary tool. Level 2 and 3
are context for understanding the professional workflow.

### How the Multi-Agent Review Pipeline Works (Level 3)

When a PR is opened, five specialized agents run in parallel:

| Agent | Role |
|---|---|
| Agent 1 | CLAUDE.md compliance — checks your project rules |
| Agent 2 | Bug sweep — logic errors in the changed code |
| Agent 3 | Git blame + history context — spots regressions |
| Agent 4 | Past PR comments — flags recurring patterns |
| Agent 5 | Comment/code alignment — stale comments vs new code |

Each agent scores its findings 0–100. A verification subagent is spun
up for each candidate finding to validate it against actual code. Only
issues scoring ≥ 80 are posted. This keeps the false positive rate below
1% — less noise means reviewers trust and act on the findings.

### What AI Review Catches (and Misses)

**Consistently catches:**

* Logic errors that are obvious once pointed out but easy to skim past
* Missing auth guards added elsewhere in the codebase but not in new
  routes
* Memory leaks — cleanup missing in `finally` blocks
* Type mismatches that silently corrupt data
* Hardcoded credentials or secrets
* CLAUDE.md rule violations (naming, indentation, forbidden patterns)
* Stale comments that no longer match the code

**Misses or struggles with:**

* Business logic correctness — AI doesn't know your domain rules
* Architectural decisions — "is this the right approach?" is human work
* Performance at scale — requires load testing, not static analysis
* Security in new, novel attack patterns not in training data
* Integration correctness — whether two services contract correctly

**Rule:** Treat AI review output as a thorough junior reviewer's notes.
The human still owns the merge decision.

---

## Tools
* [GitHub Pull Requests - VSCode Extension](../tools/github.md#set-up-vscode)
* [GitHub - Command Line](../tools/github.md#set-up-command-line)
* [Claude - Code Review](../tools/claude/cli.md#set-up-code-review)

## Code Review Trigger Mechansisms

### Level 1: Local Review via CLI

Available to anyone with Claude Code installed. No extra setup.

**Review a staged diff before committing:**

```bash
DIFF_REVIEW_PROMPT="Review this diff for:
- Logic errors
- Missing error handling
- Security issues (hardcoded secrets, injection patterns)
- CLAUDE.md violations
Be concise. Flag only high-confidence issues.
"

git diff --staged | claude -p "$DIFF_REVIEW_PROMPT"
```

**Review a specific file:**

```bash
FILE_NAME="index.html"
FILE_REVIEW_PROMPT="
Review $FILE_NAME for bugs, edge cases, style violations, and security issues.
Focus on the JavaScript event handlers.
Output JSON with severity ratings.
"

claude -p "$FILE_REVIEW_PROMPT" --allowedTools "Read"
```

**Review the last commit**

```bash
# last commit piped in
git diff HEAD~1 | claude -p "/code-review" --output-format json

# specific aspect reviewed of PR: bugs or security
git diff HEAD~1 | claude -p "/code-review bugs"

claude -p "/code_review security"

```

**Install the native (built-in) plugins including code-review**

```bash
# Add the official Anthropic marketplace
claude plugin marketplace add anthropics/claude-code 

# Install code-review plugin
claude install code-review@claude-code

# Optional: Install PR review toolkit
claude install pre-review-toolkit@claude-code

# Validate - list installed plugins
claude plugin list

# Update all plugins
# Native plugins are auto-updated, 3rd party require manual updates
claude plugin update
```

**Run code-review plugin:**

```bash
# Review and post inline comments to the PR
/code-review --comment
```

```bash
REVIEW_DIFF_FORMAT="
Review this diff for bugs, security issues, and CLAUDE.md compliance
"
PR_NUM=... # replace with PR#
gh pr diff $PR_NUM | claude -p "$REVIEW_DIFF_PROMPT"
```

The plugin launches 4-5 agents in parallel, scores each finding, and only
surfaces issues with ≥ 80 confidence. 

Use REPL rather than headless mode as `/code-review` uses 
parallel subagents requiring full agentic loop, which `-p` may 
not support. Hence, triggering prompt based code-review may be 
more reliable headless pattern.  

### Level 2: GitHub Actions 

#### Level 2a: Workflow triggered by GitHub Actions

1. Authorize: 
  * `gh secret list` shows that authorization token CLAUDE_CODE_AUTH_TOKEN (Subscription) or key ANTHROPIC_API_LEY (pay as you go) is uploaded to Repo
  * GitHub Repo => Setting => Secrets  Variables => Actions. 
  * Validate: `claude auth status --text` shows auth mode.

3. Permit Workflows
  * GitHub Repo => Settings => Actions => General: "Allow GiHub Actions to create and approve pull requests" is enabled.
  * Validate: GitHub Repo => Actions => "Claude PR Review" listed on left. If it has an icon - yellow (queued) or green (in progress) - it is working.


#### Level 2b: Self-Hosted GitHub Actions

Add this workflow file to your repo to trigger Claude review on `@claude`
mentions in PR comments:

**`.github/workflows/claude-review.yml`:**

```yaml
name: Claude PR Review
on:
  issue_comment:
    types: [created]
jobs:
  claude-review:
    if: |
      github.event.issue.pull_request &&
      contains(github.event.comment.body, '@claude')
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write
      id-token: write
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: anthropics/claude-code-action@v1
        with:
          claude_code_oauth_token: ${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          github_token: ${{ secrets.GITHUB_TOKEN }}
          show_full_output: true
          claude_args: "--max-turns 20 --allowedTools 'Bash(gh pr diff*),Bash(gh pr view*),Bash(gh api*),Bash(python3*),Write'"
          prompt: |
            Review PR #${{ github.event.issue.number }} in this repository.

            Steps:
            1. Run: gh pr diff ${{ github.event.issue.number }}
            2. Analyze for:
               - Logic errors, bugs, and edge cases
               - Security issues and vulnerabilities
               - Missing error handling
               - CLAUDE.md rule violations
            3. Write your review as JSON to /tmp/review.json using the Write tool
            4. Post using: gh api repos/${{ github.repository }}/pulls/${{ github.event.issue.number }}/reviews --input /tmp/review.json

            IMPORTANT: GitHub Actions CAN post APPROVE reviews. You are not
            the PR author so the restriction does not apply to you.
            You MUST use exactly one of these event values in the JSON:
            - "REQUEST_CHANGES" if high-confidence bugs found
            - "APPROVE" if no high-confidence bugs found  
            - "COMMENT" only for observations that are neither blocking nor approving
            Never downgrade APPROVE to COMMENT.
            Only flag high-confidence issues.
```

To trigger: add a comment `@claude review` on any PR "Conversations" GitHub tab.

**Cost control:** scope by file globs to avoid reviewing generated files:

```yaml
prompt: |
  Review only files matching src/**/*.{js,html,css,py}.
  Skip generated files, lockfiles, and vendor directories.
```

### Level 3: Managed Code Review (Team/Enterprise)

For organizations on Claude Team ($30/seat/month) or Enterprise:

1. Admin enables Code Review in **Claude Code settings**
2. Install the **Claude GitHub App** on your org
3. Select which repositories to include
4. Set trigger per repo:
   * **Once after PR creation** — single review on open
   * **After every push** — catches new issues as the PR evolves
   * **Manual** — only runs when you comment `@claude review`

Once enabled, reviews run automatically. No developer configuration
needed. Results appear as inline comments on the PR diff within ~20
minutes on average.

Cost: $15–25 per review, billed by token usage (not a flat fee). A
small PR under 200 lines may cost $8–12; a 2,000-line PR may cost
$30–40.

---

### How to Review Recommendations

#### GitHub:
* Add `@claude review, provide inline suggestions as comments for improvements` 
at the bottom of the "Conversation" tab of a GitHub PR to trigger 
Claude review on `@claude`mentions in PR comments 
* `@claude review this logic` by clicking next to the `+` sign next 
to a specific line of code - you get feedback on just that section 
* Use /code-review --comment from Claude CLI. Reference the 
"Files Changes" GitHub tab to see inline (diff) comment blocks 
from "Claude" appear directly below code line. These comments are also 
mirrored in the bottom of "Converation" GitHub tab

#### Terminal: 
* `gh pr view --comments` # streams the comments to stdout of Terminal

#### VS Code
* Open the GitHub Pull Requests panel (left sidebar)
* Find your PR and click it
* Expand "Changes" to see inline comments
* Claude's comments appear inline on the diff lines it flagged

## Exercise: Local Code Review in Three Levels

### Setup

```bash
# Navigate to the hello world project
cd $REPO_ROOT/projects/web_site/hello_world_claudeCLI

# Make sure you have a clean working state
git status
```

### Step 1 — Introduce a deliberate bug

Add this broken function to `index.html` just before `</script>`:

```javascript
// Deliberately broken: does not handle null input
function formatName(name) {
  return "Hello, " + name.toUpperCase() + "!";
}
```

Stage but do not commit:

```bash
git add index.html
```

### Step 2 — Level 1 review: CLI diff review

```bash
git diff --staged | claude -p "Review this JavaScript diff.
Find:
1. Logic errors or crashes
2. Edge cases not handled
3. Any security concerns
Be specific about line numbers if possible."
```

**Expected finding:** `name.toUpperCase()` will throw if `name` is
`null` or `undefined`. Claude should flag this as a bug.

### Step 3 — Level 1 review: writer/reviewer pattern

Use a second Claude session to review the first Claude's own output — a
core principle from the Claude Code best practices guide:

```bash
# First session writes a fix
claude -p "Fix the null handling bug in this JavaScript:

function formatName(name) {
  return 'Hello, ' + name.toUpperCase() + '!';
}

Return only the fixed function with a WHY comment." \
  --allowedTools "Write" > /dev/null

# Second session reviews the fix (fresh context = unbiased review)
git diff index.html | claude -p "A colleague fixed a null-handling bug.
Review their fix:
1. Does it actually fix the null case?
2. Are there other edge cases (undefined, empty string, whitespace)?
3. Is the WHY comment accurate?
Be direct."
```

This is the **writer/reviewer pattern**: one Claude generates, another
reviews. Fresh context avoids the bias of reviewing code you just wrote.

### Step 4 — Apply the fix and validate

```bash
# Accept the fix
python3 -m http.server 8888
# Open http://localhost:8888
# Test: submit empty name, submit a name with spaces, submit normally
```

### Step 5 — Commit with a conventional message

```bash
git add index.html
git commit -m "fix: Phase 1: Step 3 - handle null and empty name in formatName"
```

### Step 6 — Simulate a CLAUDE.md rule violation

Add a 4-space-indented block to `index.html` (violates the 2-space rule
in CLAUDE.md):

```html
    <!-- 4-space indent: violates CLAUDE.md style rule -->
    <p id="bad-indent">bad</p>
```

Run the review again:

```bash
git diff | claude -p "Review this diff against the CLAUDE.md rules:
- 2-space indentation only
- Max 80-column line length
- WHY comments on non-obvious blocks
Flag any violations with the exact rule being broken."
```

**Expected finding:** CLAUDE.md violation — 4-space indentation detected.

Revert the violation:

```bash
git checkout index.html
```

---
## Code Review Best Practices

### The Core Question: Is Claude Reviewing Claude Safe?

> *"Is it as dangerous as a fox protecting the chicken?"*

The short answer is: **it depends on how you do it, and the risk is
real but manageable.** Here is the full picture.

---

### The Self-Review Problem

When a single AI model generates code and then reviews that same code,
a well-documented failure mode called **sycophancy bias** occurs.

AI models have a well-documented tendency toward agreement. When you
ask a model to review something it generated — or something that
stylistically resembles its own outputs — it often validates the work
rather than critically challenging it. Models trained on human feedback
learn that humans tend to prefer responses that confirm their
assumptions. That same training dynamic creates a bias toward approval
when the model is reviewing code, plans, or any other output.

IBM Research's 2026 AAAI paper quantified the problem: LLM-as-Judge
alone detects only about 45% of code errors.

So yes, **there is a real fox-and-chicken problem** — but it is not
binary. The severity depends on three factors:

#### Factor 1: Same session vs fresh session

The worst case is asking Claude to review code it just wrote **in the
same conversation**. The context window still contains the reasoning
that produced the code — the model sees what it expects to see.

A **fresh session** (after `/clear` or in a new terminal) is
meaningfully better. The reviewer has no memory of generating the code
and approaches it cold. This is the **writer/reviewer pattern** — one
session generates, another reviews.

```bash
# Session 1: generate
claude -p "$(cat plan.md)" --allowedTools "Write" > /dev/null

# Session 2: review (fresh context — no shared memory)
git diff | claude -p "Review this diff as if you have never seen
this code. Find bugs, edge cases, and security issues."
```

Asking the agent to perform a code review on its own work is
surprisingly fruitful — but the reviewer and the author must be
treated as separate contexts.

#### Factor 2: Stochastic independence — are they really independent?

**The honest answer: partially, not fully.**

LLMs are stochastic — the same prompt produces different outputs on
different runs. But stochasticity alone does not guarantee independence.
If both runs share the same model weights, training data, and RLHF
fine-tuning, they share the same systematic blind spots.

Think of it this way:

| Scenario | Independence level | Analogy |
|---|---|---|
| Same session, same model | ❌ None | Asking yourself to proofread your own essay |
| Fresh session, same model | ⚠️ Partial | Asking yourself after sleeping on it |
| Same model family, different agent | ⚠️ Partial | Asking a colleague from the same school |
| Different model, same provider | ✅ Better | Asking a peer with different training |
| Different model, different provider | ✅ Best | Asking an external auditor |

Whether multi-agent same-provider mitigations are sufficient is
genuinely uncertain. Agents from the same provider family may still
share architectural biases regardless of specialization.

#### Factor 3: What is being reviewed?

The self-review problem matters most for:

* **Security vulnerabilities** — a model that doesn't know about a
  vulnerability class won't flag it regardless of session independence
* **Business logic correctness** — the model doesn't know your domain
* **Novel architectural errors** — patterns the model hasn't seen in
  training

It matters **less** for:

* **CLAUDE.md rule violations** — deterministic rule matching is not
  subject to sycophancy
* **Syntax and type errors** — structural issues are reliably detected
* **Null/undefined handling** — common patterns are well-covered
* **Style and hygiene** — formatting rules are rule-based, not
  inference-based

---

### What Anthropic Does About It

Anthropic's own managed Code Review (Team/Enterprise) is specifically
architected to reduce same-model bias:

The multi-agent design is specifically an architectural response to
the self-review problem: multiple independent specialized agents, rather
than one model making one pass, with different agents having different
scopes analyzing the same code independently, reducing the chance that a
shared blind spot affects all findings simultaneously. Each agent must
attempt to disprove its own findings before surfacing them. Code Review
never approves PRs — the human always makes the merge decision.

Before Code Review, 16% of PRs at Anthropic got substantive review
comments. After introducing the AI review system, that number increased
to 54%. Engineers reported that less than 1% of findings were
incorrect.

This is meaningful, but it does not fully solve the cross-model
independence problem. The mitigations are architectural 
(specialization + verification pass), not provider-level.

---

### Best Practice Options: Generation vs Review

Here are the four approaches in order of review independence, with
tradeoffs:

#### Option A: Claude generates, same Claude reviews (fresh session)

**When to use:** Student learning, low-stakes projects, rapid
prototyping, budget-constrained environments.

```bash
# Generate
claude -p "$(cat plan.md)" --allowedTools "Write" > /dev/null

# Review (new terminal, no --continue flag)
git diff | claude -p "You are a senior engineer reviewing a PR.
You did NOT write this code. Review it critically for:
bugs, edge cases, security, and CLAUDE.md violations."
```

**Tradeoff:** Shares systematic blind spots with the generator. Good
for catching obvious issues, CLAUDE.md violations, and style problems.
Not reliable for deep security review.

---

#### Option B: Claude generates, Codex reviews (cross-provider)

**When to use:** Production-grade code, security-sensitive features,
any code touching auth, payments, or data integrity.

Cross-provider review reduces sycophancy bias by having a model from
a different provider review code generated by another — their biases
don't perfectly overlap. Claude and GPT have different training
histories, different fine-tuning approaches, and different tendencies
around what "good code" looks like. A GPT-based reviewer is more likely
to surface issues in Claude-generated code precisely because it doesn't
share the same internal assumptions.

**Setup (using the official Codex plugin for Claude Code):**

```bash
# Install the official OpenAI Codex plugin
claude mcp add codex-plugin-cc \
  -- npx -y @openai/codex-plugin-cc

# Then delegate review to Codex from within a Claude session:
# /codex:review   ← reviews current diff via Codex/GPT
```

**Or via CLI directly (two terminals):**

```bash
# Terminal 1: Generate with Claude
claude -p "$(cat plan.md)" --allowedTools "Write" > /dev/null

# Terminal 2: Review with Codex  
git diff | codex exec -s read-only \
  "Review this diff for bugs, security issues, and edge cases.
  Be adversarial. Flag only high-confidence issues."
```

Think of it like adversarial vs. stochastic bandits: a single model
self-reviewing is the stochastic case (predictable reward noise), while
cross-model review is adversarial (the reviewer actively probes
weaknesses the executor didn't anticipate) — and adversarial bandits
are fundamentally harder to game. Two is the minimum needed to break
self-play blind spots. Adding more reviewers increases API cost and
coordination overhead with diminishing returns — the biggest gain is
going from 1→2, not 2→4.

---

#### Option C: Claude generates, human reviews (gold standard)

**When to use:** Any merge to `main`, any code touching security or
payments, any change a student or contributor submits for approval.

This is the gold standard and **never optional** for production. AI
review is a pre-filter, not a replacement for human review.

The human reviewer's job after AI review has run:

1. Read the AI review findings first — use them as a checklist
2. Focus human attention on business logic and architecture (the AI
   missed these)
3. Make the final merge decision — the AI never does this

```
AI review → catches mechanical bugs, style, security patterns
Human review → catches business logic, architecture, intent
Both → needed for production-grade code
```

---

#### Option D: Multi-model debate (research-grade, high-signal)

For the highest-stakes code — auth systems, payment logic, core
infrastructure — run multiple models and have them challenge each
other's findings:

In a multi-model debate setup, each model reviews the same PR
independently, then all reviews are shared with all participants, and
each model updates its position based on the others. L2 detection (
routine, mid-difficulty bugs) doubled — from 3/10 to 7/10 — using this
debate mechanism compared to independent single-model review.

This is overkill for student exercises but worth knowing as the
research-grade frontier of AI review.

---

### The Cross-Model Workflow: Claude + Codex

The most practical production workflow used by professional teams today
is the **four-step cross-model pipeline**:

Step 1 (Plan): Claude Code in plan mode — interviews you, produces a
phased plan. Step 2 (QA Review): Codex CLI reviews the plan against
the actual codebase, inserts intermediate phases with findings, adds to
the plan without rewriting it. Step 3 (Implement): Claude Code executes
phase by phase with test gates. Step 4 (Verify): Codex CLI verifies the
implementation against the plan.

```
STEP 1: PLAN          → Claude Opus (plan mode)
STEP 2: REVIEW PLAN   → Codex / GPT  (adversarial review)
STEP 3: IMPLEMENT     → Claude Sonnet (execute phase by phase)
STEP 4: VERIFY CODE   → Codex / GPT  (verify vs plan)
STEP 5: HUMAN REVIEW  → You (business logic, final merge)
```

The key insight: **Claude and Codex alternate** — Claude never reviews
its own output, and Codex never reviews Codex output. The two models
are complementary, not redundant.

GPT-5.4 on high thinking excels at architectural reasoning and
sustained plan execution. Opus 4.6 excels at execution quality,
proactive gap analysis, and consistency over long sessions. The best
results come from using both models to review each other's work.

---

### Deterministic Guardrails: What AI Review Cannot Replace

Both Claude and Codex miss issues that **rule-based deterministic
tools** catch reliably. These must run in addition to AI review, not
instead of it:

| Tool type | What it catches | Cost |
|---|---|---|
| Linter (ESLint, flake8) | Style, unused vars, syntax | Free |
| Type checker (mypy, tsc) | Type mismatches | Free |
| Secret scanner (truffleHog, gitleaks) | Hardcoded credentials | Free |
| SAST (Semgrep, CodeQL) | Security vulnerability patterns | Free tier |
| Test suite | Behavioral correctness | Your test investment |

Wherever possible, use your lint and test rules to bake in quality,
and leave auto code review for more semantic issues that tools can't
check. If you want to set a maximum length for your files or maximum
level of indentation, use your lint tool. A semantic code review looks
at how well the code is designed — naming, fallback values, design
decisions — that lint cannot check.

The full defensive stack is:

```
Commit hook  → linter + type checker + secret scanner (deterministic)
Pre-PR       → AI review, fresh session or cross-model (semantic)
PR open      → GitHub Actions / Claude Code Review (automated)
PR review    → Human reviewer (business logic + architecture)
Merge        → Human decision only
```

---

### Summary: Decision Framework

| Situation | Recommended review approach |
|---|---|
| Student exercise, learning | Claude generates → Claude reviews (fresh session) |
| Personal project, low stakes | Claude generates → Claude reviews (fresh session) |
| Team project, shared codebase | Claude generates → Codex reviews OR human reviews |
| Security-sensitive code | Claude generates → Codex reviews AND human reviews |
| Any PR to `main` | AI pre-filter → human final decision, always |
| Production auth / payments | Multi-model + human + SAST, no exceptions |

**The bottom line:** Same-model review is better than no review, but
it is not a reliable security boundary. For anything that matters,
the minimum viable standard is a fresh session or a different model.
The human reviewer is never optional for production merges.

---

## Reflection

| Question | Your Observation |
|---|---|
| What did the CLI review catch that you would have noticed anyway? | |
| What did it catch that you might have missed under time pressure? | |
| Did the writer/reviewer pattern produce a better fix than a single session? | |
| What did the review miss that only a human would know? | |
| When would you use Level 1 vs Level 2 vs Level 3 review? | |

---

## Key Takeaways

* **AI review complements, not replaces, human review.** It handles
  the mechanical checks — null safety, auth guards, hardcoded secrets,
  style violations — so human reviewers can focus on architecture and
  business logic.
* **Local review before commit is the highest-leverage habit.** It
  costs pennies and catches issues before they reach a PR queue.
* **The writer/reviewer pattern works.** A fresh Claude session reviews
  more accurately than the same session that wrote the code.
* **CLAUDE.md is the configuration layer.** Without it, AI review uses
  generic heuristics. With it, reviews enforce your specific project
  rules on every diff.
* **Review output is untrusted until verified.** AI generates 1.75x more
  logic errors than human-written code on average (ACM 2025). Review the
  review.

---

## Documentation

When a code review finding is acted upon, document the WHY in the commit
and in a code comment:

```javascript
// WHY: formatName previously crashed on null/undefined input when the
// submit handler fired before the user typed anything.
// Fixed in Phase 1 Step 3 review — see review_notes/2026-04-12.md
function formatName(name) {
  if (!name || !name.trim()) return "Hello, World!";
  return "Hello, " + name.trim() + "!";
}
```

Review findings that surface recurring patterns should be added to
`CLAUDE.md` so future sessions don't repeat the mistake:

```markdown
## CLAUDE.md addition after review session:
## Lessons Learned
- formatName and similar input handlers MUST guard against null,
  undefined, and whitespace-only strings before calling string methods
```

---

## Tokenomics

### Cost by review level

| Level | Tool | Cost per review | Requires |
|---|---|---|---|
| Local CLI diff | `claude -p` + `git diff` | ~$0.01–0.05 | Claude Code + API key |
| Local /code-review plugin | `/code-review` | ~$0.05–0.20 | Claude Code installed |
| GitHub Actions | `claude-code-action` | ~$0.10–2.00 | API key + free GH Actions |
| Managed Code Review | Claude Code Team/Ent | ~$15–25 | Team/Enterprise plan |

For the education lab: all exercises use the **local CLI** approach —
total cost for the full exercise is under $0.10.

### Cost-saving practices for review sessions

* **Scope the diff tightly** — pipe only the changed file, not the
  entire repo: `git diff index.html | claude -p "review"`
* **Use Sonnet, not Opus, for review** — Sonnet handles the vast
  majority of review tasks at 40% lower cost
* **Set a token budget in the prompt** — `"Be concise. Max 5 findings.
  Skip nits."` prevents expensive verbose output
* **Use `/clear` between review and fix sessions** — do not carry
  review context into the implementation session

---

## References

* [Claude Code Review (Official Docs)](https://code.claude.com/docs/en/code-review)
* [Claude Code GitHub Action (Open Source)](https://github.com/anthropics/claude-code-action)
* [Code Review Plugin (Source)](https://github.com/anthropics/claude-code/tree/main/plugins/code-review)
* [Claude Code Best Practices](https://code.claude.com/docs/en/best-practices)
* [Set Up Code Review (Help Center)](https://support.claude.com/en/articles/14233555-set-up-code-review-for-claude-code)
* [How to Review Claude Code Output](https://www.lowcode.agency/blog/how-to-review-claude-code-output)

---

## Output

* [Notes](../learnings/session_notes/code_review.md)
