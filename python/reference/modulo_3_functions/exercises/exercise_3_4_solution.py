"""
EXERCISE 3.4: Password Validator - SOLUTION
"""

def is_valid_length(password, min_length=8):
    """Check if password meets minimum length requirement."""
    try:
        return len(password) >= min_length
    except TypeError:
        return False

def has_uppercase(password):
    """Check if password contains uppercase letter."""
    try:
        return any(c.isupper() for c in password)
    except TypeError:
        return False

def has_lowercase(password):
    """Check if password contains lowercase letter."""
    try:
        return any(c.islower() for c in password)
    except TypeError:
        return False

def has_digit(password):
    """Check if password contains a digit."""
    try:
        return any(c.isdigit() for c in password)
    except TypeError:
        return False

def has_special_char(password):
    """Check if password contains special character."""
    try:
        special_chars = "!@#$%^&*"
        return any(c in special_chars for c in password)
    except TypeError:
        return False

def validate_password(password):
    """
    Validate password against all requirements.
    
    Args:
        password (str): Password to validate
    
    Returns:
        tuple: (is_valid, messages)
            is_valid (bool): True if all requirements met
            messages (list): List of failed requirements
    """
    try:
        if not isinstance(password, str):
            return False, ["Password must be a string"]
        
        messages = []
        
        if not is_valid_length(password):
            messages.append("Password must be at least 8 characters long")
        
        if not has_uppercase(password):
            messages.append("Password must contain at least one uppercase letter")
        
        if not has_lowercase(password):
            messages.append("Password must contain at least one lowercase letter")
        
        if not has_digit(password):
            messages.append("Password must contain at least one digit")
        
        if not has_special_char(password):
            messages.append("Password must contain at least one special character (!@#$%^&*)")
        
        is_valid = len(messages) == 0
        return is_valid, messages
    
    except Exception as e:
        return False, [f"Error validating password: {e}"]


# Test the validator
print("=== Password Validator Tests ===\n")

test_passwords = [
    "Pass123",          # Missing special char
    "MyP@ssw0rd",       # Valid
    "short",            # Too short
    "noupperca$e1",     # No uppercase
    "NOLOWERCASE1!",    # No lowercase
    "NoDigits!",        # No digits
    "ValidPass123!",    # Valid
]

for pwd in test_passwords:
    valid, messages = validate_password(pwd)
    print(f"Password: '{pwd}'")
    if valid:
        print("✓ Password is valid!\n")
    else:
        print("✗ Password issues:")
        for msg in messages:
            print(f"  - {msg}")
        print()

# BONUS: Password strength meter
def password_strength(password):
    """
    Calculate password strength.
    
    Args:
        password (str): Password to check
    
    Returns:
        str: 'Weak', 'Medium', or 'Strong'
    """
    try:
        score = 0
        
        if is_valid_length(password, 8):
            score += 1
        if is_valid_length(password, 12):
            score += 1
        if has_uppercase(password):
            score += 1
        if has_lowercase(password):
            score += 1
        if has_digit(password):
            score += 1
        if has_special_char(password):
            score += 1
        
        if score <= 2:
            return 'Weak'
        elif score <= 4:
            return 'Medium'
        else:
            return 'Strong'
    
    except Exception:
        return 'Invalid'

print("=== BONUS: Password Strength Meter ===\n")
test_passwords_strength = [
    "pass",
    "Password",
    "Password1",
    "P@ssw0rd",
    "MySecureP@ssw0rd123",
]

for pwd in test_passwords_strength:
    strength = password_strength(pwd)
    print(f"'{pwd}' - Strength: {strength}")
