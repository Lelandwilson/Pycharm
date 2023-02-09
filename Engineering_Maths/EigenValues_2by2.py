import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la

A = np.array([[4,-2],[-2,1]])
print(A)

results = la.eig(A)
print("Eigenvalues are:")
print(results[0])


print("Corresponding eigenvectors are:")
print(results[1])

print("Unpack tupil")
eigvals, eigvecs = la.eig(A)
print(eigvals)
print(eigvecs)
eigvals = eigvals.real
print("The roots of the above polynomial:")
print(eigvals)
lambda1 = eigvals[1]
print(lambda1)

v1 = eigvecs[:,1].reshape(2,1)
print(v1)
A @ v1
print("if [0,0] then the eigenvectors associated with distinct eigenvalues of a symmetric matrix are orthogonal.")
print(lambda1 * v1)