"""
EXAMPLE 3: if Statement
Making decisions in your code
"""

print("=== Basic if Statement ===")
age = 20

if age >= 18:
    print("You are an adult")
    print("You can vote")

print("This line always runs")
print()

# Example with user input
print("=== Temperature Check ===")
temperature = int(input("What's the temperature? "))

if temperature > 30:
    print("It's very hot!")
    print("Stay hydrated!")

if temperature < 0:
    print("It's freezing!")
    print("Wear warm clothes!")

print()

# Example with strings
print("=== Password Check ===")
password = input("Enter password: ")

if password == "secret123":
    print("Access granted!")
    print("Welcome back!")
