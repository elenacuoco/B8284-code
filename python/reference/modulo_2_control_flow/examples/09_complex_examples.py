"""
EXAMPLE 9: Nested Loops and Complex Logic
Combining everything we learned
"""

print("=== Multiplication Table ===")
# Nested loop example
for i in range(1, 6):
    for j in range(1, 6):
        result = i * j
        print(f"{result:3}", end=" ")  # :3 means 3 spaces width
    print()  # New line after each row
print()

# Pattern printing
print("=== Triangle Pattern ===")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()
print()

# Number guessing game (complete)
print("=== Number Guessing Game ===")
import random

secret_number = random.randint(1, 20)
attempts = 0
max_attempts = 5

print("I'm thinking of a number between 1 and 20")
print(f"You have {max_attempts} attempts")

while attempts < max_attempts:
    guess = int(input("\nYour guess: "))
    attempts += 1
    
    if guess == secret_number:
        print(f"🎉 Correct! You won in {attempts} attempts!")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
    
    remaining = max_attempts - attempts
    if remaining > 0:
        print(f"Attempts remaining: {remaining}")
    else:
        print(f"Game over! The number was {secret_number}")
