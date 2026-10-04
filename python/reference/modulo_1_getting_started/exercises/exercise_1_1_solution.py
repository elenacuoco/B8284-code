"""
EXERCISE 1.1: Age Calculator - SOLUTION
"""

from datetime import date

# Get the current year
current_year = date.today().year

# Ask user for information
name = input("What's your name? ")

# Convert age to integer
age = int(age)

# Calculate the year they'll turn 100
year_100 = current_year + (100 - age)

# Print the message
print(f"Hello {name}! You'll celebrate 100 years in {year_100}!")
