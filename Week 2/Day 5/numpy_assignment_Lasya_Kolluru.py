"""
================================================================================
AI TRAINING – NUMPY ASSIGNMENT: Week 2 Day 5
Arrays, Dimensions, Indexing, Slicing & Vectorized Operations
Learn -> Create Arrays -> Access Data -> Process Efficiently

Student Name : Lasya Kolluru
GitHub Username: Lasya-Kolluru
Email        : kollurlasyachoudri@gmail.com
File         : numpy_assignment_Lasya_Kolluru.py
Deliverable  : Week 2 Day 5 Assignment - NumPy Fundamentals
================================================================================
"""

import numpy as np


# ==============================================================================
# Part A – Create NumPy Arrays
# ==============================================================================
def part_a_create_arrays():
    """
    Demonstrates creating 1D, 2D, and 3D NumPy arrays from nested lists,
    inspecting data types (dtype), and creating utility arrays (zeros, ones).
    """
    print("\n" + "=" * 60)
    print("PART A: CREATE NUMPY ARRAYS")
    print("=" * 60)

    # 1. 1D array from [10, 20, 30, 40, 50]
    arr1 = np.array([10, 20, 30, 40, 50])

    # 2. 2D array from [[10, 20, 30], [40, 50, 60]]
    arr2 = np.array([[10, 20, 30],
                     [40, 50, 60]])

    # 3. 3D array using values 1 to 8, arranged into two 2x2 blocks
    arr3 = np.array([[[1, 2],
                      [3, 4]],
                     [[5, 6],
                      [7, 8]]])

    # 4. Print each array and identify its data type using dtype
    print("1D Array:")
    print(arr1)
    print("Data type:", arr1.dtype)

    print("\n2D Array:")
    print(arr2)
    print("Data type:", arr2.dtype)

    print("\n3D Array:")
    print(arr3)
    print("Data type:", arr3.dtype)

    # 5. Create an array of five zeros and an array of five ones
    zeros = np.zeros(5)
    ones = np.ones(5)

    print("\nArray of zeros:")
    print(zeros)
    print("Zeros dtype:", zeros.dtype)

    print("\nArray of ones:")
    print(ones)
    print("Ones dtype:", ones.dtype)

    return arr1, arr2, arr3, zeros, ones


# ==============================================================================
# Part B – Dimensions and Shape
# ==============================================================================
def part_b_dimensions_and_shape(arr1, arr2, arr3, zeros, ones):
    """
    Demonstrates inspecting ndim, shape, and size across arrays of varying dimensions.
    Also explains the theoretical distinction and predicts array shapes.
    """
    print("\n" + "=" * 60)
    print("PART B: DIMENSIONS AND SHAPE")
    print("=" * 60)

    arrays = [
        ("1D Array", arr1),
        ("2D Array", arr2),
        ("3D Array", arr3),
        ("Zeros Array", zeros),
        ("Ones Array", ones),
    ]

    for label, arr in arrays:
        print(f"\n{label}")
        print("ndim:", arr.ndim)
        print("shape:", arr.shape)
        print("size:", arr.size)

    # Prediction
    predicted_shape = (3, 4)
    print(f"\nPredicted shape for a 3-row, 4-column array: {predicted_shape}")

    # Conceptual Explanation
    print("\n--- Conceptual Distinction: ndim vs shape vs size ---")
    print("• ndim  : The number of axes / dimensions (e.g., 1 for vector, 2 for matrix, 3 for tensor).")
    print("• shape : A tuple of integers describing the number of elements along each axis (e.g., (2, 3)).")
    print("• size  : The total count of individual elements in the array (equal to the product of shape elements).")


# ==============================================================================
# Part C – Indexing
# ==============================================================================
def part_c_indexing():
    """
    Demonstrates 1D positive and negative indexing, mutating array elements in-place,
    and multi-dimensional 2D row/column coordinate indexing.
    """
    print("\n" + "=" * 60)
    print("PART C: INDEXING")
    print("=" * 60)

    marks = np.array([72, 85, 91, 66, 78, 95])
    print("Initial marks array:", marks)

    # 1. First element and last element
    print("First element:", marks[0])
    print("Last element:", marks[-1])

    # 2. Element at index 2
    print("Element at index 2:", marks[2])

    # 3. Second-last element using negative indexing
    print("Second-last element:", marks[-2])

    # 4. Change the value 66 to 70 and print updated array
    marks[3] = 70
    print("Updated array:", marks)

    # 5. Access 22 and 13 from 2D array [[11, 12, 13], [21, 22, 23]]
    arr_2d = np.array([[11, 12, 13],
                       [21, 22, 23]])
    print("\n2D Array:\n", arr_2d)
    print("Element 22 (row 1, col 1):", arr_2d[1, 1])
    print("Element 13 (row 0, col 2):", arr_2d[0, 2])


