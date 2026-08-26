"""
Matrix Operations Tool - Python Developer Internship
------------------------------------------------------
A menu-driven command-line tool for performing common matrix operations
using NumPy: addition, subtraction, multiplication, scalar multiplication,
transpose, determinant, and inverse.
"""

import numpy as np


def input_matrix(name="matrix"):
    """Prompt the user to enter a matrix row by row."""
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))
    print(f"Enter the {rows}x{cols} matrix, one row at a time "
          f"(values separated by spaces):")
    data = []
    for i in range(rows):
        while True:
            row_input = input(f"Row {i + 1}: ").split()
            if len(row_input) != cols:
                print(f"Expected {cols} values, got {len(row_input)}. Try again.")
                continue
            try:
                data.append([float(x) for x in row_input])
                break
            except ValueError:
                print("Please enter numbers only.")
    return np.array(data)


def add(a, b):
    if a.shape != b.shape:
        raise ValueError("Matrices must have the same dimensions to add.")
    return a + b


def subtract(a, b):
    if a.shape != b.shape:
        raise ValueError("Matrices must have the same dimensions to subtract.")
    return a - b


def multiply(a, b):
    if a.shape[1] != b.shape[0]:
        raise ValueError(
            f"Cannot multiply {a.shape} by {b.shape}: "
            f"columns of first must match rows of second."
        )
    return a @ b


def scalar_multiply(a, k):
    return a * k


def transpose(a):
    return a.T


def determinant(a):
    if a.shape[0] != a.shape[1]:
        raise ValueError("Determinant requires a square matrix.")
    return np.linalg.det(a)


def inverse(a):
    if a.shape[0] != a.shape[1]:
        raise ValueError("Inverse requires a square matrix.")
    det = np.linalg.det(a)
    if abs(det) < 1e-10:
        raise ValueError("Matrix is singular (determinant is 0); inverse does not exist.")
    return np.linalg.inv(a)


MENU = """
========== Matrix Operations Tool ==========
1. Addition
2. Subtraction
3. Multiplication
4. Scalar Multiplication
5. Transpose
6. Determinant
7. Inverse
8. Exit
=============================================
"""


def run():
    print(MENU)
    while True:
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "8":
            print("Exiting Matrix Operations Tool. Goodbye!")
            break

        try:
            if choice == "1":
                a = input_matrix("Matrix A")
                b = input_matrix("Matrix B")
                print("\nResult (A + B):\n", add(a, b))

            elif choice == "2":
                a = input_matrix("Matrix A")
                b = input_matrix("Matrix B")
                print("\nResult (A - B):\n", subtract(a, b))

            elif choice == "3":
                a = input_matrix("Matrix A")
                b = input_matrix("Matrix B")
                print("\nResult (A x B):\n", multiply(a, b))

            elif choice == "4":
                a = input_matrix("Matrix A")
                k = float(input("Enter scalar value: "))
                print(f"\nResult ({k} * A):\n", scalar_multiply(a, k))

            elif choice == "5":
                a = input_matrix("Matrix A")
                print("\nResult (Transpose of A):\n", transpose(a))

            elif choice == "6":
                a = input_matrix("Matrix A")
                print("\nResult (Determinant of A):\n", round(determinant(a), 4))

            elif choice == "7":
                a = input_matrix("Matrix A")
                print("\nResult (Inverse of A):\n", inverse(a))

            else:
                print("Invalid choice. Please enter a number from 1 to 8.")

        except ValueError as e:
            print(f"Error: {e}")

        print(MENU)


if __name__ == "__main__":
    run()
