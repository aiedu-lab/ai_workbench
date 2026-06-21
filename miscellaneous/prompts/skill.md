# Skill

# File Organizer Skill

```text
You are a helpful assistant.
Context: I want to organize a given folder.
Task: Propose a safe and reversible plan.
Constraints:
- Do not delete files
- Do not change original files
- Group by file type
- Ask before execution

Output: Step-by-step checklist
```

---

# Professional Rewrite Skill

```bash
Context:
This is a professional email to a [RECIPIENT].

Task:
Rewrite the message below to sound professional and polite.

Message:
[MESSAGE]

Constraints:
* Polite tone
* Clear ask
* No slang
* Max 2 sentences

Output:
Formal email only - no explations or reasoning.
```

---

# Data Pipeline Clean & Transform Skill

```text
Context:
I have a CSV file at [INPUT_CSV] with stock price data.
Columns: date, symbol, open, high, low, close, volume

Task:
Clean and transform the data:
1. Remove rows where open, close, or volume is missing.
2. Add column daily_change = close - open.
3. Add column pct_change = round((close-open)/open*100, 2).
4. Save the result as [OUTPUT_CSV].

Validation (run first against sample data):
  python3 -c "
  import pandas as pd
  df = pd.read_csv('tests/data/pipeline/sample.csv')
  assert df.shape[1] == 7, 'Expected 7 columns'
  print('Sample OK:', df.shape)
  "

Constraints:
- Do not modify the original input file.
- Print: "Cleaned N rows. Saved to [OUTPUT_CSV]."
- If a required column is missing, stop and report the error.

Output:
Cleaned CSV saved to [OUTPUT_CSV] plus a one-line summary.
```
