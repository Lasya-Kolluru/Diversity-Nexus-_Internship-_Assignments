# ============================================================================== 
# Question: Part L - Main Project: Text-Cleaning & Profile Formatter
# Problem statement: Accept messy profile data and turn it into a clean profile.
# Input: Full name, email, phone, city, job role, and short bio.
# Processing: Clean strings, validate email, extract first/last name, and format.
# Output: Professional profile summary with data-quality result.
# ============================================================================== 

print("Enter Profile Details")
full_name = input("Full Name: ").strip().title()
email = input("Email: ").strip().lower()
phone = input("Phone Number: ").strip()
city = input("City: ").strip().title()
job_role = input("Job Role: ").strip().title()
bio = input("Short Bio: ").strip()
bio_length = len(bio)
email_has_at = "@" in email
email_has_domain = email.endswith(".com") or email.endswith(".in")
email_valid = "Yes" if email_has_at and email_has_domain else "No"
space_index = full_name.find(' ')
first_name = full_name[:space_index]
last_name = full_name[space_index + 1:]

print("\n================ PROFILE ================")
print(f"Name       : {full_name}")
print(f"First Name : {first_name}")
print(f"Last Name  : {last_name}")
print(f"Email      : {email}")
print(f"Phone      : {phone}")
print(f"City       : {city}")
print(f"Role       : {job_role}")
print(f"Bio Length : {bio_length} characters")
print("\n------------- DATA QUALITY -------------")
print(f"Email Valid : {email_valid}")
print("=========================================")

# ============================================================================== 
# Output / Sample results:
# Enter Profile Details
# Full Name: lasya kolluru
# Email: LASYA.KOLLURU@GMAIL.COM
# Phone Number: 9876543210
# City: nellore
# Job Role: student
# Short Bio: I am learning Python
#
# ================ PROFILE ================
# Name       : Lasya Kolluru
# First Name : Lasya
# Last Name  : Kolluru
# Email      : lasya.kolluru@gmail.com
# Phone      : 9876543210
# City       : Nellore
# Role       : Student
# Bio Length : 23 characters
#
# ------------- DATA QUALITY -------------
# Email Valid : Yes
# =========================================
#
# Explanation:
# The program strips extra spaces, formats names and cities using title(),
# lowercases the email, checks the email using "@" and endswith(),
# and extracts first/last names with string logic and slicing.
# ============================================================================== 
