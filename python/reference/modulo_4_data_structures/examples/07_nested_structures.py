"""
Example 07: Nested Structures

Demonstrates combining different data structures for complex data.
"""

print("=== List of Dictionaries ===")
# Very common pattern: list of records
students = [
    {"name": "Alice", "age": 20, "grade": 95},
    {"name": "Bob", "age": 21, "grade": 88},
    {"name": "Charlie", "age": 20, "grade": 92}
]

print("Students:")
for student in students:
    print(f"  {student['name']}: {student['grade']}%")
print()

# Calculate average grade
total = sum(student["grade"] for student in students)
average = total / len(students)
print(f"Class average: {average:.1f}%")
print()

print("=== Dictionary with Lists ===")
# Another common pattern
contact_book = {
    "Alice": {
        "phone": "555-1234",
        "email": "alice@email.com",
        "hobbies": ["reading", "hiking"]
    },
    "Bob": {
        "phone": "555-5678",
        "email": "bob@email.com",
        "hobbies": ["gaming", "coding"]
    }
}

print("Contact Book:")
for name, info in contact_book.items():
    print(f"\n{name}:")
    print(f"  Phone: {info['phone']}")
    print(f"  Email: {info['email']}")
    print(f"  Hobbies: {', '.join(info['hobbies'])}")
print()

print("=== Complex Nested Structure ===")
# Real-world example: company data
company = {
    "name": "Tech Corp",
    "employees": [
        {
            "name": "Alice",
            "position": "Engineer",
            "skills": ["Python", "JavaScript"],
            "projects": [
                {"name": "Project A", "status": "completed"},
                {"name": "Project B", "status": "in progress"}
            ]
        },
        {
            "name": "Bob",
            "position": "Designer",
            "skills": ["Photoshop", "Figma"],
            "projects": [
                {"name": "Project C", "status": "completed"}
            ]
        }
    ]
}

print(f"Company: {company['name']}")
print("\nEmployees:")
for emp in company["employees"]:
    print(f"\n  {emp['name']} - {emp['position']}")
    print(f"    Skills: {', '.join(emp['skills'])}")
    print(f"    Projects:")
    for project in emp["projects"]:
        print(f"      - {project['name']} ({project['status']})")
