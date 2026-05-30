# Speed Reading Mindmap

Convert any PDF, web page, or text file into an interactive
HTML mindmap using a four-agent AI pipeline. A single script
(`piper.sh`) orchestrates all phases — from input
conversion through synthesis, rendering, QA review, and final
independent verification.

---

## Pipeline — Waterfall View

`piper.sh` prints a 3-column waterfall at each phase transition.
Symbols: `[✓]` done · `[⟳]` active · `[~]` skipped · `[ ]`
pending. A stderr spinner animates during every active agent call.

```
Phase                                          Function                Artifact
─────────────────────────────────────────────  ──────────────────────  ──────────
[✓] sanitizer                                  arg parser              n/a
└─ [✓] setup                                   tool checker            n/a
     └─ [✓] converter                          note taker              .tmp/<book>-detailed-notes.md
          └─ [✓] Seth                          synthesizer             .tmp/<book>-mindmap-content.json
               └─ [⟳] validator                loop until success
                    |  Leo · Quinn · Sentinel  (attempt 2 of 3)
                    └─ [⟳] Leo                  map creator             .tmp/<book>-mindmap.html
                         └─ [ ] Quinn            QA reviewer             qa
                              └─ [ ] Sentinel    final gate              qa
```

**Book-name prefix**: all `.tmp/` files use the book filename.
For `example/TheComingWave.pdf`:

```
example/.tmp/TheComingWave-detailed-notes.md
example/.tmp/TheComingWave-mindmap-content.json
example/.tmp/TheComingWave-mindmap.html
```

---

## Usage

```bash
cd projects/llm_wiki/speed-reading

# Show all options and phase names
./piper.sh --help

# From a PDF book
./piper.sh example/TheComingWave.pdf \
  example/TheComingWave_mindmap.html

# From a plain-text or Markdown notes file
./piper.sh my-notes.md mindmap.html

# From an HTML article (URL)
./piper.sh https://example.com/article.html mindmap.html
```

Open the output `.html` file in any browser to explore the
mindmap.

### Resuming with `--from-phase`

Each phase writes a named artifact to `.tmp/`. If a run is
interrupted (e.g. API rate limit), resume from the first
incomplete phase — the script checks the prior-phase artifact
before skipping. For example, if Seth has completed for
`TheComingWave.pdf` but Leo failed, resume at `leo`:

```bash
# Seth already produced:
#   example/.tmp/TheComingWave-mindmap-content.json
# Resume at Leo (runs Leo + Quinn + Sentinel):
./piper.sh --from-phase leo \
  example/TheComingWave.pdf example/TheComingWave_mindmap.html
```

For a different book `my-notes.md`, the same pattern applies
— Seth would produce `<output-dir>/.tmp/my-notes-mindmap-
content.json` and `--from-phase leo` would verify it exists
before proceeding.

---

## Agents

Active agent prompts used by `piper.sh`:

| Agent | System prompt | Role |
|---|---|---|
| Seth | `agents/seth-content-synthesizer.md` | Distils notes into structured JSON |
| Leo | `agents/leo-layout-engineer.md` | Renders JSON to self-contained HTML |
| Quinn | `agents/quinn-qa-reviewer.md` | QA-reviews the rendered mindmap |
| Sentinel | `agents/sentinel-final-guardian.md` | Final independent verification; overrules Quinn on any missed failure |

### Reference / Doctrine Files

These files are NOT used as agent system prompts; they contain
pipeline doctrine and design rules for human reference:

| File | Purpose |
|---|---|
| `agents/piper-pipeline-orchestrator.md` | Pipeline doctrine: task scope locking, layer policies, agent coordination rules. **`piper.sh` is the concrete implementation of this doctrine.** Reference when extending the pipeline or debugging coordination issues. |
| `ai-mindmap.md` | Non-negotiable map rules and global doctrine for content and layout quality. |

---

## Templates

| File | Purpose |
|---|---|
| `templates/mindmap-content.template.json` | JSON schema Seth must match |
| `templates/mindmap-layout.template.json` | Layout parameters for Leo |
| `templates/detailed-notes.template.md` | Starter note-taking format |

Use `templates/detailed-notes.template.md` while reading a
book, then run `piper.sh` on the resulting notes file.

---

## Prerequisites

- `pdftotext` (from `poppler-utils`) — for PDF input
- `html2text` — for HTML input
- `claude` CLI authenticated (`claude --version` returns ok)

`labsetup.py` installs all prerequisites automatically.
Manual install: `sudo apt install poppler-utils html2text`.
