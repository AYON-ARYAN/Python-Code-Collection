import numpy as np

matrix = np.array([[2, 0, 0],
                   [0, 3, 0],
                   [0, 0, 5]])

eigenvalues, eigenvectors = np.linalg.eig(matrix)

print("Eigenvalues are : \n")
print(eigenvalues)

print("\nEigenvectors are : \n")
print(eigenvectors)
