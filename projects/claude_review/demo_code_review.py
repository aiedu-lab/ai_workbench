#!/usr/bin/env python3

import math

def divide(a: int | float, b: int | float) -> float:
  """
  Divide a by b.
  Raise ValueError for invalid inputs.
  """
  if isinstance(a, bool) or 
    not isinstance(a, (int, float)) or 
    not math.isfinite(a):
    raise ValueError(f"Dividend must be a number: {a!r}")
  if isinstance(b, bool) or
    not isinstance(b, (int, float)) or
    not math.isfinite(b) or
    b == 0:
    raise ValueError(f"Divisor must be a non-zero number: {b!r}")
  return a / b

def get_user(users: dict[int, str], user_id: int) -> str:
  """
  Get a user by ID. 
  raises ValueError if
   - users is not a dict
   - user_id is a boolean OR not an int 
   - user_id as Key is not found in dict.
  """
  if not isinstance(users, dict):
    raise ValueError(f"Invalid users map: {users!r}")
  if isinstance(user_id, bool) or not isinstance(user_id, int):
    raise ValueError(f"Invalid user id: {user_id!r}")
  if user_id not in users:
    raise ValueError(f"User ID not in dictionary: {user_id} not found")
  return users[user_id]

def main():
  """Run demo calls for divide() and get_user()."""
  print(divide(10, 2))
  users = {1: "Alice", 2: "Bob"}
  print(get_user(users, 2))

if __name__ == "__main__":
  main()

