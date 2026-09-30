# ==============================================================================
# Question: Part G - Program 6: Age Calculator
# Problem statement: Ask age and show age after 5, 10 and 20 years.
# Input: Current age (integer)
# Processing / formula: age + 5, age + 10, age + 20
# Output: Age after 5, 10, and 20 years.
# ==============================================================================

age = int(input("Enter your current age: "))

print("Age in 5 years:", age + 5)
print("Age in 10 years:", age + 10)
print("Age in 20 years:", age + 20)

# ==============================================================================
# Output / Test Cases:
#
# Test case 1: 
# Input:
#   Enter your current age: 20
# Output:
#   Age in 5 years: 25
#   Age in 10 years: 30
#   Age in 20 years: 40
#
# Test case 2: 
# Input:
#   Enter your current age: 50
# Output:
#   Age in 5 years: 55
#   Age in 10 years: 60
#   Age in 20 years: 70
#
# Error faced and fix: Error when adding a number to the age. Fixed by converting the input string to an integer using int().
# One thing learned: We must convert input() to a number before doing any math.
# ==============================================================================
