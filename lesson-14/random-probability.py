import numpy as np
import matplotlib.pyplot as plt

values = np.array([1, 2, 3, 4])
probs = np.array([.15, .15, .3, .4])
vals = np.random.choice(values, size=10000, p=probs)
plt.hist(vals)
plt.show()
