import matplotlib.pyplot as plt
import numpy as np

colors = ['blue', 'red', 'orange', 'green']
categories = ['A', 'B', 'C', 'D']
values = np.random.randint(1, 15, 4)

plt.bar(categories, values, color=colors)
plt.title("Bar test")
plt.xlabel('kategoriyalar')
plt.ylabel('qiiymatlar')
plt.show()