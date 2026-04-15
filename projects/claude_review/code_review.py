def divide(a: int | float, b: int | float) -> float:
  """Divide a by b."""
  if b == 0:
    raise ValueError("Cannot divide by zero")
  return a / b

def get_user(users: dict[int, str], user_id: int) -> str:
  """Get a user by ID."""
  if user_id not in users:
    raise ValueError(f"User ID {user_id} not found"
  return users[user_id]

def main():
  print(divide(10, 2))
  users = {1: "Alice", 2: "Bob"}
  print(get_user(users, 2))

if __name__ == "__main__":
  main()

