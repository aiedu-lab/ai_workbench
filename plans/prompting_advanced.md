# Advanced Prompting Techniques

## Objective

Learn how to move from "one-off prompts" to **reusable, structured, and
scalable prompting techniques**.

---

## Tools

* Claude (Chat or Desktop) — for drafting and refining prompts
* Highlight-to-Prompt — select text and iteratively improve prompts

---

## Concepts

### 1. Skills (Reusable Prompts)

#### What it is

A **skill** is a prompt you reuse again and again for a specific job.

#### Analogy

Like a **calculator function** (e.g., `sum()`), instead of doing math
manually every time.

#### Example

Instead of writing this every time:

```
Rewrite this message to sound professional and polite.
```

Define a reusable skill:

```
Context:
This is a professional email.

Task:
Rewrite the message.

Constraints:
* Polite tone
* Clear ask
* No slang
* Max 2 sentences

Output:
Formal email
```

Now reuse it everywhere.

#### When NOT useful

* One-time tasks
* Very simple queries

Overkill example: `"Summarize this article"`

---

### 2. Progressive Disclosure

#### What it is

Break a complex task into **small steps**, instead of asking everything
at once.

#### Analogy

Like asking a teacher:

* Step 1: Explain the idea
* Step 2: Give examples
* Step 3: Test me

#### Example

Bad (all at once):

```
Build a full plan for organizing my files and execute it.
```

Better — step-by-step:

```
Step 1: Propose a safe plan to organize my files.
Step 2: Explain why this plan is safe and reversible.
Step 3: Execute only Step 1.
```

#### Why it works

* Easier to debug
* Prevents mistakes
* Builds trust

#### When NOT useful

* Very small tasks
* When speed matters more than precision

---

### 3. Templatization

#### What it is

Create a **fixed structure** for prompts so they are consistent.

#### Analogy

Like a **form** you fill out every time instead of writing from scratch.

#### Template

```
Context:
...

Task:
...

Constraints:
...

Output:
...
```

#### Example

```
Context:
Audience is a 10-year-old.

Task:
Explain photosynthesis.

Constraints:
* Use simple words
* Use an analogy

Output:
1 paragraph + 1 example
```

#### Benefits

* Consistent output
* Easier to improve
* Reusable across projects

#### When NOT useful

* Casual exploration
* Quick brainstorming

---

### 4. Phased Template for Planning

`plan.md` may bloat along with the scope of the project. This becomes a
"context boat anchor" that slows down your agent. You need a structure that
prioritizes active state over historical record.

[Phased Template](../plans/canonical/phased_template.md) offers a structure —
a sliding window approach — that prioritizes active state over historical
record. Detailed steps only exist for the current phase; completed work is
collapsed and eventually evicted to a secondary file.

---

### 5. Plugins (Packages of Skills)

#### What it is

A **plugin** is a collection of related skills for a domain.

#### Analogy

Like a **toolbox**: Hammer + Screwdriver + Wrench. Each tool = a skill.

#### Example: Writing Plugin

* Rewrite professionally
* Summarize text
* Generate bullet points

#### Example Prompt

```
Use the writing plugin:
* summarize the text
* rewrite in simple language
* generate 3 bullet points
```

#### When NOT useful

* Beginners (too abstract)
* Small tasks

---

### 6. Prompt Types

#### (A) System Prompt

Defines behavior and personality:

```
You are a careful assistant who prioritizes safety and clarity.
```

#### (B) Application / Agent Prompt

Defines workflow and rules:

```
Only operate inside this directory.
Do not delete files.
Ask before executing.
```

#### (C) User Prompt

Defines the specific task:

```
Organize my downloads folder.
```

#### When NOT useful

* Beginners — too many layers can confuse; start with user prompts first

---

### 7. Chain of Thought (Reasoning)

> **Where does this topic belong in the Agenda?**
>
> Chain of Thought is **introduced** in
> [Prompting Basics](prompting_basics.md) — the concept, one simple
> example, "show your work." By the time attendees reach Advanced
> Prompting they have run real exercises across web sites, apps, and
> multi-agent workflows. This section **formalizes** CoT as a reusable
> skill, a plugin component, and a debugging tool — building on the
> experience they already have.

#### What it is

Chain of Thought (CoT) prompting asks the model to **show its reasoning
steps** before giving a final answer, rather than jumping directly to a
conclusion.

#### Analogy

Like asking a student to **show their work** on a math test, not just
write the answer. The steps reveal where the thinking went right or wrong.

#### Basic vs CoT prompt

Without CoT:

```
Context:
You are a financial advisor.

Task:
Should a 17-year-old invest in crypto?

Output:
Yes or No with one sentence.
```

With CoT:

```
Context:
You are a financial advisor advising a high school student.

Task:
Should a 17-year-old invest in crypto?

Constraints:
* Think step by step before answering
* Consider: risk tolerance, time horizon, liquidity needs, regulations
* State each consideration explicitly

Output:
Numbered reasoning steps, then a final recommendation
```

#### Why CoT improves output quality

| Without CoT | With CoT |
|---|---|
| Answer may be confidently wrong | Errors visible in the steps |
| No way to audit the logic | Each step is checkable |
| One-shot failure | Can fix the specific broken step |
| Hard to improve | Easy to iterate on one step |

#### CoT + Template (combined)

```
Context:
[your situation]

Task:
[your question]

Reasoning:
Think step by step. List each assumption and inference explicitly.

Constraints:
[your constraints]

Output:
Numbered reasoning steps → Final answer
```

