# Personal Knowledge Management (PKM)

Use AI agents and specification-driven techniques to build and
maintain a personal knowledge base. Each PKM mode lives in its
own subdirectory with its own execution plan and exercises.

## Operating Protocol

Ask the agent to execute the mode's execution plan (`proc_article.md`
or `src/piper.py`) per the repo root `CLAUDE.md` operating
protocol (Plan Update Protocol, one step per turn, commit after
each step).

---

## PKM Modes

| Mode | Subdirectory | Description |
|---|---|---|
| Knowledge Graph Wiki | [`silicon_ai/`](silicon_ai/README.md) | Ingest articles into a linked markdown wiki; visualize in Obsidian |
| Speed Reading Mindmap | [`speed-reading/`](speed-reading/README.md) | Convert books or articles into interactive HTML mindmaps |

Each subdirectory contains its own README with file layout,
workflows, and student exercises.
