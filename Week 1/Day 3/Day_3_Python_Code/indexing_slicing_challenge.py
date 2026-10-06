# ============================================================================== 
# Question: Part E - Indexing & Slicing Challenge
# Problem statement: Work with the string "Artificial Intelligence".
# Input: text = "Artificial Intelligence"
# Processing: Use indexing, slicing, .find(), and .count().
# Output: Extracted parts and character statistics.
# ============================================================================== 

text = "Artificial Intelligence"

print(text[0])
print(text[-1])
print(text[:10])
print(text[11:])
print(text[::-1])
print(text[::2])
print(text[3:13])
print(text.find("i"))
print(text.count("i"))

try:
    print(text[100])
except IndexError as error:
    print("IndexError:", error)

# ============================================================================== 
# Output / Sample results:
# A
# e
# Artificial
# Intelligence
# ecnegilletnI laicifitrA
# Atfca_ nli c
# ificial In
# 3
# 4
# IndexError: string index out of range
#
# Explanation:
# text[0] gives the first character; text[-1] gives the last.
# text[11:] starts from the word "Intelligence". Reversing uses [::-1].
# text[100] fails because the index is outside the valid string range.
# ============================================================================== 
