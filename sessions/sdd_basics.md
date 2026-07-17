# Concept: Spec Driven Development (SDD)

## 🎯 Objective
Learn how to build software by writing the "instructions" before writing
the code. Spec Driven Development (SDD) teaches AI agents exactly what
to build, how to build it, and in what order.

## 🧠 The Core Artifacts

### 1. `CLAUDE.md` (The Operating Protocol)
This is the rulebook for your AI. Instead of relying on legacy
environment files or repetitive prompting, we put the essence of our
coding standards here.
* **What it does:** Tells the agent what languages to use, how to
  format code, and what tools to run.
* **Example Rule:**
```text
Always write tests before implementing the logic.
Use Vite for the frontend.
```

### 2. `plan.md` (The Blueprint)
The step-by-step checklist. AI agents get confused if you ask for an
entire app at once. `plan.md` breaks the project into manageable,
verifiable phases.

## 🔑 Key Takeaway
You are the *architect*. The AI is the *typist*. If the code fails,
the bug is usually in your `plan.md` or `CLAUDE.md`, not the AI's
execution.

## 🏃 Exercise
For the hands-on SDD project, see
[Exercise: Create Group Meetup Organizer using SDD](client_application.md).

## Specification Driven Beyond Code

SDD applies a spec-first workflow to software — but the same pattern
works across many creative and knowledge domains. The AI is always the
typist; the human defines the spec and validates the output:

| Domain | Name | Spec | AI generates |
|--------|------|------|--------------|
| Software | [**SDD**](client_application.md#exercise--group-meetup-organizer-non-agentic-version) | `CLAUDE.md` + `plan.md` | Code, tests, configs |
| Presentation | [**SDP**](presentation_n_design.md#exercise-b--group-meetup-organizer-pitch-deck-toy-version-0-gamma) | Slide outline or brief | Decks, UI mockups |
| Knowledge base | [**SDPKM**](llm_wiki.md#the-exercise-compounding-knowledge) | Topic list + vault structure | Cross-linked wiki notes |
| Workbench | [**SDW**](../miscellaneous/software_defined_workbench/plan.md) | `miscellaneous/software_defined_workbench/plan.md` | Lab sessions, tools, exercises |
| Bootstrapping | **SDB** | Idea brief + market scope | Research memos, GTM plans, product mocks |
| Engineering Design | **SDCAD** | Design constraints + tolerances | AutoDesk drawings, simulation configs |
| Creative Tooling | **SDCT** | Scene description + style guide | Blender models, shader scripts, animations |
| Research synthesis | **SDRS** | Research question + source list | Literature summaries, citation graphs |

See [example SDD prompts](../projects/sdd_prompts/prompts.md) for
reusable templates that apply across any row above.
| Data pipelines | [**SDDP**](client_multiagent.md#exercise-2-mini-data-pipeline) | Schema + transformation rules | ETL scripts, dbt models, validation tests |

> This workbench itself is built using Specifications.
> See [`plan.md`](../miscellaneous/software_defined_workbench/plan.md)
> as a live example of SDW — every session and exercise in the lab
> was generated from that plan.

The SDD session teaches the pattern for code. The same mindset —
write the spec first, generate from it, iterate — transfers directly
to SDP ([Presentation & Design](presentation_n_design.md)) and
SDPKM ([LLM Wiki / PKM](llm_wiki.md)).

## Specifications as a Universal Interface

A specification can drive **any digital service** that exposes an
LLM-readable interface — an MCP server or an API with schema,
types, and descriptions that make the rules of execution explicit.
The LLM reads the spec, interprets the interface contract, and
generates or executes the required actions.

If the physical world is digitally controlled — via robots,
CNC machines, or IoT actuators — LLMs can drive activities that
span both digital and physical realms, using MCP or APIs as the
digital interface to the physical world. The specification is
always the contract; the interface is always the boundary.

---

## Human-Driven vs Spec-Driven vs Vibe-Coded

| Mode | Human owns | AI owns |
|---|---|---|
| **Human-Driven (HDD)** | Module design, API contracts, data flow | Function bodies, tests, boilerplate |
| **Spec-Driven (SDD)** | Specification document, acceptance criteria | Code, structure, iteration |
| **Vibe-Coded** | High-level intent | Everything else |

**HDD** is the safest pattern for high-penalty domains (finance,
safety-critical systems) where a hallucinated API contract causes
data loss or harm — the human locks every interface before any code
is written.

**SDD** is the default for structured delivery: the spec is the
contract, the AI generates from it, and the human reviews diffs.

**Vibe-Coded** maximises speed and is appropriate for exploration,
prototypes, and throwaway scripts where correctness is not
critical — iterate fast, throw away when done.

## References
* [SciFin Video Session - video session by Mohit Aron](
    https://drive.google.com/file/d/1wYSUCL2zcvaK2kYEfbl-YGFicNZZSlxr/view
  )
