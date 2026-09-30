# ==============================================================================
# Question: Part G - Program 7: Type Inspector
# Problem statement: Show what input() returns, then convert the value to 
#                    int/float where possible.
# Input: A number typed by the user (string)
# Processing / formula: Check type of input, convert to integer and check type, 
#                       convert to float and check type.
# Output: Original value and its type, integer value and type, float value and type.
# ==============================================================================

value = input("Enter a whole number: ")
print("Original:", value, type(value))

int_val = int(value)
print("As Integer:", int_val, type(int_val))

float_val = float(value)
print("As Float:", float_val, type(float_val))

# ==============================================================================
# Output / Test Cases:
#
# Test case 1: 
# Input:
#   Enter a whole number: 42
# Output:
#   Original: 42 <class 'str'>
#   As Integer: 42 <class 'int'>
#   As Float: 42.0 <class 'float'>
#
# Test case 2: 
# Input:
#   Enter a whole number: 100
# Output:
#   Original: 100 <class 'str'>
#   As Integer: 100 <class 'int'>
#   As Float: 100.0 <class 'float'>
#
# Error faced and fix: Got an error when typing a decimal like 5.5. Fixed by only typing whole numbers so int() works properly.
# One thing learned: The input() function always captures data as a string first.
# ==============================================================================
