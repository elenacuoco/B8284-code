"""
EXERCISE 4.3: Student Grade Tracker - SOLUTION
"""

def add_student(grade_tracker, name):
    """Add a new student to the grade tracker."""
    if name not in grade_tracker:
        grade_tracker[name] = []
        print(f"Added student: {name}")
    else:
        print(f"Student '{name}' already exists")

def add_grade(grade_tracker, name, score):
    """Add a grade for a student."""
    if name in grade_tracker:
        if 0 <= score <= 100:
            grade_tracker[name].append(score)
            print(f"Added grade {score} for {name}")
        else:
            print("Error: Score must be between 0 and 100")
    else:
        print(f"Error: Student '{name}' not found")

def get_average(grade_tracker, name):
    """Calculate the average grade for a student."""
    if name in grade_tracker and grade_tracker[name]:
        return sum(grade_tracker[name]) / len(grade_tracker[name])
    return None

def get_class_average(grade_tracker):
    """Calculate the average grade for the entire class."""
    all_grades = []
    for grades in grade_tracker.values():
        all_grades.extend(grades)
    
    if all_grades:
        return sum(all_grades) / len(all_grades)
    return None

def get_top_student(grade_tracker):
    """Find the student with the highest average."""
    if not grade_tracker:
        return None
    
    top_student = None
    top_average = -1
    
    for name in grade_tracker:
        avg = get_average(grade_tracker, name)
        if avg and avg > top_average:
            top_average = avg
            top_student = name
    
    return top_student, top_average

def display_report(grade_tracker):
    """Display a complete grade report."""
    print("\n=== Grade Report ===")
    
    if not grade_tracker:
        print("  (no students)")
        return
    
    for name, grades in grade_tracker.items():
        if grades:
            avg = get_average(grade_tracker, name)
            print(f"{name}: {grades} → Average: {avg:.1f}")
        else:
            print(f"{name}: No grades yet")
    
    class_avg = get_class_average(grade_tracker)
    if class_avg:
        print(f"\nClass Average: {class_avg:.1f}")
    
    top = get_top_student(grade_tracker)
    if top:
        print(f"Top Student: {top[0]} ({top[1]:.1f})")

def get_letter_grade(average):
    """BONUS: Convert numeric average to letter grade."""
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def display_report_with_letters(grade_tracker):
    """BONUS: Display report with letter grades."""
    print("\n=== Grade Report (with Letter Grades) ===")
    
    if not grade_tracker:
        print("  (no students)")
        return
    
    for name, grades in grade_tracker.items():
        if grades:
            avg = get_average(grade_tracker, name)
            letter = get_letter_grade(avg)
            print(f"{name}: {grades} → Average: {avg:.1f} ({letter})")
        else:
            print(f"{name}: No grades yet")


# Test the functions
print("=== Grade Tracker System ===\n")

grade_tracker = {}

# Add students
add_student(grade_tracker, "Alice")
add_student(grade_tracker, "Bob")
add_student(grade_tracker, "Charlie")
print()

# Add grades
add_grade(grade_tracker, "Alice", 95)
add_grade(grade_tracker, "Alice", 88)
add_grade(grade_tracker, "Alice", 92)

add_grade(grade_tracker, "Bob", 78)
add_grade(grade_tracker, "Bob", 85)
add_grade(grade_tracker, "Bob", 80)

add_grade(grade_tracker, "Charlie", 92)
add_grade(grade_tracker, "Charlie", 95)
add_grade(grade_tracker, "Charlie", 93)
print()

# Display standard report
display_report(grade_tracker)

# Get specific average
print(f"\nAlice's average: {get_average(grade_tracker, 'Alice'):.1f}")

# BONUS: Display with letter grades
display_report_with_letters(grade_tracker)
