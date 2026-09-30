# ============================================================================== 
# Question: Part C - String Basics Lab
# Problem statement: Explore strings using indexing, slicing, and immutability.
# Input: A sample string "collage".
# Processing: Print length, characters, slices, reverse, error cases.
# Output: String values and error messages.
# ============================================================================== 

name = "collage"
print("Name:", name)                  # collage
print("Length:", len(name))          # 7
print("First character:", name[0])   # c
print("Last character:", name[-1])   # e
print("First 3 letters:", name[0:3])# col
print("Last 3 letters:", name[-3:]) # age
print("Every second character:", name[::2])  # clae
print("Reversed:", name[::-1])      # egalloc

try:
    print(name[10])
except IndexError as error:
    print("IndexError:", error)

try:
    name[0] = "C"
except TypeError as error:
    print("TypeError:", error)

# ============================================================================== 
# Output / Sample results:
# Name: collage
# Length: 7
# First character: c
# Last character: e
# First 3 letters: col
# Last 3 letters: age
# Every second character: clae
# Reversed: egalloc
# IndexError: string index out of range
# TypeError: 'str' object does not support item assignment
#
# Explanation:
# Strings are indexed from 0. name[-1] gives the last character.
# Slicing extracts ranges, and strings are immutable, so direct changes fail.
# ============================================================================== 
