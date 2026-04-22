import json
import os

import requests

decision = json.load(open("decision.json"))
if decision.get("cancelled"):
  msg = "❌ **Meetup cancelled** — not enough members available."
else:
  attendees = ", ".join(decision["attendees"])
  msg = (
    f"📅 **Meetup confirmed!**\n"
    f"**Date:** {decision['date']}\n"
    f"**Venue:** {decision['venue']}\n"
    f"**Attending:** {attendees}"
  )

requests.post(
  os.environ["DISCORD_WEBHOOK_URL"],
  json={"content": msg},
)
print("Notification sent.")
