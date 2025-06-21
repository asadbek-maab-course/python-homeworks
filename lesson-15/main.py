import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 5, 5, 8, 10]

plt.plot(x, y, color="blue")

a = [4, 3, 5, 6, 8]
plt.scatter(x, a, s=[40*i for i in range(1, 6)], cmap='viridis', c=[1, 2, 3, 4, 5])

plt.colorbar()
plt.xlabel("x o'qi")
plt.ylabel("y o'qi")

plt.show()
