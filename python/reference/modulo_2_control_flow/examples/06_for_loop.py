"""
EXAMPLE 6: for Loop
Repeating actions a specific number of times
"""

print("=== Basic for Loop ===")
for i in range(5):
    print(f"Iteration {i}")
print()

# Different range() usage
print("=== range(1, 6) - from 1 to 5 ===")
for i in range(1, 6):
    print(i, end=" ")
print("\n")

print("=== range(0, 10, 2) - even numbers ===")
for i in range(0, 10, 2):
    print(i, end=" ")
print("\n")

# Looping through a list
print("=== Loop Through List ===")
fruits = ["apple", "banana", "cherry", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")
print()

# Practical example: Multiplication table
print("=== Multiplication Table of 5 ===")
for i in range(1, 11):
    result = 5 * i
    print(f"5 x {i} = {result}")
print()

# Countdown
print("=== Countdown ===")
for i in range(10, 0, -1):
    print(i)
print("Blast off! 🚀")
