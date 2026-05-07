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

### The Framework

The LLM Wiki uses **Specification Driven PKM**: each subject
lives in its own subdirectory with a dedicated `Home.md`,
`plan.md`, and taxonomy folders (`concepts/`, `people/`,
`tech/`). `raw_sources/` holds fetched articles locally
(gitignored); `analysis/` stores synthesis outputs.

Three workflows cover every update scenario:

| Scenario | Workflow |
|---|---|
| New subject | Create subdirectory; adapt `plan.md`; run Phases 1–4 |
| New article, existing subject | Register in `articles.md`; run Phase 5 |
| Updated article | Uncheck `[✓]→[ ]` in `articles.md`; re-run Phase 5 |

> For the full directory layout and workflow steps, see
> [projects/llm_wiki/README.md](
> ../projects/llm_wiki/README.md).

### Phase 1: The First Ingest

**Concept:** Initialise the `SiliconAndAI` vault (Phases 1–2
of `plan.md`), fetch the Moore's Law Wikipedia article to
`raw_sources/public/`, then run Phase 3 (Data Ingestion):
Claude creates concept, people, and technology notes linked
with Obsidian `[[wikilinks]]`. Open Obsidian Graph View to
see the first cluster of linked notes appear.

> For commands and prompts, see
> [Phases 1–3 of the detailed plan](
> ../projects/llm_wiki/SiliconAndAI/plan.md).

### Phase 2: The Compound Effect

**Concept:** Register the History of AI article in
`articles.md` (state `[ ]`), fetch it via Phase 2 of
`plan.md`, then run Phase 5 (Incremental Ingestion). Claude
enriches existing notes and draws explicit cross-links —
watch Obsidian Graph View connect Moore's Law breakthroughs
to AI milestones without any manual linking.

> For commands and prompts, see
> [Phase 5: Incremental Ingestion](
> ../projects/llm_wiki/SiliconAndAI/plan.md).

### Phase 3: The Synthesis

**Concept:** Run Phase 4 (Verification) of `plan.md` to
check for orphaned notes, then issue the synthesis prompt.
Claude saves the analysis to `analysis/` — no internet
search; synthesis is drawn entirely from the curated
knowledge graph it built.

**Key Takeaway:** The AI is not searching the open internet;
it is synthesizing from the curated knowledge graph it built.

> For the synthesis prompt and verification steps, see
> [Phase 4: Verification](
> ../projects/llm_wiki/SiliconAndAI/plan.md).

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
