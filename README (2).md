# Matrix Operations Tool

A menu-driven command-line tool for performing common matrix operations,
built with NumPy.

## Files
- `matrix_tool.py` — the CLI tool

## How to run
```bash
pip install numpy
python matrix_tool.py
```

## Features
The tool presents a menu and lets you perform the following operations
on matrices you enter interactively:

1. **Addition** — adds two matrices of the same dimensions
2. **Subtraction** — subtracts two matrices of the same dimensions
3. **Multiplication** — multiplies two matrices (checks compatible dimensions)
4. **Scalar Multiplication** — multiplies a matrix by a constant
5. **Transpose** — flips a matrix over its diagonal
6. **Determinant** — computes the determinant of a square matrix
7. **Inverse** — computes the inverse of a square matrix (if it exists)
8. **Exit**

## Error handling
The tool validates input and gives clear error messages for:
- Mismatched dimensions for addition/subtraction
- Incompatible dimensions for multiplication
- Non-square matrices for determinant/inverse
- Singular matrices (determinant = 0) that have no inverse
- Non-numeric input

## Example
```
Enter your choice (1-8): 1
Enter number of rows for Matrix A: 2
Enter number of columns for Matrix A: 2
Enter the 2x2 matrix, one row at a time (values separated by spaces):
Row 1: 1 2
Row 2: 3 4
Enter number of rows for Matrix B: 2
Enter number of columns for Matrix B: 2
Enter the 2x2 matrix, one row at a time (values separated by spaces):
Row 1: 5 6
Row 2: 7 8

Result (A + B):
 [[ 6.  8.]
 [10. 12.]]
```
