"""
Example 09: Complete Examples

Real-world examples combining multiple data structures.
"""

print("=== Example 1: Grade Book System ===")
grade_book = {
    "Alice": [95, 88, 92, 96],
    "Bob": [78, 85, 80, 88],
    "Charlie": [92, 95, 93, 97]
}

print("Grade Book:")
for student, grades in grade_book.items():
    average = sum(grades) / len(grades)
    print(f"  {student}: grades={grades}, average={average:.1f}")

# Find best student
best_student = max(grade_book.items(), 
                   key=lambda x: sum(x[1])/len(x[1]))
print(f"\nBest student: {best_student[0]}")
print()

print("=== Example 2: Shopping Cart ===")
cart = [
    {"name": "Apple", "price": 0.50, "quantity": 6},
    {"name": "Banana", "price": 0.30, "quantity": 10},
    {"name": "Orange", "price": 0.70, "quantity": 4}
]

print("Shopping Cart:")
total = 0
for item in cart:
    subtotal = item["price"] * item["quantity"]
    total += subtotal
    print(f"  {item['name']}: ${item['price']} × {item['quantity']} = ${subtotal:.2f}")

print(f"\nTotal: ${total:.2f}")
print()

print("=== Example 3: Inventory Management ===")
inventory = {
    "apple": {"stock": 50, "price": 0.50, "category": "fruit"},
    "banana": {"stock": 30, "price": 0.30, "category": "fruit"},
    "carrot": {"stock": 40, "price": 0.40, "category": "vegetable"},
    "bread": {"stock": 20, "price": 2.50, "category": "bakery"}
}

# Check stock levels
print("Low stock items (< 25):")
for item, details in inventory.items():
    if details["stock"] < 25:
        print(f"  {item}: {details['stock']} units")

# Calculate inventory value
total_value = sum(d["stock"] * d["price"] for d in inventory.values())
print(f"\nTotal inventory value: ${total_value:.2f}")

# Group by category
categories = {}
for item, details in inventory.items():
    category = details["category"]
    if category not in categories:
        categories[category] = []
    categories[category].append(item)

print("\nItems by category:")
for category, items in categories.items():
    print(f"  {category}: {', '.join(items)}")
print()

print("=== Example 4: Social Network ===")
# Simple friend network using sets
friends = {
    "Alice": {"Bob", "Charlie", "David"},
    "Bob": {"Alice", "Charlie", "Eve"},
    "Charlie": {"Alice", "Bob", "David", "Eve"},
    "David": {"Alice", "Charlie"},
    "Eve": {"Bob", "Charlie"}
}

# Find mutual friends
def mutual_friends(person1, person2):
    return friends[person1] & friends[person2]

# Friend recommendations (friends of friends)
def recommend_friends(person):
    # Get all friends of friends
    recommendations = set()
    for friend in friends[person]:
        recommendations |= friends[friend]
    
    # Remove person and existing friends
    recommendations -= {person}
    recommendations -= friends[person]
    
    return recommendations

print("Alice's friends:", friends["Alice"])
print("Bob's friends:", friends["Bob"])
print("Mutual friends:", mutual_friends("Alice", "Bob"))
print("Friend recommendations for Alice:", recommend_friends("Alice"))
