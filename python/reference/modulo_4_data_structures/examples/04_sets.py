"""
Example 04: Sets

Demonstrates sets - unordered collections of unique items.
"""

print("=== Creating Sets ===")
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
empty = set()  # Note: {} creates an empty dict, not set!

print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Empty set: {empty}")
print()

print("=== Automatic Duplicate Removal ===")
numbers_with_dupes = {1, 2, 2, 3, 3, 3, 4, 5, 5}
print(f"Set with duplicates: {numbers_with_dupes}")

# Convert list to set (removes duplicates)
my_list = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique = set(my_list)
print(f"List: {my_list}")
print(f"Unique values: {unique}")
print()

print("=== Adding and Removing Items ===")
fruits = {"apple", "banana"}
print(f"Start: {fruits}")

fruits.add("cherry")
print(f"After add: {fruits}")

fruits.remove("banana")  # Error if not found
print(f"After remove: {fruits}")

fruits.discard("orange")  # No error if not found
print(f"After discard (non-existent): {fruits}")
print()

print("=== Set Operations ===")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union (|): {set1 | set2}")
print(f"Intersection (&): {set1 & set2}")
print(f"Difference (-): {set1 - set2}")
print(f"Symmetric difference (^): {set1 ^ set2}")
print()

print("=== Fast Membership Testing ===")
# Sets are MUCH faster for checking if item exists
large_set = set(range(1000000))
print(f"999999 in large_set: {999999 in large_set}")
print("(This check is almost instant with sets!)")
print()

print("=== Practical Example: Common Friends ===")
alice_friends = {"Bob", "Charlie", "David", "Eve"}
bob_friends = {"Alice", "Charlie", "Frank", "David"}

common_friends = alice_friends & bob_friends
print(f"Alice's friends: {alice_friends}")
print(f"Bob's friends: {bob_friends}")
print(f"Common friends: {common_friends}")

all_friends = alice_friends | bob_friends
print(f"All friends: {all_friends}")
