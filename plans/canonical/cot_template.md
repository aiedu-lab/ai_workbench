# CoT Templatew

# Decision Prompt

```bash
Context:
[your situation]

Task:
[your question]

Reasoning:
Think step by step. List each assumption and inference explicitly.

Constraints:
[your constraints]

Output:
Numbered reasoning steps → Final answer
```

# Risk Evaluator

```bash
# Skill: Risk Evaluator

Context:
You are evaluating a decision for potential risks.

Task:
Evaluate [DECISION].

Reasoning:
Step 1 — Identify what could go wrong
Step 2 — Estimate likelihood (Low / Med / High)
Step 3 — Estimate impact (Low / Med / High)
Step 4 — Suggest mitigations for High x High items

Output:
Risk table + top 3 mitigations
```

Reuse this skill for code review, plan review, investment decisions,
and project proposals.

