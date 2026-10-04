"""
EXERCISE 5.2: CSV Grade Processor - SOLUTION
"""

import csv

# Create sample input file
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

print("✓ Created students_input.csv\n")


def get_letter_grade(average):
    """Convert numeric average to letter grade."""
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


def process_grades(input_file, output_file):
    """
    Read grades from CSV, calculate averages, and write results.
    
    Returns:
        list: Processed student data with averages
    """
    students = []
    
    # Read input file
    with open(input_file, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row["name"]
            math = int(row["math"])
            english = int(row["english"])
            science = int(row["science"])
            
            # Calculate average
            average = (math + english + science) / 3
            letter_grade = get_letter_grade(average)
            
            students.append({
                "name": name,
                "average": average,
                "letter_grade": letter_grade
            })
    
    # Write output file
    with open(output_file, "w", newline='') as file:
        fieldnames = ["name", "average", "letter_grade"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(students)
    
    return students


def calculate_statistics(students):
    """Calculate class statistics."""
    averages = [s["average"] for s in students]
    
    # Grade distribution
    grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for student in students:
        grade_counts[student["letter_grade"]] += 1
    
    # Find highest and lowest
    highest = max(students, key=lambda s: s["average"])
    lowest = min(students, key=lambda s: s["average"])
    
    return {
        "class_average": sum(averages) / len(averages),
        "highest": highest,
        "lowest": lowest,
        "grade_distribution": grade_counts
    }


def find_students_by_threshold(students, threshold, above=True):
    """BONUS: Find students above or below a threshold."""
    if above:
        return [s for s in students if s["average"] >= threshold]
    else:
        return [s for s in students if s["average"] < threshold]


# Process the grades
print("=== Processing Grades ===")
students = process_grades("students_input.csv", "students_output.csv")
print(f"✓ Processed {len(students)} students")
print("✓ Created students_output.csv\n")

# Display results
print("=== Results ===")
for student in students:
    print(f"{student['name']}: {student['average']:.1f} ({student['letter_grade']})")

# Calculate statistics
print("\n=== Class Statistics ===")
stats = calculate_statistics(students)
print(f"Class average: {stats['class_average']:.1f}")
print(f"Highest: {stats['highest']['name']} ({stats['highest']['average']:.1f})")
print(f"Lowest: {stats['lowest']['name']} ({stats['lowest']['average']:.1f})")

print("\n=== Grade Distribution ===")
for grade, count in stats['grade_distribution'].items():
    print(f"{grade}: {count}")

# BONUS: Find students by threshold
print("\n=== BONUS: Students with Average >= 90 ===")
top_students = find_students_by_threshold(students, 90, above=True)
for student in top_students:
    print(f"  {student['name']}: {student['average']:.1f}")

print("\n=== BONUS: Students with Average < 85 ===")
struggling = find_students_by_threshold(students, 85, above=False)
for student in struggling:
    print(f"  {student['name']}: {student['average']:.1f}")
