"""
AI TRAINING - WEEK 2
DAY 4 ASSIGNMENT: OOP Basics: Classes, Objects, Constructors, Methods & Inheritance
Plan -> Create Classes -> Use Objects -> Reuse Code

Author: Lasya Kolluru
GitHub: Lasya-Kolluru
Deliverable: oop_practice_Lasya_Kolluru.py
"""

# ==============================================================================
# PART A - CLASS AND OBJECT BASICS
# ==============================================================================
print("=" * 70)
print("PART A - CLASS AND OBJECT BASICS")
print("=" * 70)

class StudentBasic:
    """Class representing a student with a constructor."""
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

# Create two student objects
student1 = StudentBasic("Rahul", 21)
student2 = StudentBasic("Priya", 22)

print(f"Student 1 Initial: {student1.name}, Age: {student1.age}")
print(f"Student 2 Initial: {student2.name}, Age: {student2.age}")

# Mutating student1's name
student1.name = "Lasya"
print("\nAfter updating Student 1's name to 'Lasya':")
print(f"Student 1: {student1.name}, Age: {student1.age}")
print(f"Student 2: {student2.name}, Age: {student2.age}")
print("-> Observation: Mutating student1 does not affect student2 because they are distinct instances with separate memory allocations.")


# ==============================================================================
# PART B - CONSTRUCTORS AND ATTRIBUTES
# ==============================================================================
print("\n" + "=" * 70)
print("PART B - CONSTRUCTORS AND ATTRIBUTES")
print("=" * 70)

class Mobile:
    """Class representing a mobile phone device."""
    def __init__(self, brand: str, model: str, price: float):
        self.brand = brand
        self.model = model
        self.price = price

# Creating three Mobile objects
phone1 = Mobile("Samsung", "A55", 35000)
phone2 = Mobile("Apple", "iPhone 15", 65000)
phone3 = Mobile("Vivo", "V27", 30000)

print(f"Mobile 1: {phone1.brand} {phone1.model} | Price: Rs. {phone1.price:,.2f}")
print(f"Mobile 2: {phone2.brand} {phone2.model} | Price: Rs. {phone2.price:,.2f}")
print(f"Mobile 3: {phone3.brand} {phone3.model} | Price: Rs. {phone3.price:,.2f}")

# Adding dynamic attribute storage
phone1.storage = "128GB"
print(f"\nPhone 1 Dynamic Storage: {phone1.storage}")

# Modifying price
phone1.price = 36000
print(f"Updated Samsung Price: Rs. {phone1.price:,.2f}")

# Error handling: Missing required positional argument
print("\nTesting missing constructor parameter error:")
try:
    phone4 = Mobile("Samsung", "S24")
except TypeError as e:
    print(f"Caught TypeError: {e}")
    print("-> Reason: The __init__ method requires 3 arguments (brand, model, price). Omitting price violates the signature.")


# ==============================================================================
# PART C - METHODS (INSTANCE METHODS & STATE MUTATION)
# ==============================================================================
print("\n" + "=" * 70)
print("PART C - METHODS & ENCAPSULATED OPERATIONS")
print("=" * 70)

class BankAccount:
    """Class modeling a bank account with deposit, withdraw, and balance checking."""
    def __init__(self, account_holder: str, balance: float = 0.0):
        self.account_holder = account_holder
        self.balance = max(0.0, float(balance))

    def display_balance(self) -> None:
        """Displays current account status."""
        print(f"Account Holder: {self.account_holder} | Current Balance: Rs. {self.balance:,.2f}")

    def deposit(self, amount: float) -> None:
        """Deposits funds into the account with positive value validation."""
        if amount <= 0:
            print(f"[FAIL] Deposit Failed: Deposit amount must be positive. (Attempted: Rs. {amount})")
            return
        self.balance += amount
        print(f"[SUCCESS] Deposit Successful: Rs. {amount:,.2f} deposited.")

    def withdraw(self, amount: float) -> None:
        """Withdraws funds if positive and sufficient funds are available."""
        if amount <= 0:
            print(f"[FAIL] Withdrawal Failed: Withdrawal amount must be positive. (Attempted: Rs. {amount})")
            return
        if amount > self.balance:
            print(f"[FAIL] Withdrawal Failed: Insufficient funds. (Requested: Rs. {amount:,.2f}, Available: Rs. {self.balance:,.2f})")
            return
        self.balance -= amount
        print(f"[SUCCESS] Withdrawal Successful: Rs. {amount:,.2f} dispensed.")

# Testing BankAccount operations
account = BankAccount("Rahul", 1000)
account.display_balance()

print("\n-- Transaction Flow --")
account.deposit(-200)   # Invalid negative deposit
account.deposit(500)    # Valid deposit
account.display_balance()

account.withdraw(2000)  # Overdraw attempt
account.withdraw(300)   # Valid withdrawal
account.display_balance()


# ==============================================================================
# PART D - METHODS THAT RETURN VALUES
# ==============================================================================
print("\n" + "=" * 70)
print("PART D - METHODS THAT RETURN VALUES")
print("=" * 70)

class Rectangle:
    """Class representing a geometric rectangle with calculated properties."""
    def __init__(self, length: float, width: float):
        self.length = float(length)
        self.width = float(width)

    def area(self) -> float:
        """Calculates and returns rectangle area."""
        return self.length * self.width

    def perimeter(self) -> float:
        """Calculates and returns rectangle perimeter."""
        return 2 * (self.length + self.width)

r1 = Rectangle(5, 4)
r2 = Rectangle(10, 12)

