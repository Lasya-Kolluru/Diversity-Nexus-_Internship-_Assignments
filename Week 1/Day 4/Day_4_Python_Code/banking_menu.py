# ==============================================================================
# Question: Part H3 - Simple Banking Menu
# Problem statement: Check balance, deposit, withdraw, or exit.
# Input: A menu choice and, when needed, a transaction amount.
# Processing: Select a menu branch and validate the transaction.
# Output: The selected result and updated balance when applicable.
# ==============================================================================

account_name = "Lasya-Kolluru"
balance = 5000

print(f"Welcome to Simple Bank, {account_name}!")
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")
choice = input("Enter your choice (1-4): ").strip()

if choice == "1":
    print(f"Your current balance is: Rs {balance}")
elif choice == "2":
    try:
        deposit_amount = int(input("Enter amount to deposit: "))
    except ValueError:
        print("Invalid amount! Enter a positive whole number.")
    else:
        if deposit_amount <= 0:
            print("Invalid amount! Deposit must be greater than zero.")
        else:
            balance += deposit_amount
            print(f"Deposit successful. Your new balance is: Rs {balance}")
elif choice == "3":
    try:
        withdraw_amount = int(input("Enter amount to withdraw: "))
    except ValueError:
        print("Invalid amount! Enter a positive whole number.")
    else:
        if withdraw_amount <= 0:
            print("Invalid amount! Withdrawal must be greater than zero.")
        else:
            if withdraw_amount <= balance:
                balance -= withdraw_amount
                print(f"Withdrawal successful. Your new balance is: Rs {balance}")
            else:
                print(f"Transaction failed! Insufficient balance. Balance: Rs {balance}")
elif choice == "4":
    print(f"Thank you for using Simple Bank, {account_name}. Goodbye!")
else:
    print("Invalid choice! Please select an option from 1 to 4.")

# ==============================================================================
# Output / Sample runs (each test is a separate program run):
# Choice 1: Your current balance is: Rs 5000
#
# Choice 2, deposit 2000: Deposit successful. Your new balance is: Rs 7000
#
# Choice 3, withdraw 1000: Withdrawal successful. Your new balance is: Rs 4000
#
# Choice 3, withdraw 8000: Transaction failed! Insufficient balance. Balance: Rs 5000
#
# Choice 4: Thank you for using Simple Bank, Lasya-Kolluru. Goodbye!
#
# Choice 7: Invalid choice! Please select an option from 1 to 4.
# ==============================================================================