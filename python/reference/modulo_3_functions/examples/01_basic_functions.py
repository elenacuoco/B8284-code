"""
EXAMPLE 1: Basic Functions
Learn how to define and call functions
"""

# Define a simple function
def greet():
    print("Hello, World!")
    print("Welcome to Python functions!")

# Call the function
print("=== Calling greet() ===")
greet()
print()

# Another simple function
def say_goodbye():
    print("Goodbye!")
    print("See you later!")
    print("Thanks for learning Python!")

print("=== Calling say_goodbye() ===")
say_goodbye()
print()

# Function that does calculations
def show_multiplication_table():
    print("Multiplication table of 5:")
    for i in range(1, 11):
        print(f"5 x {i} = {5 * i}")

print("=== Calling show_multiplication_table() ===")
show_multiplication_table()
