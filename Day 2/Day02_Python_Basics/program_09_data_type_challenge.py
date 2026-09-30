# ==============================================================================
# Question: Part G - Program 9: Data Type Challenge
# Problem statement: Create int, float, str, bool and None. Print values/types. 
#                    Convert selected values and explain.
# Input: No user input (hardcoded variables)
# Processing / formula: Assign variables, check their types, convert integer 
#                       to float, float to string.
# Output: Values and types of all variables, plus conversion results.
# ==============================================================================

integer = 10
decimal = 5.5
text = "Hello"
boolean = True
empty = None

print(integer, type(integer))
print(decimal, type(decimal))
print(text, type(text))
print(boolean, type(boolean))
print(empty, type(empty))

print("Converted Int to Float:", float(integer))
print("Converted Float to String:", str(decimal))

# ==============================================================================
# Output / Test Cases:
#
# Test case 1: (Default values)
# Output: 
#   10 <class 'int'>
#   5.5 <class 'float'>
#   Hello <class 'str'>
#   True <class 'bool'>
#   None <class 'NoneType'>
#   Converted Int to Float: 10.0
#   Converted Float to String: 5.5
#
# Test case 2: (Change integer to 20 and run)
# Output: 
#   20 <class 'int'>
#   5.5 <class 'float'>
#   Hello <class 'str'>
#   True <class 'bool'>
#   None <class 'NoneType'>
#   Converted Int to Float: 20.0
#   Converted Float to String: 5.5
#
# Error faced and fix: Confused about how to print None. Fixed by just printing it normally without quotes.
# One thing learned: None is its own special data type called NoneType.
# ==============================================================================
