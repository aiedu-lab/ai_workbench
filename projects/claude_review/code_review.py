#!/usr/bin/env python3

import math

def divide(a: int | float, b: int | float) -> float:
  """
  Divide a by b
  raises ValueError if 
  - a or b is a boolean (since bool is a subclass of int in Python)
  - a or b is not a finite int/float number 
  - b is zero.
  """
  if (
    isinstance(a, bool) or
    (not isinstance(a, float) and not isinstance(a, int)) or
    not math.isfinite(a)
  ):
    raise ValueError(f"Invalid dividend: {a!r}")
  if (
    (not isinstance(b, float) and not isinstance(b, int)) or
    not math.isfinite(b) or
    b == 0
  ):
    raise ValueError(f"Invalid divisor: {b!r}")
  return a / b

def get_user(users: dict[int, str], user_id: int) -> str:
  """
  Get a user by ID. 
  raises ValueError if
   - users is not a dict
   - user_id is not an int 
   - user_id as Key is not found in dict.
  """
  if not isinstance(users, dict):
    raise ValueError(f"Invalid users map: {users!r}")
  if not isinstance(user_id, int):
    raise ValueError(f"Invalid user id: {user_id!r}")
  if user_id not in users:
    raise ValueError(f"User ID {user_id} not found")
  return users[user_id]

def main():
  """Run demo calls for divide() and get_user()."""
  print(divide(10, 2))
  users = {1: "Alice", 2: "Bob"}
  print(get_user(users, 2))

if __name__ == "__main__":
  main()

