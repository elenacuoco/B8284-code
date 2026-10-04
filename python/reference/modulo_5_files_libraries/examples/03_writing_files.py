"""
Example 03: Writing to Files

Demonstrates different ways to write data to files.
"""

print("=== Write Mode ('w') - Creates New or Overwrites ===")
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is line 2\n")
    file.write("This is line 3\n")

with open("output.txt", "r") as file:
    print(file.read())

print("=== Append Mode ('a') - Adds to End ===")
with open("output.txt", "a") as file:
    file.write("This line was appended\n")
    file.write("So was this one\n")

with open("output.txt", "r") as file:
    print(file.read())

print("=== Warning: 'w' Mode Overwrites! ===")
with open("output.txt", "w") as file:
    file.write("All previous content was deleted!\n")

with open("output.txt", "r") as file:
    print(file.read())

print("=== Writing Multiple Lines at Once ===")
lines = [
    "First line\n",
    "Second line\n",
    "Third line\n"
]

with open("output.txt", "w") as file:
    file.writelines(lines)

with open("output.txt", "r") as file:
    print(file.read())

print("=== Writing from a List ===")
fruits = ["apple", "banana", "cherry", "date"]

with open("fruits.txt", "w") as file:
    for fruit in fruits:
        file.write(f"{fruit}\n")

print("Contents of fruits.txt:")
with open("fruits.txt", "r") as file:
    print(file.read())

print("=== Important Notes ===")
print("1. 'w' mode creates file if it doesn't exist")
print("2. 'w' mode DELETES existing content")
print("3. Use 'a' mode to add without deleting")
print("4. Don't forget \\n for newlines!")
