"""
Example 07: Creating and Using Modules

This example demonstrates how to organize code into reusable modules.

First, we'll create a utility module, then import and use it.
"""

# Create a utility module file
utils_code = '''"""
utils.py - Utility functions for the application
"""

def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b (with error handling)."""
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"

# Module-level constant
PI = 3.14159

# Module-level variable
version = "1.0.0"

def get_info():
    """Return module information."""
    return f"Utils module version {version}"
'''

with open("utils.py", "w") as file:
    file.write(utils_code)

print("✓ Created utils.py module")
print()

# Now use the module
print("=== Importing Entire Module ===")
import utils

print(utils.greet("Alice"))
print(f"5 + 3 = {utils.add(5, 3)}")
print(f"10 - 4 = {utils.subtract(10, 4)}")
print(f"PI = {utils.PI}")
print(utils.get_info())
print()

print("=== Importing Specific Functions ===")
from utils import greet, multiply

print(greet("Bob"))
print(f"4 * 7 = {multiply(4, 7)}")
print()

print("=== Import with Alias ===")
import utils as u

print(u.greet("Charlie"))
print(f"15 / 3 = {u.divide(15, 3)}")
print()

print("=== Viewing Module Contents ===")
print("Module attributes:")
attributes = [attr for attr in dir(utils) if not attr.startswith('_')]
for attr in attributes:
    print(f"  - {attr}")
print()

print("=== Module Help ===")
print(f"Help for greet function:")
help(utils.greet)
print()

# Create another example module
math_utils_code = '''"""
math_utils.py - Mathematical utility functions
"""

def factorial(n):
    """Calculate factorial of n."""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_prime(n):
    """Check if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    """Generate first n Fibonacci numbers."""
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]
'''

with open("math_utils.py", "w") as file:
    file.write(math_utils_code)

print("✓ Created math_utils.py module")
print()

print("=== Using math_utils Module ===")
import math_utils

print(f"5! = {math_utils.factorial(5)}")
print(f"Is 17 prime? {math_utils.is_prime(17)}")
print(f"First 10 Fibonacci numbers: {math_utils.fibonacci(10)}")
