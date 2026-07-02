# Agent Loop

Excellent set of questions — you're probing the actual architecture, and several of your intuitions are sharper than the marketing descriptions. Let me take these one at a time.

## 1. Multiple LLMs — do directions contradict?

Your second guess is right: **one LLM drives a given loop cycle; routing decides which.** An agent almost never has two LLMs "co-piloting" the same decision simultaneously, precisely because their outputs would race. Instead you see a few patterns:

- **Router/dispatch:** a cheap model classifies the request, then hands the whole loop to the model best suited (cost, latency, capability). The driving model is fixed for that task.
- **Role separation:** different LLMs own different *jobs*, not the same job — e.g. a planner model decomposes, a worker model executes, a judge/critic model evaluates. They run at different stages, so they don't contradict; they hand off.
- **Ensemble/vote:** rare, used for high-stakes single decisions, where you deliberately sample multiple models and reconcile — but that's a tool *within* a cycle, not two drivers.

The contradiction you're worried about only happens if you let two models both emit the "next action." Architectures avoid that by making the loop **single-driver per cycle** and treating any other model as a tool the driver calls.

## 2. Can a cycle return a sequence of tools? Linear or graph?

Yes — and this is one of the bigger recent shifts. Early agent loops were strictly **one tool call → observe result → back to LLM**. Modern ones support the LLM emitting **multiple tool calls in a single turn**, which the harness can run in parallel or sequence. So a cycle can return: tool, tool, tool.

On the shape: it's genuinely **all of the ones you listed, depending on layer:**

