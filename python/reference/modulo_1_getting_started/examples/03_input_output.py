"""
EXAMPLE 3: Input and Output
How to interact with the user
"""

# Ask the user for information
print("=== Information Gathering ===")
name = input("What's your name? ")
city = input("Which city do you live in? ")
hobby = input("What's your favorite hobby? ")

# Display the collected information
print("\n=== Summary ===")
print("Name:", name)
print("City:", city)
print("Hobby:", hobby)

# Use f-string for formatting (modern method)
print(f"\n What a pity to meet you {name}! It's great to know that in {city} you enjoy {hobby}!")
