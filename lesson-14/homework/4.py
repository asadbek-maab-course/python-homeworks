import numpy as np

A = np.array([
    [10, -2, 3],
    [-2, 8, -1],
    [3, -1, 6]
])
B = np.array([12, -5, 15])
ans = np.linalg.solve(A, B)
i1, i2, i3 = ans
print(i1, i2, i3)