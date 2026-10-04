"""
EXERCISE 2.1: FizzBuzz - SOLUTION
"""

for i in range(1, 51):
    if i % 15 == 0:  # Divisible by both 3 and 5
        print("FizzBuzz")
    elif i % 3 == 0:  # Divisible by 3
        print("Fizz")
    elif i % 5 == 0:  # Divisible by 5
        print("Buzz")
    else:
        print(i)
