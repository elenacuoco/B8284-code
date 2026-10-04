"""
EXAMPLE 7: while Loop
Repeating while a condition is True
"""

print("=== Basic while Loop ===")
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1  # Same as: count = count + 1
print()

# Sum numbers until reaching 100
print("=== Sum Until 100 ===")
total = 0
number = 1
while total < 100:
    total += number
    print(f"Added {number}, total: {total}")
    number += 1
print()

# User input validation
print("=== Password Entry ===")
password = ""
attempts = 0

while password != "python":
    password = input("Enter password (hint: python): ")
    attempts += 1
    
    if password != "python":
        print("Wrong password, try again!")

print(f"Access granted! (took {attempts} attempts)")
print()

# Menu system
print("=== Simple Menu ===")
choice = ""
while choice != "quit":
    print("\nOptions: start, help, quit")
    choice = input("Choose an option: ").lower()
    
    if choice == "start":
        print("Starting program...")
    elif choice == "help":
        print("This is the help section")
    elif choice == "quit":
        print("Goodbye!")
    else:
        print("Invalid option")
