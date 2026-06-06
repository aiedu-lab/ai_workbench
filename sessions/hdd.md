# Concept: Human Driven Development (HDD)

## 🎯 Objective

Understand Human Driven Development — a pattern where the human
designs the full solution top-down (modules, APIs, data flow, test
cases) and the AI fills in the implementation details. Best suited
for high-penalty domains where an incorrect guess is costly.

---

## 🧠 The Core Concept

In HDD the human owns the architecture; the AI owns the code.

| Human owns | AI owns |
|---|---|
| Module decomposition | Function bodies |
| API contracts & signatures | Unit tests |
| Data structures | Docstrings |
| Execution sequence | Boilerplate |

The human's design document is the single source of truth. The AI
never speculates about *what* to build — only *how* to implement a
spec that is already fully described.

### When to use HDD

- **High-penalty domains** — finance, medical, safety-critical
  systems where a hallucinated interface causes data loss or harm.
- **Complex multi-module systems** — when inter-module contracts
  must be locked before any code is written.
- **Teaching contexts** — forces learners to think algorithmically
  before reaching for AI completion.

### HDD vs SDD vs Vibe-Coded

See the comparison table in
[Concept: Spec Driven Development](sdd_basics.md#human-driven-vs-spec-driven-vs-vibe-coded).

### Principles

1. **Probabilistic, not deterministic** — the same prompt does not
   produce identical code. GenAI output cannot be assumed correct
   by construction; it must be verified.
2. **Human accountability** — the human is ultimately accountable
   for the code. Accountability is meaningless without review.
3. **Review feasibility** — authentic review of generated code is
   only feasible when the scope of each review is ≤~200 lines 
   with each review focused on independent code structures i.e. 
   componentized with clear separation of concerns. 
   Hence, keep the structure surface of components small and 
   focused so the human can actually endorse what was built.

### Factors

- **Humans are smarter, but AI is faster** — the human supplies
  judgment and design; AI supplies execution speed.
- **Context overflow degrades quality** — AI output deteriorates
  when the context is too wide. Keep each AI task focused and
  limited in scope to one component at a time.

---

## 🏃 Exercise — Tower of Hanoi

**Project:** `projects/tower_of_hanoi/`

The Tower of Hanoi is a classic recursive puzzle. The human designs
the module layout and move-sequence contract; the AI implements
`Disc`, `Tower`, and `Solver` exactly to spec.

### Run

```bash
cd projects/tower_of_hanoi

# Solve in one shot — prints all moves
python3 src/main.py <num_discs>

# Step through one move at a time (press Enter each step)
python3 src/main.py <num_discs> --step
```

Example (3 discs):

```
$ python3 src/main.py 3
Move disc 1 from A to C
Move disc 2 from A to B
Move disc 1 from C to B
Move disc 3 from A to C
Move disc 1 from B to A
Move disc 2 from B to C
Move disc 1 from A to C
```

### Prompt file

`projects/tower_of_hanoi/toh_prompt.md` — the HDD spec the AI was
given. Read it before running the code to see how a complete spec
eliminates ambiguity.

### Discussion

- How much of the solution did the human specify before AI wrote
  any code?
- What would happen if the AI had guessed the API contract instead
  of following the spec?
- Where would bugs be harder to trace — in a vibe-coded version or
  in this HDD version?

## Credits

**How to use AI to generate production code**: by Mohit Aron 10-May-2026
