# Prompting Basics

## Concepts
* Prompt structure:
  * Context → Task → Constraints → Output
  * Negative prompting
* Prompts is the "new" code:
  * versioned, reviewable
  * reusable, templateable
  * deployable
  * testable, debugable, improveable

## Exercise
* ```bash
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
* Exercise 2: 
  ```bash 
  Rewrite badly written message
  "hey can u send me the doc asap i need it"
  ```
  * [Poor Prompt](../prompts/poor.md#Prompting--Rewrite--Basic)
  * [Structured Prompt](../prompts/best.md#Prompting--Rewrite--Better)
    * everything same except quality of instruction

## Lessons
* Context defines relevance
* Constraints define safety
* Output format defines usability
* Bad prompts don’t fail loudly—they fail subtly

## References
* [Prompt Engineering Basics](https://www.youtube.com/watch?v=xSH4KQJjTos)
* [Anthropic Prompt Library](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)
* [Anthropic System Prompting Guide](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts)
* [Anthropic Prompt Engineering Tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial)

## Output
* [Notes](../learnings/session_notes/prompting.md)