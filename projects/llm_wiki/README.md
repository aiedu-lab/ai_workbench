# PERSONAL KNOWLEDGE MANAGEMENT - PKM

## Objective
Used for **Personal Knowledge Management (PKM)**
and uses specification driven techniques to build `LLM Wiki`
on different high level subject with each topic kept in a
separate directory. Cross-links between notes use Obsidian
`[[wikilink]]` format throughout.

## Methodology
**Specification Driven PKM** where distinct Subjects are contained
in a subdirectory. For example, all **Knowledge Graph (KG)** on
`Silicon and AI relation and evolution` are in `SiliconAndAI`.

## Repository Layout
```
PKM/
  README.md             # This file
  SiliconAndAI/         # Subject — silicon scaling & AI history
    articles.md
    Home.md
    plan.md
    concepts/
    people/
    raw_sources/        # gitignored
      public/
      private/
    tech/
    analysis/           # gitignored — query outputs and synthesis
  <NextSubject>/        # Template for future subjects
```

---

## Workflows

### Adding a New Subject

1. **Create the directory** at repo root:
   ```
   <SubjectName>/
   ```
2. **Choose a taxonomy** for the subject's subdirectories.
   Examples:
   - Industry landscape: `companies/`, `concepts/`, `market/`, `tech/`
   - Academic/historical: `concepts/`, `people/`, `tech/`
3. **Create `articles.md`** with two empty sections:
   ```markdown
   ## Public Articles
   ## Private Articles
   ```
4. **Copy `plan.md`** from an existing subject and adapt:
   - Update the required folder structure list to match your taxonomy.
   - Update Phase 3 directory scan steps to match your taxonomy.
   - Update the Phase 4 synthesis prompt to reflect the subject.
5. **Run Phase 1** of `plan.md` — creates subdirs, `raw_sources/`,
   and a skeleton `Home.md`.
6. **Add initial articles** to `articles.md` (`[ ]` state).
7. **Run Phase 2** — fetches public URLs to `raw_sources/public/`;
   confirms private files in `raw_sources/private/`. Marks `[x]`.
8. **Run Phase 3** — ingests all articles into the knowledge graph.
   After each article is ingested, mark it `[✓]` in `articles.md`
   and delete its raw file from `raw_sources/` (private files are
   sensitive; public files are re-fetchable from `articles.md`).
9. **Run Phase 4** — verifies the graph, fixes orphans, runs the
   subject-specific synthesis prompt.

---

### Adding a New Article to an Existing Subject

1. **Register the article** in `<subject>/articles.md`:
   - Private file → drop in `raw_sources/private/`; add under
     `## Private Articles` (top section):
     ```
     * [ ] [Title](./raw_sources/private/<filename>.md)
     ```
   - Public URL → append under `## Public Articles` (bottom section,
     for easy appending):
     ```
     * [ ] [Title](https://...)
     ```
2. **Run Phase 2** (fetch / confirm):
   - Public: download URL → save to `raw_sources/public/<slug>`.
   - Private: confirm file exists at the listed path.
   - Mark the entry `[x]` in `articles.md`.
3. **Run Phase 5** (Incremental Ingestion):
   - Reads the `[x]` file from `raw_sources/`.
   - Extracts new themes; enriches or creates notes in the
     taxonomy directories.
   - Cross-links new content with ALL relevant existing notes
     and back-links existing notes to the new content.
   - Updates `Home.md` (Recent Additions + affected sections).
   - Runs an orphan check; resolves any new orphans.
   - Marks the entry `[✓]` in `articles.md`.
   - Raw source files are gitignored — they stay on local disk and
     are never pushed to git. No deletion needed.

> **Key principle:** The knowledge graph (`concepts/`, `people/`,
> `tech/`, etc.) is the durable artifact. `raw_sources/` is
> ephemeral processing input — gitignored and safe to delete once
> an article is marked `[✓]`.

---

### Updating an Existing Article

If you know an already-ingested article has changed:

1. **Uncheck it** in `articles.md`: change `[✓]` back to `[ ]`.
2. **Run Phase 2** as normal:
   - Public: re-fetches the URL → saves updated file → marks `[x]`.
   - Private: human copies the updated file to `raw_sources/private/`;
     Phase 2 confirms it exists and marks `[x]`.
3. **Run Phase 5** as normal — the enrichment instruction
   ("enrich existing notes, do NOT create duplicates") makes
   re-ingestion safe:
   - **No change in article:** nothing new to add → notes unchanged.
     Re-ingestion is idempotent.
   - **New content in article:** new facts flow into existing notes.
   - **Deleted content in article:** old facts stay in the KG.
     This is accepted behaviour — the KG is append-only by design.

> **Article update policy:** Articles are treated as immutable
> once marked `[✓]`. The KG is append-only — facts are enriched,
> never retracted. If an article is deleted or substantially
> wrong, manually edit the affected notes directly.
