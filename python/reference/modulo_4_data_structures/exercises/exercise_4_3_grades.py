"""
EXERCISE 4.3: Student Grade Tracker

OBJECTIVE:
Create a grade tracking system using nested data structures.

REQUIREMENTS:
1. Store multiple students with multiple test scores
2. Use dictionary with lists: {student_name: [scores]}
3. Implement these functions:
   - add_student(grade_tracker, name)
   - add_grade(grade_tracker, name, score)
   - get_average(grade_tracker, name)
   - get_class_average(grade_tracker)
   - get_top_student(grade_tracker)
   - display_report(grade_tracker)

EXAMPLE USAGE:
grade_tracker = {}
add_student(grade_tracker, "Alice")
add_grade(grade_tracker, "Alice", 95)
add_grade(grade_tracker, "Alice", 88)
add_grade(grade_tracker, "Alice", 92)
display_report(grade_tracker)

EXPECTED OUTPUT:
=== Grade Report ===
Alice: [95, 88, 92] → Average: 91.7
Bob: [78, 85, 80] → Average: 81.0
Charlie: [92, 95, 93] → Average: 93.3

Class Average: 88.7
Top Student: Charlie (93.3)

BONUS:
Add letter grades (A, B, C, D, F) based on averages.

GOOD LUCK! 📚
"""

# WRITE YOUR CODE BELOW:
