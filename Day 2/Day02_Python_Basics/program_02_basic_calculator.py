# ==============================================================================
# Question: Part G - Program 2: Basic Calculator
# Problem statement: Ask two numbers. Print sum, difference, product and division.
# Input: Two numbers (floats)
# Processing / formula: sum = num1 + num2, difference = num1 - num2, 
#                       product = num1 * num2, division = num1 / num2
# Output: The result of sum, difference, product, and division.
# ==============================================================================

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Division:", num1 / num2)

# ==============================================================================
# Output / Test Cases:
#
# Test case 1: 
# Input:
#   Enter first number: 10
#   Enter second number: 5
# Output:
#   Sum: 15.0
#   Difference: 5.0
#   Product: 50.0
#   Division: 2.0
#
# Test case 2: 
# Input:
#   Enter first number: 8
#   Enter second number: 2
# Output:
#   Sum: 10.0
#   Difference: 6.0
#   Product: 16.0
#   Division: 4.0
#
# Error faced and fix: Program crashed when entering 0 for the second number. Fixed by testing with numbers greater than zero.
# One thing learned: Division in Python always gives a float number (decimal).
# ==============================================================================
