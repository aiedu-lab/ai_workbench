# Prompting Basics

## Prompts
Prompt is the way to communicate with AI just as code is the way to communicate with computers.

### Concepts
* Prompt structure:
  * Context → Task → Constraints → Output
  * Negative prompting
* Prompts is the "new" code:
  * versioned, reviewable
  * reusable, templateable
  * deployable
  * testable, debugable, improveable

### Exercise
Exercise 1: 
```bash
Explain "How credit card works"
```
* [Poor Prompt](../prompts/poor.md#Prompting--CreditCard--Basic)
  * generic explanation
  * mixed complexity
  * no audience targeting
  * long and vague
* [Improved Prompt](../prompts/poor.md#Prompting--CreditCard--Improved)
* simpler language
  * better audience targeting
* [Structured Prompt](../prompts/best.md#Prompting--CreditCard--Better)
  * structured: Context => Task => Constraints => Output
  * clarity and structure
  * brevity and consistency
* [Negative Prompt](../prompts/best.md#Prompting--CreditCard--Negative)
  * removes jargon and enforces discipline
  * tighter output
* [Failure Injection Prompt](../prompts/failures.md#Prompting--CreditCard--Failure)
  * confusing output and tone
  * violates audience and length constraint 
  * conflicting constraint => bad output

Exercise 2: 
```bash 
Rewrite badly written message
"hey can u send me the doc asap i need it"
```
* [Poor Prompt](../prompts/poor.md#Prompting--Rewrite--Basic)
* [Structured Prompt](../prompts/best.md#Prompting--Rewrite--Better)
  * everything same except quality of instruction

## Chain of Thought (CoT) Prompting
CoT asks the model to show its reasoning steps before giving a 
final answer, rather than jumping directly to a conclusion.

Without CoT, the model produces an answer. With CoT, the model produces
the *path to the answer* — and you can inspect and fix each step.

---

## Analogy

Like asking a student to **show their work** on a math test, not just
write the answer.

The steps reveal where the thinking went right or wrong. A wrong answer
with visible steps is far easier to fix than a wrong answer with no
explanation.

---

## Why it matters

| Without CoT | With CoT |
|---|---|
| Answer may be confidently wrong | Errors visible in the steps |
| No way to audit the logic | Each step is checkable |
| One-shot failure | Can fix the specific broken step |
| Hard to improve | Easy to iterate on one step |

---

## How to trigger it

Add one of these phrases to any prompt:

```bash
Think step by step before answering.
```

```bash
Explain your reasoning first, then give your final answer.
```

```bash
List your assumptions before concluding.
```

That is all. No special syntax required.

---

## Simple Example

**Without CoT:**

```bash
Should I bring an umbrella today?
Weather: 60% chance of rain, wind 15 mph, temperature 65°F.
```

The model may answer "Yes" or "No" with no explanation.

**With CoT:**

```bash
Should I bring an umbrella today?
Weather: 60% chance of rain, wind 15 mph, temperature 65°F.

Think step by step before answering.
```

Expected output:

```bash
Step 1 — Rain probability: 60% is above the threshold where rain
         is more likely than not. That favors bringing an umbrella.

Step 2 — Wind: 15 mph wind makes a standard umbrella less useful
         and potentially annoying. This slightly reduces the benefit.

Step 3 — Temperature: 65°F is mild. A light rain jacket might
         serve both purposes.

Conclusion: Bring a compact umbrella or a light rain jacket.
         A full-size umbrella may be impractical in the wind.
```

The reasoning is auditable. You can disagree with Step 2 and adjust.

---

## When to use CoT

**Use it when:**

* The answer is non-obvious or involves trade-offs
* You want to verify the logic, not just the conclusion
* You are making a decision with real consequences
* The task has multiple valid approaches

**Skip it when:**

* The task is simple and factual (`"What is 12 x 8?"`)
* Speed matters more than explanation
* You are doing quick brainstorming

---

## CoT + Template (first combination)

The simplest way to make CoT consistent is to add a `Reasoning` field
to the standard template:

```bash
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

---

## Exercise: Spot the Difference

**Prompt A (no CoT):**

```bash
Context:
I am a high school student with $500 saved.

Task:
Should I buy a used gaming laptop or invest the $500?

Output:
One sentence recommendation.
```

**Prompt B (with CoT):**

```bash
Context:
I am a high school student with $500 saved.

Task:
Should I buy a used gaming laptop or invest the $500?

Reasoning:
Think step by step. Consider: immediate utility, long-term value,
opportunity cost, liquidity, and age-appropriate risk.

Output:
Numbered reasoning steps → Final recommendation
```

Run both prompts. Compare:

* Which output do you trust more?
* Which output is easier to argue with or improve?
* Which step in Prompt B surprised you?

---

## Key Takeaway

CoT is not a special feature. It is a **habit**.

Add "think step by step" to any prompt where the answer matters.
The reasoning steps cost a few extra tokens. The visibility they
provide is worth it.

You will see CoT formalized as a **reusable skill** and built into  
**plugins** in [Advanced Prompting](prompting_advanced.md).

---

## Lessons

* Context defines relevance
* Constraints define safety
* Output format defines usability
* Bad prompts don’t fail loudly—they fail subtly

---

## References
* [Prompt Engineering Basics](https://www.youtube.com/watch?v=xSH4KQJjTos)
* [Anthropic Prompt Library](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
* [Anthropic System Prompting Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts)
* [Anthropic Prompt Engineering Tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial)
* [Advanced Prompting](prompting_advanced.md) — CoT as a skill and
  plugin component
* [Planning](planning.md) — CoT applied to plan-first thinking

## Output
* [Notes](../learnings/session_notes/prompting.md)