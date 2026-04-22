# Plan: Spec Driven Content Creation (SDCC)

TL;DR
This plan breaks the SDCC effort into discrete phases for the slide 
session, client workflow session, server workflow session, SDD 
refactor, agenda update, and final review. Each phase contains
concrete steps for the specific session file targets, and we will 
execute one step at a time.

## Phase 1: SLIDES
[x] Review and expand `slides.md` to add:
  * Gamma install and start instructions 
  * student/team discount guidance
  * guardrails for safe content generation
  * tokenomics guidance for cost control
  * validation exercises that prove students understand prompting and structure
[x] Confirm any supporting references in `introduction.md` and 
`README.md` if needed.
  * Login verification moved into slides.md Setup > Install/Start.
  * README.md agenda entry already correct — no changes needed.
  * Mark the slide session content ready for review.

## Phase 2: CLIENT WORKFLOW
[x] Review `client_work_automation.md` and add:
  * Claude CoWork install and try instructions
  * student/team discount guidance
  * guardrails for safe CoWork automation and file handling
  * tokenomics guidance for cost-conscious use
  * validation exercises that ensure students grok safe workflow execution
[x] Ensure `client_application.md` incorporates the SDD exercise narrative and clearly connects with the client workflow practice.
  * SDD framing blockquote added; stack (React+TS+FastAPI+MongoDB) from sdd_basics.md adopted.
  * event_organizer.md generalized for any meetup (study groups, social clubs).
  * README.md agenda rows updated for consistency.
[x] Mark the client workflow session content ready for review.

## Phase 3: SERVER WORKFLOW
[x] Review `server_multiagent.md` and add:
  * OpenClaw install and try instructions
  * student/team discount guidance
  * guardrails for safe server-side workflow execution
  * tokenomics guidance for multi-agent server workflows
  * validation exercises that ensure students understand orchestration and failure handling
[x] Confirm the server workflow content aligns with `server_application.md` and `sdlc_ai.md`.
  * server_application.md removed — content consolidated into server_multiagent.md
    (Phase 1: single agent; Phase 4: server/Docker deployment).
  * Flight Tracker preserved as alternative project note in server_multiagent.md.
  * tools/temporal/cli.md created and linked. sdlc_ai.md confirmed aligned.
  * README.md two server rows merged into one with OpenClaw + Temporal tool links.
[x] Mark the server workflow session content ready for review.

## Phase 4: SDD REFACTOR
[x] Review `sdd_basics.md` and refactor it to emphasize concept and methodology only.
[x] Consolidate the concrete SDD exercise narrative into client_application.md or a dedicated exercise file if needed.
[x] Ensure the SDD concept file links clearly to the client application exercise.
[x] Mark the SDD refactor ready for review.
  * Absorbed into Phase 2 Step 3 (inseparable from client_application.md update).

## Phase 5: AGENDA UPDATE
[x] Update `README.md` Agenda to place:
  * `code_review.md` immediately after the client application development exercise
  * `sdlc_ai.md` next, before server and advanced workflow sessions
[x] Clarify tool labels and session timings for the updated flow.
  * Tool labels and timings were already consistent — no changes needed.
[x] Mark the agenda update ready for review.

## Phase 6: FINAL REVIEW
[x] Review all revised files for consistency and correct references.
  * slides.md: fixed broken session-notes path, trailing whitespace, missing newline.
  * sdd_basics.md: updated exercise link text to match README agenda label.
  * client_application.md: added blank line after ## Tools.
  * event_organizer.md: fixed 'Thursady' typo; 'chosen restaurant' → 'chosen venue'.
  * All Output section plan.md links confirmed as intentional forward references.
  * Orphaned learnings/session_notes/server_application.md noted (pre-existing).
[x] Confirm the updated agenda, SDD refactor, and exercise content support the intended learning progression.
  * Progression: build app → review code → understand SDLC → automate workflows → scale to server.
  * SDD concept (sdd_basics.md) cleanly separated from exercise (client_application.md).
  * All Tools/Setup sections consistent across session files.
[x] Save a final completion note in plan.md and prepare to execute the next approved step.
  * All 6 phases complete. Branch feat/sdlc ready for PR and review.
 
## Verification
* Each phase explicitly names the target markdown files.
* Each step is actionable and sequential, supporting one-at-a-time execution.
* The plan stays within the SDCC scope and does not change unrelated files.
