# ============================================================================== 
# Question: Practice 2 - Name Formatter
# Problem statement: Ask for first and last names, clean them, and format nicely.
# Input: First and last names in random case with spaces.
# Processing: strip() + title() + f-string
# Output: Full name in Title Case.
# ============================================================================== 

first = input("First Name: ").strip()
last = input("Last Name: ").strip()
full_name = f"{first.title()} {last.title()}"
print(f"Full Name: {full_name}")

# ============================================================================== 
# Output / Test Cases:
# Test case 1:
# Input: First Name: john
#        Last Name: DOE
# Output: Full Name: John Doe
#
# Test case 2:
# Input: First Name: aLiCe
#        Last Name: sMITH
# Output: Full Name: Alice Smith
#
# Edge case:
# Input: First Name:   
#        Last Name: smith
# Output: Full Name: Smith
#
# Explanation:
# strip() removes extra spaces around each name, title() capitalizes the first
# letter of every part, and the f-string joins them into a final name.
# ============================================================================== 
