"""
Example 08: List Comprehensions

Demonstrates list comprehensions - a concise way to create lists.
"""

print("=== Basic List Comprehension ===")
# Traditional way
squares = []
for i in range(10):
    squares.append(i ** 2)
print(f"Squares (traditional): {squares}")

# List comprehension way
squares = [i ** 2 for i in range(10)]
print(f"Squares (comprehension): {squares}")
print()

print("=== With Condition ===")
# Only even numbers
evens = [i for i in range(20) if i % 2 == 0]
print(f"Even numbers: {evens}")

# Only positive numbers
numbers = [-2, -1, 0, 1, 2, 3, 4]
positives = [n for n in numbers if n > 0]
print(f"Positive numbers: {positives}")
print()

print("=== String Operations ===")
# Convert to uppercase
words = ["hello", "world", "python"]
uppercase = [word.upper() for word in words]
print(f"Original: {words}")
print(f"Uppercase: {uppercase}")

# Get lengths
lengths = [len(word) for word in words]
print(f"Lengths: {lengths}")
print()

print("=== Nested List Comprehension ===")
# Create a matrix
matrix = [[i * j for j in range(5)] for i in range(5)]
print("Multiplication table:")
for row in matrix:
    print(row)
print()

print("=== Dictionary Comprehension ===")
# Create dictionary from lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
my_dict = {k: v for k, v in zip(keys, values)}
print(f"Dictionary: {my_dict}")

# Square dictionary
squares_dict = {i: i**2 for i in range(6)}
print(f"Squares dict: {squares_dict}")
print()

print("=== Set Comprehension ===")
# Unique squared values
numbers = [1, 2, 2, 3, 3, 4, 5]
unique_squares = {n**2 for n in numbers}
print(f"Unique squares: {unique_squares}")
