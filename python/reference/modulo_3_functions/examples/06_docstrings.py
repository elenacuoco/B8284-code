"""
EXAMPLE 6: Docstrings
Documenting your functions
"""

# Basic docstring
def greet(name):
    """Greet a person by name."""
    print(f"Hello, {name}!")

print("=== Basic Docstring ===")
greet("Alice")
print(greet.__doc__)  # Access docstring
print()

# Detailed docstring
def calculate_area(width, height):
    """
    Calculate the area of a rectangle.
    
    Parameters:
        width (float): The width of the rectangle in meters
        height (float): The height of the rectangle in meters
    
    Returns:
        float: The area in square meters
    
    Example:
        >>> calculate_area(5, 3)
        15.0
    """
    return width * height

print("=== Detailed Docstring ===")
area = calculate_area(5, 3)
print(f"Area: {area}")
print("\nDocumentation:")
print(calculate_area.__doc__)
print()

# Using help() function
def convert_temperature(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    
    Args:
        celsius (float): Temperature in Celsius
    
    Returns:
        float: Temperature in Fahrenheit
    
    Formula:
        F = (C × 9/5) + 32
    """
    return (celsius * 9/5) + 32

print("=== Using help() ===")
help(convert_temperature)
print()

# Complex function with good documentation
def validate_password(password):
    """
    Check if a password meets security requirements.
    
    Requirements:
        - At least 8 characters long
        - Contains at least one uppercase letter
        - Contains at least one lowercase letter
        - Contains at least one digit
    
    Parameters:
        password (str): The password to validate
    
    Returns:
        tuple: (is_valid, message)
            is_valid (bool): True if password is valid
            message (str): Description of validation result
    
    Examples:
        >>> validate_password("Pass123")
        (False, "Password too short")
        
        >>> validate_password("Password123")
        (True, "Password is valid")
    """
    if len(password) < 8:
        return False, "Password too short (minimum 8 characters)"
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    
    if not has_upper:
        return False, "Password must contain uppercase letter"
    if not has_lower:
        return False, "Password must contain lowercase letter"
    if not has_digit:
        return False, "Password must contain a digit"
    
    return True, "Password is valid"

print("=== Complex Function Documentation ===")
valid, msg = validate_password("Pass123")
print(f"Password 'Pass123': {msg}")

valid, msg = validate_password("Password123")
print(f"Password 'Password123': {msg}")
