import numpy as np
#Cramers rule or Gauss
# A = first matrix
# B = second matrix
a = np.array([[5,5,5], [1,2,4], [4,2,0]])
b = np.array([7.0,2.4,4.0])
x = np.linalg.solve(a, b)

print("[i1, i2, i3]")
print(x)