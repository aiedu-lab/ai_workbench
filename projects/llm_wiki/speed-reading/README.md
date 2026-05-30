# Speed Reading Mindmap

Convert any PDF, web page, or text file into an interactive
HTML mindmap using a four-agent AI pipeline. A single script
(`src/piper.py`) orchestrates all phases — from input
conversion through synthesis, rendering, QA review, and final
independent verification.

---

## Pipeline — Waterfall View

`src/piper.py` prints a 3-column waterfall at each phase
transition. Symbols: `[✓]` done · `[⟳]` active · `[~]`
skipped · `[ ]` pending. A stderr spinner animates during
every active agent call.

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
python3 src/piper.py --help
```

### Worked example — The Coming Wave (PDF)

```bash
# Full run from scratch
python3 src/piper.py \
  --input  example/TheComingWave.pdf \
  --output example/TheComingWave-mindmap.html

# Resume if Seth completed but Leo/Quinn/Sentinel failed
# (Seth artifact: example/.tmp/TheComingWave-mindmap-content.json)
python3 src/piper.py \
  --from-phase validator-loop \
  --input  example/TheComingWave.pdf \
  --output example/TheComingWave-mindmap.html
```

Open `example/TheComingWave-mindmap.html` in any browser.

### Other input types

```bash
# From a plain-text or Markdown notes file
python3 src/piper.py --input my-notes.md --output mindmap.html

# From an HTML article (URL)
python3 src/piper.py \
  --input  https://example.com/article.html \
  --output article-mindmap.html
```

### Resuming with `--from-phase`

Each phase writes a named artifact to `.tmp/`. If a run is
interrupted (e.g. API rate limit), check which artifact was
last written and resume from the next phase:

| Last artifact written | Resume flag |
|---|---|
| `<book>-detailed-notes.md` | `--from-phase seth` |
| `<book>-mindmap-content.json` | `--from-phase validator-loop` |

The script verifies the prior artifact exists before skipping.

---

## Code Layout

```
src/
  piper.py        CLI entry point; argument parsing; invokes Piper
  orchestrator.py Piper class; all five pipeline phases
  display.py      PhaseDisplay class; 3-column waterfall renderer
  spinner.py      Spinner class; threaded stderr progress indicator
```

| Module | Class | Responsibility |
|---|---|---|
| `piper.py` | — | Parses `--input/--output/--from-phase/--help`; runs `Piper` |
| `orchestrator.py` | `Piper` | Sequences sanitizer → setup → converter → Seth → validator-loop; retry logic |
| `display.py` | `PhaseDisplay` | Renders the 3-column Unicode waterfall at each phase transition |
| `spinner.py` | `Spinner` | Daemon thread that animates `/-\|` on stderr while agents run |

---

## Agents

Active agent prompts used by `src/piper.py`:

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
| `agents/piper-pipeline-orchestrator.md` | Pipeline doctrine: task scope locking, layer policies, agent coordination rules. **`src/piper.py` is the concrete implementation of this doctrine.** Reference when extending the pipeline or debugging coordination issues. |
| `ai-mindmap.md` | Non-negotiable map rules and global doctrine for content and layout quality. |

---

## Templates

| File | Purpose |
|---|---|
| `templates/mindmap-content.template.json` | JSON schema Seth must match |
| `templates/mindmap-layout.template.json` | Layout parameters for Leo |
| `templates/detailed-notes.template.md` | Starter note-taking format |

Use `templates/detailed-notes.template.md` while reading a
book, then run `src/piper.py` on the resulting notes file.

---

## Prerequisites

- `pdftotext` (from `poppler-utils`) — for PDF input
- `html2text` — for HTML input
- `claude` CLI authenticated (`claude --version` returns ok)

`labsetup.py` installs all prerequisites automatically.
Manual install: `sudo apt install poppler-utils html2text`.
