"""
EXERCISE 5.2: CSV Grade Processor

OBJECTIVE:
Read student grades from CSV, process them, and write results to a new CSV.

REQUIREMENTS:
1. Read grades from "students_input.csv" (name, math, english, science)
2. Calculate average for each student
3. Assign letter grade (A: 90+, B: 80+, C: 70+, D: 60+, F: <60)
4. Write results to "students_output.csv" with: name, average, letter_grade
5. Calculate and print class statistics

SAMPLE INPUT (students_input.csv):
name,math,english,science
Alice,95,88,92
Bob,78,85,80
Charlie,92,95,93
Diana,88,90,87

EXPECTED OUTPUT (students_output.csv):
name,average,letter_grade
Alice,91.7,A
Bob,81.0,B
Charlie,93.3,A
Diana,88.3,B

CLASS STATISTICS:
Class average: 88.6
Highest: Charlie (93.3)
Lowest: Bob (81.0)
Grade distribution: A=2, B=2, C=0, D=0, F=0

BONUS:
Add a function to find students with average above/below a threshold.

GOOD LUCK! 📊
"""

import csv

# First, create the input file
input_data = [
    ["name", "math", "english", "science"],
    ["Alice", "95", "88", "92"],
    ["Bob", "78", "85", "80"],
    ["Charlie", "92", "95", "93"],
    ["Diana", "88", "90", "87"]
]

with open("students_input.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(input_data)

print("✓ Created students_input.csv for testing\n")

# WRITE YOUR CODE BELOW:
