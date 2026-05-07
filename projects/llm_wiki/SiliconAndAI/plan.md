# Plan: LLM Wiki Initialization & Knowledge Ingestion

## 🎯 Objective
Transform this empty folder into a highly structured, interlinked 
personal knowledge base. You (the AI) will act as an autonomous 
librarian. You will read raw materials, extract concepts, and 
create a connected web of markdown files using Obsidian 
`[[wikilinks]]` format.

## 📁 Required Folder Structure
Before processing any data, ensure the following directory structure exists:
* articles.md       # references to all articles building our knowledge graph
* concepts          # for abstract ideas and theories
* people            # for historical figures and researchers
* raw_sources/
    public/     # URL-fetched public articles (html/md)
    private/    # privately supplied articles (md)
* tech              # for specific technologies, hardware, algorithms, etc.
* `Home.md`         # The entry point/index of the wiki

---

## 🏃‍♂️ Execution Phases

> **Before executing any phase**, read `articles.md` and apply this
> idempotency rule:
> - If every entry is `[✓]` → mark Phases 1–4 COMPLETED; stop.
>   Phase 5 will also find no `[x]` entries to process.
> - If any entry is `[x]` → skip Phases 1–3; run Phase 5 only.
> - If any entry is `[ ]` → run Phases 1–4 in order.
>
> Phases 1–4 run **once** during initial setup.
> Phase 5 is the **only** phase that runs for every new article
> added thereafter.

### Phase 1: Vault Initialization ✅ COMPLETED
- [x] Verify (or create if not present) the file/folder structure above.
- [x] Verify (or Create) `Home.md`. It should contain a welcome message
      and empty sections for "Recent Additions," "Core Concepts,"
      "People," and "Technologies."
- [x] `articles.md` has two sections: `## Private Articles` (local paths
      under `raw_sources/private/`) first, then `## Public Articles`
      (URLs fetched to `raw_sources/public/`) at the bottom so new
      public URLs are easy to append. Articles already
      fetched/placed are marked `[x]`; pending ones are `[ ]`.
- [x] Confirm `raw_sources/` is listed in `.gitignore`. Raw source
      files stay on local disk and are never committed to git.

### Phase 2: Data Fetching ✅ COMPLETED
- [x] For each `[ ]` entry in `## Public Articles`, fetch the URL
      and save to `raw_sources/public/<slug>.(html|md)`.
      Mark the entry `[x]` in `articles.md`.
- [x] For each `[ ]` entry in `## Private Articles`, confirm the
      file exists at the listed `raw_sources/private/` path.
      Mark the entry `[x]` in `articles.md`.
 
### Phase 3: Data Ingestion ✅ COMPLETED
- [x] Read the provided documents in `raw_sources/`.
- [x] For each document, extract the core and major themes.
      For each new theme, create a new file in `concepts` if one does
      not exist with a summary of the definition, implications, etc.
      Example: for "Moore's Law", summarize the definition and
      implications.
- [x] Create new files or update existing files in `people/` covering
      any people mentioned in the text.
      Example: Gordon Moore
- [x] Create new files or update existing files in `tech/` covering any
      technology mentioned in the text.
      Example: Transistors, Microprocessors
- [x] **Crucial Synthesis Step:**
      - Ensure that each of the topics in files of different directories
        are cross linked to files in other directories.
        Example: each concept within `concepts/` uses `[[wikilinks]]`
        to reference topics not yet linked i.e. `people`, `tech/`, ...
        Similarly, each person within `people/` uses `[[wikilinks]]` to
        reference topics not yet linked i.e. `tech/`
      - For every new document, review *existing* files. Update them
        with new context from the new document and draw explicit
        connections using `[[wikilinks]]`.
      - Link to ALL relevant existing notes in other directories —
        not just one.
      - When ingesting a new article, also update existing notes that
        are now relevant to it i.e. add a back-link from the existing
        note to the new one.
        Example: how the scaling of transistors enabled the training
        of deep neural networks.
- [x] Update `Home.md` to reflect the newly integrated knowledge graph
      with links and cross references to the file/content including
      any new ones.
- [x] For each article just ingested, mark it `[✓]` in `articles.md`.
      Raw source files are gitignored — they stay on local disk and
      are never committed. If a file was accidentally committed to
      git, remove it with: `git rm --cached <path>`.

### Phase 4: Verification ✅ COMPLETED
- [x] Run a check across all markdown files in `concepts/`, `people/`,
      and `tech/`.
- [x] Identify any "Orphaned" notes i.e. notes that do not have any
      `[[wikilinks]]` pointing to them or out of them.
- [x] If orphans exist, logically connect them to existing concepts.
- [x] Prompt the agent "Based ONLY on my wiki, explain how hardware
      limitations dictated the timeline of AI advancements and save
      your analysis in `analysis/hw_relation_to_ai_advancement.md`."
- [x] Announce completion to the user. For future articles, proceed
      to Phase 5.

### Phase 5: Incremental Ingestion 🔁 REPEATABLE

Run this phase each time a new article URL is added to
`articles.md` or a file is dropped into `raw_sources/`.

#### Checkpoint key used in `articles.md`
- `[ ]` — URL identified, not yet fetched
- `[x]` — saved to `raw_sources/public/` (public) or confirmed in
         `raw_sources/private/` (private); not yet ingested
- `[✓]` — fully ingested and cross-linked into wiki

#### Steps
- [ ] Read `articles.md`. Find all entries marked `[x]`
      (fetched but not yet ingested). These are the only files to process.
- [ ] For each `[x]` entry, read the corresponding file in `raw_sources/`.
- [ ] Extract new concepts, people, technologies, companies, and market data.
      For each extracted item:
      - If a note already exists in the relevant directory, **enrich** it
        (append new facts, add new `[[wikilinks]]`). Do NOT create a duplicate.
      - If no note exists, create one.
- [ ] For every new or enriched note, link to ALL relevant existing notes
      in other directories. Also update those existing notes with a
      back-link to the new/enriched note.
- [ ] Update `Home.md`: add links to any brand-new notes under the
      appropriate section. Update "Recent Additions."
- [ ] Run orphan check: scan all notes in `concepts/`, `people/`,
      `tech/` for notes with no inbound or outbound `[[wikilinks]]`.
      Resolve any new orphans before proceeding.
- [ ] Mark the processed entry in `articles.md` as `[✓]`.
      Raw source file stays on local disk (gitignored). If it was
      accidentally committed to git: `git rm --cached <path>`.
- [ ] Announce: list new notes created, existing notes enriched, and
      any orphans resolved.
