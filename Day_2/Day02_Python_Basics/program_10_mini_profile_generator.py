# ==============================================================================
# Question: Part G - Program 10: Mini Profile Generator
# Problem statement: Ask name, age, height, student status and optional phone. 
#                    Display values and types.
# Input: Name (string), Age (integer), Height (float), 
#        Student status (integer to bool), Phone (string/None)
# Processing / formula: Convert inputs to proper types and display them with type()
# Output: Profile details and the data type of each detail.
# ==============================================================================

name = input("Enter name: ")
age = int(input("Enter age: "))
height = float(input("Enter height: "))
is_student = bool(int(input("Student? (1 for Yes, 0 for No): ")))
phone = input("Enter phone number: ")

print("Name:", name, type(name))
print("Age:", age, type(age))
print("Height:", height, type(height))
print("Student:", is_student, type(is_student))
print("Phone:", phone, type(phone))

# ==============================================================================
# Output / Test Cases:
#
# Test case 1: 
# Input:
#   Enter name: Sam
#   Enter age: 20
#   Enter height: 1.75
#   Student? (1 for Yes, 0 for No): 1
#   Enter phone number: 12345
# Output:
#   Name: Sam <class 'str'>
#   Age: 20 <class 'int'>
#   Height: 1.75 <class 'float'>
#   Student: True <class 'bool'>
#   Phone: 12345 <class 'str'>
#
# Test case 2:
# Input:
#   Enter name: Mia
#   Enter age: 25
#   Enter height: 1.60
#   Student? (1 for Yes, 0 for No): 0
#   Enter phone number: 98765
# Output:
#   Name: Mia <class 'str'>
#   Age: 25 <class 'int'>
#   Height: 1.6 <class 'float'>
#   Student: False <class 'bool'>
#   Phone: 98765 <class 'str'>
#
# Error faced and fix: Typing 0 for student status gave "True". Fixed by converting the string to an integer first, then to a boolean.
# One thing learned: Any non-empty string like "0" or "False" is considered True in Python unless converted to a number first.
# ==============================================================================
