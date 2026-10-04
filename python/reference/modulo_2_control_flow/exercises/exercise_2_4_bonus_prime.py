"""
EXERCISE 2.4: Prime Number Checker (BONUS)

OBJECTIVE:
Write a program that checks if a number is prime.

A prime number is a number greater than 1 that can only be divided 
evenly by 1 and itself (e.g., 2, 3, 5, 7, 11, 13, 17, 19, 23...)

The program should:
1. Ask the user for a number
2. Check if it's prime
3. Print whether it is or isn't prime
4. If not prime, show one factor (besides 1 and itself)

EXAMPLE OUTPUT:
Enter a number: 17
17 is a PRIME number!

Enter a number: 15
15 is NOT prime (divisible by 3)

Enter a number: 1
1 is not considered prime

HINTS:
- Numbers less than 2 are not prime
- Use a for loop to check if any number from 2 to n-1 divides n evenly
- If you find a divisor, it's not prime
- Use the % operator to check divisibility
- You can use break when you find the first divisor

CHALLENGE:
Make it more efficient by only checking up to the square root of n!

GOOD LUCK! 🔢
"""

# WRITE YOUR CODE BELOW:
