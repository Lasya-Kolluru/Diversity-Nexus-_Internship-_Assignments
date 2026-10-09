"""
Student Module
AI Training - Week 2 Day 4
Author: Lasya Kolluru
"""

class Student:
    """
    Represents a student enrolled in a course with validation and performance tracking.
    """
    def __init__(self, name: str, roll_number: int, marks: float, course: str = "General"):
        if not (0 <= marks <= 100):
            raise ValueError(f"Marks must be between 0 and 100. Received: {marks}")
        
        self.name = name.strip().title()
        self.roll_number = roll_number
        self.marks = marks
        self.course = course.strip()

    def display_details(self) -> None:
        """Displays formatted student details."""
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Course: {self.course}")
        print(f"Marks: {self.marks}")

    def result(self) -> str:
        """Determines academic outcome based on passing threshold (40)."""
        return "Pass" if self.marks >= 40 else "Fail"

    def __repr__(self) -> str:
        return f"Student(name='{self.name}', roll_number={self.roll_number}, marks={self.marks}, course='{self.course}')"
