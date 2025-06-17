import numpy as np
import matplotlib.pyplot as plt

t = np.random.uniform(low=1, high=20, size=1000)
plt.hist(t)
plt.show()