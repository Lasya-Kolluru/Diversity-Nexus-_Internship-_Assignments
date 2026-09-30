# ==============================================================================
# Question: Part G - Program 4: Temperature Converter
# Problem statement: Ask Celsius and convert to Fahrenheit.
# Input: Temperature in Celsius (float)
# Processing / formula: Fahrenheit = (Celsius * 9/5) + 32
# Output: The temperature in Fahrenheit.
# ==============================================================================

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit:", fahrenheit)

# ==============================================================================
# Output / Test Cases:
#
# Test case 1: 
# Input:
#   Enter temperature in Celsius: 0
# Output:
#   Temperature in Fahrenheit: 32.0
#
# Test case 2: 
# Input:
#   Enter temperature in Celsius: 30
# Output:
#   Temperature in Fahrenheit: 86.0
#
# Error faced and fix: The math calculation was confusing. Fixed by adding brackets around (celsius * 9/5) to make it clear.
# One thing learned: Python follows standard math rules (BODMAS) for calculations.
# ==============================================================================
