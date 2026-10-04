"""
EXERCISE 3.3: Grade Calculator - SOLUTION
"""

def calculate_final_grade(scores, weights=None):
    """
    Calculate final grade from scores and optional weights.
    
    Args:
        scores (list): List of numerical scores (0-100)
        weights (list, optional): List of weights (must sum to 1.0)
    
    Returns:
        tuple: (numeric_grade, letter_grade) or (None, None) if error
    """
    try:
        # Validate scores list
        if not scores:
            raise ValueError("Scores list cannot be empty")
        
        # Check all scores are valid
        for score in scores:
            if not isinstance(score, (int, float)) or score < 0 or score > 100:
                raise ValueError(f"Invalid score: {score}")
        
        # Calculate average
        if weights is None:
            # Equal weights
            average = sum(scores) / len(scores)
        else:
            # Weighted average
            if len(scores) != len(weights):
                raise ValueError("Scores and weights must have same length")
            
            if abs(sum(weights) - 1.0) > 0.01:  # Allow small floating point error
                raise ValueError("Weights must sum to 1.0")
            
            average = sum(score * weight for score, weight in zip(scores, weights))
        
        # Determine letter grade
        if average >= 90:
            letter = 'A'
        elif average >= 80:
            letter = 'B'
        elif average >= 70:
            letter = 'C'
        elif average >= 60:
            letter = 'D'
        else:
            letter = 'F'
        
        return average, letter
    
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
        return None, None


# Test the function
print("=== Grade Calculator Tests ===")

# Test 1: Equal weights
scores1 = [85, 92, 78, 95]
avg, letter = calculate_final_grade(scores1)
print(f"Scores: {scores1}")
print(f"Average: {avg:.1f}, Grade: {letter}\n")

# Test 2: With weights
scores2 = [85, 92, 78, 95]
weights2 = [0.3, 0.3, 0.2, 0.2]
avg, letter = calculate_final_grade(scores2, weights2)
print(f"Scores: {scores2}")
print(f"Weights: {weights2}")
print(f"Weighted Average: {avg:.1f}, Grade: {letter}\n")

# Test 3: Error cases
print("=== Error Handling Tests ===")
calculate_final_grade([])  # Empty list
calculate_final_grade([85, 92, 150])  # Invalid score
calculate_final_grade([85, 92], [0.5])  # Mismatched lengths
print()

# BONUS: Class statistics
def get_class_stats(student_grades):
    """
    Calculate statistics for a class.
    
    Args:
        student_grades (list): List of grade tuples (name, score)
    
    Returns:
        dict: Statistics including min, max, average
    """
    try:
        if not student_grades:
            raise ValueError("No students in class")
        
        scores = [score for name, score in student_grades]
        
        stats = {
            'min': min(scores),
            'max': max(scores),
            'average': sum(scores) / len(scores),
            'count': len(scores)
        }
        
        return stats
    
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
        return None

print("=== BONUS: Class Statistics ===")
class_grades = [
    ("Alice", 92),
    ("Bob", 85),
    ("Charlie", 78),
    ("Diana", 95),
    ("Eve", 88)
]

stats = get_class_stats(class_grades)
if stats:
    print(f"Class size: {stats['count']} students")
    print(f"Highest score: {stats['max']}")
    print(f"Lowest score: {stats['min']}")
    print(f"Class average: {stats['average']:.1f}")
