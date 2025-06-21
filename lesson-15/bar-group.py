import matplotlib.pyplot as plt
import numpy as np

categories = ['A', 'B', 'C', 'D']
x = np.arange(len(categories))

values1 = np.random.randint(1, 15, 4)
values2 = np.random.randint(1, 15, 4)

plt.bar(x-.1, values1, color="blue", width=0.2)
plt.bar(x+.1, values2, color="green", width=0.2)
plt.title("Bar test")
plt.xlabel('kategoriyalar')
plt.ylabel('qiiymatlar')
plt.show()