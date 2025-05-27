import math as m
class Vector:
    x: int
    y: int
    z: int
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z
    
    def magnitude(self):
        return m.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    
    def normalize(self):
        return Vector(
            self.x / self.magnitude(),
            self.y / self.magnitude(),
            self.z / self.magnitude()
        )

    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, other):
        if type(other) is int:
            return Vector(
                self.x * other,
                self.y * other,
                self.z * other
            )
        elif type(other) is Vector:
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            raise TypeError("can't multiply Vector and " + type(other).__name__)
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Print the vector
print(v1)          # Output: Vector(1, 2, 3)

# Addition
v3 = v1 + v2
print(v3)          # Output: Vector(5, 7, 9)

# Subtraction
v4 = v2 - v1
print(v4)          # Output: Vector(3, 3, 3)

# Dot product
dot_product = v1 * v2
print(dot_product) # Output: 32

# Scalar multiplication
v5 = v1 * 3
print(v5)          # Output: Vector(3, 6, 9)

# Magnitude
print(v1.magnitude())  # Output: 3.7416573867739413

# Normalization
v_unit = v1.normalize()
print(v_unit)      
