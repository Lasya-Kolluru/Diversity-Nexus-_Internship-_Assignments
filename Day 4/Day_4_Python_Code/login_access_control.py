# ==============================================================================
# Question: Part J - Nested Login and Access Control
# Problem statement: Check a username, password, then standard/admin access.
# Input: Username, password, and (after valid credentials) admin status.
# Processing: Use nested conditions so each decision depends on the previous one.
# Output: Separate success and failure messages.
# ==============================================================================

correct_username = "Lasya-Kolluru"
demo_password = "python123"  # Practice only; never use hardcoded passwords in real accounts.

username = input("Enter username: ").strip()
password = input("Enter password: ")

if username == correct_username:
    if password == demo_password:
        admin_answer = input("Are you an admin? (yes/no): ").strip().lower()
        if admin_answer == "yes":
            print(f"Login successful! Welcome Admin {username}. You have full system controls.")
        elif admin_answer == "no":
            print(f"Login successful! Welcome User {username}. You have standard access.")
        else:
            print("Invalid admin answer! Enter yes or no.")
    else:
        print(f"Login failed! Incorrect password for user {username}.")
else:
    print(f"Login failed! Username '{username}' not found in our system.")

# ==============================================================================
# Output / Sample runs (each test is a separate program run):
# Username Lasya-Kolluru, password python123, admin yes:
# Login successful! Welcome Admin Lasya-Kolluru. You have full system controls.
#
# Username Lasya-Kolluru, password python123, admin no:
# Login successful! Welcome User Lasya-Kolluru. You have standard access.
#
# Username Lasya-Kolluru, wrong password:
# Login failed! Incorrect password for user Lasya-Kolluru.
#
# Username someone-else, any password:
# Login failed! Username 'someone-else' not found in our system.
#
# Username Lasya-Kolluru, password python123, admin maybe:
# Invalid admin answer! Enter yes or no.
# ==============================================================================