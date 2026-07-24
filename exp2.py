# Python Program to Perform Matrix Operations using NumPy

import numpy as np

# Input two 2x2 matrices
print("Enter elements of first 2x2 matrix:")
A = np.array([[int(input()), int(input())],
              [int(input()), int(input())]])

print("Enter elements of second 2x2 matrix:")
B = np.array([[int(input()), int(input())],
              [int(input()), int(input())]])

print("\nMatrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Matrix Addition
print("\nAddition (A + B):")
print(A + B)

# Matrix Subtraction
print("\nSubtraction (A - B):")
print(A - B)

# Matrix Multiplication
print("\nMultiplication (A × B):")
print(np.dot(A, B))

# Transpose of Matrix A
print("\nTranspose of Matrix A:")
print(A.T)

# Inverse of Matrix A
if np.linalg.det(A) != 0:
    print("\nInverse of Matrix A:")
    print(np.linalg.inv(A))
else:
    print("\nInverse of Matrix A does not exist (Determinant = 0).")

