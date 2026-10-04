"""
BONUS EXERCISE 1.4: Your Profile - SOLUTION
"""

# Collect information
print("Create your profile!")
print()
full_name = input("Full name: ")
age = input("Age: ")
city = input("City: ")
hobby = input("Favorite hobby: ")
movie = input("Favorite movie: ")

# Convert age for calculations
age_int = int(age)
days_lived = age_int * 365

# Display the profile
print()
print("=" * 40)
print("            MY PROFILE")
print("=" * 40)
print(f"Name:        {full_name}")
print(f"Age:         {age} years")
print(f"City:        {city}")
print(f"Hobby:       {hobby}")
print(f"Movie:       {movie}")
print(f"Days:        ~{days_lived} days lived!")
print("=" * 40)
