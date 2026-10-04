"""
EXAMPLE 5: if-elif-else Statement
Checking multiple conditions
"""

print("=== Grade Calculator ===")
score = int(input("Enter your score (0-100): "))

if score >= 90:
    grade = "A"
    message = "Excellent!"
elif score >= 80:
    grade = "B"
    message = "Good job!"
elif score >= 70:
    grade = "C"
    message = "Average"
elif score >= 60:
    grade = "D"
    message = "You passed"
else:
    grade = "F"
    message = "You failed"

print(f"Your grade: {grade} - {message}")
print()

# Traffic light example
print("=== Traffic Light ===")
light = input("What color is the light? (red/yellow/green): ").lower()

if light == "red":
    print("STOP!")
elif light == "yellow":
    print("Slow down")
elif light == "green":
    print("Go")
else:
    print("Invalid color")

print()

# Age categories
print("=== Age Category ===")
age = int(input("Enter age: "))

if age < 13:
    print("You are a child")
elif age < 20:
    print("You are a teenager")
elif age < 65:
    print("You are an adult")
else:
    print("You are a senior")
