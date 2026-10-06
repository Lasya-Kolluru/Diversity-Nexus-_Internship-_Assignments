# ==============================================================================
# Question: Part I - Debugging Lab
# Problem statement: Correct six common conditional-logic mistakes.
# Input: Fixed test values.
# Processing: Apply comparison, ordering, range, menu, and nested-if fixes.
# Output: Correct result for each fixed example.
# ==============================================================================

print("Bug 1")
age = 18
if age == 18:
    print("Adult")

print("Bug 2")
marks = 85
if marks >= 80:
    print("Excellent")
elif marks >= 50:
    print("Pass")
else:
    print("Fail")

print("Bug 3")
age = 25
if age >= 18 and age <= 60:
    print("Eligible")
else:
    print("Not eligible")

print("Bug 4")
has_id = True
age = 17
if age >= 18 and has_id:
    print("Allowed")
else:
    print("Not allowed")

print("Bug 5")
choice = 2
if choice == 1:
    print("Deposit")
elif choice == 2:
    print("Withdraw")
elif choice == 3:
    print("Check Balance")
else:
    print("Invalid choice")

print("Bug 6")
username = "admin"
password = "1234"
if username == "admin":
    if password == "1234":
        print("Success")
    else:
        print("Wrong password")
else:
    print("Wrong username")

# ==============================================================================
# Output / Sample results:
# Bug 1
# Adult
# Bug 2
# Excellent
# Bug 3
# Eligible
# Bug 4
# Not allowed
# Bug 5
# Withdraw
# Bug 6
# Success
#
# Bug 1: = assigns a value; == compares two values.
# Bug 2: The original marks >= 50 branch catches 85 before marks >= 80.
#        Check the higher threshold first and give it the Excellent outcome.
# Bug 3: A number must be at least 18 AND at most 60; OR accepts out-of-range ages.
# Bug 4: age >= 18 is False, so the AND expression is False even though has_id is True.
# Bug 5: Each menu choice needs its own distinct value; the final option is 3.
# Bug 6: The original checked one password against two different strings.
#        Check username and password as separate values.
# ==============================================================================