# Concept & Exercise: The LLM Wiki (Agentic PKM)

## 🎯 Objective
Learn how to transition from manually organizing notes to using an 
AI agent as the "Librarian" for your personal knowledge management (PKM). 
We will use Claude Code to autonomously build and maintain a local 
markdown wiki, and Obsidian to visualize it.

## 🧠 The Core Concept
* **Traditional RAG:** Chunking text and using math (vectors) to 
guess what is relevant.
* **The LLM Wiki (Karpathy Pattern):** Using an LLM to actively write, 
summarize, and cross-reference markdown files, creating a human-readable 
knowledge graph.

> **Why not just build a RAG pipeline?**
> Traditional RAG (covered in
> [Advanced Prompting — §8 Embeddings & RAG](prompting_advanced.md#embeddings--retrieval-augmented-generation-rag))
> requires chunking documents, generating embeddings, a vector database,
> and retrieval code. The LLM Wiki skips all of that: the LLM organizes
> knowledge into human-readable, diff-able, Obsidian-navigable markdown.
> For a personal knowledge base the LLM Wiki is simpler and more
> maintainable. RAG remains the right choice when your corpus exceeds
> what a prompt context window can hold and you need at-scale retrieval.

## 🛠️ Installation & Setup
1. **The Viewer:** Download and install [Obsidian](https://obsidian.md/).
2. **The Brain:** Ensure you have the `claude-code` CLI installed.
3. **The Vault:** Create a new folder on your laptop called
   `my-ai-brain` and open it as a "Vault" in Obsidian.
4. **The Structure:** Inside the vault, create a folder named
   `raw_sources/`.

### Validation

- [ ] `claude --version` prints a version number
- [ ] Obsidian opens without error; `my-ai-brain` vault is visible
- [ ] `raw_sources/` folder appears in the Obsidian file explorer
- [ ] `claude` starts without errors when run inside the vault folder

## 🏃‍♂️ The Exercise: Compounding Knowledge

We will watch the AI connect two seemingly unrelated articles.

### Phase 1: The First Ingest

**Concept:** Download a source article (e.g. the "Moore's Law"
Wikipedia page) into `raw_sources/` and prompt Claude Code to
build an initial structured wiki — separate files for concepts,
people, and technologies, linked with Obsidian `[[wikilinks]]`.
Open Obsidian Graph View to see the first cluster of linked
notes appear.

> For exact download commands and prompts, see
> [Phase 2: First Ingestion](
> ../projects/llm_wiki/plan_template.md#phase-2-first-ingestion-moores-law)
> in the detailed plan.

### Phase 2: The Compound Effect

**Concept:** Download a second article (e.g. "History of
Artificial Intelligence") and ingest it into the existing wiki.
Claude cross-references the new content with existing notes
automatically — watch the Obsidian Graph View draw connections
between Moore's Law and AI breakthroughs without any manual
linking.

> For exact download commands and prompts, see
> [Phase 3: Second Ingestion](
> ../projects/llm_wiki/plan_template.md#phase-3-second-ingestion-history-of-ai)
> in the detailed plan.

### Phase 3: The Synthesis

**Concept:** Query your personal knowledge graph for a
synthesized answer (e.g. "How did hardware limitations dictate
the timeline of AI advancements?"). Claude answers using only
the notes it built — no internet search — and saves the
response as a new markdown file in the wiki.

**Key Takeaway:** The AI is not searching the open internet; it
is synthesizing from the curated knowledge graph it built.

> For the exact synthesis prompt, see
> [Phase 4: Synthesis](
> ../projects/llm_wiki/plan_template.md#phase-4-synthesis)
> in the detailed plan.

---

### Phase 4: Expand with a New Topic

**Suggested topic: GPU Computing**
> Why this topic? GPU Computing connects directly to both Moore's Law
> (billions of transistors packed onto a single chip) and the History
> of AI (the GPU-powered deep learning revolution of 2012 that ended
> the second AI Winter). Ingesting it will generate many new cross-links
> to existing notes — Dennard Scaling, Deep Learning, Transformer
> Architecture, Gordon Moore, and more.

You are free to choose any topic you find interesting. If you pick
your own topic, follow the same four steps below and explore whatever
connections emerge.

#### Step 1: Download the source

Download a source article on your chosen topic into
`raw_sources/`. See [the detailed plan](
../projects/llm_wiki/plan_template.md) for the exact command.

#### Step 2: Ingest and link

Prompt Claude Code to ingest the new source, create concept,
people, and technology notes following the existing wiki
pattern, and cross-reference with existing notes. Update
`Home.md`. See [the detailed plan](
../projects/llm_wiki/plan_template.md) for the exact prompt.

Link verification (zero orphans, zero broken wikilinks) is
covered in the detailed plan.

#### Step 3: Explore the knowledge graph

Open **Obsidian Graph View**. Navigate `Home.md` and look for
connections between GPU Computing and the previous topics. Note
which existing notes gained new incoming links — this is where
your knowledge graph compounded.

> **If you chose your own topic:** navigate `Home.md` to
> discover which previous topics your new topic relates to —
> the cross-links reveal the connections. Then form your own
> synthesis question that ties your new topic to at least two
> existing ones.

---

### Coherent Home.md Growth

`Home.md` is the **index**, not the encyclopaedia. Each topic that
enters the vault should add only a small number of canonical entries
to `Home.md` — one line per major concept, person, or technology.
The detail lives in the individual notes.

**Model:** look at how Moore's Law and AI History were factored in
(Phases 1–2). Each topic added:
- A handful of entries under **Recent Additions**
- Key concept titles under **Core Concepts**
- Names under **People** (grouped by era or field)
- Key technologies under **Technologies**

Follow the same pattern for every new topic. A cluttered `Home.md`
defeats the purpose — if a concept is niche, skip it or add it as
a sub-bullet under an existing entry.

> **Rule:** if removing a `Home.md` entry wouldn't confuse a future
> reader of the vault, don't add it.

---

### Optional Extension — Group Meetup Organizer PKM

Bridge this session back to the main project arc:

```text
Ingest plans/specs/event_organizer.md. Create concept notes for
Poller, Selector, and Notifier. Create a technology note for
Discord Webhooks. Cross-reference with existing AI and systems
notes where they connect. Update Home.md.
```

This connects the PKM session to the Group Meetup Organizer project
that runs through every other session in the lab.
