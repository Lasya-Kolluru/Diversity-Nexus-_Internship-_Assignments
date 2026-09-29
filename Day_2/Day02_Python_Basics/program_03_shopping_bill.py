# ==============================================================================
# Question: Part G - Program 3: Shopping Bill
# Problem statement: Ask item name, quantity and price. Calculate total.
# Input: Item name (string), Quantity (integer), Price (float)
# Processing / formula: Total = Quantity * Price
# Output: Item name and total bill amount.
# ==============================================================================

item_name = input("Enter item name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price per item: "))

total = quantity * price

print("Item:", item_name)
print("Total Bill:", total)

# ==============================================================================
# Output / Test Cases:
#
# Test case 1: 
# Input:
#   Enter item name: Apple
#   Enter quantity: 5
#   Enter price per item: 1.5
# Output:
#   Item: Apple
#   Total Bill: 7.5
#
# Test case 2: 
# Input:
#   Enter item name: Book
#   Enter quantity: 2
#   Enter price per item: 15.0
# Output:
#   Item: Book
#   Total Bill: 30.0
#
# Error faced and fix: No Errors faced.
# One thing learned: Multiplying an integer and a float always gives a float.
# ==============================================================================
