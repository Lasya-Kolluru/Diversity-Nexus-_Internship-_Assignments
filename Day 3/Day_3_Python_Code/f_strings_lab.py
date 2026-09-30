# ============================================================================== 
# Question: Part F - f-Strings
# Problem statement: Use f-strings to display dynamic values clearly.
# Input: Name, age, city, product details, and numeric values.
# Processing: Create formatted output using f-strings.
# Output: Human-readable sentences and bills.
# ============================================================================== 

# Example 1: Personal details
name = "Lasya"
age = 20
city = "Nellore"
print(f"My name is {name}, I am {age} years old, and I live in {city}.")

# Example 2: Product bill
product = "Pen"
price = 20
quantity = 3
total = price * quantity
print(f"Product: {product}")
print(f"Price: ₹{price}")
print(f"Quantity: {quantity}")
print(f"Total: ₹{total}")

# Example 3: Student marks
student_name = "Lasya"
total_marks = 450
average = 90
print(f"Student Name: {student_name}")
print(f"Total Marks: {total_marks}")
print(f"Average: {average}")

# Example 4: Calculation result
a = 15
b = 5
result = a + b
print(f"{a} + {b} = {result}")

# Example 5: Fixed decimal output
price_value = 20.2
print(f"Price: {price_value:.2f}")

# ============================================================================== 
# Output / Sample results:
# My name is Lasya, I am 20 years old, and I live in Nellore.
# Product: Pen
# Price: ₹20
# Quantity: 3
# Total: ₹60
# Student Name: Lasya
# Total Marks: 450
# Average: 90
# 15 + 5 = 20
# Price: 20.20
# ============================================================================== 
