"""
EXAMPLE 3: Return Values
Getting results back from functions
"""

# Simple return
def add(a, b):
    result = a + b
    return result

print("=== Basic Return ===")
total = add(5, 3)
print(f"5 + 3 = {total}")

# Using return value directly
print(f"10 + 20 = {add(10, 20)}")
print()

# Return in calculations
def multiply(a, b):
    return a * b

def square(n):
    return n * n

print("=== Using Return Values ===")
result1 = multiply(4, 5)
result2 = square(7)
print(f"4 * 5 = {result1}")
print(f"7 squared = {result2}")
print()

# Practical example: Temperature converter
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

print("=== Temperature Converter ===")
temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")

temp_f = 77
temp_c = fahrenheit_to_celsius(temp_f)
print(f"{temp_f}°F = {temp_c:.1f}°C")
print()

# Multiple return values
def get_circle_properties(radius):
    pi = 3.14159
    circumference = 2 * pi * radius
    area = pi * radius ** 2
    return circumference, area

print("=== Multiple Return Values ===")
circ, area = get_circle_properties(5)
print(f"Circle with radius 5:")
print(f"Circumference: {circ:.2f}")
print(f"Area: {area:.2f}")
print()

# Return without value (returns None)
def print_header(title):
    print("=" * 40)
    print(title.center(40))
    print("=" * 40)
    # No return statement

result = print_header("Welcome")
print(f"Function returned: {result}")  # None
