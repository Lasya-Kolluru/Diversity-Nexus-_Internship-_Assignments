# ==============================================================================
# Question: Part B – Explore Before Coding
# Exercises testing Python types, conversions, and behaviors.
# ==============================================================================

# 1. What does type(variable) tell you?
# A. It tells what kind of data is stored in a variable.

# 2. Create an int, float, str, bool and None value. Check their types.
age = 20
height = 5.5
name = "lasya"
is_student = True
result = None

print(type(age))
print(type(height))
print(type(name))
print(type(is_student))
print(type(result))
# Output:
# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'bool'>
# <class 'NoneType'>

# 3. What happens when you add an int and a float?
# A. Python converts the int into a float automatically (implicit type conversion).
print(age + height)
print(type(age + height))
# Output:
# 25.5
# <class 'float'>

# 4. What happens when you join two strings with +?
# A. The + operator concatenates strings into a single string.
first_name = "Lasya"
last_name = "Kolluru"
print(first_name + last_name)
# Output:
# Lasyakolluru

# 7. Difference between 10 and '10'
a = 10
b = '10'
print(type(a))
print(type(b))
# Output:
# <class 'int'>
# <class 'str'>

# 8. Difference between True and 'True'
A = True
B = 'true'
print(type(A))
print(type(B))
# Output:
# <class 'bool'>
# <class 'str'>

# 9. What does int('25') produce?
x = int('25')
print(type(x))
print(x)
# Output:
# <class 'int'>
# 25

# 10. What does int('25.5') do?
# ValueError: invalid literal for int() with base 10: '25.5'

# 11. What does str(25) produce?
s = str(25)
print(s)
print(type(s))
# Output:
# 25
# <class 'str'>

# 12. What do bool(0), bool(1), bool('') and bool('hello') produce?
print(bool(0))
print(bool(1))
print(bool(''))
print(bool('hello'))
# Output:
# False
# True
# False
# True

# 13. What does None mean?
res = None
print(res)
print(type(res))
# Output:
# None
# <class 'NoneType'>
