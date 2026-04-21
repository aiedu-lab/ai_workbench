#!/usr/bin/env python3
"""Parse labenv.yaml and export non-confidential env vars.

Validates that DISCORD_WEBHOOK_URL is already set out-of-band
(retrieved from #meetup-notifications per instructor.md Section 2).
Exits non-zero with a clear message if the secret is absent.
"""
import os
import sys
import yaml
from pathlib import Path

LABENV = Path(__file__).parent / "labenv.yaml"
SECRET_KEY = "DISCORD_WEBHOOK_URL"


def main() -> None:
  with LABENV.open() as f:
    env = yaml.safe_load(f)

  for key, value in env.items():
    os.environ[key] = str(value)
    print(f"  SET  {key}={value}")

  if os.environ.get(SECRET_KEY):
    print(f"\n  OK   {SECRET_KEY} is set (value hidden)")
    print("\nEnvironment ready.")
    return

  print(
    f"\nERROR: {SECRET_KEY} is not set.\n"
    "Retrieve it from the pinned message in "
    "#meetup-notifications and run:\n"
    f"  export {SECRET_KEY}=<webhook-url>\n"
    "Never add this value to any committed file.",
    file=sys.stderr,
  )
  sys.exit(1)

if __name__ == "__main__":
  main()
