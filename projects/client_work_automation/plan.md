# Project Plan: Multiagent Workflow On Client

> **Maintenance Rule:** When a Phase is 100% complete, move its
> detailed steps to `docs/archive/phase_X.md` and replace it here
> with a one-line summary. Keep this file under 150 lines of active
> content — it is loaded into every Claude Code session and a bloated
> plan wastes context tokens.

---

## 🟡 Phase 1: Multi-Agent Code Review Pipeline

*Status: Proposed*

* [ ] **Step 1.1: Claude Code generates organizer script**
  * Context: script that organizes files in a folder
  * Task: python script moved files into folders based on file type 
  * Output: `organizer.py` from prompt — file sorter based on file type
  * Validation: test script against a directory with different file types;
    unit test data is created by running tests/test_dir.sh that creates 
    .tmp/test_dir directory and then different types of files inside it
  * Commit: `feat: Phase 1: Step 1 - generate organizer script`
  * Tag: `v1.1-organizer-script_step-completed`

* [ ] **Step 1.2: Codex reviews the script**
  * `codex exec` reviews for bugs, safety, failure modes
  * Output: `organizer_review.md`

* [ ] **Step 1.3: Claude Code applies fixes**
  * Read review, apply targeted fixes only, produce `organizer.fixed.py`

* [ ] **Step 1.4: Human diff review and acceptance**
  * `diff organizer.py organizer.fixed.py` → accept if appropriate
  * Commit: `feat: Phase 1: Step 4 - fixed organizer script`
  * Tag: `v1.4-organizer-script-fixed-review-step-completed`

---

## Session Rehydration Checklist

> Claude: read this block at the start of every session before acting.

```
Currently on  : Phase __, Step __ — [step title]
Last completed: Phase __, Step __ — [step title]
Last tag      : v__.__-[summary]-step-completed
Next action   : [one sentence]
```

Fill in the blanks from the checkboxes above, then confirm with the
user before proceeding.
