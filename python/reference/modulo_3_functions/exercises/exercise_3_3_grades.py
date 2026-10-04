"""
EXERCISE 3.3: Grade Calculator

OBJECTIVE:
Create a function that calculates student grades.

Function name: calculate_final_grade(scores, weights=None)

REQUIREMENTS:
- Takes a list of scores (0-100)
- Optional weights parameter (list of decimals that sum to 1.0)
- If no weights provided, use equal weights
- Return the weighted average
- Return both numeric grade and letter grade
- Handle errors (empty list, invalid scores, etc.)

LETTER GRADES:
- A: 90-100
- B: 80-89
- C: 70-79
- D: 60-69
- F: below 60

EXAMPLE USAGE:
# Equal weights
scores = [85, 92, 78, 95]
avg, letter = calculate_final_grade(scores)
print(f"Average: {avg:.1f}, Grade: {letter}")

# With weights (e.g., tests worth more than homework)
scores = [85, 92, 78, 95]
weights = [0.3, 0.3, 0.2, 0.2]
avg, letter = calculate_final_grade(scores, weights)
print(f"Weighted Average: {avg:.1f}, Grade: {letter}")

BONUS:
Add a function to calculate class statistics:
- get_class_stats(student_grades) -> returns min, max, average

GOOD LUCK! 📊
"""

# WRITE YOUR CODE BELOW:
