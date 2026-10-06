# ============================================================================== 
# Question: Practice 4 - Email Inspector
# Problem statement: Validate an email string using membership and suffix checks.
# Input: Email address.
# Processing: Check '@', domain (.com/.in), and position using find().
# Output: Validity information.
# ============================================================================== 

email = input("Email: ")
has_at = '@' in email
valid_end = email.endswith(".com") or email.endswith(".in")
at_pos = email.find('@')

print(f"Has @: {has_at}")
print(f"Valid End: {valid_end}")
print(f"Position of @: {at_pos}")

# ============================================================================== 
# Output / Test Cases:
# Test case 1:
# Input: Email: test@gmail.com
# Output:
# Has @: True
# Valid End: True
# Position of @: 4
#
# Test case 2:
# Input: Email: lasya@test.in
# Output:
# Has @: True
# Valid End: True
# Position of @: 5
#
# Edge case:
# Input: Email: hello@
# Output:
# Has @: True
# Valid End: False
# Position of @: 5
#
# Explanation:
# '@' in email checks presence, endswith() checks the domain, and find()
# locates the exact index of '@'.
# ============================================================================== 
