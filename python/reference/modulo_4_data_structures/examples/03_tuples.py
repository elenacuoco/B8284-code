"""
Example 03: Tuples

Demonstrates tuples - immutable sequences that cannot be changed after creation.
"""

print("=== Creating Tuples ===")
coordinates = (10, 20)
person = ("Alice", 25, "Engineer")
single_item = (42,)  # Note the comma!
empty = ()

print(f"Coordinates: {coordinates}")
print(f"Person: {person}")
print(f"Single item: {single_item}")
print(f"Empty tuple: {empty}")
print()

print("=== Accessing Tuple Items ===")
print(f"X coordinate: {coordinates[0]}")
print(f"Y coordinate: {coordinates[1]}")
print(f"Person name: {person[0]}")
print(f"Person age: {person[1]}")
print()

print("=== Tuple Unpacking ===")
x, y = coordinates
print(f"x = {x}, y = {y}")

name, age, job = person
print(f"Name: {name}, Age: {age}, Job: {job}")

# Swapping variables (elegant with tuples!)
a, b = 5, 10
print(f"Before swap: a={a}, b={b}")
a, b = b, a
print(f"After swap: a={a}, b={b}")
print()

print("=== Why Tuples Are Immutable ===")
try:
    coordinates[0] = 15
except TypeError as e:
    print(f"Error: {e}")
print("Tuples protect your data from accidental changes!")
print()

print("=== Tuple Methods ===")
numbers = (1, 2, 3, 2, 4, 2, 5)
print(f"Tuple: {numbers}")
print(f"Count of 2: {numbers.count(2)}")
print(f"Index of 3: {numbers.index(3)}")
print(f"Length: {len(numbers)}")
print()

print("=== Common Use Cases ===")
# RGB color
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
print(f"Colors - Red: {RED}, Green: {GREEN}, Blue: {BLUE}")

# Function returning multiple values
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([3, 1, 4, 1, 5, 9, 2, 6])
print(f"Min: {minimum}, Max: {maximum}")
