import math

def divide(a: int | float, b: int | float) -> float:
  """
  Divide a by b; raises ValueError if b is zero OR
  if not a finite float number (e.g., NaN or infinity).
  """
  # Note b == 0 check fails
  # if b = float('nan') or float('inf')
  # So we also check if b is not a number or not finite
  if b == 0 or (isinstance(b, float) and not math.isfinite(b)):
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

