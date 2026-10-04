"""
EXAMPLE 5: Variable Scope
Understanding local and global variables
"""

# Global variable
global_message = "I am global!"

def show_global():
    print(global_message)  # Can read global variables

print("=== Global Variable ===")
show_global()
print(global_message)  # Also works here
print()

# Local variable
def show_local():
    local_message = "I am local!"
    print(local_message)

print("=== Local Variable ===")
show_local()
# print(local_message)  # ERROR! Would not work here
print()

# Parameters are local
def greet(name):  # name is local to this function
    print(f"Hello, {name}!")

print("=== Parameter Scope ===")
greet("Alice")
# print(name)  # ERROR! name doesn't exist here
print()

# Same variable name in different functions
def function_a():
    x = 10
    print(f"In function_a: x = {x}")

def function_b():
    x = 20  # Different variable!
    print(f"In function_b: x = {x}")

print("=== Different Local Variables ===")
function_a()
function_b()
print()

# Good practice: Use return instead of modifying global
count = 0

def increment_bad():
    global count  # Not recommended
    count += 1
    return count

def increment_good(current_count):
    return current_count + 1

print("=== Good Practice Example ===")
print(f"Initial count: {count}")
count = increment_bad()
print(f"After bad increment: {count}")
count = increment_good(count)
print(f"After good increment: {count}")
print()

# Function with local calculations
def calculate_total(prices):
    """Calculate total with local variables."""
    subtotal = sum(prices)
    tax = subtotal * 0.20
    total = subtotal + tax
    # subtotal, tax are local - die when function ends
    return total

print("=== Local Calculation Variables ===")
items = [10, 20, 30]
final_total = calculate_total(items)
print(f"Total: ${final_total:.2f}")
# print(subtotal)  # ERROR! subtotal is local to function
