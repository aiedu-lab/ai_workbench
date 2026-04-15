import math

def divide(a: int | float, b: int | float) -> float:
  """
  Divide a by b
  raises ValueError if a or b is not a finite number OR
  if b is zero.
  """
  if (
    not isinstance(a, float) and not isinstance(a, int)) or
    not math.isfinite(a)
  ):
    raise ValueError(f"Invalid dividend: {a!r}")
  if (
    not isinstance(b, float) and not isinstance(b, int)) or
    not math.isfinite(b) or
    b == 0
  ):
    raise ValueError(f"Invalid divisor: {b!r}")
  return a / b

def get_user(users: dict[int, str], user_id: int) -> str:
  """Get a user by ID. ValueError if user_id not found."""
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

