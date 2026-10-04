"""
EXERCISE 4.1: Shopping List Manager - SOLUTION
"""

def add_item(shopping_list, name, quantity, price):
    """Add an item to the shopping list."""
    item = {
        "name": name,
        "quantity": quantity,
        "price": price
    }
    shopping_list.append(item)
    print(f"Added: {name}")

def remove_item(shopping_list, name):
    """Remove an item from the shopping list by name."""
    for item in shopping_list:
        if item["name"] == name:
            shopping_list.remove(item)
            print(f"Removed: {name}")
            return
    print(f"Item '{name}' not found")

def calculate_total(shopping_list):
    """Calculate the total cost of all items."""
    total = 0
    for item in shopping_list:
        total += item["quantity"] * item["price"]
    return total

def display_list(shopping_list):
    """Display the shopping list with prices."""
    print("\n=== Shopping List ===")
    if not shopping_list:
        print("  (empty)")
        return
    
    for item in shopping_list:
        subtotal = item["quantity"] * item["price"]
        print(f"  {item['name']}: {item['quantity']} × ${item['price']:.2f} = ${subtotal:.2f}")

def find_most_expensive(shopping_list):
    """BONUS: Find the most expensive item (by subtotal)."""
    if not shopping_list:
        return None
    
    most_expensive = max(shopping_list, 
                        key=lambda x: x["quantity"] * x["price"])
    return most_expensive


# Test the functions
print("=== Shopping List Manager ===\n")

shopping_list = []

# Add items
add_item(shopping_list, "Apple", 6, 0.50)
add_item(shopping_list, "Banana", 10, 0.30)
add_item(shopping_list, "Bread", 2, 2.50)
add_item(shopping_list, "Milk", 1, 3.99)

# Display list
display_list(shopping_list)

# Calculate total
total = calculate_total(shopping_list)
print(f"\nTotal: ${total:.2f}\n")

# Remove an item
remove_item(shopping_list, "Banana")
display_list(shopping_list)
print(f"New Total: ${calculate_total(shopping_list):.2f}\n")

# BONUS: Most expensive item
most_expensive = find_most_expensive(shopping_list)
if most_expensive:
    subtotal = most_expensive["quantity"] * most_expensive["price"]
    print(f"Most expensive item: {most_expensive['name']} (${subtotal:.2f})")
