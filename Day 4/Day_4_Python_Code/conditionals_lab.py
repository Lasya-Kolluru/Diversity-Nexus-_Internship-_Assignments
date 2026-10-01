# ==============================================================================
# Question: Parts A-C - Conditional Structure and Operators
# Problem statement: Demonstrate if/elif/else, comparisons, and Boolean logic.
# Input: Values set in the examples below.
# Processing: Evaluate conditions and select the matching branch.
# Output: Printed decisions and True/False results.
# ==============================================================================

print("Basic if")
age = 20
if age >= 19:
    print("Enter your name:")

print("\nif/else")
marks = 70
if marks >= 90:
    print("A Grade")
else:
    print("B Grade")

print("\nif/elif/else")
marks = 30
if marks >= 90:
    print("A Grade")
elif marks >= 60:
    print("B Grade")
else:
    print("Fail")

print("\nNested if")
marks = 80
if marks >= 50:
    if marks >= 75:
        print("Good marks")

print("\nComparison operators")
print(10 > 5)
print(10 < 5)
print(10 == 10)
print(10 != 10)
print(25 >= 25)
print(24 <= 20)
print("Python" == "python")
print("AI" != "ML")
print(100 == "100")

print("\nLogical operators")
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print(True or False)
print(False or False)
print(not True)
print(not False)

print("\nReal-life examples")
age = 20
has_student_id = True
print(age >= 18 and has_student_id)
day = "Monday"
print(day == "Saturday" or day == "Monday")
is_going = True
print(not is_going)

# ==============================================================================
# Output / Sample results:
# Basic if
# Enter your name:
#
# if/else
# B Grade
#
# if/elif/else
# Fail
#
# Nested if
# Good marks
#
# Comparison operators
# True
# False
# True
# False
# True
# False
# False
# True
# False
#
# Logical operators
# True
# False
# False
# False
# True
# False
# False
# True
#
# Real-life examples
# True
# True
# False
#
# "Python" == "python" is False because string equality is case-sensitive.
# 100 == "100" is False because one value is an integer and the other is a string.
# ==============================================================================