# ==============================================================================
# Part D – Slicing
# ==============================================================================
def part_d_slicing():
    """
    Demonstrates 1D slicing with start:stop:step, negative step/offsets,
    2D subarray extraction using row and column slice ranges, and slice stop-index rationale.
    """
    print("\n" + "=" * 60)
    print("PART D: SLICING")
    print("=" * 60)

    values = np.array([5, 10, 15, 20, 25, 30, 35, 40])
    print("Values array:", values)

    # 1. First four elements
    print("First four elements:", values[:4])

    # 2. Elements from index 2 up to, but not including, index 6
    print("Index 2 to 5:", values[2:6])

    # 3. Every second element
    print("Every second element:", values[::2])

    # 4. Last three elements
    print("Last three elements:", values[-3:])

    # 5. Matrix slice: first two rows and last two columns
    matrix = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])
    print("\n3x3 Matrix:\n", matrix)
    print("First two rows and last two columns:\n", matrix[:2, -2:])

    # 6. Explanation of stop index exclusion
    print("\nExplanation:")
    print("The stop index is excluded because Python and NumPy adopt half-open intervals [start, stop).")
    print("This ensures that the slice length is always (stop - start) and adjacent slices (arr[:k] and arr[k:])")
    print("cleanly partition the array without duplicating or skipping elements.")


# ==============================================================================
# Part E – Vectorized Operations
# ==============================================================================
def part_e_vectorized_operations():
    """
    Demonstrates element-wise arithmetic, scalar broadcasting,
    boolean comparison masking, and explains vectorization mechanics.
    """
    print("\n" + "=" * 60)
    print("PART E: VECTORIZED OPERATIONS")
    print("=" * 60)

    a = np.array([10, 20, 30, 40])
    b = np.array([1, 2, 3, 4])
    print("Array a:", a)
    print("Array b:", b)

    # 1. Element-wise arithmetic
    print("\nAddition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", a / b)

    # 2. Add 5 to every element
    print("Add 5:", a + 5)

    # 3. Multiply every element by 3
    print("Multiply by 3:", a * 3)

    # 4. Elements greater than 20
    print("Greater than 20:", a[a > 20])

    # 5. Boolean condition for marks >= 80
    marks = np.array([55, 82, 91, 67, 88])
    result = marks[marks >= 80]
    print("Marks array:", marks)
    print("Marks >= 80:", result)

    # 6. Explanation
    print("\nExplanation:")
    print("Vectorized operations express batch mathematical operations on entire arrays at once,")
    print("executing highly optimized, pre-compiled C/Fortran and SIMD loops under the hood,")
    print("completely eliminating Python interpreter loop overhead.")


# ==============================================================================
# Part F – Debugging Practice
# ==============================================================================
def part_f_debugging():
    """
    Reviews and fixes common NumPy errors:
    1. IndexError with out-of-bounds 1D index
    2. Slicing with stop out-of-bounds (behavior review)
    3. ValueError from incompatible broadcast shapes
    4. IndexError with out-of-bounds 2D row index
    """
    print("\n" + "=" * 60)
    print("PART F: DEBUGGING PRACTICE")
    print("=" * 60)

    # Problem 1
    print("\n[Debugging Problem 1]")
    print("Buggy Code  : arr = np.array([10, 20, 30]); print(arr[3])")
    print("Explanation : arr[3] causes IndexError because valid indices for size 3 are 0, 1, 2.")
    arr1 = np.array([10, 20, 30])
    fixed1 = arr1[2]
    print("Corrected Code: print(arr[2]) -> Output:", fixed1)

    # Problem 2
    print("\n[Debugging Problem 2]")
    print("Observed Code: arr = np.array([1, 2, 3, 4]); print(arr[1:10])")
    print("Explanation : arr[1:10] is valid in Python. Slicing never raises IndexError;")
    print("              it safely stops at the array boundary, returning [2, 3, 4].")
    print("              To make intent explicit, use arr[1:].")
    arr2 = np.array([1, 2, 3, 4])
    fixed2 = arr2[1:]
    print("Corrected Code: print(arr[1:]) -> Output:", fixed2)

    # Problem 3
    print("\n[Debugging Problem 3]")
    print("Buggy Code  : a = np.array([1, 2, 3]); b = np.array([10, 20]); print(a + b)")
    print("Explanation : Shapes (3,) and (2,) cannot be broadcast element-wise.")
    print("              Arrays must have identical or broadcast-compatible dimensions.")
    a3 = np.array([1, 2, 3])
    b3 = np.array([10, 20, 30])
    fixed3 = a3 + b3
    print("Corrected Code: b = np.array([10, 20, 30]); print(a + b) -> Output:", fixed3)

    # Problem 4
    print("\n[Debugging Problem 4]")
    print("Buggy Code  : arr = np.array([[1, 2], [3, 4]]); print(arr[2, 0])")
    print("Explanation : arr[2, 0] causes IndexError because axis 0 has only 2 rows (indices 0 and 1).")
    arr4 = np.array([[1, 2], [3, 4]])
    fixed4 = arr4[1, 0]
    print("Corrected Code: print(arr[1, 0]) -> Output:", fixed4)


