"""
EXAMPLE 5: Type Conversion
How to convert data from one type to another
"""

print("=== TYPE CONVERSION ===\n")

# Example 1: From string to integer
age_str = "25"
print(f"age_str = '{age_str}' (type: {type(age_str)})")

age_int = int(age_str)
print(f"age_int = {age_int} (type: {type(age_int)})")

# Now we can do mathematical operations
next_year = age_int + 1
print(f"Next year: {next_year}\n")

# Example 2: From string to float
height_str = "1.75"
height_float = float(height_str)
print(f"Height: {height_float} meters (type: {type(height_float)})\n")

# Example 3: From number to string
number = 42
number_str = str(number)
print(f"Number: {number} (type: {type(number)})")
print(f"As string: '{number_str}' (type: {type(number_str)})\n")

# Practical example: Input with conversion
print("--- Practical Example ---")
age = input("How old are you? ")
print(f"Input received: '{age}' (type: {type(age)})")

age = int(age)  # Conversion needed!
print(f"After conversion: {age} (type: {type(age)})")

future_age = age + 5
print(f"In 5 years you'll be {future_age} years old")
