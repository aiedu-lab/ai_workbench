# Speed Reading Mindmap

Convert any PDF, web page, or text file into an interactive
HTML mindmap using a four-agent AI pipeline. A single script
(`src/piper.py`) orchestrates all phases — from input
conversion through synthesis, rendering, QA review, and final
independent verification.

---

## Three Agenting Modes

The same speed-reading problem is solved three ways — one per
agenting style — each in its own subdirectory:

| Mode | Subdirectory | Description |
|---|---|---|
| Static | [`static/`](static/README.md) | Agent functions declared in specs; dispatch and lifecycle fixed in developer code (`src/piper.py`) |
| Dynamic | [`dynamic/`](dynamic/README.md) | Agent functions declared in specs; coordinator LLM routes and orchestrates dynamically |
| Vibe | [`vibe/`](vibe/README.md) | No pre-declared specs; the LLM invents agents and routing on the fly |

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
                    └─ [⟳] Leo                  map creator             .tmp/<book>-mindmap-<N>.html
                         └─ [ ] Quinn            QA reviewer             qa
                              └─ [ ] Sentinel    final gate              qa
```

**Book-name prefix**: all `.tmp/` files use the book filename.
For `examples/contents/the-coming-wave.pdf`:

```
examples/.tmp/the-coming-wave-detailed-notes.md
examples/.tmp/the-coming-wave-mindmap-content.json
examples/.tmp/the-coming-wave-mindmap-1.html  ← Leo attempt 1
examples/.tmp/the-coming-wave-mindmap-2.html  ← Leo attempt 2
examples/the-coming-wave-mindmap.html         ← final (post-Sentinel)
```

---

## Usage

```bash
cd projects/llm_wiki/speed-reading

# Show all options and phase names
python3 src/piper.py --help
```

### Worked example — AI-Native Company Playbook (URL)

```bash
# Full run with agent + waterfall logging (recommended)
# Logs go to examples/.tmp/ — already gitignored.
python3 src/piper.py \
  --input         https://www.dench.com/blog/the-ai-native-company-playbook \
  --output        examples/ai-native-company-playbook-mindmap.html \
  --log-dir       examples/.tmp \
  --waterfall-log examples/.tmp/piper-waterfall.log

# In a second terminal — monitor Leo attempt 1 in real time:
tail -f examples/.tmp/ai-native-company-playbook-leo-1.log

# Check pipeline progress / final status (works even if
# stdout was unavailable — e.g. launched from an agent):
tail -30 examples/.tmp/piper-waterfall.log
# Validator-loop agents include attempt number (retries get -2, -3):
#   ai-native-company-playbook-leo-1.log
#   ai-native-company-playbook-quinn-1.log
#   ai-native-company-playbook-sentinel-1.log
# Seth has no retries, so no attempt suffix:
#   ai-native-company-playbook-seth.log
```

Log files are prefixed with the book name — consistent with all
other `.tmp/` artifacts — so multiple books share the same
directory without collision. Stale logs for a book are deleted
automatically at the start of each new run.
The waterfall display (stdout) is unaffected.

```bash
# Resume if Seth done but validator-loop / leo failed
# (validator-loop and leo are identical — use either name)
python3 src/piper.py \
  --from-phase leo \
  --input   https://www.dench.com/blog/the-ai-native-company-playbook \
  --output  examples/ai-native-company-playbook-mindmap.html \
  --log-dir examples/.tmp

# Resume from Quinn — Leo's HTML exists, session ran out of tokens
python3 src/piper.py \
  --from-phase quinn \
  --input   https://www.dench.com/blog/the-ai-native-company-playbook \
  --output  examples/ai-native-company-playbook-mindmap.html \
  --log-dir examples/.tmp

# Resume from Sentinel — Leo + Quinn done, only Sentinel left
python3 src/piper.py \
  --from-phase sentinel \
  --input   https://www.dench.com/blog/the-ai-native-company-playbook \
  --output  examples/ai-native-company-playbook-mindmap.html \
  --log-dir examples/.tmp
```

Open `examples/ai-native-company-playbook-mindmap.html` in
any browser.

### URL corpus archival

All source materials live in a `contents/` subfolder within the
output directory, keeping raw corpus separate from generated
mindmap HTML:

- **URL inputs**: `piper.py` downloads the HTML automatically
  to `contents/{book}.html`.
- **PDF inputs**: place the PDF in `contents/` manually before
  running, then pass `--input contents/TheComingWave.pdf`.

```
examples/
  contents/
    the-coming-wave.pdf                     ← PDF source corpus
    the-ai-native-company-playbook.html     ← downloaded HTML corpus
  the-ai-native-company-playbook-mindmap.html  ← mindmap output
  read-list.md                             ← processing record
