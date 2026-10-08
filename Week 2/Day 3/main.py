"""
AI TRAINING – WEEK 2 DAY 3
Demonstration of Reusable Python Modules and Utility Functions
Author: Lasya Kolluru
"""

from utils import clean_name, calculate_average, is_valid_email

def main():
    print("Testing clean_name:")
    print("Input: '   yasaswini   ' -> Result:", clean_name("   yasaswini   "))

    print("\nTesting calculate_average:")
    scores = [80, 90, 100]
    print(f"Input: {scores} -> Result:", calculate_average(scores))

    print("\nTesting is_valid_email:")
    email1 = "yasaswini@gmail.com"
    email2 = "bad-email.com"
    print(f"Is '{email1}' valid? ->", is_valid_email(email1))
    print(f"Is '{email2}' valid? ->", is_valid_email(email2))

if __name__ == "__main__":
    main()
