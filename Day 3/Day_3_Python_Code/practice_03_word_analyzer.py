# ============================================================================== 
# Question: Practice 3 - Word Analyzer
# Problem statement: Analyze a sentence without loops.
# Input: A sentence entered by the user.
# Processing: len(), indexing, count(), and vowel totals.
# Output: Length, first letter, last letter, spaces, and vowels.
# ============================================================================== 

text = input("Sentence: ")
text_lower = text.lower()
vowels = (
    text_lower.count("a") +
    text_lower.count("e") +
    text_lower.count("i") +
    text_lower.count("o") +
    text_lower.count("u")
)

print(f"Length: {len(text)}")
print(f"First: {text[0]}")
print(f"Last: {text[-1]}")
print(f"Spaces: {text.count(' ')}")
print(f"Vowels: {vowels}")

# ============================================================================== 
# Output / Test Cases:
# Test case 1:
# Input: Sentence: Hello World
# Output:
# Length: 11
# First: H
# Last: d
# Spaces: 1
# Vowels: 3
#
# Test case 2:
# Input: Sentence: Python
# Output:
# Length: 6
# First: P
# Last: n
# Spaces: 0
# Vowels: 1
#
# Edge case:
# Input: Sentence: a
# Output:
# Length: 1
# First: a
# Last: a
# Spaces: 0
# Vowels: 1
#
# Explanation:
# len() counts total characters, text[0] gets the first character,
# text[-1] gets the last character, count(" ") finds spaces,
# and the vowel count adds the number of vowels in the sentence.
# ============================================================================== 
