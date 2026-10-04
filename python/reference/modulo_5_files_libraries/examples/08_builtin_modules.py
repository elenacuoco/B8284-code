"""
Example 08: Built-in Modules

Demonstrates useful modules from Python's standard library.
These modules come with Python - no installation needed!
"""

print("=== Math Module ===")
import math

print(f"Square root of 16: {math.sqrt(16)}")
print(f"Pi: {math.pi}")
print(f"Euler's number: {math.e}")
print(f"2^8: {math.pow(2, 8)}")
print(f"Ceiling of 4.3: {math.ceil(4.3)}")
print(f"Floor of 4.7: {math.floor(4.7)}")
print(f"Factorial of 5: {math.factorial(5)}")
print()

print("=== Random Module ===")
import random

print(f"Random integer 1-10: {random.randint(1, 10)}")
print(f"Random float 0-1: {random.random()}")
print(f"Random choice: {random.choice(['apple', 'banana', 'cherry'])}")

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"Shuffled list: {numbers}")

sample = random.sample(range(1, 50), 6)  # Lottery numbers!
print(f"Random sample (6 numbers): {sorted(sample)}")
print()

print("=== Datetime Module ===")
import datetime

now = datetime.datetime.now()
print(f"Current date and time: {now}")
print(f"Formatted: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Date only: {now.strftime('%B %d, %Y')}")
print(f"Time only: {now.strftime('%I:%M %p')}")

birthday = datetime.datetime(1990, 5, 15)
age = now.year - birthday.year
print(f"Age if born May 15, 1990: {age} years")

tomorrow = now + datetime.timedelta(days=1)
print(f"Tomorrow: {tomorrow.strftime('%Y-%m-%d')}")
print()

print("=== OS Module ===")
import os

print(f"Current directory: {os.getcwd()}")
print(f"Files in current directory:")
for file in os.listdir()[:5]:  # Show first 5
    print(f"  - {file}")

print(f"Path separator: '{os.sep}'")
print(f"User home: {os.path.expanduser('~')}")

# Check if path exists
if os.path.exists("students.csv"):
    print(f"students.csv size: {os.path.getsize('students.csv')} bytes")
print()

print("=== Time Module ===")
import time

print("Counting...")
for i in range(1, 4):
    print(f"  {i}")
    time.sleep(0.5)  # Wait 0.5 seconds
print("Done!")

start = time.time()
# Do something
sum([i**2 for i in range(1000)])
end = time.time()
print(f"Execution time: {(end - start)*1000:.2f} milliseconds")
print()

print("=== Statistics Module ===")
import statistics

data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(f"Data: {data}")
print(f"Mean: {statistics.mean(data)}")
print(f"Median: {statistics.median(data)}")
print(f"Standard deviation: {statistics.stdev(data):.2f}")

grades = [85, 90, 78, 92, 88, 95, 82]
print(f"\nGrades: {grades}")
print(f"Average grade: {statistics.mean(grades):.1f}")
print()

print("=== Collections Module ===")
from collections import Counter, defaultdict

# Counter - count occurrences
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = Counter(words)
print(f"Word counts: {word_count}")
print(f"Most common: {word_count.most_common(2)}")

# defaultdict - dictionary with default values
scores = defaultdict(list)
scores["Alice"].append(95)
scores["Alice"].append(88)
scores["Bob"].append(92)
print(f"Scores: {dict(scores)}")
