def divide(a, b):
  """Divide a by b."""
  if b == 0:
    raise ValueError("Cannot divide by zero")
  return a / b

def get_user(users, id):
  """Get a user by ID."""
  return users.get(id)

def main():
  print(divide(10, 2))
  users = {1: "Alice", 2: "Bob"}
  print(get_user(users, 3))

if __name__ == "__main__":
  main()
