"""
Example 01: List Basics

This file demonstrates the fundamental operations with lists in Python.
Lists are ordered, changeable collections that can contain any type of data.
"""

# Creating lists
print("=== Creating Lists ===")
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty = []

print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Mixed types: {mixed}")
print(f"Empty list: {empty}")
print()

# List length
print("=== List Length ===")
print(f"Number of fruits: {len(fruits)}")
print(f"Number of numbers: {len(numbers)}")
print()

# Accessing items by index
print("=== Accessing Items ===")
print(f"First fruit: {fruits[0]}")
print(f"Second fruit: {fruits[1]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Second to last: {fruits[-2]}")
print()

# Slicing (getting ranges)
print("=== Slicing ===")
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Full list: {numbers}")
print(f"First 3: {numbers[:3]}")
print(f"Last 3: {numbers[-3:]}")
print(f"Middle (index 3-6): {numbers[3:7]}")
print(f"Every other: {numbers[::2]}")
print(f"Reversed: {numbers[::-1]}")
print()

# Checking if item exists
print("=== Membership Testing ===")
if "apple" in fruits:
    print("We have apples!")
if "orange" not in fruits:
    print("No oranges in stock")
