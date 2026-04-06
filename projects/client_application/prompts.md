# Prompts – Client App

---

## 1. Plan Review Prompt

Review `plan.md` and explain the approach step by step.

---

## 2. Scoped Execution Prompt

Review `plan.md`.

Only operate inside this directory.  
Do not access parent folders or external directories.  

Execute **Step 1 only** from the plan.  
Explain what you are doing before running anything.

---

## 3. Failure Analysis Prompt

The previous step failed.

- Explain why it failed  
- Identify incorrect assumptions  
- Propose a fix before retrying  

---

## 4. Constraint Prompt

- Do not read files outside this directory  
- Only use files under `src/`  
- Do not modify unrelated files  

---

## 5. Reflection Prompt

What did you get wrong in previous steps?  
What should be changed in `plan.md`?
