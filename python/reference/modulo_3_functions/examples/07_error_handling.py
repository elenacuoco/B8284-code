"""
EXAMPLE 7: Basic Error Handling
Using try/except to handle errors gracefully
"""

# Without error handling - program crashes
print("=== WITHOUT Error Handling ===")
print("Let's see what happens with bad input...")
# number = int(input("Enter a number: "))  # Try entering "abc"
# print(f"Your number is {number}")
# Program would crash here!
print()

# With error handling - program continues
print("=== WITH Error Handling ===")
try:
    number = int(input("Enter a number: "))
    print(f"Your number is {number}")
except ValueError:
    print("That's not a valid number!")
print("Program continues...")
print()

# Division by zero
print("=== Division by Zero ===")
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    result = numerator / denominator
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter valid numbers!")
print()

# Multiple error types
def safe_division(a, b):
    """Perform division with error handling."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None
    except TypeError:
        print("Both values must be numbers!")
        return None

print("=== Safe Division Function ===")
print(f"10 / 2 = {safe_division(10, 2)}")
print(f"10 / 0 = {safe_division(10, 0)}")
print(f"10 / 'abc' = {safe_division(10, 'abc')}")
print()

# Catching any error
print("=== Catch All Errors ===")
def safe_calculation():
    try:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        operation = input("Operation (+, -, *, /): ")
        
        if operation == '+':
            result = x + y
        elif operation == '-':
            result = x - y
        elif operation == '*':
            result = x * y
        elif operation == '/':
            result = x / y
        else:
            print("Invalid operation!")
            return
        
        print(f"Result: {result}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please try again!")

safe_calculation()
