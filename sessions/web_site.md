# Web Site on Server

## Tools
* [Lovable](https://lovable.dev/) - AI website builder (login verified)

## Activities

### Demo Lovable:
* Review [plan.md](https://github.com/asarcar/aiedulabhelloworld/blob/main/plan.md)
* Use [Lovable](https://app.lovable.dev/dashboard) to execute plan.

### Demo Claude CLI:
* Review [plan.md](../projects/web_site/hello_world_claudeCLI/plan.md)
* Change to project subdirectory
```bash
set REPO_ROOT=...
cd $REPO_ROOT/projects/web_site/hello_world_claudeCLI
```
* Use Claude CLI to executes plan:
```bash
# discard console o/p
claude -p "$(cat plan.md)" --allowedTools "Write" > /dev/null
```
* Start web service to see effect
```bash
python3 -m http.server 8888
```
* Validate Change: Open http://localhost:8888 in browser

### Demo Reflection
Lovable or Claude CLI - which one to use? Why?
* Which one produced “better” application?
* Which one builds UI faster? Which one can handle file/data flexibly?
* Which one offers more control - creative, changes, cost, speed, performance?
* Which one is easier to operate?

### Exercise - Event Organizer

1. Process: **Planning → Execute → Reflect**

2. Planning: **Intent → Plan → Fortify → Validate → Iterate**

2. Plan: **Analyze → Update prompt → Iterate**

4. Fortify: 
* Push agent to reveal and identify potential failure scenarios 
* Cross question agent to justify the plan and its reasoning
* Intentionally give the agent conflicting instructions to see how 
it handles the conflict.
  ```bash
  Initiate rescheduling when anyone cancels. 
  Never reschedule once everyone agrees.
  ```

On Completion: 
* Push to Github branch
* Submit Pull Request from branch to mainline

## Reflection
* Incremental changes?
* Areas where generated content is poor?
* Other use cases
  * Marketing - PR, blogs
  * Communication - program updates, internal announcements
  * Education - course updates, announcements

## Tokenomics
### Usage Models
Two ways to use AI:
1. Fixed monthly subscription - Lovable, ChatGPT Plus, Claude Pro
* Fixed price, easy, less control - bundled, easier, imprecise

2. Pay-per-use: AWS, Anthropic API, OpenAI API
* Variable price but but direct, controlled, cheapest

### Cost Control - For Pay-per-use
* Establish cost awareness: /cost - odometer of balance Claude CLI
* Establish health practices:
  * Never run claude code on lots of files e.g. root, Downloads, Home, ...
  * Use constraint prompts: 
    * "only read files in src/, not node_modules or large data files, ..."
* System Set up: claude login/logout, set ANTHROPIC_API_KEY
* Safety protocol Set up:
  * Set a Hard Spend Limit of $5.0 - if the agent goes into a loop, 
    it only "steals" five dollars, not your whole bank account
  * Before running any CLI agent, every participant must practice Kill Switch Drillthe "Force Stop" command.
  * Action: Press Ctrl + C (Windows/Linux/WSL) or Cmd + . to 
    immediately terminate a runaway agent.

### Cost Control - General Strategies
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

### Discounts
* [Lovable Student Discount](https://lovable.dev/students)
  * The “Learner” 50% Discount: for Pro subscription at $12.50/month. 
* [Anthropic Student Builder Application](https://www.anthropic.com/api/student-builder-application)
  * $50 free API credits for student projects

### Kill Switch Drill
* Start a loop by asking Claude Code to:
```bash
Count to 1 million one by one in the terminal 
and emit the number each time.
```
* Execute the Kill: Have everyone immediately terminate 
  * Ctrl + C (Windows/Linux/WSL) or Cmd + . (Mac)
* Lesson: If terminal is scrolling faster than you can read, 
  * you are losing money. Kill it, fix the plan, then restart.

## References
* [Lovable vs Replit](https://lovable.dev/guides/lovable-vs-replit-platform-comparison)
* [Anthropic Console (API Key & Limits)](https://platform.claude.com/)
* [Claude Code CLI Documentation](https://docs.claude.com/code/)
* [Claude Code Quickstart Guide](https://docs.claude.com/code/quickstart)
* [Plan Draft for Event Organizer](../plans/draft/event_organizer.md)

---

## Output
* [Plan](https://github.com/asarcar/aiedulabhelloworld/blob/main/plan.md)
* [Notes](../learnings/session_notes/web_site.md)