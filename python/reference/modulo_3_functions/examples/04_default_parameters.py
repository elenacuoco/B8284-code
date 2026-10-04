"""
EXAMPLE 4: Default Parameters
Optional parameters with default values
"""

# Basic default parameter
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

print("=== Default Parameters ===")
greet("Alice")              # Uses default "Hello"
greet("Bob", "Hi")          # Custom greeting
greet("Charlie", "Hey")     # Custom greeting
print()

# Multiple default parameters
def create_profile(name, age=18, country="Unknown"):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Country: {country}")
    print()

print("=== Multiple Defaults ===")
create_profile("Alice")                    # All defaults
create_profile("Bob", 25)                  # Custom age
create_profile("Charlie", 30, "USA")       # All custom
print()

# Practical example: Price calculator
def calculate_price(price, tax_rate=0.20, discount=0):
    """Calculate final price with tax and discount."""
    price_with_tax = price + (price * tax_rate)
    final_price = price_with_tax - discount
    return final_price

print("=== Price Calculator ===")
print(f"Price $100: ${calculate_price(100):.2f}")
print(f"Price $100 (15% tax): ${calculate_price(100, 0.15):.2f}")
print(f"Price $100 (20% tax, $10 off): ${calculate_price(100, 0.20, 10):.2f}")
print()

# Named arguments (keyword arguments)
def describe_pet(animal, name, age=1):
    print(f"I have a {age}-year-old {animal} named {name}")

print("=== Named Arguments ===")
describe_pet("dog", "Rex")
describe_pet("cat", "Whiskers", 3)
describe_pet(name="Buddy", animal="hamster", age=2)  # Order doesn't matter!
print()

# Power function with default exponent
def power(base, exponent=2):
    """Calculate base raised to exponent."""
    return base ** exponent

print("=== Power Function ===")
print(f"5 squared: {power(5)}")           # Default: square
print(f"5 cubed: {power(5, 3)}")          # Custom: cube
print(f"2 to the 10th: {power(2, 10)}")   # Custom: 10th power
