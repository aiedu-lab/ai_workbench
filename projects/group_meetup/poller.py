import json
import yaml

cfg = yaml.safe_load(open("config.yaml"))
date = cfg["options"]["dates"][0]
venues = cfg["options"]["venues"]
responses = {}

print(f"\nPolling: {cfg['group']} — {date}\n")
for member in cfg["members"]:
  name = member["name"]
  ans = input(f"  {name} — available? (y/n): ").strip().lower()
  available = ans == "y"
  venue = None
  if available:
    print("    Venue options:")
    for i, v in enumerate(venues, 1):
      print(f"      {i}. {v}")
    raw = input(
      f"    {name} — preference (1-{len(venues)}): "
    ).strip()
    try:
      venue = venues[int(raw) - 1]
    except (ValueError, IndexError):
      venue = venues[0]
  responses[name] = {"available": available, "venue": venue}

with open("responses.json", "w") as f:
  json.dump(responses, f, indent=2)
print("\nresponses.json written.")
