"""
EXERCISE 2.3: Simple Calculator Menu - SOLUTION
"""

print("=== CALCULATOR ===")

while True:
    # Show menu
    print("\nOptions: add, subtract, multiply, divide, quit")
    operation = input("Choose operation: ").lower()
    
    # Check if user wants to quit
    if operation == "quit":
        print("Goodbye!")
        break
    
    # Check if operation is valid
    if operation not in ["add", "subtract", "multiply", "divide"]:
        print("Invalid operation!")
        continue
    
    # Get numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    # Perform calculation
    if operation == "add":
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    elif operation == "subtract":
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    elif operation == "multiply":
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
    elif operation == "divide":
        if num2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
