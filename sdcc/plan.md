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
[ ] Review `client_work_automation.md` and add:
  * Claude CoWork install and try instructions
  * student/team discount guidance
  * guardrails for safe CoWork automation and file handling
  * tokenomics guidance for cost-conscious use
  * validation exercises that ensure students grok safe workflow execution
[ ] Ensure `client_application.md` incorporates the SDD exercise narrative and clearly connects with the client workflow practice.
[ ] Mark the client workflow session content ready for review.

## Phase 3: SERVER WORKFLOW
[ ] Review `server_multiagent.md` and add:
  * OpenClaw install and try instructions
  * student/team discount guidance
  * guardrails for safe server-side workflow execution
  * tokenomics guidance for multi-agent server workflows
  * validation exercises that ensure students understand orchestration and failure handling
[ ] Confirm the server workflow content aligns with `server_application.md` and `sdlc_ai.md`.
[ ] Mark the server workflow session content ready for review.

## Phase 4: SDD REFACTOR
[ ] Review `sdd_basics.md` and refactor it to emphasize concept and methodology only.
[ ] Consolidate the concrete SDD exercise narrative into client_application.md or a dedicated exercise file if needed.
[ ] Ensure the SDD concept file links clearly to the client application exercise.
[ ] Mark the SDD refactor ready for review.

## Phase 5: AGENDA UPDATE
[ ] Update `README.md` Agenda to place:
  * `code_review.md` immediately after the client application development exercise
  * `sdlc_ai.md` next, before server and advanced workflow sessions
[ ] Clarify tool labels and session timings for the updated flow.
[ ] Mark the agenda update ready for review.

## Phase 6: FINAL REVIEW
[ ] Review all revised files for consistency and correct references.
[ ] Confirm the updated agenda, SDD refactor, and exercise content support the intended learning progression.
[ ] Save a final completion note in plan.md and prepare to execute the next approved step.
 
## Verification
* Each phase explicitly names the target markdown files.
* Each step is actionable and sequential, supporting one-at-a-time execution.
* The plan stays within the SDCC scope and does not change unrelated files.
