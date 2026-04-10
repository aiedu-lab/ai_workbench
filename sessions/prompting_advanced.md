# Advanced Prompting Techniques

## Objective

Learn how to move from “one-off prompts” to 
**reusable, structured, and scalable prompting techniques**.

---

## Tools

* Claude Desktop (Chat) → for drafting and refining prompts
  * Feature: Highlight-to-Prompt → select text, iteratively improve prompts

---

## Concepts

### 1. Skills (Reusable Prompts)

#### What it is

A **skill** is a prompt you reuse again and again for a specific job.

#### Analogy

Like a **calculator function** (e.g., `sum()`), instead of doing math manually every time.

#### Example

Instead of writing the below prompt every time: 

```bash
Rewrite this message to sound professional and polite.
```

Define the below "reusable" skill that is then reused 
everywhere just as one uses functions in math.

[professional email rewriter skill](../projects/skill.md#professional-rewrite-skill) 

#### When NOT useful

* One-time tasks
* Very simple queries

Overkill example:

```bash
Summarize this article
```

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

* Bad (all at once):
```bash
Build a full plan for organizing my files and execute it.
```

* Better: step-by-step guide with each step laid out separately:
```bash
Propose a safe plan to organize my files.
```
```bash
Explain why this plan is safe and reversible.
```
```bash
Execute only Step 1.
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
It is like a **form** you fill out every time instead of writing 
from scratch. 
For example, this [Prompt Template](../prompts/template.md#prompt-template) can be used to realize the example [Prompt](../projects/prompting_advanced/prompt.md#invest-or-buy-laptop)


#### Template substitution mechanisms

1. Shell variable substitution:
[var_sub.sh](../projects/prompting_advanced/var_sub.sh)

2. Python f-string:
[cot_prompt.py](../projects/prompting_advanced/cot_prompt.py)
can be reused across many calls where you want to call the same 
template with different data in a loop or script. 

3. Reading data from a file: 
[run.py](../projects/prompting_advanced/run.py) merges in runtime 
the [template](../projects/prompting_advanced/template.txt) and
the [data](../projects/prompting_advanced/data.json), where each 
are stored separately.

#### Benefits

* Consistent output
* Easier to improve
* Reusable across projects

#### When NOT useful

* Casual exploration
* Quick brainstorming

---

### 4. Phased Template for Planning

`plan.md` may bloat along with the scope of the project. This 
becomes a "context boat anchor" that slows down your agent. 
You need a structure that prioritizes active state over 
historical record.

[Phased Plan Template](../plans/canonical/phased_plan_template.md)
offers a structure - sliding window approach- that 
prioritizes active state over historical record. Detailed steps 
only exist for the current phase; completed work is collapsed 
and eventually evicted to a secondary file.

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

```bash
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

Defines behavior and personality

```bash
You are a careful assistant who prioritizes safety and clarity.
```

#### (B) Application / Agent Prompt

Defines workflow and rules

```bash
Only operate inside this directory.
Do not delete files.
Ask before executing.
```

#### (C) User Prompt

Defines the specific task

```bash
Organize my downloads folder.
```

#### When NOT useful

* Beginners → too many layers can confuse; start with user prompts first

---

### 7. Chain of Thought (Reasoning)

Chain of Thought (CoT) prompting asks the model to 
**show its reasoning steps** before giving a final 
answer, rather than jumping directly to a
conclusion. 

#### Basic vs CoT prompt

Without CoT:

```bash
Context:
You are a financial advisor.

Task:
Should a 17-year-old invest in crypto?

Output:
Yes or No with one sentence.
```

With CoT:

```bash
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

#### CoT Examples: Template & Skill

Reference:
* [CoT + Template (combined)](../plans/canonical/cot_template.md#decision-prompt)
* [Risk Evaluator](../plans/canonical/cot_template.md#risk-evaluator)

Once you identify a high-value reasoning pattern, turn the CoT structure
into a **reusable skill**:

---

## Exercise: Smart Rewrite Assistant

Build a reusable **writing skill** — then extend it with a plugin and
a Chain of Thought layer.

---

### Step 1 — Basic Prompt (Baseline)

Observe the output of the following prompt:

```bash
Rewrite this message better:

"hey can u send me the doc asap i need it"
```

---

### Step 2 — Structured Prompt (Template)

Use the template structure:
RECIPIENT="colleague"
MESSAGE="hey can u send me the doc asap i need it"

[professional email rewriter skill](../projects/skill.md#professional-rewrite-skill)

**Reflection:** What specifically improved vs Step 1?

---

### Step 3 — Turn into a Skill (Save and Reuse)

Name this prompt `professional-rewrite-skill` and reuse it for:

* Emails to boss, professor, teacher
* Internship outreach messages
* Team Slack messages

**Exercise:** Apply the skill to this message:

```bash
hey prof can i get extension on the hw its been a lot this week
```

---

### Step 4 — Add Chain of Thought

Extend the skill to explain its reasoning:

```bash
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
manually? Were any steps surprising?

---

### Step 5 — Build a Mini Plugin (3 Skills Combined)

Create a **Writing Plugin** by chaining three skills in one prompt:

```bash
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

```bash
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

```bash
What are the problems with this message?
"hey can u send me the doc asap i need it"
```

**Turn 2:**

```bash
Now rewrite it fixing only the tone problems you listed.
```

**Turn 3:**

```bash
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
