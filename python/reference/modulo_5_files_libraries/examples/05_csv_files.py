"""
Example 05: Working with CSV Files

Demonstrates reading and writing CSV (Comma-Separated Values) files.
"""

import csv

print("=== Creating a CSV File ===")
students = [
    ["name", "age", "grade"],
    ["Alice", "20", "95"],
    ["Bob", "21", "88"],
    ["Charlie", "20", "92"],
    ["Diana", "22", "97"]
]

with open("students.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(students)

print("✓ Created students.csv")
print()

print("=== Reading CSV with csv.reader ===")
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)  # Get first row (header)
    print(f"Header: {header}")
    print("\nStudents:")
    for row in reader:
        name, age, grade = row
        print(f"  {name}: {age} years old, grade {grade}")
print()

print("=== Reading CSV as Dictionaries (Better!) ===")
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    print("Students:")
    for row in reader:
        print(f"  {row['name']}: grade {row['grade']}")
print()

print("=== Writing CSV from Dictionaries ===")
students_dict = [
    {"name": "Eve", "age": 23, "grade": 89},
    {"name": "Frank", "age": 21, "grade": 94},
    {"name": "Grace", "age": 22, "grade": 91}
]

with open("students2.csv", "w", newline='') as file:
    fieldnames = ["name", "age", "grade"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(students_dict)

print("✓ Created students2.csv")
print()

print("=== Processing CSV Data ===")
total_grade = 0
count = 0

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        total_grade += int(row["grade"])
        count += 1

average = total_grade / count
print(f"Class average: {average:.1f}")
print()

print("=== Filtering CSV Data ===")
print("Students with grade >= 90:")
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if int(row["grade"]) >= 90:
            print(f"  {row['name']}: {row['grade']}")
print()

print("=== CSV with Different Delimiter ===")
# Sometimes CSV uses semicolons or tabs
data = [
    ["Product", "Price", "Quantity"],
    ["Apple", "0.50", "100"],
    ["Banana", "0.30", "150"]
]

with open("products.csv", "w", newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(data)

print("✓ Created products.csv with semicolon delimiter")

with open("products.csv", "r") as file:
    reader = csv.reader(file, delimiter=';')
    for row in reader:
        print(row)
