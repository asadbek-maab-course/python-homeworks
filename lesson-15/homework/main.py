import matplotlib.pyplot as plt
import numpy as np

# task 1
x = np.arange(-10, 11)
y = x*x - 4*x + 4
plt.plot(x, y, color = "red")
plt.title("f(x) = x^2 - 4x + 4")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()

# task 2
x = np.arange(0, 2*np.pi, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, c='blue', marker='o', linestyle='-', label="sin(x)")
plt.plot(x, y2, c='green', linestyle='--', label="cos(x)")
plt.title("sinx and cosx")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.legend()
plt.show()

# task 3
fig, axes = plt.subplots(nrows=2, ncols=2)
x = np.arange(-20, 20)
axes[0, 0].plot(x, x*x*x, c='blue')
axes[0, 0].set_title("x^3")
axes[0, 0].set_xlabel("X axis")
axes[0, 0].set_ylabel("Y axis")

axes[0, 1].plot(x, np.sin(x), c='green')
axes[0, 1].set_title("sinx")
axes[0, 1].set_xlabel("X axis")
axes[0, 1].set_ylabel("Y axis")

axes[1, 0].plot(x, np.power(np.e, x), c='red')
axes[1, 0].set_title("e^x")
axes[1, 0].set_xlabel("X axis")
axes[1, 0].set_ylabel("Y axis")

axes[1, 1].plot(np.arange(0, 40), np.log(x+1), c='orange')
axes[1, 1].set_title("log(x+1)")
axes[1, 1].set_xlabel("X axis")
axes[1, 1].set_ylabel("Y axis")

plt.tight_layout()
plt.show()

# task 4
x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)
markers_list = [i for i in '.,*<1234>pP']
for i in range(len(y)):
    marker = np.random.choice(markers_list)
    plt.scatter(x[i], y[i], marker=marker, s=(i+50))
plt.grid(1)
plt.title('4. Scatter plot')

plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.tight_layout()
plt.show()

# task 5
data = np.random.normal(0, 1, 1000)
plt.hist(data, alpha=0.7, bins=30)
plt.title('task 5 : Histogram')
plt.xlabel('Values')
plt.ylabel('Frequencies')
plt.show()

# task 6
x = np.arange(-5, 5, 0.01)
y = np.arange(-5, 5, 0.01)
xx, yy = np.meshgrid(x, y)
f = np.cos(x*x + y*y)
ff = np.cos(xx*xx + yy*yy)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(xx, yy, ff, cmap='viridis')
fig.colorbar(surf)

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('6. 3D plotting')
plt.show()

# task 7
products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
values = [200, 150, 250, 175, 225]

plt.bar(products, values, color = ['r', 'orange', 'b', 'aqua', 'g'])
plt.title("7. Bar Chart")
plt.xlabel('Products')
plt.ylabel('Sales alues')
plt.show()

# task 8
categories = ['Category A', 'Category B', 'Category C']
colors = ['skyblue', 'lightcoral', 'lightgreen']
ts = ['T1', 'T2', 'T3', 'T4']
category_datas = np.random.randint(5, 20, (3, 4))
fig, ax = plt.subplots(figsize = (10, 7))
for i in range(3):
    if i == 0:
        ax.bar(ts, category_datas[i], label = categories[i], color=colors[i])
    else:
        ax.bar(ts, category_datas[i], bottom=category_datas[i-1], label = categories[i], color=colors[i])
ax.set_xlabel('Time Period', fontsize=12)
ax.set_ylabel('Contribution', fontsize=12)
ax.set_title('Contribution of Different Categories Over Time', fontsize=14)
ax.legend(title='Categories')
ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()