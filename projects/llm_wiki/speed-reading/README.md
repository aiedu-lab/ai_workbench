# Speed Reading Mindmap

Convert any PDF or text book into an interactive HTML mind-map
using a three-agent pipeline. The human reads and takes notes;
the AI pipeline synthesises, renders, and QA-reviews the result.

---

## Pipeline Architecture

```
build_mindmap.sh
      │
      │ (converts PDF/HTML/text → plain notes)
      ▼
  piper.sh (orchestrator)
      │
      ├─── Seth (content-synthesizer)
      │         notes → mindmap-content.json
      │
      ├─── Leo (layout-engineer)
      │         mindmap-content.json → mindmap.html
      │
      └─── Quinn (qa-reviewer)
                mindmap.html → APPROVED / NOT APPROVED
                (Leo+Quinn retry up to 3 times)
```

| Agent | File | Role |
|---|---|---|
| Seth | `agents/seth-content-synthesizer.md` | Distils notes into structured JSON |
| Leo | `agents/leo-layout-engineer.md` | Renders JSON to self-contained HTML |
| Quinn | `agents/quinn-qa-reviewer.md` | QA-reviews the rendered mindmap |
| Piper | `agents/piper-pipeline-orchestrator.md` | Pipeline doctrine reference |

---

## Usage

The main entry point is `build_mindmap.sh`. It accepts a PDF,
HTML page, or plain-text/Markdown file and produces a
`mindmap.html` you can open in any browser.

```bash
cd projects/llm_wiki/speed-reading

# From a PDF book
./build_mindmap.sh TheComingWave.pdf mindmap.html

# From a plain-text or Markdown notes file
./build_mindmap.sh my-notes.md mindmap.html

# From an HTML article (URL)
./build_mindmap.sh https://example.com/article.html mindmap.html
```

Open `mindmap.html` in a browser to explore the mind-map.

---

## Manual Run

To run the agent pipeline directly (if you already have
plain-text notes):

```bash
./piper.sh detailed-notes.md mindmap.html
```

`piper.sh` runs Seth → Leo → Quinn and retries Leo+Quinn up to
3 times if Quinn outputs `NOT APPROVED`.

---

## Agents

- **Seth** (`agents/seth-content-synthesizer.md`) — reads
  detailed notes, extracts key concepts, outputs structured
  JSON matching `templates/mindmap-content.template.json`.
- **Leo** (`agents/leo-layout-engineer.md`) — reads the
  JSON and renders a self-contained `mindmap.html` using the
  vis-network library.
- **Quinn** (`agents/quinn-qa-reviewer.md`) — reviews the
  rendered HTML; outputs `NOT APPROVED` with issues if quality
  checks fail.

---

## Templates

| File | Purpose |
|---|---|
| `templates/mindmap-content.template.json` | JSON schema Seth must match |
| `templates/mindmap-layout.template.json` | Layout parameters for Leo |
| `templates/detailed-notes.template.md` | Starter note-taking format |

Fill `templates/detailed-notes.template.md` while reading the
book, then run `build_mindmap.sh` on the resulting notes file.

---

## Prerequisites

- `pdftotext` (from `poppler-utils`) — for PDF input
- `html2text` — for HTML input
- `claude` CLI authenticated (`claude --version` returns ok)

`labsetup.py` installs all prerequisites automatically.
Manual install: `sudo apt install poppler-utils html2text`.
