#! /usr/bin/env python3

import getpass
import sys

def get_os_username() -> str:
  # Most reliable across environments (WSL, containers, SSH)
  return getpass.getuser()

def get_github_username() -> str:
  return NotImplementedError

def main() -> None:
  os_user_name = get_os_username()
  print(f"Hello {os_user_name}")

if __name__ == "__main__":
  sys.exit(main())
