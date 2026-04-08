# Advanced Prompting Techniques

## Objective

Learn how to move from “one-off prompts” to **reusable, structured, and scalable prompting techniques**.

---

## Tools

* Claude (Chat or Desktop) → for drafting and refining prompts
* Highlight-to-Prompt → select text and iteratively improve prompts

---

## Concepts

### 1. Skills (Reusable Prompts)

#### What it is

A **skill** is a prompt you reuse again and again for a specific job.

#### Analogy

Like a **calculator function** (e.g., `sum()`), instead of doing math manually every time.

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

Overkill example:

> “Summarize this article”

---

### 2. Progressive Disclosure

#### What it is

Break a complex task into **small steps**, instead of asking everything at once.

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
  1. ```bash
  Propose a safe plan to organize my files.
  ```
  2. ```bash
  Explain why this plan is safe and reversible.
  ```
  3. ```bash
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

#### Analogy

Like a **form** you fill out every time instead of writing from scratch.

#### Template

```bash
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

```bash
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

### 4. Plugins (Packages of Skills)

#### What it is

A **plugin** is a collection of related skills for a domain.

#### Analogy

Like a **toolbox**:

* Hammer
* Screwdriver
* Wrench

Each tool = a skill

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

### 5. Prompt Types

#### (A) System Prompt

Defines behavior/personality

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

* Beginners → too many layers can confuse
* Start with user prompts first

---

## Exercise (Core Anchor)

### Task: Smart Rewrite Assistant

Build a reusable **writing skill**.

---

### Step 1 — Basic Prompt

```bash
Rewrite this message better:

"hey can u send me the doc asap i need it"
```

---

### Step 2 — Structured Prompt

```bash
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

---

### Step 3 — Turn into a Skill

Save this prompt and reuse it for:

* School emails
* Teacher communication
* Internship messages

---

### Step 4 — Progressive Disclosure

```bash
Explain why your rewrite is better.
```

---

### Step 5 — Failure Injection

```bash
Rewrite casually and professionally at the same time.
```

Observe confusion and conflicting output.

---

### Reflection

* What improved the output?
* Which constraint mattered most?
* What broke the prompt?

---

## Key Practices

* Always define:
  * Context
  * Constraints
* Start simple → add structure later
* Reuse good prompts (skills)
* Break tasks into steps (progressive disclosure)
* Debug prompts, not just outputs

---

## Tokenomics

* Avoid long prompts unless needed
* Reuse templates instead of rewriting
* Batch changes in one prompt
* Use chat for thinking before execution
* Limit retries (max 2–3)

---

## References

* [Prompting Basics](prompting_basics.md)
* [Plan-first thinking](planning.md)

---

## Output
* [Notes](../learnings/session_notes/prompting_advanced.md)