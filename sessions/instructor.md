# Instructor Preflight Checklist

Complete every step and its validation before students arrive.
Time required: approximately 60 minutes.

> **Class ID convention:** choose a short unique identifier for
> this class run (e.g. `2026-spring`, `2026-fall-hs`). Replace
> every occurrence of `<CLASS_ID>` below with your chosen value.
> This prevents name collisions when the same instructor runs
> multiple cohorts.

---

## Section 1 — Collect Student Roster (5 min)

Before provisioning anything, collect one row per student in a
local roster file (never committed — contains personal info):

| Full name   | GitHub username | Discord username | Laptop OS   | Admin? | Server acct? |
|-------------|-----------------|------------------|-------------|--------|--------------|
| Alice Smith | `alicesmith`    | `@alice`         | Win11+WSL2  | yes    | yes          |
| Bob Jones   | `bobjones42`    | `@bob`           | macOS 14    | yes    | yes          |

**GitHub username** — validate each one resolves:

```bash
# Replace USERNAME with each student's handle
curl -s https://api.github.com/users/USERNAME \
  | python -c "import sys,json; d=json.load(sys.stdin); \
    print('OK:', d['login']) if 'login' in d \
    else print('NOT FOUND')"
```

**Discord username** — new-format handles are `@username` (no
discriminator). Old-format: `username#1234`. Confirm each student
has a Discord account before inviting (Section 2).

**Laptop OS** — accept only `Win11+WSL2` or `macOS 13+`. Students
on older OS versions must upgrade before the lab.

**Admin/sudo** — required for tool installation (Section 4).
Students without admin access cannot complete the exercises.

**Server account** — required for Phase 6 Docker deployment.
Provision in Section 3; mark this column `yes` after that step.
