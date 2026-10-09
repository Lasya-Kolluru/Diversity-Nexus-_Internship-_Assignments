"""
Main Driver Program
AI Training - Week 2 Day 4: Modular Student Record System
Author: Lasya Kolluru
"""

from student import Student

class GraduateStudent(Student):
    """
    Child class inheriting from Student, introducing specialization attribute.
    """
    def __init__(self, name: str, roll_number: int, marks: float, specialization: str, course: str = "Postgraduate"):
        super().__init__(name, roll_number, marks, course)
        self.specialization = specialization.strip()

    def display_details(self) -> None:
        """Overrides parent display_details to include specialization."""
        super().display_details()
        print(f"Specialization: {self.specialization}")


def find_highest_scorer(students: list[Student]) -> Student:
    """Finds and returns the student object with the highest marks."""
    if not students:
        raise ValueError("Student list cannot be empty.")
    return max(students, key=lambda s: s.marks)


def main():
    print("=" * 60)
    print("STUDENT RECORD SYSTEM (MODULAR EXECUTION)")
    print("=" * 60)

    # 1. Create a collection of student objects
    students = [
        Student("Rahul", 1, 85, "Python"),
        Student("Priya", 2, 92, "Cyber Security"),
        Student("Arjun", 3, 38, "Data Science"),
        Student("Ananya", 4, 76, "Artificial Intelligence")
    ]

    # 2. Iterate and display student details and results
    print("\n--- Student Roster & Academic Status ---")
    for s in students:
        s.display_details()
        print(f"Result: {s.result()}")
        print("-" * 35)

    # 3. Find and display top performer
    topper = find_highest_scorer(students)
    print("\nTop Academic Performer:")
    print(f"Name: {topper.name}")
    print(f"Roll Number: {topper.roll_number}")
    print(f"Marks: {topper.marks}")
    print(f"Course: {topper.course}")

    # 4. Demonstrate boundary validation error handling
    print("\n--- Testing Input Validation ---")
    try:
        invalid_student = Student("Ravi", 5, 120, "Cloud Computing")
    except ValueError as err:
        print(f"Caught Expected Error: {err}")

    # 5. Demonstrate GraduateStudent Inheritance
    print("\n--- Testing GraduateStudent (Inheritance) ---")
    grad_student = GraduateStudent("Kiran", 6, 88, "Deep Learning & NLP", "M.Tech AI")
    grad_student.display_details()
    print(f"Result: {grad_student.result()}")

    print("\n" + "=" * 60)
    print("[SUCCESS] System Execution Completed Successfully.")
    print("=" * 60)


if __name__ == "__main__":
    main()
