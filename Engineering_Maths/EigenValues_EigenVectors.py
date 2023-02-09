import scipy.linalg as la
import numpy as np

#From problem 4

A = np.array([[1,0,0,0],[0,2,0,0],[0,0,3,0],[0,0,0,-1]])
print("The matrix:")
print(A)

print("Unpack tuple:")
eigvals, eigvecs, = la.eig(A)
print("Eigen Values are:")
print(eigvals)

print("Convert the eigenvalues to real numbers:")
eigvals = eigvals.real
print(eigvals)
# print(eigvals[0])
# print(eigvals[1])
# print(eigvals[2])
print("The eigenvectors are:")
print(eigvecs)

#construct P:
P = eigvecs
print("Constructed matrix is")
print(P)
D = np.diag((eigvals[0],eigvals[1],eigvals[2],eigvals[3])) #these are the eigenvalues
# D = np.diag((0,5,-2)) #these are the eigenvalues

print("The daigonal matrix is:")
print(D)

#verify using the formula Pinverse*A*P
D_verify = la.inv(P) @A @P
print("The verified diagonal matrix of A is:")
print(D_verify)

