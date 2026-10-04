"""
EXAMPLE 9: Complete Function Examples
Putting it all together
"""

# Example 1: Temperature converter with validation
def convert_temp(value, from_unit, to_unit):
    """
    Convert temperature between Celsius and Fahrenheit.
    
    Args:
        value (float): Temperature value to convert
        from_unit (str): 'C' for Celsius, 'F' for Fahrenheit
        to_unit (str): 'C' for Celsius, 'F' for Fahrenheit
    
    Returns:
        float: Converted temperature or None if error
    """
    try:
        value = float(value)
        from_unit = from_unit.upper()
        to_unit = to_unit.upper()
        
        if from_unit == to_unit:
            return value
        
        if from_unit == 'C' and to_unit == 'F':
            return (value * 9/5) + 32
        elif from_unit == 'F' and to_unit == 'C':
            return (value - 32) * 5/9
        else:
            print("Invalid units! Use 'C' or 'F'")
            return None
    
    except (ValueError, TypeError):
        print("Invalid temperature value!")
        return None

print("=== Temperature Converter ===")
print(f"25°C in Fahrenheit: {convert_temp(25, 'C', 'F'):.1f}°F")
print(f"77°F in Celsius: {convert_temp(77, 'F', 'C'):.1f}°C")
print()

# Example 2: Grade calculator
def calculate_grade(scores):
    """
    Calculate average grade and letter grade.
    
    Args:
        scores (list): List of numerical scores
    
    Returns:
        tuple: (average, letter_grade) or (None, None) if error
    """
    try:
        if not scores:
            raise ValueError("Score list is empty")
        
        average = sum(scores) / len(scores)
        
        if average >= 90:
            letter = 'A'
        elif average >= 80:
            letter = 'B'
        elif average >= 70:
            letter = 'C'
        elif average >= 60:
            letter = 'D'
        else:
            letter = 'F'
        
        return average, letter
    
    except TypeError:
        print("Error: All scores must be numbers")
        return None, None
    except ValueError as e:
        print(f"Error: {e}")
        return None, None

print("=== Grade Calculator ===")
student_scores = [85, 92, 78, 95, 88]
avg, grade = calculate_grade(student_scores)
if avg:
    print(f"Scores: {student_scores}")
    print(f"Average: {avg:.1f}")
    print(f"Grade: {grade}")
print()

# Example 3: Password validator
def validate_and_create_account(username, password, email):
    """
    Validate user registration information.
    
    Args:
        username (str): Desired username
        password (str): Desired password
        email (str): Email address
    
    Returns:
        tuple: (success, message)
    """
    # Validate username
    if len(username) < 3:
        return False, "Username too short (minimum 3 characters)"
    
    if not username.isalnum():
        return False, "Username must be alphanumeric"
    
    # Validate password
    if len(password) < 8:
        return False, "Password too short (minimum 8 characters)"
    
    has_digit = any(c.isdigit() for c in password)
    has_upper = any(c.isupper() for c in password)
    
    if not has_digit:
        return False, "Password must contain at least one digit"
    
    if not has_upper:
        return False, "Password must contain at least one uppercase letter"
    
    # Validate email
    if '@' not in email or '.' not in email:
        return False, "Invalid email address"
    
    # All validations passed
    return True, "Account created successfully!"

print("=== Account Validator ===")
test_cases = [
    ("jo", "Pass123", "joe@email.com"),
    ("john", "pass123", "john@email.com"),
    ("john", "Pass123", "john@email.com"),
    ("john", "Pass123", "invalid-email"),
]

for username, password, email in test_cases:
    success, message = validate_and_create_account(username, password, email)
    print(f"User: {username}")
    print(f"Result: {message}\n")

# Example 4: Simple calculator with history
calculation_history = []

def calculator_with_history(operation, a, b):
    """
    Perform calculation and save to history.
    
    Args:
        operation (str): '+', '-', '*', or '/'
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Result of calculation
    """
    try:
        if operation == '+':
            result = a + b
        elif operation == '-':
            result = a - b
        elif operation == '*':
            result = a * b
        elif operation == '/':
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = a / b
        else:
            raise ValueError(f"Invalid operation: {operation}")
        
        # Save to history
        calculation_history.append(f"{a} {operation} {b} = {result}")
        return result
    
    except (ZeroDivisionError, ValueError) as e:
        print(f"Error: {e}")
        return None

print("=== Calculator with History ===")
calculator_with_history('+', 10, 5)
calculator_with_history('*', 7, 3)
calculator_with_history('/', 20, 4)
calculator_with_history('/', 10, 0)  # Error case

print("\nCalculation History:")
for calc in calculation_history:
    print(f"  {calc}")
