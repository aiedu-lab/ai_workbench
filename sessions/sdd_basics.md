# Spec Driven Development - SDD

# Concept & Exercise: Spec Driven Development (SDD)

## 🎯 Objective
Learn how to build software by writing the "instructions" before writing 
the code. Spec Driven Development (SDD) teaches AI agents exactly what 
to build, how to build it, and in what order. We will use as an exercise
building a simple project to experience this end-to-end.

## 🧠 The Core Artifacts

### 1. `CLAUDE.md` (The Operating Protocol)
This is the rulebook for your AI. Instead of relying on legacy environment 
files or repetitive prompting, we put the essence of our coding standards 
here. 
* **What it does:** Tells the agent what languages to use, how to format 
code, and what tools to run.
* **Example Rule:**  
```markdown 
Always write tests before implementing the logic. 
Use Vite for the frontend.
```
### 2. `plan.md` (The Blueprint)
The step-by-step checklist. AI agents get confused if you ask for an entire
app at once. `plan.md` breaks the project into manageable, verifiable phases.

---

## 🛠️ Exercise: **Group Event Tracker**
A simple web app to coordinate local social events, such as study 
group meetings.
* **Frontend:** React + TypeScript (via Vite) - *Simple, fast UI.*
* **Backend:** FastAPI (Python) - *Handles the business logic.*
* **Database:** MongoDB - *Stores the events.*

### The Data Model
Before coding, we define the data structure in our spec:
```json
// Event Model
{
  "id": "string",
  "title": "AI Workbench Prep",
  "location": "Cupertino Library",
  "date": "2026-05-15T15:00:00Z",
  "attendees": ["Adi", "Sid"]
}
```
---

## 🏃‍♂️ Executing the Plan

We will **Test-Driven Development (TDD)** to guide our CLI agent through 
these phases. The agent is not allowed to move to the next step until the 
tests for the current step pass.

### Phase 1: Backend Foundation (TDD Focus)
1. **Spec:** Instruct the agent to create a FastAPI route for `POST /events`.
2. **Test:** The agent must *first* write a Pytest that sends a mock event 
and expects a `200 OK`.
3. **Run:** Run the test (it fails).
4. **Code:** The agent writes the FastAPI logic to make the test pass.

### Phase 2: Database Integration
1. **Spec:** Connect the FastAPI backend to a local (or cloud) MongoDB 
instance.
2. **Test:** Write a test that saves an event and retrieves it by `id`.
3. **Run & Code:** Ensure the data model matches our spec and saves 
correctly.

### Phase 3: The Frontend
1. **Spec:** Initialize a Vite/React/TS app. Create a simple form with 
inputs for Title, Location, Date, and Attendees.
2. **Test:** Write a quick unit test (using React Testing Library) to 
ensure the form submission triggers an API call.
3. **Run & Code:** Wire the UI to our FastAPI backend.

### Key Takeaway for Students 
You are the *architect*. The AI is the *typist*. If the code fails, 
the bug is usually in your `plan.md` or `CLAUDE.md`, not the AI's 
execution.
