"""
EXERCISE 3.1: Calculator Function - SOLUTION
"""

def calculator(num1, num2, operation):
    """
    Perform basic arithmetic operations.
    
    Args:
        num1 (float): First number
        num2 (float): Second number
        operation (str): Operation to perform (+, -, *, /)
    
    Returns:
        float: Result of the calculation, or None if error
    """
    try:
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Cannot divide by zero!")
                return None
            return num1 / num2
        else:
            print(f"Error: Invalid operation '{operation}'")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


# Test the function
print("=== Calculator Tests ===")
print(f"10 + 5 = {calculator(10, 5, '+')}")
print(f"10 - 5 = {calculator(10, 5, '-')}")
print(f"10 * 5 = {calculator(10, 5, '*')}")
print(f"10 / 5 = {calculator(10, 5, '/')}")
print(f"10 / 0 = {calculator(10, 0, '/')}")
print(f"10 % 5 = {calculator(10, 5, '%')}")
