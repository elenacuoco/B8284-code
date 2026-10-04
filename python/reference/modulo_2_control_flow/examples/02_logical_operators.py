"""
EXAMPLE 2: Logical Operators
Combining multiple conditions with and, or, not
"""

# AND operator - both must be True
print("=== AND Operator ===")
age = 25
has_license = True
can_drive = age >= 18 and has_license
print(f"Age: {age}, Has license: {has_license}")
print(f"Can drive? {can_drive}")
print()

# OR operator - at least one must be True
print("=== OR Operator ===")
is_weekend = True
is_holiday = False
can_relax = is_weekend or is_holiday
print(f"Weekend: {is_weekend}, Holiday: {is_holiday}")
print(f"Can relax? {can_relax}")
print()

# NOT operator - reverses the value
print("=== NOT Operator ===")
is_working = False
is_free = not is_working
print(f"Working: {is_working}")
print(f"Free: {is_free}")
print()

# Complex example
print("=== Complex Example ===")
temperature = 28
is_sunny = True
is_raining = False

good_beach_day = temperature > 25 and is_sunny and not is_raining
print(f"Temperature: {temperature}°C")
print(f"Sunny: {is_sunny}")
print(f"Raining: {is_raining}")
print(f"Good beach day? {good_beach_day}")
