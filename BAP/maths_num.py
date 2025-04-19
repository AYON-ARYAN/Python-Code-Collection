import numpy as np

m1 = np.array([[1, 2], [3, 4]])  # Square matrix for demonstration purposes
m2 = np.array([[7, 8, 9], [10, 11, 12]])

print("Matrix m1:")
print(m1)
print("Matrix m2:")
print(m2)

a = np.dot(m1, m2.T)  # Use the transpose of m2
print("Result of matrix multiplication (m1 * m2_transpose):")
print(a)

print("Transpose of matrix m2:")
print(m2.T)

# Activity 2: Finding Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(m1)  # Finding eigenvalues and eigenvectors of m1
print("Eigenvalues of m1:")
print(eigenvalues)
print("Eigenvectors of m1:")
print(eigenvectors)
