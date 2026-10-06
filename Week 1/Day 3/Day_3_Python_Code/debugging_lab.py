# ============================================================================== 
# Question: Part K - Debugging Lab
# Problem statement: Identify and fix common Python errors involving index,
# type conversion, and string methods.
# Input: Mixed valid and invalid values.
# Processing: Fix errors caused by invalid indexing and type mismatch.
# Output: Corrected and working examples.
# ============================================================================== 

# Bug 1
name = input("Name: ")
print(name[0])

# Bug 2
age = '20'
print(f"Age: {int(age) + 1}")

# Bug 3
name = 'phani'
age = 30
print("Hello " + name + str(age))

# Bug 4
for email in ["lasya@gmail.com", "lasya@gmail.in", "kolluru@gmail.com"]:
    print(email, email.endswith(".com"))

# Bug 5
code = 'IND-MOB-2026-001'
print(code[0])

# Bug 6
text = '  hello world  '
print(text.upper().strip())

# ============================================================================== 
# Output / Sample results:
# Name: Lasya
# L
# Age: 21
# Hello phani30
# lasya@gmail.com True
# lasya@gmail.in False
# kolluru@gmail.com True
# I
# HELLO WORLD
#
# Explanation:
# The invalid index error happens when a requested position is outside the string.
# Converting strings to int and numbers to str solves type errors.
# endswith() checks whether the email ends with the required domain.
# The valid range for the product code is 0 to 15, so code[20] is invalid.
# The order of operations matters: upper() first, then strip() removes spaces.
# ============================================================================== 
