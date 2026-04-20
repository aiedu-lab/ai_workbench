import json
import yaml
from collections import Counter

cfg = yaml.safe_load(open("config.yaml"))
date = cfg["options"]["dates"][0]
responses = json.load(open("responses.json"))

available = {
  name: data
  for name, data in responses.items()
  if data["available"]
}

if not available:
  decision = {"cancelled": True}
else:
  venue_votes = [data["venue"] for data in available.values()]
  counts = Counter(venue_votes)
  top = max(counts.values())
  # alphabetical tie-breaking for determinism
  venue = sorted(v for v, c in counts.items() if c == top)[0]
  decision = {
    "date": date,
    "venue": venue,
    "attendees": sorted(available.keys()),
  }

with open("decision.json", "w") as f:
  json.dump(decision, f, indent=2)
print("decision.json written:", decision)