```

This means you can re-run the pipeline from `--from-phase seth`
or later without network access.

### Is the mindmap final or an in-progress draft?

Two authoritative signals:

**`read-list.md`** (most reliable) — updated at each phase
completion. `[✓]` means all agents approved; any other tag
means the pipeline stopped at that phase:

```bash
cat examples/read-list.md
# - [✓] [the-coming-wave](...) — fully approved
# - [seth] [the-coming-wave](...) — Seth done, Leo not started
```

**`--waterfall-log`** (when stdout unavailable) — shows the
pipeline state at each transition. The last snapshot in the
file is the final state:

```bash
tail -30 examples/.tmp/piper-waterfall.log
# Final snapshot shows [✓]/[~] for every phase when done.
# Shows [⟳] on the last active phase if interrupted.
```

Neither the output HTML nor its file-system timestamp is
reliable alone — Leo writes a draft HTML during the validator
loop that Quinn/Sentinel may then reject and Leo rewrite.

### Processed materials record

`read-list.md` in the output directory tracks every book or
article processed by `piper.py`. Status symbols:

| Symbol | Meaning |
|---|---|
| `[ ]` | Not yet started |
| `[converter]` / `[seth]` / `[leo]` / `[quinn]` | Last completed phase |
| `[✓]` | Mindmap fully built |

`piper.py` updates this file automatically at each completed phase.
To see all processed materials and their status:

```bash
cat examples/read-list.md
```

### Other input types

```bash
# From a plain-text or Markdown notes file
python3 src/piper.py --input my-notes.md --output mindmap.html

# From a URL (HTML auto-downloaded to examples/contents/)
python3 src/piper.py \
  --input   https://www.dench.com/blog/the-ai-native-company-playbook \
  --output  examples/the-ai-native-company-playbook-mindmap.html \
  --log-dir examples/.tmp
```

### Resuming with `--from-phase`

Each phase writes a named artifact to `.tmp/`. If a run is
interrupted (e.g. API rate limit), check which artifact was
last written and resume from the next phase:

| Last artifact written | Resume flag |
|---|---|
| `<book>-detailed-notes.md` | `--from-phase seth` |
| `<book>-mindmap-content.json` | `--from-phase validator-loop` or `--from-phase leo` |
| `.tmp/<book>-mindmap-1.html` exists (Leo attempt 1 done) | `--from-phase quinn` |
| Leo + Quinn done (attempt 1) | `--from-phase sentinel` |

The script verifies the prior artifact exists before skipping.

---

## Track / Debug / Troubleshoot

### Is the pipeline running?

```bash
# Is the orchestrator process alive?
pgrep -a -f "piper.py"

# Is a claude agent subprocess active right now?
pgrep -a -f "claude.*bypassPermissions" | grep -v pgrep
```

### Which agent is active, and is it making progress?

Agent logs live in `.tmp/` and are prefixed by book name.
The `.raw.jsonl` file grows with every event (tool calls,
thinking, text); the `.log` file grows only when the agent
emits text output. Compare sizes a few seconds apart:

```bash
# All agent logs for a book, newest first
ls -lt examples/.tmp/the-coming-wave-*.log | head -6

# Is the active agent making progress? Run twice ~10s apart;
# if the byte count grows, the agent is live.
ls -t examples/.tmp/the-coming-wave-*.raw.jsonl | head -1 \
  | xargs wc -c

# Stream the active agent's text output in real time
tail -f examples/.tmp/the-coming-wave-leo-3.log
```

### Is the mindmap final and fully approved?

**`read-list.md` is the authoritative signal:**

```bash
cat examples/read-list.md
# [✓]          mindmap fully approved by Quinn + Sentinel
# [seth]        Seth done; Leo not yet started
# [leo]         Leo draft in .tmp/; Quinn/Sentinel not yet run
# [converter]   Notes extracted; Seth not yet run
```

The HTML at `examples/<book>-mindmap.html` exists **only
after Sentinel approves** — Leo writes its drafts to
`examples/.tmp/<book>-mindmap.html` and rewrites on each
retry. Do not rely on the file's presence or timestamp alone.

### Why are some agent log files 0 bytes?

Two causes:

1. **Normal** — agent is in thinking/tool-call mode; only
   the `.raw.jsonl` is growing. The `.log` grows once the
   agent emits text.
2. **Bug (historic)** — `claude --print --output-format
   stream-json` requires `--verbose`; without it the CLI
   exits silently, leaving both `.log` and `.raw.jsonl` at 0
   bytes. Fixed: `src/orchestrator.py` now includes
   `--verbose` in every agent invocation.

### Attempt count and retry history

The validator loop retries Leo up to 3 times when Quinn or
Sentinel rejects. Logs and HTML drafts are numbered by attempt:

```
.tmp/<book>-seth.log            ← Seth (no retries)
.tmp/<book>-leo-1.log           ← Leo attempt 1
.tmp/<book>-mindmap-1.html      ← Leo attempt 1 HTML draft
.tmp/<book>-quinn-1.log
.tmp/<book>-sentinel-1.log
.tmp/<book>-leo-2.log           ← Leo attempt 2 (if 1 rejected)
.tmp/<book>-mindmap-2.html      ← Leo attempt 2 HTML draft
...
<book>-mindmap.html             ← final copy (Sentinel approved)
```

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
