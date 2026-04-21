# Recap

## Tools

* **Web Tool**: [Lovable](https://lovable.dev/) - High magic, easy export.
* **CLI Tool**: [Claude Code](https://code.claude.com/) - API-based, cost-efficient

## Key Takeways

* **Master Rule**: If the code breaks, the plan is wrong. Fix the Plan, not the Code.
* [**YouTube: Basics of AI**](https://www.youtube.com/watch?v=xSH4KQJjTos&vl=en)

## What We Built

The Group Meetup Organizer started as a pitch deck and ended as a
deployed Docker stack. Each version was deliberately incomplete so
you could feel the gap and understand why the next layer was needed.

| Session | Version | What it could do | What was missing |
|---------|---------|------------------|------------------|
| Slides | Pitch deck | Describe the system | Everything else |
| Web Site | Toy UI | Show a form + result | Real logic, real data |
| Client App | 3 Python scripts | Poll → Select → Notify | Concurrency, failure recovery |
| Client Agent | Single agent | One agent, all 3 steps | Isolated retries |
| Multi-Agent | 3 agents + Temporal | Durable, retryable pipeline | Cloud deployment |
| Server Deploy | Docker stack | Runs on a real server | You decide what's next |

---

## Summary

### **Evolution of AI**

#### Predictive AI: 

**Predicts** a number or category which then is used for decisions. 
That is what happens next is based on past data. 
Example: prediction of an applicants' credit score or credit category 
is `good` or `bad` credit history based on past financial activity. 
This prediction is then used to approve or deny credit loan application.
Another example is responding to `will it rain tomorrow` with a `yes` or 
`no` answer based on recent weather history.

#### Generative AI
**Generates** something new. Example is response to someone asking 
`what activities may I pursue to improve my credit score` or 
`tell me a story about rain`.

### **Generative Model Evolution**
Foundation -> Reasoning -> Tool use -> Computer use

#### Foundation Capability

Claude/GPT LLM early versions were brains that answered in response to questions

#### Reasoning Capability

Claude/GPT LLM later versions were brains that broke complex problems into 
multiple steps, solved each step and verified it is on the right path, 
and then finally arrived at the solution.

#### Tool Capability

Claude Code application agents that can natively call structured interfaces
  * Structured interfaces are software API, system API (file read), search API, ...
  * Example - Weather Analysis: call weather API to get data

#### Computer Capability

Claude CoWork agents that "acts" using any native "facility" available
on your machine
  * Example - Weather Analysis: open browser, search weather, read page, read screen, ...

---

## Key Patterns

1. **SDD loop:** Spec → plan.md → Generate → Run → Reflect.
   If the code breaks, the plan is wrong. Fix the plan.

2. **Code Review pipeline:** Local CLI → GitHub Actions →
   Multi-agent (5 specialized agents). Each level catches what
   the previous missed.

3. **Agent architecture:** Use multiple agents when tasks are
   independent and failures must be isolated. Use one agent when
   steps are sequential and shared state is cheap.

4. **Embeddings + RAG:** Similar meaning → similar vectors → high
   cosine similarity → retrieved context. This is why relevance
   filtering works and how RAG grounds LLM answers in your data.