print(f"Rectangle 1 (5 x 4): Area = {r1.area():.2f}, Perimeter = {r1.perimeter():.2f}")
print(f"Rectangle 2 (10 x 12): Area = {r2.area():.2f}, Perimeter = {r2.perimeter():.2f}")


# ==============================================================================
# PART E - INHERITANCE OVERVIEW
# ==============================================================================
print("\n" + "=" * 70)
print("PART E - INHERITANCE (PARENT & CHILD CLASSES)")
print("=" * 70)

class Person:
    """Parent base class representing an individual."""
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def introduce(self) -> None:
        """Displays common introduction."""
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

class Employee(Person):
    """Child class inheriting from Person, adding employee_id."""
    def __init__(self, name: str, age: int, employee_id: str):
        super().__init__(name, age)
        self.employee_id = employee_id

    def show_employee_id(self) -> None:
        """Displays employee ID."""
        print(f"Employee ID: {self.employee_id}")

class Trainer(Person):
    """Child class inheriting from Person, adding subject."""
    def __init__(self, name: str, age: int, subject: str):
        super().__init__(name, age)
        self.subject = subject

    def show_subject(self) -> None:
        """Displays specialization subject."""
        print(f"Training Specialization: {self.subject}")

# Instantiating child class objects
employee = Employee("Ananya", 23, "E101")
employee.introduce()
employee.show_employee_id()

print()
trainer = Trainer("Rahul", 30, "Python AI & ML")
trainer.introduce()
trainer.show_subject()

# Testing calling child-specific method from parent object
print("\nTesting calling child method on parent object:")
person = Person("Priya", 25)
try:
    person.show_employee_id()
except AttributeError as e:
    print(f"Caught AttributeError: {e}")
    print("-> Reason: Inheritance is strictly top-down (parent -> child). The parent Person class does not know about Employee's methods.")


# ==============================================================================
# PART G - QUICK DEBUGGING LABS
# ==============================================================================
print("\n" + "=" * 70)
print("PART G - QUICK DEBUGGING EXERCISES")
print("=" * 70)

# Debugging 1: Fix self attribute assignment
class FixedStudent:
    def __init__(self, name):
        self.name = name  # Fixed: attached name to instance self

s = FixedStudent("Rahul")
print(f"Debug 1 Fixed: {s.name}")

# Debugging 2: Fix missing constructor argument
class FixedCar:
    def __init__(self, brand):
        self.brand = brand

c = FixedCar("Toyota")  # Fixed: provided required argument
print(f"Debug 2 Fixed: {c.brand}")

# Debugging 3: Fix missing self in instance method
class FixedCalculator:
    def add(self, a, b):  # Fixed: added self parameter
        return a + b

calc = FixedCalculator()
print(f"Debug 3 Fixed: 5 + 3 = {calc.add(5, 3)}")

# Debugging 4: Fix inheritance hierarchy
class Animal:
    def speak(self):
        print("Animal sound")

class FixedDog(Animal):  # Fixed: inherited from Animal
    def bark(self):
        print("Woof")

d = FixedDog()
print("Debug 4 Fixed:")
d.speak()
d.bark()


# ==============================================================================
# PART H - MAIN HANDS-ON ACTIVITY: STUDENT RECORD SYSTEM
# ==============================================================================
print("\n" + "=" * 70)
print("PART H - MAIN HANDS-ON ACTIVITY: STUDENT RECORD SYSTEM")
print("=" * 70)

class RecordStudent:
    """Represents a student record with validation and grade evaluation."""
    def __init__(self, name: str, roll_number: int, marks: float):
        if not (0 <= marks <= 100):
            raise ValueError(f"Marks must be between 0 and 100. Received: {marks}")
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_details(self) -> None:
        """Prints formatted student information."""
        print(f"Name: {self.name:<10} | Roll No: {self.roll_number:<3} | Marks: {self.marks:<5.1f} | Result: {self.result()}")

    def result(self) -> str:
        """Returns Pass if marks >= 40, otherwise Fail."""
        return "Pass" if self.marks >= 40 else "Fail"

class GraduateStudent(RecordStudent):
    """Child class extending RecordStudent with specialization."""
    def __init__(self, name: str, roll_number: int, marks: float, specialization: str):
        super().__init__(name, roll_number, marks)
        self.specialization = specialization

    def display_details(self) -> None:
        super().display_details()
        print(f"  +-- Specialization: {self.specialization}")

# 1. Create list of students
student_roster = [
    RecordStudent("Rahul", 1, 85),
    RecordStudent("Priya", 2, 92),
    RecordStudent("Arjun", 3, 38),
    RecordStudent("Ananya", 4, 76)
]

print("--- Class Student Roster ---")
for student in student_roster:
    student.display_details()

# 2. Find Highest Scorer
def find_highest_scorer(students: list[RecordStudent]) -> RecordStudent:
    return max(students, key=lambda s: s.marks)

topper = find_highest_scorer(student_roster)
print("\n--- Top Scorer Analysis ---")
print(f"Highest Scorer : {topper.name}")
print(f"Highest Marks  : {topper.marks}")
print(f"Roll Number    : {topper.roll_number}")

# 3. Test Invalid Marks Validation
print("\n--- Testing Invalid Marks Validation ---")
try:
    invalid_s = RecordStudent("Ravi", 5, 120)
except ValueError as e:
    print(f"Validation Caught: {e}")

# 4. Test GraduateStudent
print("\n--- Testing Graduate Student Record ---")
grad = GraduateStudent("Kiran", 6, 88, "Artificial Intelligence")
grad.display_details()

print("\n" + "=" * 70)
print("[SUCCESS] ALL OOP DEMONSTRATIONS COMPLETED SUCCESSFULLY!")
print("=" * 70)
