import numpy as np

@np.vectorize
def f2c(t):
    return (t - 32) * (5 / 9)

temps = np.array([32, 68, 100, 212, 77])
temps_c = f2c(temps)

print(temps_c)