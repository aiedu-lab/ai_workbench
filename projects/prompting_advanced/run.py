import json
import anthropic

# Load template and data separately
template = open("template.txt").read()
data     = json.load(open("data.json"))

# Substitute — replace every {{KEY}} with its value
prompt = template
for key, value in data.items():
  prompt = prompt.replace(f"{{{{{key.upper()}}}}}", value)

# Call Claude
client = anthropic.Anthropic()
response = client.messages.create(
  model="claude-sonnet-4-6",
  max_tokens=1024,
  messages=[{"role": "user", "content": prompt}]
)
print(response.content[0].text)