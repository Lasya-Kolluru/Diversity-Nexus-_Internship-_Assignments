"""
AI TRAINING – DAY 6 ASSIGNMENT
Module Name: day_06_utility_module.py
Student Name: Lasya Kolluru
Description: A reusable function-based utility module demonstrating core Python function concepts:
             - Refactored loops
             - Normal parameters and return values
             - Default arguments
             - *args and **kwargs
             - Input validation and math utilities
"""


# 1. Refactored Day 5 Loop / Logic: Even or Odd Checker
def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0


# 2. Refactored Day 5 Loop: Prime Number Checker
def is_prime(number):
    """Check if a number is a prime number."""
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


# 3. Refactored Day 5 Loop: Palindrome Checker
def is_palindrome(value):
    """Check if a number or string reads the same backwards."""
    word = str(value)
    return word == word[::-1]


# 4. Refactored Day 5 Loop: Find Factors
def find_factors(number):
    """Return a list of all factors of a given number."""
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


# 5. Input Validation: Calculate Student Grade
def calculate_grade(marks):
    """Return letter grade based on marks with validation."""
    if marks < 0 or marks > 100:
        return "Invalid marks"
    elif marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"


# 6. Default Argument 1: Shopping Total Calculator
def calculate_total(price, quantity=1):
    """Calculate total price with a default quantity of 1."""
    return price * quantity


# 7. Default Argument 2: Greeting Utility
def greet_user(name, greeting="Welcome"):
    """Greet a user with a customizable or default greeting."""
    return f"{greeting} {name}"


# 8. Math Utility: Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    """Convert Celsius temperature to Fahrenheit."""
    return (celsius * 9 / 5) + 32


# 9. *args Function: Flexible Sum Calculator
def calculate_sum(*numbers):
    """Calculate the sum of any number of numerical arguments."""
    return sum(numbers)


# 10. **kwargs Function: Dynamic Profile Builder
def build_profile(**details):
    """Build and return a profile dictionary from keyword arguments."""
    return details


if __name__ == "__main__":
    print("--- Testing day_06_utility_module.py ---")
    print("is_even(10):", is_even(10))
    print("is_prime(17):", is_prime(17))
    print("is_palindrome(121):", is_palindrome(121))
    print("find_factors(12):", find_factors(12))
    print("calculate_grade(82):", calculate_grade(82))
    print("calculate_grade(105):", calculate_grade(105))
    print("calculate_total(50):", calculate_total(50))
    print("calculate_total(50, 3):", calculate_total(50, 3))
    print("greet_user('Lasya'):", greet_user("Lasya"))
    print("greet_user('Lasya', 'Hello'):", greet_user("Lasya", "Hello"))
    print("celsius_to_fahrenheit(0):", celsius_to_fahrenheit(0))
    print("calculate_sum(10, 20, 30, 40):", calculate_sum(10, 20, 30, 40))
    print("build_profile:", build_profile(name="Lasya", role="Student", age=21))