- The LLM-emitted batch within one turn is effectively a **parallel set** (no conditional logic between them — the LLM hasn't seen their results yet).
- Conditional / branching logic emerges **across cycles** — the LLM sees results, then decides the next batch. So the *dynamic* graph with conditionals lives in the loop iteration, not in a single emission.
- A **skill** can embed a *fixed* graph — code with `if/else`, loops, sequential tool+script steps — that the harness runs deterministically without consulting the LLM between steps. That's the "cookbook" case (see #4).

So you have two control planes: the **LLM-driven dynamic graph** (re-decided each cycle) and **code-driven fixed graphs** (inside skills, no LLM in the inner loop).

## 3. Agent-to-agent — tool call, or something more?

You've spotted the real tension. Today, **the dominant model is "subagent call = tool call"** — the parent's LLM emits a tool invocation whose implementation happens to spin up another agent loop. This is how Claude Code's Task/subagent dispatch works.

But your objection is correct: **a pure tool returns a result; an agent may need to clarify.** Two things resolve this in practice:

- Most subagent calls are deliberately scoped to be **non-interactive** — the parent passes a fully-specified task, and the subagent is told *not* to ask questions but to make reasonable assumptions and report back. The "tool" abstraction holds because clarification is designed out.
- When genuine multi-turn negotiation between agents *is* needed, you move beyond the tool model to **agent-to-agent protocols** (like Google's A2A) where agents exchange messages, maintain shared task state, and can ask/answer — a peer conversation, not a function call.

So: simple delegation → tool-call model; genuine collaboration → a messaging protocol. The industry mostly lives in the first because it's simpler and composes cleanly.

## 4. How does a skill's cookbook (tools + scripts) run inside an LLM-only loop?

This is the cleanest part once you see it. **The skill executes one level *below* the agent loop.** The loop is "talk to LLM → run a tool → repeat." A skill is invoked *as one of those tool/action steps*, but what runs is **deterministic code**, not another LLM round-trip per step.

Concretely: the LLM says "use the `pdf-fill` skill." The harness loads that skill's instructions/scripts and **executes the recipe itself** — call tool A, run a Python script, call tool B, branch on output — all without returning to the LLM between those sub-steps. Control returns to the LLM only when the skill finishes (or fails). So from the loop's perspective it *was* a single action; internally it was a multi-step program.

There's a subtlety: some "skills" are really just **instructions/context injected into the LLM** (the LLM then chooses to make the calls itself, cycle by cycle), while others are **executable code** the harness runs directly. The first stays inside the LLM loop; the second runs beneath it. Anthropic's Skills lean toward the "instructions + bundled scripts" hybrid — the LLM reads `SKILL.md`, then either follows steps itself or runs the provided code.

## 5. If skills are this powerful, why have subagents at all?

The crux question, and the answer is **context isolation**, not capability. A skill, however sophisticated, executes **in the parent's context window** — its instructions, intermediate tool outputs, and scratch work all land in the *same* conversation the parent LLM is reasoning over. A subagent runs in a **separate context window with its own LLM instance.**

That difference buys you things a skill structurally cannot:

- **Context firewall:** A subagent can churn through 50 tool calls and 100K tokens of noisy intermediate output, then return only a clean 200-token summary. The parent never sees the mess. A skill's intermediate output (if it routes back through the LLM) pollutes the parent's context. This is the single biggest reason subagents exist.
- **Independent reasoning budget:** The subagent's LLM does its *own* multi-cycle reasoning loop. A skill's code is deterministic — it can call an LLM as a tool, but it isn't itself an autonomous reasoner that plans, observes, and re-plans over many cycles.
- **Parallelism with isolation:** You can fan out N subagents, each with its own context, working concurrently, then aggregate. Skills don't give you N independent reasoning contexts.
- **Different model/config:** A subagent can run a different model, different system prompt, different tool permissions entirely.

The clean mental model: **a skill is a *procedure* (possibly complex, possibly with embedded code and conditional logic) that runs in your context; a subagent is a *delegated reasoner* with its own context and its own loop.** If the work is "follow these steps," a skill suffices. If the work is "go figure this out, I don't want to watch you think, just give me the answer" — that's a subagent, and the value is the isolation, not anything the steps couldn't technically express.

---

A useful unifying picture: there are **three nested loops** — the outer agent loop (LLM-driven, dynamic, conditional), skills as **fixed sub-programs** that run beneath a single step of it, and subagents as **entire nested copies** of the outer loop with their own context. Your instinct to collapse everything into "one agent + skills" is architecturally coherent for *procedural* work; it breaks specifically where you need **isolated reasoning contexts**, which is a property of the runtime, not of what the steps can express.

Three sharp pushbacks. You're right on two of them and half-right on the third. Let me be precise.

## 1. What is "the task"?

I was sloppy with that word. Let me define it cleanly: **the task is the unit of work the loop runs to completion before control returns to whoever invoked it** — i.e. your first reading (the overarching goal handed in externally), *not* a single loop iteration.

So the granularity is: one externally-handed goal → one agent loop → many iterations until the LLM signals "done." The **driving model is fixed for the duration of that loop**, across all its iterations. It is *not* re-routed per iteration. A single tool-evaluation iteration is *not* "a task" in the sense I meant.

The reason routing happens once at the top, not per-iteration: routing mid-loop would mean swapping the model that holds the accumulated reasoning context, which defeats the point — the new model inherits a conversation it didn't reason its way into. So in practice, **route once → that model drives the whole loop.** (A subagent is how you get a *different* model onto a *sub-goal* — but that's a fresh loop with its own context, which is exactly the distinction from #2.). 

When we say "the model holds the accumulated reasoning context", we mean the harness builds up a growing transcript over the loop's iterations. That transcript was written for and by a specific model — its style, its tool-call formatting, its reasoning conventions. If you swap the driving model mid-loop, the new model is handed a transcript it didn't generate, and must now continue reasoning over prior steps shaped by a different model's "voice" and decisions. It works (it's just text), but it's awkward — like a co-author taking over mid-paragraph. That's the real reason to route once: not because the old model "holds" anything, but because mid-stream model swaps force a model to inherit another model's reasoning trail. Your correction is exactly right; the statefulness is in the harness's transcript, never in the model.

## 2. Aren't "context firewall," "independent reasoning," and "parallel fan-out" all the same point?

**Yes — you've correctly collapsed them.** They are not three independent benefits. They are **three consequences of one root property: a subagent gets its own separate context window + its own LLM instance.** I over-itemized. Let me restate honestly:

There is **one** structural difference between a skill and a subagent: **a subagent runs in an isolated context with its own model invocation; a skill runs in the caller's context.** Everything I listed — the firewall, the independent reasoning budget, the parallel fan-out — are just that one fact viewed from different angles. You were right to be suspicious.

On your specific challenges:

- **"Independent reasoning budget is a restatement"** — Correct. A skill *can* inject instructions that trigger the parent LLM into a multi-cycle reasoning loop. But that reasoning happens **in the parent's context**, consuming the parent's window and reasoning over the parent's history. The subagent's reasoning happens **elsewhere**. The difference was never "can it reason multi-cycle" — it's *whose context the reasoning occupies*. Same root property. You caught a genuine redundancy.

- **"Fan-out is a restatement"** — Also correct. N isolated contexts is just "isolated context" × N.

- **"Can't parallelism be achieved with skills somehow?"** — Here's the one place there's a real residual. A skill's *code* can absolutely run things concurrently — spawn threads, fire parallel HTTP/tool calls, `asyncio.gather` a batch. So **parallel tool execution: yes, skills can do it.** What a skill cannot do is run **N independent LLM reasoning loops that each privately accumulate and discard their own context.** A skill could call the LLM API N times in parallel as a tool — but then *the parent harness/code is orchestrating those calls deterministically*, and their outputs come back into the parent's controlled scope. That's parallelism *of model calls*, not parallelism *of autonomous agents that own their context lifecycle*. The distinction is thin but real: it's the difference between "my code calls an LLM 5 times concurrently" and "5 agents independently decide how to use their own contexts and hand me summaries."

So the honest reduction: **the entire skill-vs-subagent distinction is context isolation.** Every other benefit derives from it. You were right to compress.

## 3. "Different tool permissions" — you're mostly right, and you've caught a real imprecision

Your model is correct: **the LLM emits a tool-call request; it does not emit permissions. Scope/credential enforcement is a harness property, deliberately kept outside the LLM** — exactly the security boundary you described in your very first Q2. I should not have implied the LLM "has" different permissions.

But here's the subtlety that makes the phrase not entirely wrong: **the harness can bind a *different permission set to a different agent context.*** When the parent spawns a subagent, the harness can configure that subagent's runtime with a narrower tool allowlist / credential scope than the parent's. So:

- The **LLM** never carries permissions — you're right.
- But the **subagent (the runtime construct)** is a place the harness can *attach* a distinct permission boundary. The parent might have filesystem-write; the subagent it spawns is configured by the harness with read-only.

A skill, by contrast, **executes within the parent's runtime and therefore under the parent's permission set** — it has no separate enforcement boundary the harness can independently scope. So "different tool permissions" is correctly stated as: *the harness can enforce a different permission scope on a subagent's context than on the parent's*, because the subagent is a separate runtime construct. It was never a property of the LLM. Your correction stands; the capability lives in the harness binding policy to context, not in the model.

This actually loops straight back to your original Q2: a subagent boundary is *also* a permission boundary the harness controls — which is exactly why "subagent as isolated context" and "least-privilege enforcement" are deeply related. The isolation that gives you the context firewall is the *same* isolation that gives the harness a clean seam to attach a tighter credential scope. One mechanism, two payoffs.

---

These are good structural questions, and the honest answer up front is that **"session" is the loosest word in this whole vocabulary** — it doesn't have a single crisp definition the way "task" or "context window" do. Let me give you the common usages, then answer your actual structural questions, which are sharper than the terminology.

## What is a "session"?

"Session" is used at (at least) three different granularities, and people rarely say which:

- **Transport/connection sense:** one continuous interactive sitting — you open the CLI, work, close it. This can span *many* goals. When the docs talked earlier about `user:sessions:claude_code` scope or `claude --resume`, that's this sense: a persistent conversation thread you can leave and return to.
- **Task sense (your candidate):** one goal → one agent loop → done. This is closer to what *you* mean and what's architecturally clean.
- **Runtime-instance sense:** one spawned agent process/context with its own LLM invocations — which for a subagent maps onto exactly one delegated subtask.

So your instinct — "session = the task/goal that triggered an agent loop with its own reasoning loop and context" — is a **defensible and coherent definition**, and it's the right one for a subagent. But for a *top-level interactive* agent, "session" usually means the **outer container that can hold multiple sequential tasks** (the sitting), not a single task. That's the key asymmetry that answers your question 3.

## Is context rebuilt after a goal completes, or carried across tasks?

**It depends on the surface, and this is a design choice, not a law.** Both happen:

- **Carried over (interactive sitting):** In a CLI/chat session, when you finish one goal and type the next request, the **prior transcript stays in the context window.** The harness keeps appending. Your second task sees the first task's history. This is why long sessions accumulate context (and cost) — and why `/clear` exists: to *deliberately* reset the transcript and start fresh within the same sitting.
- **Rebuilt (fresh task / stateless invocation):** A headless one-shot run, a fresh subagent dispatch, or a `/clear`'d session starts with **no prior task history** — only the system prompt, tools, and the new goal.

So context-carryover is the **default for interactive sittings** and **absent for isolated dispatches**. The mechanism is identical (harness assembles a transcript); the policy differs (does the harness retain the previous task's messages or not).

A subtlety worth flagging: even when "carried over," it's not unbounded. Harnesses **compact/summarize** older turns when the window fills — so across many tasks, early context is often *lossily summarized*, not retained verbatim. (Earlier we touched on this as the context-firewall benefit of subagents — the parent avoids accumulating the child's mess precisely because the child's context is separate and discarded.)

## Your parent-vs-child lifetime asymmetry — is it fair?

**Yes, and this is the cleanest and most correct part of your model.** The asymmetry you propose is real:

- **Child (subagent) session = scoped to its subtask.** The harness spawns it for one delegated component, it runs its loop, returns a result, and its context is **discarded.** Its lifetime is exactly the subtask. It does not persist, does not carry over to the next subtask, and the parent decides whether to spawn a fresh one for the next component. This is precisely the context-isolation property from your earlier questions — the child's context lifecycle *is* the subtask.
- **Parent session ⊇ the task.** Here's the one correction: the parent's session is usually **at least as long as the task, and often longer.** If the parent is a top-level interactive agent, its session is the *sitting* — it survives the completion of task 1 and goes on to task 2, 3, … within the same context (until cleared/closed). If the parent is *itself* a subagent of someone higher up, then its session = its own delegated task, and the same rule recurses.

So the precise statement of your asymmetry:

**A child agent's session lives exactly as long as the subtask it was handed (spawn → result → discard). A parent agent's session lives at least as long as a single task, and — if it's an interactive top-level agent — across multiple sequential tasks until the sitting ends or is explicitly cleared.**

The reason for the asymmetry is exactly the design intent you've been circling: the child is **ephemeral by construction** so its intermediate reasoning doesn't pollute or outlive its purpose (the firewall), while the parent is **persistent by construction** so it can accumulate the thread of work across goals and integrate the children's clean summaries. Same mechanism (harness-managed transcripts), opposite retention policy, each chosen to serve its role.

One clean mental model to carry: **think "session = however long the harness keeps a given context alive," and then note the harness keeps a child's context alive for one subtask and a top-level parent's context alive for a whole sitting.** The word "session" floats; the *retention policy of the harness* is the thing that's actually precise — anchor on that and the ambiguity dissolves.

---

This is the right synthesis question, and the short answer is: **you've identified something real — a skill that wraps the Claude SDK can spawn subagents, which means "skill" and "agent-orchestrator" stop being cleanly separable.** Once a skill can call `query()` from the SDK, it can itself become a full agent runtime. So the architectural line you've been tracing genuinely blurs here. But there are limitations, and they're worth naming precisely because most of them are **operational, not capability** limits.

## First, the key reframing

When a skill is just instructions + bundled scripts, it runs *beneath* the parent loop in the parent's context. But the moment that skill's code **imports the Claude SDK and calls it**, that script is no longer "running in the parent's context" — it's **opening its own independent model invocations with its own context.** At that point your skill *is* an agent harness; it just happens to be packaged as a skill and triggered from inside another agent's loop.

So "use skills that spawn subagents at their discretion" is not a workaround that dodges the skill-vs-subagent distinction — **it's a way of building subagents and labeling the entry point a skill.** That's legitimate. Anthropic's own SDK is built for exactly this. The question becomes: what do you lose by making the *orchestration logic* live inside skill-code rather than being declared as first-class specialized agents?

## What this approach handles fine

- **Capability:** Nothing a specialized agent can *compute* is off-limits. A skill-with-SDK can plan, spawn N subagents, fan out, aggregate, branch on results. Turing-complete code orchestrating LLM calls can express any topology.
- **Dynamic decisions:** "spawn a subagent only when the task warrants it" is just an `if` in your skill code calling `query()`. Fine.
- **Context isolation:** You still get it — because the isolation comes from the *separate SDK invocation*, not from how the agent was declared. Your skill spawning a subagent gets the same firewall.

So for a **single developer building a personal/automation stack**, this approach is not just viable — it's often the *right* one. You get one coherent codebase, reuse, and dynamic control.

## Where the limitations actually bite

These are the things "skills that spawn subagents at their discretion" gives up versus **declaring specialized agents as first-class entities** (e.g. Claude Code's `.claude/agents/*.md` subagent definitions, or a registry of named agents):

**1. Discoverability & routing by the *parent's* LLM.**
A first-class declared subagent has a name, a description, and a tool-surface the **parent model can see and choose among**. The parent LLM does the routing: "this is a security-review task → dispatch the `security-reviewer` agent." If your orchestration is buried inside imperative skill-code, the *parent model* can't reason about it — **you've moved the routing decision from the LLM into your code.** Sometimes that's what you want (deterministic). But you lose the model's judgment about *which* specialist to invoke. With many specialists, model-driven routing scales better than a hand-written dispatcher you have to maintain.

**2. Declarative permission/identity boundaries.**
This is the big one and connects to your original Q2. A first-class agent definition is a **natural seam to attach scoped tool permissions, a distinct system prompt, a different model, and audit identity** — declaratively, enforced by the harness. When you spawn subagents from inside skill-code via the SDK, **you are now responsible for configuring those scopes correctly in code, every time.** The harness will happily run whatever permission set your code passes. So you've taken the least-privilege enforcement that a declarative agent gets "for free" and made it *your code's responsibility* — exactly the "hostage to the agent-framework code" concern you raised at the very beginning. Declared agents externalize that boundary; skill-spawned agents internalize it into your imperative logic, where mistakes are easier and audits are harder.

**3. Observability, tracing, and lifecycle management.**
Platforms treat declared agents as first-class objects: per-agent traces, token accounting, rate-limit handling, retries, failure isolation, "which agent did what." When subagent spawning is an implementation detail inside skill-code, much of that becomes **opaque** — your spawns may not show up cleanly in the harness's agent-level telemetry. For a personal stack, fine. For anything you need to debug, audit, or operate at scale, you're rebuilding observability the platform would otherwise give you.

**4. Reusability across *different* parents.**
A declared specialist agent is reusable by *any* orchestrator — it's a named, addressable unit. Orchestration logic baked into one skill is reusable only by whoever invokes that skill. You can factor your skill-code well to mitigate this, but you're doing the factoring the agent abstraction would enforce.

**5. Composition and protocols.**
If specialists ever need to talk to *each other* (not just be called by one parent), or be invoked by external systems, first-class agents fronted by a protocol (A2A, MCP-exposed) compose in ways that an internal skill-spawn loop doesn't. Skill-spawned subagents are private to their parent's process.

## The honest bottom line

**There is no capability a specialized agent has that a skill-with-SDK cannot express** — because spawning via the SDK *is* how you'd build the specialized agent anyway. The distinction is **not "can it do the work" but "where does the structure live":**

- **Skill-spawns-subagents:** structure lives in *imperative code you own*. Maximum flexibility, minimum ceremony. You hand-roll routing, permission-scoping, observability, and reuse. Excellent for a solo/automation context where you control everything and want one codebase.
- **First-class specialized agents:** structure lives in *declarative definitions the harness enforces*. You get model-driven routing, declarative least-privilege seams, per-agent observability, and cross-orchestrator reuse — at the cost of more upfront structure and less dynamic freedom.

The decision rule: **choose skill-spawned subagents when the orchestration is dynamic, private, and you want it in code; choose declared specialized agents when the boundaries (permission, identity, routing, audit) need to be enforced and inspected by something other than your own code.** And the tell that you've outgrown the skill approach is precisely when you find yourself **hand-writing permission scoping and dispatch logic inside skills** — that's the harness's job re-implemented by hand, which loops directly back to your very first concern about being hostage to framework code. At that point, promoting those specialists to first-class declared agents is what *gives* you the enforceable least-privilege seam you wanted.

---

## Prompt caching with stateless models — where does the cache live?

Great question, and the resolution is: **the cache lives on the provider's side, behind the API, but it caches *computation*, not "state."** Statelessness is about *conversational memory*; caching is about *not recomputing identical work*. These don't conflict. Here's the mechanism:

When the model processes your prompt, the expensive step is converting those input tokens into internal attention representations (the "KV cache" — key/value tensors for every token). For a 50K-token context, that's a lot of compute, redone from scratch on every call — **even though the first 49K tokens are byte-for-byte identical to last call.**

Prompt caching lets the provider **store those computed internal representations** for a prefix of your prompt, keyed by the exact token content. On the next call, if the prefix matches, the provider **skips recomputing it** and loads the cached tensors instead. You still send the full prompt every time (the model is still stateless from your side), but the provider recognizes "I've already done the math for this exact prefix" and reuses it.

Key properties that follow from this:

- **It's prefix-based and exact-match.** Caching works on the *longest identical leading sequence*. Change one token early in the prompt and everything after it is a cache miss — which is exactly why you put stable content (system prompt, tools, long documents) at the **front** and volatile content (the latest user turn) at the **back**.
- **It's provider-side, not harness-side.** Your code does nothing except (with Anthropic) mark a cache breakpoint. The stored tensors live in the provider's infrastructure, not yours. The harness still assembles and sends the whole prompt.
- **It's ephemeral and economic, not memory.** Anthropic's cache entries live ~5 minutes (refreshed on hits), and the benefit is **cost + latency** — cached input tokens are billed at a steep discount and skip the prefill compute. It is *not* a way for the model to "remember" anything across calls; if the cache expires, the next call simply recomputes the prefix and produces the identical result.

So the two facts coexist cleanly: **the model is stateless** (no conversational memory; you resend everything), and **the provider caches the prefill computation** (so identical prefixes aren't re-crunched). One is about *what the model knows*; the other is about *what the provider recomputes*. Caching changes the bill and the speed, never the output.

A clean way to hold it: statelessness is a property of the **model's semantics** (each call is independent and self-contained), while prompt caching is an optimization in the **serving infrastructure** (don't redo identical matrix math). You're sending the full context either way — the cache just means the provider already has the oven warm for the part that didn't change.
