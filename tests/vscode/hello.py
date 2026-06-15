#! /usr/bin/env python3

import getpass
import sys

def get_os_username() -> str:
  # Most reliable across environments (WSL, containers, SSH)
  return getpass.getuser()

def get_github_username() -> str:
  return "adisa"

def main() -> None:
  github_username = get_github_username()
  print(f"hello, {github_username}!")

if __name__ == "__main__":
  sys.exit(main())
