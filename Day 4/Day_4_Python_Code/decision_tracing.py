# ==============================================================================
# Question: Part D - Decision Tracing
# Problem statement: Follow each condition and observe which branch executes.
# Input: Fixed values for age, marks, amount, username, and password.
# Processing: Evaluate conditions from top to bottom.
# Output: One result for each example.
# ==============================================================================

print("1)")
age = 20
if age >= 18:
    print("Adult")
else:
    print("Minor")

print("2)")
marks = 82
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
else:
    print("C")

print("3)")
age = 20
has_id = True
if age >= 18 and has_id:
    print("Allowed")
else:
    print("Not allowed")

print("4)")
amount = 5000
if amount >= 10000:
    print("High")
elif amount >= 5000:
    print("Medium")
else:
    print("Low")

print("5)")
username = "admin"
password = "1234"
if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Unknown user")

# ==============================================================================
# Output / Sample results:
# 1)
# Adult
# 2)
# B
# 3)
# Allowed
# 4)
# Medium
# 5)
# Login successful
#
# Trace 1: 20 >= 18 is True, so the if branch prints Adult.
# Trace 2: 82 >= 90 is False; 82 >= 75 is True, so the elif branch prints B.
# Trace 3: 20 >= 18 and has_id are both True, so the if branch prints Allowed.
# Trace 4: 5000 >= 10000 is False; 5000 >= 5000 is True, so it prints Medium.
# Trace 5: Both the username and password checks are True, so it prints Login successful.
# ==============================================================================