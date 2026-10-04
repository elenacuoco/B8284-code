"""
Example 02: The 'with' Statement (Context Manager)

Demonstrates the proper way to handle files using 'with'.
This automatically closes files, even if errors occur.
"""

# Create a sample file
with open("sample.txt", "w") as file:
    file.write("Line 1\nLine 2\nLine 3\n")

print("=== Using 'with' - Automatic File Closing ===")
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)
# File is automatically closed here!

print("File closed:", file.closed)  # True
print()

print("=== Reading Line by Line with 'with' ===")
with open("sample.txt", "r") as file:
    for i, line in enumerate(file, 1):
        print(f"Line {i}: {line.strip()}")
print()

print("=== Reading All Lines into List ===")
with open("sample.txt", "r") as file:
    lines = file.readlines()

print(f"Total lines: {len(lines)}")
print(f"Lines list: {lines}")
print()

print("=== Why 'with' is Better ===")
print("Benefits:")
print("  1. Automatic closing (no need to call file.close())")
print("  2. Cleaner code")
print("  3. Safe - closes even if error occurs")
print("  4. Best practice in Python")
print()

# Example: with handles errors gracefully
print("=== Error Handling with 'with' ===")
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found, but 'with' handled cleanup properly!")
