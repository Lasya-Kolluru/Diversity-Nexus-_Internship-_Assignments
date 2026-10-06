# ==============================================================================
# Question: Part K - Movie Ticket Pricing
# Problem statement: Set a ticket price using age, seat, day, and membership.
# Input: Age, day type, seat type, and membership status.
# Processing: Validate inputs, then apply age and nested VIP discount rules.
# Output: Ticket category and price, or an input error.
# ==============================================================================

customer_name = "Lasya-Kolluru"

try:
    age = int(input("Enter age: "))
except ValueError:
    print("Invalid age! Enter a whole number from 0 to 120.")
else:
    day_type = input("Enter day type (weekday/weekend): ").strip().lower()
    seat_type = input("Enter seat type (standard/vip): ").strip().lower()
    has_membership = input("Membership? (yes/no): ").strip().lower()

    if age < 0 or age > 120:
        print(f"Hello {customer_name}, invalid age entered! Please try again.")
    elif day_type not in ("weekday", "weekend"):
        print("Invalid day type! Enter weekday or weekend.")
    elif seat_type not in ("standard", "vip"):
        print("Invalid seat type! Enter standard or vip.")
    elif has_membership not in ("yes", "no"):
        print("Invalid membership answer! Enter yes or no.")
    elif age <= 12:
        print(f"Hello {customer_name}, Child ticket. Price: Rs 100")
    elif age >= 60:
        print(f"Hello {customer_name}, Senior ticket. Price: Rs 150")
    else:
        if seat_type == "vip":
            if has_membership == "yes" and day_type == "weekday":
                print(f"Hello {customer_name}, VIP member weekday discount. Price: Rs 300")
            else:
                print(f"Hello {customer_name}, Full VIP ticket. Price: Rs 400")
        else:
            print(f"Hello {customer_name}, Standard adult ticket. Price: Rs 200")

# ==============================================================================
# Output / Sample runs (each test is a separate program run):
# Age 25, weekend, standard, no membership:
# Hello Lasya-Kolluru, Standard adult ticket. Price: Rs 200
#
# Age 12, weekday, standard, no membership:
# Hello Lasya-Kolluru, Child ticket. Price: Rs 100
#
# Age 60, weekend, vip, yes membership:
# Hello Lasya-Kolluru, Senior ticket. Price: Rs 150
#
# Age 30, weekday, vip, yes membership:
# Hello Lasya-Kolluru, VIP member weekday discount. Price: Rs 300
#
# Age 30, weekend, vip, yes membership:
# Hello Lasya-Kolluru, Full VIP ticket. Price: Rs 400
#
# Age -5, weekday, standard, no membership:
# Hello Lasya-Kolluru, invalid age entered! Please try again.
# ==============================================================================