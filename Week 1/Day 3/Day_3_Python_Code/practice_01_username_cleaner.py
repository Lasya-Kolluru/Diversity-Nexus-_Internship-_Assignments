# ============================================================================== 
# Question: Practice 1 - Username Cleaner
# Problem statement: Ask for a username, remove spaces, convert to lowercase.
# Input: Username string with optional extra spaces.
# Processing: username.strip().lower()
# Output: Cleaned username.
# ============================================================================== 

username = input("Username: ").strip().lower()
print(f"Cleaned Username: {username}")

# ============================================================================== 
# Output / Test Cases:
# Test case 1:
# Input: Username: Admin
# Output: Cleaned Username: admin
#
# Test case 2:
# Input: Username: USERname
# Output: Cleaned Username: username
#
# Edge case:
# Input: Username: "   "
# Output: Cleaned Username: 
#
# Explanation:
# strip() removes leading and trailing spaces, and lower() converts letters to
# lowercase. This makes usernames consistent and easy to validate.
# ============================================================================== 
