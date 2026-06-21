# Provider Cost Control

## General Strategies

* Use Chat Mode for Planning: Use "Chat" mode for brainstorming 
or debugging logic before committing to a generation. Chatting 
typically does not consume project editing credits.

* Batch Requests: Instead of prompting for one small change at a time, 
group multiple related updates into a single prompt. This is true 
for LLM-API calls as well. Example:  
```bash
Update header color to blue, add 'Contact' link to footer, and center logo
```

* Debug with Browser DevTools: Before using a credit to "Fix an error," 
check the Browser Console ```F12``` to see if it's a simple configuration 
issue you can fix by just pointing the AI to the specific error log.

## Specific Strategies

### CLI Agents
* Never run agents covering a large scope, say on root directory
* Always constrain file scope (e.g., `src/`)
* [Kill Switch](provider_cost_control.md#kill-switch) for runaway agents
* Set API spend limits (e.g., $5)

### Pay Per Use

The cost control strategy of AI usage depends on the pricing model:

#### Fixed monthly subscription - Lovable, ChatGPT Plus, Claude Pro

* Fixed price, easy, less control - bundled, easier, imprecise - 
* Most have a hard cap on token usage, e.g. 100k tokens/timeslot
* Once cap is reached, you can't use the tool until next timeslot or
  upgrade to a higher tier plan, which has its own hard cap.

#### API consumption based: AWS, Anthropic API, OpenAI API

* Variable price but direct, controlled, cheapest

Bottom line, the most economic model is API consumption based but 
requires more discipline and cost control practices.

#### Cost Control Practices

* Establish cost awareness: /cost - odometer of balance Claude CLI
* Establish health practices:
  * Never run claude code on lots of files e.g. root, Downloads, Home, ...
  * Use constraint prompts: 
    * "only read files in src/, not node_modules or large data files, ..."
* System Set up: claude login/logout, set ANTHROPIC_API_KEY
* Safety protocol Set up:
  * Set a Hard Spend Limit of $5.0 - if the agent goes into a loop, 
    it only "steals" five dollars, not your whole bank account
  * Before running any CLI agent, every participant must practice 
    [Kill Switch Drill](provider_cost_control.md#kill-switch-drill).

#### Kill Switch Drill

#### Start a loop by asking Claude Code or OpenAI Codex to:
```bash
Count to 1 million one by one in the terminal 
and emit the number each time.
```
#### Kill Switch
Ctrl + C (Windows/Linux/WSL) or Cmd + . (Mac)

#### Lesson
If terminal is scrolling faster than you can read, 
you are losing money. Kill it, fix the plan, then restart.

## Discounts

* [Anthropic Student Builder Application](https://www.anthropic.com/api/student-builder-application)
  * $50 free API credits for student projects

