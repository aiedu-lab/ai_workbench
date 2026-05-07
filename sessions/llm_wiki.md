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

### Before You Begin: Reset to Pristine State

The `plan.md` and `articles.md` in your subject directory may
already have completed checkboxes from a prior run. Copy the
pristine versions to reset them before starting Phase 1:

```bash
cp projects/llm_wiki/SiliconAndAI/pristine/plan.md \
   projects/llm_wiki/SiliconAndAI/plan.md
cp projects/llm_wiki/SiliconAndAI/pristine/articles.md \
   projects/llm_wiki/SiliconAndAI/articles.md
```

> The `pristine/` directory is committed to git and never
> modified during execution — always safe to copy from.

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

### Phase 4: Expand with a New Article

**Topic: GPU Computing.**
> Why GPU Computing? It connects directly to both Moore's Law
> (billions of transistors packed onto a single chip) and the
> History of AI (the GPU-powered deep learning revolution of
> 2012 that ended the second AI Winter). Ingesting it generates
> new cross-links to Dennard Scaling, Deep Learning, Transformer
> Architecture, Gordon Moore, and more.

#### Step 1: Register and fetch the article

Add a GPU Computing URL to `articles.md` (state `[ ]`).
Run Phase 2 of `plan.md` to fetch it to
`raw_sources/public/` and mark it `[x]`.

> See [Phase 2: Data Fetching](
> ../projects/llm_wiki/SiliconAndAI/plan.md)
> for the exact command.

#### Step 2: Incremental ingestion

Run Phase 5 (Incremental Ingestion) of `plan.md`. Claude
enriches or creates notes, cross-links new content with ALL
relevant existing notes, updates `Home.md`, and resolves
any new orphans.

> See [Phase 5: Incremental Ingestion](
> ../projects/llm_wiki/SiliconAndAI/plan.md)
> for the exact prompt.

#### Step 3: Explore the knowledge graph

Open **Obsidian Graph View**. Navigate `Home.md` and look
for connections between GPU Computing and the previous
topics. Note which existing notes gained new incoming links
— this is where your knowledge graph compounded.

---

### Coherent Home.md Growth

Each subject's `Home.md` lives in its own subdirectory and
is the **index** for that subject, not a vault-wide
encyclopaedia.

**Expanding an existing subject (Phase 4):** each new
article enriches the subject's existing `Home.md` — add
only a small number of canonical entries, one line per major
new concept, person, or technology. Niche concepts go as
sub-bullets.

**Model:** look at how Moore's Law and History of AI were
factored in (Phases 1–2). Each article added:
- A handful of entries under **Recent Additions**
- Key concept titles under **Core Concepts**
- Names under **People** (grouped by era or field)
- Key technologies under **Technologies**

**Adding a new subject (Optional Extension):** create a new
subdirectory with its own `Home.md` and `plan.md` — it does
not modify the existing subject's `Home.md`.

> **Rule:** if removing a `Home.md` entry wouldn't confuse
> a future reader of the vault, don't add it.

---

### Optional Extension — Group Meetup Organizer PKM

This is a **new subject** exercise — follow the
"Adding a New Subject" workflow from
[projects/llm_wiki/README.md](
../projects/llm_wiki/README.md),
not the Phase 4 incremental-ingestion pattern.

1. Create a `GroupMeetup/` subdirectory at the vault root.
2. Copy and adapt `SiliconAndAI/plan.md` for the
   `GroupMeetup` taxonomy (`concepts/`, `tech/`).
3. Add `plans/specs/event_organizer.md` as a private article
   in `GroupMeetup/articles.md` (state `[ ]`).
4. Run Phases 1–4 of the new `plan.md`:
   - Initialise dirs, `Home.md`, `articles.md`
   - Fetch / confirm `event_organizer.md` in `raw_sources/`
   - Ingest: create notes for Poller, Selector, Notifier,
     Discord Webhooks; cross-reference with any AI or
     systems notes that connect
   - Verify: resolve orphans

The new `GroupMeetup/Home.md` is created fresh — it does
not modify `SiliconAndAI/Home.md`. This connects the PKM
session to the Group Meetup Organizer project running
through every other session in the lab.
