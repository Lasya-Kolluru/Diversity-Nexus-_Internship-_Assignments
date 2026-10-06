# ==============================================================================
# Question: Part H2 - Scholarship Eligibility Checker
# Problem statement: Determine full, partial, or no scholarship eligibility.
# Input: Student name, GPA, attendance percentage, and sports quota status.
# Processing: Validate inputs and apply the scholarship rules in order.
# Output: One of three eligibility outcomes or an input error.
# ==============================================================================

student_name = input("Enter student name: ").strip() or "Lasya-Kolluru"

try:
    gpa = float(input("Enter GPA (0.0-10.0): "))
    attendance = int(input("Enter attendance (0-100): "))
except ValueError:
    print("Invalid input! GPA must be numeric and attendance must be a whole number.")
else:
    sports_quota = input("Sports quota? (yes/no): ").strip().lower()

    if gpa < 0 or gpa > 10 or attendance < 0 or attendance > 100:
        print("Invalid input! GPA must be 0-10 and attendance must be 0-100.")
    elif sports_quota not in ("yes", "no"):
        print("Invalid sports-quota answer! Enter yes or no.")
    elif gpa >= 9.0 and attendance >= 80:
        print(f"Result for {student_name}: Eligible for Full Scholarship!")
    elif gpa >= 8.0 and (attendance >= 75 or sports_quota == "yes"):
        print(f"Result for {student_name}: Eligible for Partial Scholarship!")
    else:
        print(f"Result for {student_name}: Not Eligible for a scholarship.")

# ==============================================================================
# Output / Sample runs (each test is a separate program run):
# Input: Lasya-Kolluru, GPA 9.2, attendance 85, sports quota no
# Result for Lasya-Kolluru: Eligible for Full Scholarship!
#
# Input: Lasya-Kolluru, GPA 8.0, attendance 60, sports quota yes
# Result for Lasya-Kolluru: Eligible for Partial Scholarship!
#
# Input: Lasya-Kolluru, GPA 7.5, attendance 95, sports quota no
# Result for Lasya-Kolluru: Not Eligible for a scholarship.
#
# Input: Lasya-Kolluru, GPA 10.5, attendance 85, sports quota no
# Invalid input! GPA must be 0-10 and attendance must be 0-100.
# ==============================================================================