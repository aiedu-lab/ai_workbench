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
```markdown
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
```markdown
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
1. **Prompt:** *"Based ONLY on my wiki, explain how hardware limitations 
dictated the timeline of AI advancements."*
2. **Key Takeaway:** The AI isn't searching the open internet; it is 
providing a synthesized answer based entirely on the curated knowledge 
graph it built for you.
