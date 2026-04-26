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

## 🛠️ Installation & Setup
1. **The Viewer:** Download and install [Obsidian](https://obsidian.md/).
2. **The Brain:** Ensure you have the `claude-code` CLI installed.
3. **The Vault:** Create a new folder on your laptop called `my-ai-brain` 
and open it as a "Vault" in Obsidian.
4. **The Structure:** Inside the vault, create a folder named `raw_sources/`.

## 🏃‍♂️ The Exercise: Compounding Knowledge

We will watch the AI connect two seemingly unrelated articles.

### Phase 1: The First Ingest
1. **Source:** Download a Wikipedia PDF about "Moore's Law" and put it in 
`raw_sources/`.
```text
curl -o raw_sources/moores_law.html \
"https://en.wikipedia.org/wiki/Moore%27s_law"
```
2. **Action:** Open your terminal in the vault folder and run `claude`.
3. **Prompt:** *"Read the PDF in raw_sources. Create a structured markdown 
wiki. Create separate files for key concepts, people, and technologies. 
Use Obsidian [[wikilinks]] to connect them."*
4. **Observe:** Open Obsidian and look at the Graph View. You will see a 
small cluster of linked notes.

### Phase 2: The Compound Effect
1. **Source:** Download an article about "The History of Artificial 
Intelligence" and drop it into `raw_sources/`.
```text
curl -o raw_sources/history_of_ai.html \
"https://en.wikipedia.org/wiki/History_of_artificial_intelligence"
```
2. **Action:** In your running Claude terminal, prompt: 
*"Ingest the new AI history article. Update our existing wiki pages with 
new context, create new pages only where necessary, and ensure everything 
is heavily cross-referenced using [[links]]."*
3. **Observe:** Watch the Obsidian Graph View. You will see Claude 
automatically draw lines connecting the compute scaling of 
Moore's Law to the breakthroughs in AI—connections you didn't have 
to make yourself.

### Phase 3: The Synthesis

1. **Prompt:**

```text
Based ONLY on my wiki, explain how hardware limitations
dictated the timeline of AI advancements. Please generate
the response as a separate file hw_relation_to_ai_advancement.md
in the project/llm_wiki/ directory.
```

2. **Key Takeaway:** The AI isn't searching the open internet; it is
providing a synthesized answer based entirely on the curated knowledge
graph it built for you.

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

```bash
curl -o raw_sources/gpu_computing.html \
  "https://en.wikipedia.org/wiki/Graphics_processing_unit"
```

#### Step 2: Ingest and link

```text
Ingest raw_sources/gpu_computing.html. Create concept notes,
people notes, and technology notes following the same pattern
as the existing wiki. Cross-reference new notes with existing
ones (especially Moore's Law, Dennard Scaling, Deep Learning,
and Transformer Architecture) where the topics connect. Update
Home.md to include the new topic under the appropriate sections.
```

#### Step 3: Verify

```bash
python3 projects/llm_wiki/verify_links.py
```

All checks must pass: zero orphans, zero broken wikilinks.

#### Step 4: Explore the knowledge graph

Open **Obsidian Graph View**. Navigate `Home.md` and look for
connections between GPU Computing and the previous topics. Note
which existing notes gained new incoming links — this is where
your knowledge graph compounded.

Then query your personal knowledge graph:

```text
Based ONLY on my wiki, explain how GPU computing transformed the
pace of AI breakthroughs after Moore's Law began to plateau. 
Please generate the response as a separate file 
gpu_impact_on_ai_breakthrough.md in the project/llm_wiki/ 
directory
```

A strong answer will pull from at least four topics: Moore's Law,
Dennard Scaling, Deep Learning, and Transformer Architecture —
showing that the knowledge graph is genuinely connected.

> **If you chose your own topic:** navigate `Home.md` to discover
> which previous topics your new topic relates to — the cross-links
> reveal the connections. Then form your own synthesis question that
> ties your new topic to at least two existing ones.

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
