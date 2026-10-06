# ==============================================================================
# Question: Part G - Program 8: Bill Splitter
# Problem statement: Ask bill, number of people and tip %. 
#                    Calculate total and per-person amount.
# Input: Bill amount (float), number of people (integer), tip percentage (float)
# Processing / formula: tip = bill * (tip_percent / 100), total = bill + tip, 
#                       per_person = total / people
# Output: Total bill amount and how much each person pays.
# ==============================================================================

bill = float(input("Enter bill amount: "))
people = int(input("Enter number of people: "))
tip_percent = float(input("Enter tip percentage: "))

tip_amount = bill * (tip_percent / 100)
total_amount = bill + tip_amount

print("Total Bill:", total_amount)
print("Amount per person:", total_amount / people)

# ==============================================================================
# Output / Test Cases:
#
# Test case 1: 
# Input:
#   Enter bill amount: 100
#   Enter number of people: 4
#   Enter tip percentage: 10
# Output:
#   Total Bill: 110.0
#   Amount per person: 27.5
#
# Test case 2: 
# Input:
#   Enter bill amount: 200
#   Enter number of people: 2
#   Enter tip percentage: 15
# Output:
#   Total Bill: 230.0
#   Amount per person: 115.0
#
# Error faced and fix: Tip amount was too high. Fixed by dividing the tip percentage by 100 to get a proper decimal.
# One thing learned: Percentages need to be divided by 100 before multiplying in Python math.
# ==============================================================================
