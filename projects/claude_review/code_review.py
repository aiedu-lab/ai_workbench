def divide(a, b):
  """Divide a by b."""
  return a / b

def get_user(users, id):
  """Get a user by ID."""
  return users[id]

def main():
  print(divide(10, 0))
  users = {1: "Alice", 2: "Bob"}
  print(get_user(users, 3))

if __name__ == "__main__":
  main()