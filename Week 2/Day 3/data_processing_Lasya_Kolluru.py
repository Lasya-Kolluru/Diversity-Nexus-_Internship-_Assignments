"""
AI TRAINING – WEEK 2
DAY 3 DELIVERABLE: Data Processing Script
Topic: File I/O, CSV, JSON, Exceptions, Modules & Packages
Read → Clean → Handle Errors → Export

Author: Lasya Kolluru
GitHub: Lasya-Kolluru
"""

import csv
import os

def read_csv(filename: str) -> list[dict]:
    """
    Reads a CSV file safely using DictReader and returns a list of row dictionaries.
    Handles FileNotFoundError gracefully.
    """
    if not os.path.exists(filename):
        print(f"Error: Input file '{filename}' not found.")
        return []
    
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def clean_record(record: dict) -> dict | None:
    """
    Cleans and validates a single student record.
    - Strips whitespace and applies Title Case to name and city.
    - Rejects records with empty name or city.
    - Safely converts age and marks to integers using try/except.
    - Returns cleaned dict if valid, or None if invalid.
    """
    try:
        raw_name = record.get("name", "")
        raw_city = record.get("city", "")

        name = raw_name.strip().title() if raw_name else ""
        city = raw_city.strip().title() if raw_city else ""

        # Validate mandatory string fields
        if not name or not city:
            return None

        # Safely convert and validate numeric fields
        age = int(record.get("age"))
        marks = int(record.get("marks"))

        # Boundary validation
        if age <= 0 or marks < 0 or marks > 100:
            return None

        return {
            "name": name,
            "age": age,
            "marks": marks,
            "city": city
        }
    except (ValueError, TypeError, KeyError):
        return None


def process_records(records: list[dict]) -> tuple[list[dict], list[dict]]:
    """
    Iterates through raw records and separates them into valid and invalid lists.
    """
    valid_records = []
    invalid_records = []

    for record in records:
        cleaned = clean_record(record.copy())
        if cleaned is not None:
            valid_records.append(cleaned)
        else:
            invalid_records.append(record)

    return valid_records, invalid_records


def export_csv(filename: str, records: list[dict]):
    """
    Exports a list of dictionary records to a CSV file.
    """
    if not records:
        print(f"Warning: No records to export for '{filename}'.")
        return

    fieldnames = list(records[0].keys())
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)
    print(f"Successfully exported {len(records)} records to '{filename}'.")


def main():
    print("=" * 60)
    print("AI TRAINING – WEEK 2 DAY 3: DATA PROCESSING PIPELINE")
    print("=" * 60)

    input_filename = "students.csv"
    cleaned_output = "cleaned_students.csv"
    error_output = "errors.csv"

    # Step 1: Create a sample raw CSV if it doesn't already exist or ensure messy sample data
    raw_sample_data = [
        {"name": "Rahul", "age": "21", "marks": "85", "city": "Hyderabad"},
        {"name": "Priya", "age": "22", "marks": "92", "city": "Bangalore"},
        {"name": "", "age": "20", "marks": "75", "city": "Chennai"},
        {"name": "Arjun", "age": "abc", "marks": "80", "city": "Chennai"},
        {"name": "Sneha", "age": "21", "marks": "95", "city": ""},
        {"name": "Kiran", "age": "20", "marks": "88", "city": "Hyderabad"}
    ]

    with open(input_filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age", "marks", "city"])
        writer.writeheader()
        writer.writerows(raw_sample_data)
    print(f"Sample raw input created in '{input_filename}'.")

    # Step 2: Read CSV
    records = read_csv(input_filename)
    print(f"Total raw records read: {len(records)}")

    # Step 3: Process and Clean Records
    valid_records, invalid_records = process_records(records)

    # Step 4: Export Clean and Error Files
    export_csv(cleaned_output, valid_records)
    export_csv(error_output, invalid_records)

    # Step 5: Calculate Analytics
    if valid_records:
        total_marks = sum(student["marks"] for student in valid_records)
        average_marks = total_marks / len(valid_records)

        highest_student = max(valid_records, key=lambda s: s["marks"])

        print("-" * 60)
        print("PIPELINE SUMMARY & ANALYTICS")
        print("-" * 60)
        print(f"Total Valid Records   : {len(valid_records)}")
        print(f"Total Invalid Records : {len(invalid_records)}")
        print(f"Average Marks         : {average_marks:.2f}")
        print(f"Highest Scorer        : {highest_student['name']} ({highest_student['marks']} marks)")
        print("=" * 60)
        print("Data processing pipeline executed successfully!")
    else:
        print("No valid records found to compute analytics.")


if __name__ == "__main__":
    main()
