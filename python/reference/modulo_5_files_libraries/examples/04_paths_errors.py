"""
Example 04: File Paths and Error Handling

Demonstrates working with file paths and handling file errors.
"""

import os

print("=== Current Working Directory ===")
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")
print()

print("=== Relative vs Absolute Paths ===")
# Relative path (from current directory)
print("Relative path: 'data.txt'")
print("  Looks in current directory")

# Absolute path
print(f"Absolute path: '{current_dir}\\data.txt'")
print("  Full path from root")
print()

print("=== Handling FileNotFoundError ===")
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("❌ Error: File 'nonexistent.txt' not found!")
    print("   Creating it now...")
    with open("nonexistent.txt", "w") as file:
        file.write("This file was just created!\n")
    print("✓ File created successfully")
print()

print("=== Handling PermissionError ===")
# Create a file
with open("test.txt", "w") as file:
    file.write("Test content\n")

try:
    # Try to open with proper permissions
    with open("test.txt", "r") as file:
        content = file.read()
        print("✓ File read successfully")
except PermissionError:
    print("❌ Error: No permission to access file")
print()

print("=== Checking if File Exists ===")
filename = "test.txt"
if os.path.exists(filename):
    print(f"✓ File '{filename}' exists")
    print(f"  Size: {os.path.getsize(filename)} bytes")
else:
    print(f"❌ File '{filename}' does not exist")
print()

print("=== Safe File Reading Function ===")
def safe_read_file(filename):
    """Safely read a file with error handling."""
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except PermissionError:
        return f"Error: No permission to read '{filename}'"
    except Exception as e:
        return f"Error: {e}"

# Test the function
print(safe_read_file("test.txt"))
print(safe_read_file("missing.txt"))
print()

print("=== Cleanup ===")
# Remove test files
for file in ["test.txt", "nonexistent.txt"]:
    if os.path.exists(file):
        os.remove(file)
        print(f"Removed: {file}")
