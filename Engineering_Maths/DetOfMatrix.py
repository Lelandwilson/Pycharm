import numpy as np
from scipy.linalg import det

A = np.array([[1,8,3],[3,2,1],[2,-3,2]])
print(A)
print(det(A))