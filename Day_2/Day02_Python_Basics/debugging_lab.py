# ==============================================================================
# Question: Part H – Debugging Lab
# Identify, explain and fix common Python beginner bugs.
# ==============================================================================

print("=== Bug 1: Adding Integer to Input String ===")
# Original Bug:
#   age = input('Enter age: ')
#   print(age + 5)
# Explanation and fix:
#   input() returns the age as a string. We cannot add a string and an integer.
#   So, we use int() to convert the age into an integer.
# Corrected code:
age = int(input("Enter age: "))
print("Age + 5:", age + 5)
# Output Example:
#   Enter age: 20
#   Age + 5: 25


print("\n=== Bug 2: Multiplying Input Strings ===")
# Original Bug:
#   price = input('Price: ')
#   quantity = input('Quantity: ')
#   print(price * quantity)
# Explanation and fix:
#   input() returns string values, so we use int() to convert them into numbers
#   before multiplication.
# Corrected code:
price = int(input("Price: "))
quantity = int(input("Quantity: "))
print("Total Price:", price * quantity)
# Output Example:
#   Price: 50
#   Quantity: 2
#   Total Price: 100


print("\n=== Bug 3: Adding Integer to String Variable ===")
# Original Bug:
#   marks = '90'
#   print(marks + 10)
# Explanation and fix:
#   marks contains '90' as a string, while 10 is an integer. We cannot add
#   two different data types, so we use int(marks) to convert '90' into the
#   integer 90 and then add 10.
# Corrected code:
marks = '90'
print("Marks + 10:", int(marks) + 10)
# Output:
#   Marks + 10: 100


print("\n=== Bug 4: Concatenating String and Float with + ===")
# Original Bug:
#   temperature = float(input('Temperature: '))
#   print('Temperature is ' + temperature)
# Explanation and fix:
#   temperature is a float value, while "Temperature is " is a string.
#   We cannot add different data types using +, so we use a comma in print()
#   or str() to display both values.
# Corrected code:
temperature = float(input("Temperature: "))
print("Temperature is", temperature)
# Output Example:
#   Temperature: 36.6
#   Temperature is 36.6


print("\n=== Bug 5: Concatenating String and Integer with + ===")
# Original Bug:
#   number = int(input('Number: '))
#   print('Number: ' + number)
# Explanation and fix:
#   number is an integer, and "Number: " is a string, so we use a comma or
#   str() to print them together.
# Corrected code:
number = int(input("Number: "))
print("Number:", number)
# Output Example:
#   Number: 7
#   Number: 7


print("\n=== Bug 6: Converting Int to Float ===")
# Question:
#   value = int(input('Number: '))
#   print(float(value))
# Does this work? Explain why.
# Explanation:
#   input() takes a number from the user. int() converts it into an integer,
#   and float() converts the integer into a float. This works properly.
# Code:
value = int(input("Number: "))
print("As Float:", float(value))
# Output Example:
#   Number: 15
#   As Float: 15.0
