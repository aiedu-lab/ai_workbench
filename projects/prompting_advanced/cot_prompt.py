import anthropic

def cot_prompt(situation: str, question: str, constraints: str, output: str) -> str:
    return f"""Context:
{situation}

Task:
{question}

Reasoning:
Think step by step. List each assumption and inference explicitly.

Constraints:
{constraints}

Output:
Numbered reasoning steps → Final answer
{output}
"""


# Reuse with different data
scenarios = [
  {
    "situation": "I am a high school student with $500 saved.",
    "question": "Should I buy a used gaming laptop or invest the $500?",
    "constraints": "Consider: immediate utility, long-term value, opportunity cost, liquidity.",
    "output": "Prioritized ordered list of choice. Each explained in 3 lines or less with: price, reasons, description."
  },
  {
    "situation": "I have a science project due in 3 days and haven't started.",
    "question": "Should I work alone or ask a classmate to help?",
    "constraints": "Consider: time available, quality of output, fairness, learning value.",
    "output": "Choice: 'Work alone' or 'Ask a classmate to help'. Each explained in 3 lines or less with: reasons, description." 
  },
]

client = anthropic.Anthropic()

for s in scenarios:
    prompt = cot_prompt(s["situation"], s["question"], s["constraints"], s["output"])
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    print(response.content[0].text)
    print("---")