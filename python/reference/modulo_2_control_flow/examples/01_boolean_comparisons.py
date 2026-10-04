"""
EXAMPLE 1: Boolean Values and Comparisons
Learn how to work with True/False values
"""

# Boolean variables
is_sunny = True
is_raining = False

print("Is it sunny?", is_sunny)
print("Is it raining?", is_raining)
print()

# Comparison operators
a = 10
b = 5

print("a =", a)
print("b =", b)
print()

print("a > b:", a > b)    # Greater than
print("a < b:", a < b)    # Less than
print("a >= b:", a >= b)  # Greater or equal
print("a <= b:", a <= b)  # Less or equal
print("a == b:", a == b)  # Equal to
print("a != b:", a != b)  # Not equal
print()

# Common mistake: using = instead of ==
age = 18  # This ASSIGNS the value 18
print("Can vote?", age >= 18)  # This COMPARES age with 18
