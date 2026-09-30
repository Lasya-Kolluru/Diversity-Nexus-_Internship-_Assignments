# ============================================================================== 
# Question: Practice 5 - Product Code Extractor
# Problem statement: Extract country, category, year, and serial from a product code.
# Input: Product code like IND-MOB-2026-001.
# Processing: Use slicing with proper index positions.
# Output: Country, category, year, and serial.
# ============================================================================== 

code = input("Code: ")
country = code[0:3]
category = code[4:7]
year = code[8:12]
serial = code[13:]

print(f"Country: {country}")
print(f"Category: {category}")
print(f"Year: {year}")
print(f"Serial: {serial}")

# ============================================================================== 
# Output / Test Cases:
# Test case 1:
# Input: Code: IND-MOB-2026-001
# Output:
# Country: IND
# Category: MOB
# Year: 2026
# Serial: 001
#
# Test case 2:
# Input: Code: USA-TAB-2025-002
# Output:
# Country: USA
# Category: TAB
# Year: 2025
# Serial: 002
#
# Edge case:
# Input: Code: UK-PC-26-01
# Output will be incorrect if the format does not match the expected slicing.
#
# Explanation:
# Slicing extracts exact portions of the string using start and end index values.
# This is useful when each section of a code follows a predictable pattern.
# ============================================================================== 
