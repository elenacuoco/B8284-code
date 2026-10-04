"""
EXERCISE 2.2: Number Guessing Game - SOLUTION
"""

import random

# Generate random number
secret_number = random.randint(1, 20)
max_attempts = 5
attempts = 0

print("I'm thinking of a number between 1 and 20")
print(f"You have {max_attempts} attempts\n")

# Game loop
while attempts < max_attempts:
    guess = int(input("Your guess: "))
    attempts += 1
    
    if guess == secret_number:
        print(f"🎉 Correct! You won in {attempts} attempts!")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
    
    # Show remaining attempts
    remaining = max_attempts - attempts
    if remaining > 0:
        print(f"Attempts remaining: {remaining}\n")
    else:
        print(f"\nGame over! The number was {secret_number}")
