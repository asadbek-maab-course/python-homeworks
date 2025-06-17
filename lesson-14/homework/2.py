import numpy as np

@np.vectorize
def power_of_elements(a, b):
    return np.power(a, b)

nums = [2, 3, 4, 5]
powers = [1, 2, 3, 4]
print(power_of_elements(nums, powers))