# ==============================================================================
# Part G – Main Hands-on Activity: Student Marks Analyzer
# ==============================================================================
def student_marks_analyzer():
    """
    Hands-on student marks analysis utilizing 2D NumPy arrays:
    - Shape and dimension inspection
    - Slicing specific students and subjects
    - Vectorized bonus addition with ceiling capping via np.minimum
    - Axis-based statistical reduction (mean per student across subjects)
    - Boolean masking for scores meeting distinction criteria (>= 80)
    """
    print("\n" + "=" * 60)
    print("PART G: STUDENT MARKS ANALYZER")
    print("=" * 60)

    # Initial dataset: 4 students (rows), 3 subjects (columns)
    marks = np.array([
        [78, 85, 92],
        [66, 74, 81],
        [90, 88, 95],
        [55, 69, 72]
    ])

    # 1. Print full marks array, dimensions, and shape
    print("Marks Array:\n", marks)
    print("Dimensions:", marks.ndim)
    print("Shape:", marks.shape)

    # 2. Print marks of the first student (row 0)
    first_student_marks = marks[0]
    print("First Student Marks:", first_student_marks)

    # 3. Print marks for the second subject (column index 1) for all students
    second_subject_marks = marks[:, 1]
    print("Second Subject Marks:", second_subject_marks)

    # 4 & 5. Add 5 bonus marks and cap at 100 using np.minimum
    adjusted_marks = np.minimum(marks + 5, 100)
    print("Adjusted Marks:\n", adjusted_marks)

    # 6. Calculate each student's average marks across subjects (axis=1)
    averages = np.mean(adjusted_marks, axis=1)
    print("Student Averages:", averages)

    # 7. Find highest mark in the initial marks array
    highest_initial = np.max(marks)
    print("Highest Mark:", highest_initial)

    # 8. Select all adjusted scores that are 80 or above using boolean filtering
    high_scorers = adjusted_marks[adjusted_marks >= 80]
    print("Adjusted Scores >= 80:", high_scorers)

    # 9. Highest adjusted mark
    highest_adjusted = np.max(adjusted_marks)
    print("Highest Adjusted Mark:", highest_adjusted)

    # Summary formatting
    print("\n--- Student Summary Report ---")
    student_labels = ["Student 1", "Student 2", "Student 3", "Student 4"]
    for i, (name, avg) in enumerate(zip(student_labels, averages)):
        print(f"{name}: Adjusted Marks = {adjusted_marks[i].tolist()} | Average = {avg:.2f}")


# ==============================================================================
# Part H – Conceptual Q&A / Reflection
# ==============================================================================
def part_h_reflections():
    """
    Prints structured answers for the 8 core conceptual questions in the assignment.
    """
    print("\n" + "=" * 60)
    print("PART H: EXPLAIN IN YOUR OWN WORDS")
    print("=" * 60)

    qa = [
        ("1. What is NumPy, and why is it useful?",
         "NumPy (Numerical Python) is a Python library used to work with multidimensional arrays and perform mathematical calculations efficiently with precompiled C routines."),
        ("2. What is a NumPy array?",
         "A NumPy array is a contiguous, homogeneous memory block designed to store data in one or more dimensions."),
        ("3. What is the difference between a Python list and a NumPy array?",
         "A Python list stores pointers to heterogeneous objects incurring memory and type-dispatch overhead. A NumPy array stores homogeneous elements contiguously in memory, supporting fast vectorized math."),
        ("4. What do ndim, shape, size, and dtype represent?",
         "ndim: Number of dimensions/axes.\nshape: Tuple giving length along each axis.\nsize: Total number of elements.\ndtype: Data type of elements."),
        ("5. What is indexing? What is negative indexing?",
         "Indexing accesses a specific element using its 0-based offset. Negative indexing accesses elements starting from the end with index -1."),
        ("6. What is slicing?",
         "Slicing selects a contiguous subset or stepped view of elements using the [start:stop:step] half-open interval."),
        ("7. What is a vectorized operation?",
         "A vectorized operation applies an operation across all elements simultaneously without writing explicit Python for-loops, leveraging compiled low-level routines."),
        ("8. Why must arrays generally have compatible shapes for element-wise arithmetic?",
         "Arrays must have compatible shapes so that corresponding elements can be unambiguously paired up according to NumPy broadcasting rules.")
    ]

    for question, answer in qa:
        print(f"\n{question}")
        print(f"Answer: {answer}")


# ==============================================================================
# Main Runner
# ==============================================================================
def main():
    print("=" * 70)
    print("AI TRAINING – NUMPY ASSIGNMENT (Week 2 Day 5)")
    print("Student: Lasya Kolluru | GitHub: Lasya-Kolluru")
    print("=" * 70)

    # Execute all modular components
    arr1, arr2, arr3, zeros, ones = part_a_create_arrays()
    part_b_dimensions_and_shape(arr1, arr2, arr3, zeros, ones)
    part_c_indexing()
    part_d_slicing()
    part_e_vectorized_operations()
    part_f_debugging()
    student_marks_analyzer()
    part_h_reflections()

    print("\n" + "=" * 70)
    print("ALL NUMPY ASSIGNMENT TASKS COMPLETED SUCCESSFULLY!")
    print("=" * 70)


if __name__ == "__main__":
    main()
