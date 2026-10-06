# ============================================================================== 
# Question: Part D - String Methods Lab
# Problem statement: Explore key string methods and explain their purpose.
# Input: Example strings.
# Processing: Apply methods like lower(), upper(), strip(), replace(), etc.
# Output: Result of each method.
# ============================================================================== 

print("lower():", "LASYA".lower())
print("upper():", "lasya".upper())
print("title():", "introduction".title())
print("strip():", "  hello  ".strip())
print("replace():", "i like html".replace("html", "python"))
print("split():", "I am Lasya".split())
print("join():", " ".join(["I", "am", "Lasya"]))
print("startswith():", "Python".startswith("Py"))
print("endswith():", "python".endswith("on"))
print("find():", "I like Python".find("Python"))
print("count():", "collage".count("a"))

# ============================================================================== 
# Output / Sample results:
# lower(): lasya
# upper(): LASYA
# title(): Introduction
# strip(): hello
# replace(): i like python
# split(): ['I', 'am', 'Lasya']
# join(): I am Lasya
# startswith(): True
# endswith(): True
# find(): 7
# count(): 2
#
# Explanation:
# lower() converts to lowercase, upper() converts to uppercase,
# title() capitalizes words, strip() removes extra spaces,
# replace() swaps text, split() breaks a sentence into pieces,
# join() combines pieces into one string, and count() finds occurrences.
# ============================================================================== 
