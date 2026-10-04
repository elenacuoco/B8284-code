"""
EXAMPLE 8: break and continue
Controlling loop execution
"""

print("=== break - Exit Loop Early ===")
for i in range(10):
    if i == 5:
        print("Found 5! Stopping...")
        break
    print(i)
print("Loop ended\n")

# Finding first number divisible by 7
print("=== Find First Multiple of 7 ===")
for i in range(1, 100):
    if i % 7 == 0:
        print(f"First multiple of 7: {i}")
        break
print()

# continue - Skip iteration
print("=== continue - Skip Even Numbers ===")
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"Odd number: {i}")
print()

# Print only positive numbers
print("=== Print Only Positive ===")
numbers = [5, -3, 8, -1, 0, 12, -7, 4]
for num in numbers:
    if num <= 0:
        continue
    print(num, end=" ")
print("\n")

# Infinite loop with break
print("=== Interactive Loop ===")
while True:
    answer = input("Do you want to continue? (yes/no): ").lower()
    
    if answer == "no":
        print("Exiting...")
        break
    elif answer == "yes":
        print("Continuing...")
    else:
        print("Please answer yes or no")

print("Program ended")
