# Project Plan: [Project Name]

> **Maintenance Rule:** When a Phase is 100% complete, move its detailed steps 
> to `docs/archive/phase_X.md` and replace it here with a one-line summary.

## 🟢 Phase [Current]: [Active Goal]
*Status: In Progress | Target: YYYY-MM-DD*

- [x] **Step 1.1: Core Primitive Implementation**
  - Context: Logic defined in `src/core/`
  - Validation: `bazel test //src/core/...`
- [/] **Step 1.2: Interface Integration**
  - [x] Define abstract base classes
  - [ ] Implement concrete providers
  - [ ] Connect to event sink
- [ ] **Step 1.3: Observability & Instrumentation**
  - [ ] Add OpenTelemetry traces
  - [ ] Verify payload capture in dev environment

## 🟡 Phase [Next]: [Upcoming Milestone]
*Status: Proposed*

- [ ] **Feature A:** Broad description of the next architectural shift.
- [ ] **Feature B:** Integration requirements for third-party protocols.
- [ ] **Security Audit:** Planned review of authorization predicates.

## ⚪ Phase [Future]: [Long-term Vision]
*Status: Backlog*
- High-level ideas that don't need details yet.

---

## 📁 Archived Phases
- [x] **Phase 0: Foundations** (See `docs/archive/phase_0.md`)
- [x] **Phase -1: Discovery** (See `docs/archive/phase_-1.md`)