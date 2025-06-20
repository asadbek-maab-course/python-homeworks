# task-1
import numpy as np
v1 = np.arange(10, 49)
print(v1)

# task-2
m = np.array([[i + 3*j for i in range(3)] for j in range(3)])
print(m)

# task-3
import numpy as np
m3x3 = np.empty((3,3))
print(m3x3)

# task-4
rand_arr = np.random.randint(0, 10, size=(10, 10))
print(rand_arr)

# task-5
rand_arr = np.random.randint(0, 10, size=(10, 10))
print(np.max(rand_arr))
print(np.min(rand_arr))


# task-6
rand_vec = np.random.randint(0, 30, size=(30))
print(rand_vec.mean())

# task-7
a = np.random.randint(0, 100, size=(5,5))
norm = np.linalg.norm(a)
print(norm)

# task-8
m5x3 = np.random.randint(1, 10, size=(5,3))
m3x2 = np.random.randint(1, 10, size=(3,2))
print(np.dot(m5x3, m3x2))

# task-9
m3x3 = np.random.randint(1, 10, size=(3,3))
m3x3_2 = np.random.randint(1, 10, size=(3,3))
print(np.dot(m3x3, m3x3_2))

# task-10
m4x4 = np.random.randint(1, 10, size=(4,4))
print(m4x4.transpose())

# task-11
m3x3 = np.random.randint(1, 10, size=(3,3))
detetminant = np.linalg.det(m3x3)
print(detetminant)

# task-12
A = np.random.randint(1, 10, size=(3,4))
B = np.random.randint(1, 10, size=(4, 3))
print(np.dot(A, B))

# task-13
m3x3 = np.random.randint(1, 10, size=(3,3))
m3 = np.random.randint(1, 10, size=(3))
print(np.dot(m3x3, m3.reshape(3,1)))

# task-14
A = np.array([
    [2, 4, 6],
])
b = np.array([2])
x = np.linalg.solve(A, b)
print(x)

# task-15
rowwise = np.sum(A, axis=1)
columnwise = np.sum(A, axis=0)
print(rowwise, columnwise)



