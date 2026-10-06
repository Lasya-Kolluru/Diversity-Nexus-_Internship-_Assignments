# ==============================================================================
# Question: Part I – Medium Challenge: Student Result Calculator
# Requirements:
#   • Ask student name.
#   • Ask marks in 5 subjects and convert them to numbers.
#   • Calculate total and average.
#   • Display name, total and average.
#   • Create result_status as a boolean showing the calculation is completed.
#   • Create remarks=None first, then assign a suitable message.
#   • Display the type of important variables.
#   • Test with at least 3 different mark sets.
#   • Bonus: support decimal marks using float.
# ==============================================================================

print("--- Enter Student Details ---")
student_name = input("Enter student name: ")
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))
sub4 = float(input("Enter marks for Subject 4: "))
sub5 = float(input("Enter marks for Subject 5: "))

total_marks = sub1 + sub2 + sub3 + sub4 + sub5
average_marks = total_marks / 5
result_status = True
remarks = None
remarks = "Marks successfully recorded and processed."

print("\n--- Student Result ---")
print("Name:", student_name)
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print("Calculation Completed:", result_status)
print("Remarks:", remarks)

print("\n--- Variable Types ---")
print("Type of student_name:", type(student_name))
print("Type of total_marks:", type(total_marks))
print("Type of result_status:", type(result_status))
print("Type of remarks:", type(remarks))

# ==============================================================================
# Output / Test Cases:
#
# Test 1 (Standard Whole Numbers):
# Input:
#   --- Enter Student Details ---
#   Enter student name: Alice
#   Enter marks for Subject 1: 85
#   Enter marks for Subject 2: 90
#   Enter marks for Subject 3: 88
#   Enter marks for Subject 4: 92
#   Enter marks for Subject 5: 80
# Output:
#   --- Student Result ---
#   Name: Alice
#   Total Marks: 435.0
#   Average Marks: 87.0
#   Calculation Completed: True
#   Remarks: Marks successfully recorded and processed.
#   --- Variable Types ---
#   Type of student_name: <class 'str'>
#   Type of total_marks: <class 'float'>
#   Type of result_status: <class 'bool'>
#   Type of remarks: <class 'str'>
#
# Test 2 (Decimal Marks - Bonus Feature):
# Input:
#   --- Enter Student Details ---
#   Enter student name: Bob
#   Enter marks for Subject 1: 75.5
#   Enter marks for Subject 2: 80.0
#   Enter marks for Subject 3: 65.25
#   Enter marks for Subject 4: 90.5
#   Enter marks for Subject 5: 88.0
# Output:
#   --- Student Result ---
#   Name: Bob
#   Total Marks: 399.25
#   Average Marks: 79.85
#   Calculation Completed: True
#   Remarks: Marks successfully recorded and processed.
#   --- Variable Types ---
#   Type of student_name: <class 'str'>
#   Type of total_marks: <class 'float'>
#   Type of result_status: <class 'bool'>
#   Type of remarks: <class 'str'>
#
# Test 3 (Low Marks / Zeros):
# Input:
#   --- Enter Student Details ---
#   Enter student name: Charlie
#   Enter marks for Subject 1: 0
#   Enter marks for Subject 2: 15.5
#   Enter marks for Subject 3: 20
#   Enter marks for Subject 4: 10
#   Enter marks for Subject 5: 5
# Output:
#   --- Student Result ---
#   Name: Charlie
#   Total Marks: 50.5
#   Average Marks: 10.1
#   Calculation Completed: True
#   Remarks: Marks successfully recorded and processed.
#   --- Variable Types ---
#   Type of student_name: <class 'str'>
#   Type of total_marks: <class 'float'>
#   Type of result_status: <class 'bool'>
#   Type of remarks: <class 'str'>
# ==============================================================================
