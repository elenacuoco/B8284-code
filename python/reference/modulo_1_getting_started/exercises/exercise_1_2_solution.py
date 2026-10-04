"""
EXERCISE 1.2: Discount Price Calculator - SOLUTION
"""

# Ask for information
original_price = input("Original price: ")
discount_percent = input("Discount percentage: ")

# Convert to numbers
original_price = float(original_price)
discount_percent = float(discount_percent)

# Calculate the discount and final price
discount_amount = (original_price * discount_percent) / 100
final_price = original_price - discount_amount

# Display the results
print(f"Discount applied: {discount_amount}€")
print(f"Final price: {final_price}€")
