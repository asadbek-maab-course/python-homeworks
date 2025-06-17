import numpy as np

A = np.array([
    [4, 5, 6],
    [3, -1, -1],
    [2, 1, -2]
])
B = np.array([7, 4, 5])
ans = np.linalg.solve(A, B)
x, y, z = ans
print(x, y, z)