#### Advanced: CoT as part of a Skill

Once you identify a high-value reasoning pattern, turn the CoT structure
into a **reusable skill**:

```
# Skill: Risk Evaluator

Context:
You are evaluating a decision for potential risks.

Task:
Evaluate [DECISION].

Reasoning:
Step 1 — Identify what could go wrong
Step 2 — Estimate likelihood (Low / Med / High)
Step 3 — Estimate impact (Low / Med / High)
Step 4 — Suggest mitigations for High x High items

Output:
Risk table + top 3 mitigations
```

Reuse this skill for code review, plan review, investment decisions,
and project proposals.

#### Relationship to the Agenda

| Session | CoT Role |
|---|---|
| Prompting Basics | Introduced — "show your work" concept |
| Planning | Applied — plan.md asks Claude to reason before acting |
| Web Site / App exercises | Implicit — progressive disclosure forces step reasoning |
| **Advanced Prompting (here)** | Formalized — CoT as a reusable skill and plugin component |
| Multi-Agent Workflows | Extended — each agent in a chain has its own CoT step |

---

## Exercise: Smart Rewrite Assistant

Build a reusable **writing skill** — then extend it with a plugin and
a Chain of Thought layer.

---

### Step 1 — Basic Prompt (Baseline)

Paste this into Claude:

```
Rewrite this message better:

"hey can u send me the doc asap i need it"
```

Observe the output. Note what changed and what did not.

---

### Step 2 — Structured Prompt (Template)

Now use the template structure:

```
Context:
This is a professional email to a colleague.

Task:
Rewrite the message below.

Message:
"hey can u send me the doc asap i need it"

Constraints:
* Polite tone
* Clear ask
* No slang
* Max 2 sentences

Output:
Formal email only — no explanation
```

**Reflection:** What specifically improved vs Step 1?

---

### Step 3 — Turn into a Skill (Save and Reuse)

Name this prompt `professional-rewrite-skill` and reuse it for:

* School emails to teachers
* Internship outreach messages
* Team Slack messages

**Exercise:** Apply the skill to this message:

```
hey prof can i get extension on the hw its been a lot this week
```

---

### Step 4 — Add Chain of Thought

Extend the skill to explain its reasoning:

```
Context:
This is a professional email to a colleague.

Task:
Rewrite the message below.

Message:
"hey can u send me the doc asap i need it"

Reasoning:
Before rewriting, explain step by step:
1. What tone problems exist in the original?
2. What information is missing?
3. What structure will the rewrite follow?

Constraints:
* Polite tone
* Clear ask
* No slang
* Max 2 sentences

Output:
Step-by-step reasoning → then the rewritten email
```

**Reflection:** Did the reasoning steps match what you would have noticed
manually? Were any surprising?

---

### Step 5 — Build a Mini Plugin (3 Skills Combined)

Create a **Writing Plugin** by chaining three skills in one prompt:

```
Context:
I am preparing a message for a professional audience.

Plugin: Writing Assistant
Apply all three tools in order:

Tool 1 — Diagnose:
List the 3 biggest problems with this message.

Tool 2 — Rewrite:
Rewrite it professionally (polite, clear, max 2 sentences, no slang).

Tool 3 — Explain:
In one sentence, state the most important change you made and why.

Message:
"hey can u send me the doc asap i need it"

Output:
Tool 1 result → Tool 2 result → Tool 3 result
(clearly labeled)
```

**Reflection:** Which tool in the plugin added the most value? Which
could you drop for a faster workflow?

---

### Step 6 — Failure Injection (Break the Prompt)

```
Context:
Professional email.

Task:
Rewrite casually AND professionally at the same time.

Message:
"hey can u send me the doc asap i need it"
```

Observe the confused or hedged output.

**Reflection:** Which constraint caused the failure? How would you fix
the prompt?

---

### Step 7 — Progressive Disclosure (Multi-turn)

Instead of one big prompt, break into turns:

**Turn 1:**

```
What are the problems with this message?
"hey can u send me the doc asap i need it"
```

**Turn 2:**

```
Now rewrite it fixing only the tone problems you listed.
```

**Turn 3:**

```
Now tighten it to 2 sentences maximum without losing the ask.
```

**Reflection:** Did the multi-turn approach produce a better result than
Step 2's single prompt? Why or why not?

---

### Reflection Table

| Question | Your Observation |
|---|---|
| What improved the output most? | |
| Which constraint mattered most? | |
| What broke the prompt? | |
| Did CoT add value or just noise? | |
| Which plugin tool would you drop? | |
| When would you use multi-turn vs single prompt? | |

---

## Key Practices

* Always define: Context + Constraints
* Start simple — add structure later
* Reuse good prompts (skills)
* Break tasks into steps (progressive disclosure)
* Use CoT when the answer is non-obvious or high-stakes
* Save CoT patterns as skills when you find ones that work
* Debug prompts, not just outputs

---

## Tokenomics

* Avoid long prompts unless needed
* Reuse templates instead of rewriting
* Batch changes in one prompt
* Use chat for thinking before execution
* Limit retries (max 2–3)
* CoT adds tokens — use it for complex decisions, not simple lookups

---

## References

* [Prompting Basics](prompting_basics.md) — where CoT is first introduced
* [Plan-first thinking](planning.md)

---

## Output

* [Notes](../learnings/session_notes/prompting_advanced.md)
