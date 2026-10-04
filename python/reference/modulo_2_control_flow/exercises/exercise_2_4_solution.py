"""
EXERCISE 2.4: Prime Number Checker - SOLUTION
"""

# Get number from user
number = int(input("Enter a number: "))

# Check special cases
if number < 2:
    print(f"{number} is not considered prime")
else:
    # Assume it's prime until we find a divisor
    is_prime = True
    divisor = 0
    
    # Check all numbers from 2 to number-1
    for i in range(2, number):
        if number % i == 0:
            # Found a divisor, not prime!
            is_prime = False
            divisor = i
            break
    
    # Print result
    if is_prime:
        print(f"{number} is a PRIME number! ✨")
    else:
        print(f"{number} is NOT prime (divisible by {divisor})")


# BONUS: More efficient version using square root
print("\n--- Efficient Version ---")

import math

number = int(input("Enter a number: "))

if number < 2:
    print(f"{number} is not considered prime")
else:
    is_prime = True
    divisor = 0
    
    # Only check up to square root
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            is_prime = False
            divisor = i
            break
    
    if is_prime:
        print(f"{number} is a PRIME number! ✨")
    else:
        print(f"{number} is NOT prime (divisible by {divisor})")
