# ==============================================================================
# Question: Part G - Program 5: Student Marks
# Problem statement: Ask 3 subject marks. Calculate total and average.
# Input: Marks for 3 subjects (floats)
# Processing / formula: Total = mark1 + mark2 + mark3, Average = Total / 3
# Output: Total marks and average marks.
# ==============================================================================

m1 = float(input("Enter marks for Subject 1: "))
m2 = float(input("Enter marks for Subject 2: "))
m3 = float(input("Enter marks for Subject 3: "))

total = m1 + m2 + m3
average = total / 3

print("Total Marks:", total)
print("Average:", average)

# ==============================================================================
# Output / Test Cases:
#
# Test case 1: 
# Input:
#   Enter marks for Subject 1: 80
#   Enter marks for Subject 2: 90
#   Enter marks for Subject 3: 85
# Output:
#   Total Marks: 255.0
#   Average: 85.0
#
# Test case 2: 
# Input:
#   Enter marks for Subject 1: 50
#   Enter marks for Subject 2: 60
#   Enter marks for Subject 3: 70
# Output:
#   Total Marks: 180.0
#   Average: 60.0
#
# Error faced and fix: Tried entering letters instead of numbers, and it crashed. Fixed by only typing valid numbers.
# One thing learned: Averages often become long decimal numbers depending on the inputs.
# ==============================================================================
