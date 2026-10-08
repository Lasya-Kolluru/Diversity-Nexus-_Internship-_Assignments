"""
Utility Module for Data Processing and Validation
Diversity Nexus Internship - Week 2 Day 3
Author: Lasya Kolluru
"""

def clean_name(name: str) -> str:
    """
    Strips leading and trailing whitespace and converts string to Title Case.
    """
    if not isinstance(name, str):
        return ""
    return name.strip().title()


def calculate_average(numbers: list) -> float:
    """
    Calculates the arithmetic average of a list of numbers.
    Handles empty lists safely to prevent ZeroDivisionError.
    """
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def is_valid_email(email: str) -> bool:
    """
    Validates if the provided email contains '@' and '.' with basic structural checks.
    """
    if not isinstance(email, str):
        return False
    email = email.strip()
    if "@" in email and "." in email:
        parts = email.split("@")
        if len(parts) == 2 and parts[0] and "." in parts[1]:
            domain_parts = parts[1].split(".")
            return len(domain_parts) >= 2 and all(part for part in domain_parts)
    return False


def clean_record(record: dict) -> dict | None:
    """
    Validates and cleans a student record.
    Returns cleaned dictionary if valid, None if invalid or missing required fields.
    """
    try:
        name = record.get("name", "").strip().title()
        city = record.get("city", "").strip().title()

        if not name or not city:
            return None

        age = int(record.get("age"))
        marks = int(record.get("marks"))

        if age <= 0 or marks < 0 or marks > 100:
            return None

        return {
            "name": name,
            "age": age,
            "marks": marks,
            "city": city
        }
    except (ValueError, TypeError, KeyError, AttributeError):
        return None
