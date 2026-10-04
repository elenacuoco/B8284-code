"""
Example 06: Working with JSON Files

Demonstrates reading and writing JSON (JavaScript Object Notation) files.
JSON is a universal data format used in web APIs and configuration files.
"""

import json

print("=== Writing JSON ===")
# Python dictionary to JSON file
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "skills": ["Python", "JavaScript", "SQL"],
    "is_student": False,
    "grades": {
        "math": 95,
        "english": 88,
        "science": 92
    }
}

with open("person.json", "w") as file:
    json.dump(person, file, indent=2)

print("✓ Created person.json")
print()

print("=== Reading JSON ===")
with open("person.json", "r") as file:
    loaded_person = json.load(file)

print(f"Name: {loaded_person['name']}")
print(f"Age: {loaded_person['age']}")
print(f"Skills: {', '.join(loaded_person['skills'])}")
print(f"Math grade: {loaded_person['grades']['math']}")
print()

print("=== JSON vs Python Types ===")
print("JSON            Python")
print("object    →     dict")
print("array     →     list")
print("string    →     str")
print("number    →     int/float")
print("true      →     True")
print("false     →     False")
print("null      →     None")
print()

print("=== Writing List of Dictionaries ===")
students = [
    {"name": "Alice", "grade": 95},
    {"name": "Bob", "grade": 88},
    {"name": "Charlie", "grade": 92}
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=2)

print("✓ Created students.json")
print()

print("=== Reading and Processing JSON ===")
with open("students.json", "r") as file:
    students = json.load(file)

print("Students:")
for student in students:
    print(f"  {student['name']}: {student['grade']}")

average = sum(s["grade"] for s in students) / len(students)
print(f"\nClass average: {average:.1f}")
print()

print("=== JSON String Conversion ===")
# Convert Python object to JSON string
data = {"name": "Bob", "score": 100}
json_string = json.dumps(data)
print(f"JSON string: {json_string}")
print(f"Type: {type(json_string)}")

# Convert JSON string to Python object
parsed_data = json.loads(json_string)
print(f"Parsed data: {parsed_data}")
print(f"Type: {type(parsed_data)}")
print()

print("=== Pretty Printing JSON ===")
complex_data = {
    "users": [
        {"id": 1, "name": "Alice", "active": True},
        {"id": 2, "name": "Bob", "active": False}
    ],
    "settings": {
        "theme": "dark",
        "notifications": True
    }
}

print("Compact:")
print(json.dumps(complex_data))

print("\nPretty (indented):")
print(json.dumps(complex_data, indent=2))

print("\nSorted keys:")
print(json.dumps(complex_data, indent=2, sort_keys=True))
