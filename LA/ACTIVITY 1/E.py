#determinant
import numpy as np

matrix = np.array([[2, 0, 0],
                   [3, 4, 0],
                   [5, 6, 7]])

determinant = np.linalg.det(matrix)

print("Matrix:")
print(matrix)

print("\nDeterminant:")
print(determinant)
