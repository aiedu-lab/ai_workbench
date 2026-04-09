# Web Site on Server

## Tools

* [Lovable](https://lovable.dev/) - AI website builder (login verified)
* [Claude Code CLI (API mode)](https://docs.claude.com/code/) - AI coding assistant
* [Claude Desktop (Code)](https://claude.com/download) - AI coding assistant

## Activities
* Demo: Lovable
* Demo: Claude Code CLI (API mode)
* Exercise: Build a web site using Lovable

## Demo

### Lovable

* Review [plan.md](https://github.com/asarcar/aiedulabhelloworld/blob/main/plan.md)
* Use [Lovable](https://app.lovable.dev/dashboard) to execute plan.
* Reference web site: [Hello, World!](https://hello-aiedu.lovable.app/)

### Use cases
* Program Updates - Dynamic and on-demand reporting
  * Pull data from varied sources - JIRA/GitHub (eng), Asana (product), 
    Confluence (docs) or via Glean-MCP (cross-org), etc.
  * Extract data from program spread sheets (excel, google sheets, MS project plan), 
    project status reports (internal wiki, slides, emails), etc.
  * Present program status, risks, dependencies, etc. in a structured format to 
    various level of stake holders - execs, VPs, managers, etc.
* Internal Announcements
* Marketing - PR, blogs
* Education - course delivery, testing, etc.


### Claude Code CLI (API mode)

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

### Reflection of Demo

Lovable or Claude CLI - which one to use? Why?
* Which one produced “better” application?
* Which one builds UI faster? Which one can handle file/data flexibly?
* Which one offers more control - creative, changes, cost, speed, performance?
* Which one is easier to operate?

## Exercise 

Agree on a project that you'd like to execute, such as:
```bash
Intent: Build a web site for students that know basic 
programming to learn about AI. 
```

From thereon used Claude Desktop to plan and execute.

## Reflection

* Compare "writing code" vs "managing specs"
* Incremental changes?
* Areas where generated content is poor?

## Tokenomics

* [Provider Cost Control](../tools/provider_cost_control.md)
* [Lovable Student Discount](https://lovable.dev/students)
  * “Learner” 50% Discount: for Pro subscription at $12.50/month. 

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