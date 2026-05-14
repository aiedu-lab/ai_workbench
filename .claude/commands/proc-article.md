Execute the knowledge ingestion plan for the $ARGUMENTS subject.

## Usage

/proc-article <subject>

Valid subjects: `eapm`, `silicon_ai`

## Plan and History File Locations

- `eapm` — plan: `eapm/proc_article.md`
           history: `eapm/proc_article_history.md`
- `silicon_ai` — plan:
                `projects/llm_wiki/silicon_ai/proc_article.md`
                history:
                `projects/llm_wiki/silicon_ai/proc_article_history.md`

## Steps

1. **Validate argument.** `$ARGUMENTS` must be exactly `eapm` or
   `silicon_ai`. If missing or invalid, print:
   ```
   Usage: /proc-article <subject>
   Valid subjects: eapm, silicon_ai
   ```
   Then stop.

2. **Read the plan.** Load the plan file for `$ARGUMENTS` per the
   table above to understand execution phases and the idempotency
   rule.

3. **Read articles.md.** Open `$ARGUMENTS/articles.md` and apply
   the idempotency rule:
   - All `[✓]` → report "nothing to ingest" and stop.
   - Any `[x]` → skip Phases 1–3; run Phase 5 only.
   - Any `[ ]` → run Phases 1–4 in order.

4. **Execute.** Follow all CLAUDE.md behavioral invariants:
   - Explore before acting (read files before modifying).
   - One step at a time; show diff; wait for approval.
   - Commit after each completed step.

5. **Record completion.** After any Phase 5 run, append the run
   record to the subject's history file per the table above.

6. **Announce.** Report:
   - New notes created (file names)
   - Existing notes enriched (file names)
   - Orphans resolved (if any)
   - Final articles.md state
