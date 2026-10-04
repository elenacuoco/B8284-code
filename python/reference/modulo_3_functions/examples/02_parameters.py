"""
EXAMPLE 2: Functions with Parameters
Making functions flexible with input
"""

# Single parameter
def greet(name):
    print(f"Hello, {name}!")
    print("Welcome to Python!")
    print()

print("=== Single Parameter ===")
greet("Alice")
greet("Bob")
greet("Charlie")

# Multiple parameters
def introduce(name, age, city):
    print(f"My name is {name}")
    print(f"I am {age} years old")
    print(f"I live in {city}")
    print()

print("=== Multiple Parameters ===")
introduce("Alice", 25, "New York")
introduce("Bob", 30, "London")

# Parameters in calculations
def calculate_rectangle_area(width, height):
    area = width * height
    print(f"Rectangle: {width}m x {height}m")
    print(f"Area: {area} square meters")
    print()

print("=== Calculation Parameters ===")
calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)

# Multiple uses of same function
def repeat_word(word, times):
    for i in range(times):
        print(word, end=" ")
    print()

print("=== Repeat Function ===")
repeat_word("Python", 5)
repeat_word("Hello", 3)
repeat_word("*", 10)
