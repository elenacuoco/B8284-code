"""
EXAMPLE 8: Advanced Error Handling
Using try/except/else/finally
"""

# Basic try/except/else/finally
print("=== Complete Error Handling Structure ===")
try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old")
except ValueError:
    print("Invalid age entered!")
else:
    print("Age saved successfully!")  # Only if NO error
finally:
    print("Thank you for using our program!")  # ALWAYS runs
print()

# File handling example
def read_file_safe(filename):
    """Read a file with proper error handling."""
    file = None
    try:
        print(f"Trying to open {filename}...")
        file = open(filename, 'r')
        content = file.read()
        print("File read successfully!")
        return content
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except PermissionError:
        print(f"Error: No permission to read '{filename}'")
        return None
    else:
        print("No errors occurred!")
    finally:
        if file:
            file.close()
            print("File closed")

print("=== File Reading Example ===")
# Try with a non-existent file
content = read_file_safe("nonexistent.txt")
print()

# Create a test file and try again
print("=== Creating and Reading Test File ===")
try:
    with open("test.txt", "w") as f:
        f.write("Hello from Python!")
    
    content = read_file_safe("test.txt")
    if content:
        print(f"Content: {content}")
except Exception as e:
    print(f"Error: {e}")
print()

# User input validation with else/finally
def get_valid_number(prompt):
    """Get a valid number from user with retries."""
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")
        else:
            print("Valid number received!")
            return value
        finally:
            print("Attempt completed.")

print("=== Input Validation ===")
# Uncomment to test:
# number = get_valid_number("Enter a number: ")
# print(f"You entered: {number}")
print()

# Complex example: Safe calculator
def safe_calculator():
    """Calculator with comprehensive error handling."""
    print("=== Safe Calculator ===")
    
    try:
        num1 = float(input("First number: "))
        num2 = float(input("Second number: "))
        op = input("Operation (+, -, *, /): ")
        
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            result = num1 / num2
        else:
            raise ValueError("Invalid operation")
        
    except ValueError as e:
        print(f"Input error: {e}")
        return None
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    else:
        print(f"Calculation successful: {result}")
        return result
    finally:
        print("Calculator session ended.")

# Uncomment to test:
# result = safe_calculator()
