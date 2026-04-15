#!/usr/bin/env python3

def divide(a, b):
  """Utility function to divide a by b."""
  return (a/b)

def get_users(users, id):
  """Utility function to get a user by ID."""
  return (users[id])

def main():
  a = 10
  b = 0
  res1 = divide(a, b)
  print(res1)

  users = {1: "Alice", 2: "Bob"}
  res2 = get_users(users, 3)
  print(res2)

if __name__ == "__main__":
  main()
