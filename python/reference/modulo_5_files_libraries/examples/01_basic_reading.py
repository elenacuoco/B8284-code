"""
Example 01: Basic File Reading

This file demonstrates different ways to read text files in Python.
"""

# First, let's create a sample file to work with
sample_content = """Hello, World!
This is line 2.
This is line 3.
Python is awesome!"""

with open("sample.txt", "w") as file:
    file.write(sample_content)

print("=== Method 1: read() - Entire File as String ===")
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()
print()

print("=== Method 2: readline() - One Line at a Time ===")
file = open("sample.txt", "r")
line1 = file.readline()
line2 = file.readline()
print(f"Line 1: {line1.strip()}")
print(f"Line 2: {line2.strip()}")
file.close()
print()

print("=== Method 3: readlines() - List of Lines ===")
file = open("sample.txt", "r")
lines = file.readlines()
file.close()

print(f"Type: {type(lines)}")
print(f"Number of lines: {len(lines)}")
for i, line in enumerate(lines, 1):
    print(f"  Line {i}: {line.strip()}")
print()

print("=== Method 4: Iterate Over File Object ===")
file = open("sample.txt", "r")
for line in file:
    print(f"  {line.strip()}")
file.close()
print()

print("=== Important: Always Close Files! ===")
print("If you don't close files, they may lock or cause issues.")
print("Better solution: Use 'with' statement (next example)")
