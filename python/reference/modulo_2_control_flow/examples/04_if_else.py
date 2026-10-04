"""
EXAMPLE 4: if-else Statement
Choosing between two options
"""

print("=== Age Check ===")
age = int(input("Enter your age: "))

if age >= 18:
    print("You can enter the club")
else:
    print("Sorry, adults only (18+)")

print()

# Even or Odd number
print("=== Even or Odd ===")
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is EVEN")
else:
    print(f"{number} is ODD")

print()

# Positive or Negative
print("=== Positive or Negative ===")
num = int(input("Enter a number: "))

if num >= 0:
    print(f"{num} is positive (or zero)")
else:
    print(f"{num} is negative")
