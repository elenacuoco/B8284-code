"""
EXERCISE 3.4: Password Validator (BONUS)

OBJECTIVE:
Create a comprehensive password validation system.

Create these functions:

1. is_valid_length(password, min_length=8)
   - Check if password meets minimum length

2. has_uppercase(password)
   - Check if password contains at least one uppercase letter

3. has_lowercase(password)
   - Check if password contains at least one lowercase letter

4. has_digit(password)
   - Check if password contains at least one digit

5. has_special_char(password)
   - Check if password contains special characters (!@#$%^&*)

6. validate_password(password)
   - Use all above functions
   - Return tuple: (is_valid, messages)
   - messages should list all failed requirements

REQUIREMENTS:
- Use docstrings for all functions
- Handle errors (None input, non-string input)
- Provide helpful feedback

EXAMPLE USAGE:
valid, messages = validate_password("Pass123")
if valid:
    print("Password is valid!")
else:
    print("Password issues:")
    for msg in messages:
        print(f"  - {msg}")

EXPECTED OUTPUT for "Pass123":
Password issues:
  - Password must contain at least one special character

EXPECTED OUTPUT for "MyP@ssw0rd":
Password is valid!

BONUS CHALLENGE:
Create a password strength meter (Weak/Medium/Strong)
based on how many requirements are met.

GOOD LUCK! 🔐
"""

# WRITE YOUR CODE BELOW:
