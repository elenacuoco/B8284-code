"""
Example 02: List Methods

Demonstrates all the common methods for modifying and working with lists.
"""

print("=== Adding Items ===")
fruits = ["apple", "banana"]
print(f"Start: {fruits}")

fruits.append("cherry")
print(f"After append: {fruits}")

fruits.insert(1, "orange")
print(f"After insert at index 1: {fruits}")

fruits.extend(["date", "elderberry"])
print(f"After extend: {fruits}")
print()

print("=== Removing Items ===")
fruits = ["apple", "banana", "cherry", "date", "banana"]
print(f"Start: {fruits}")

fruits.remove("banana")  # Removes first occurrence
print(f"After remove 'banana': {fruits}")

popped = fruits.pop()  # Remove and return last item
print(f"Popped: {popped}")
print(f"After pop: {fruits}")

popped = fruits.pop(1)  # Remove and return by index
print(f"Popped index 1: {popped}")
print(f"After pop(1): {fruits}")
print()

print("=== Sorting and Reversing ===")
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {numbers}")

numbers.sort()
print(f"After sort: {numbers}")

numbers.reverse()
print(f"After reverse: {numbers}")

# Sort without modifying original
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_copy = sorted(numbers)
print(f"Original unchanged: {numbers}")
print(f"Sorted copy: {sorted_copy}")
print()

print("=== Other Useful Methods ===")
numbers = [1, 2, 3, 2, 4, 2, 5]
print(f"List: {numbers}")
print(f"Count of 2: {numbers.count(2)}")
print(f"Index of 3: {numbers.index(3)}")

# Clear all items
numbers_copy = numbers.copy()
numbers_copy.clear()
print(f"After clear: {numbers_copy}")
