"""
Example 05: Dictionary Basics

Demonstrates dictionaries - collections of key-value pairs.
"""

print("=== Creating Dictionaries ===")
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "job": "Engineer"
}

print(f"Person: {person}")
print()

print("=== Accessing Values ===")
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")

# Using get() - safer, doesn't error if key missing
print(f"City: {person.get('city')}")
print(f"Email (with default): {person.get('email', 'N/A')}")
print()

print("=== Adding and Updating ===")
person["email"] = "alice@email.com"
print(f"Added email: {person}")

person["age"] = 26
print(f"Updated age: {person}")
print()

print("=== Removing Items ===")
del person["job"]
print(f"After deleting job: {person}")

city = person.pop("city")
print(f"Popped city: {city}")
print(f"After pop: {person}")
print()

print("=== Checking if Key Exists ===")
if "name" in person:
    print(f"Name is {person['name']}")

if "phone" not in person:
    print("Phone number not found")
print()

print("=== Different Key Types ===")
# Keys can be strings, numbers, tuples
scores = {
    "math": 95,
    "english": 88,
    "science": 92
}

coordinates = {
    (0, 0): "origin",
    (1, 0): "right",
    (0, 1): "up"
}

print(f"Scores: {scores}")
print(f"Coordinates: {coordinates}")
print(f"Point (1,0): {coordinates[(1, 0)]}")
