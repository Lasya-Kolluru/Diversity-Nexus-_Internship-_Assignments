# ============================================================================== 
# Question: Part A - Operators Exploration
# Problem statement: Experiment with arithmetic, comparison, logical, assignment,
# and membership operators. Use at least 2 examples for each group.
# Input: Numeric values and strings for demonstration.
# Processing: Apply operators to variables and compare values.
# Output: Result of each operation.
# ============================================================================== 

# Arithmetic operators
print("Arithmetic operators")
a = 5
b = 4
print(a + b)   # 9
print(a - b)   # 1
print(a * b)   # 20
print(a / b)   # 1.25
print(a // b)  # 1
print(a % b)   # 1
print(a ** b)  # 625

# Comparison operators
print("\nComparison operators")
x = 8
y = 3
print(x > y)   # True
print(x < y)   # False
print(x == y)  # False
print(x != y)  # True

# Logical operators
print("\nLogical operators")
print(10 > 5 and 3 < 5)   # True
print(10 > 5 or 3 > 5)    # True
print(not (10 > 5))       # False

# Assignment operators
print("\nAssignment operators")
value = 10
value += 5
print(value)   # 15
value *= 2
print(value)   # 30

# Membership operators
print("\nMembership operators")
name = "Lasya"
print("L" in name)      # True
print("O" not in name)  # True

# ============================================================================== 
# Output / Sample results:
# Arithmetic operators
# 9
# 1
# 20
# 1.25
# 1
# 1
# 625
#
# Comparison operators
# True
# False
# False
# True
#
# Logical operators
# True
# True
# False
#
# Assignment operators
# 15
# 30
#
# Membership operators
# True
# True
# ============================================================================== 
