# ==============================================================================
# Question: Part H1 - Grade Calculator
# Problem statement: Validate marks and assign one of five grades.
# Input: Student name and an integer mark from 0 to 100.
# Processing: Check invalid values first, then evaluate grade thresholds.
# Output: The student's grade and a short message.
# ==============================================================================

student_name = input("Enter student name: ").strip() or "Lasya-Kolluru"

try:
    marks = int(input("Enter marks (0-100): "))
except ValueError:
    print("Invalid marks! Enter a whole number from 0 to 100.")
else:
    if marks < 0 or marks > 100:
        print("Invalid marks! Please enter a value between 0 and 100.")
    elif marks >= 90:
        print(f"Student: {student_name} | Grade: A | Message: Excellent work!")
    elif marks >= 75:
        print(f"Student: {student_name} | Grade: B | Message: Good job!")
    elif marks >= 60:
        print(f"Student: {student_name} | Grade: C | Message: You passed.")
    elif marks >= 50:
        print(f"Student: {student_name} | Grade: D | Message: Needs improvement.")
    else:
        print(f"Student: {student_name} | Grade: F | Message: Failed. Please try again.")

# ==============================================================================
# Output / Sample runs (each test is a separate program run):
# Input: Lasya-Kolluru, 90
# Student: Lasya-Kolluru | Grade: A | Message: Excellent work!
#
# Input: Lasya-Kolluru, 75
# Student: Lasya-Kolluru | Grade: B | Message: Good job!
#
# Input: Lasya-Kolluru, 60
# Student: Lasya-Kolluru | Grade: C | Message: You passed.
#
# Input: Lasya-Kolluru, 50
# Student: Lasya-Kolluru | Grade: D | Message: Needs improvement.
#
# Input: Lasya-Kolluru, 0
# Student: Lasya-Kolluru | Grade: F | Message: Failed. Please try again.
#
# Input: Lasya-Kolluru, -5 (or 110)
# Invalid marks! Please enter a value between 0 and 100.
#
# Input: Lasya-Kolluru, abc
# Invalid marks! Enter a whole number from 0 to 100.
# ==============================================================================