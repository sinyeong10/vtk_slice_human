import math

class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def magnitude(self): #제곱의 합의 제곱근으로 크기를 구함
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self): #단위 벡터
        mag = self.magnitude()
        if mag == 0:
            return Vector3D(0, 0, 0)
        return Vector3D(self.x / mag, self.y / mag, self.z / mag)

    def dot_product(self, other): #내적
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross_product(self, other): #외적
        return Vector3D(self.y * other.z - self.z * other.y,
                        self.z * other.x - self.x * other.z,
                        self.x * other.y - self.y * other.x)

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)

    def __repr__(self): #print시
        return f"Vector3D({self.x}, {self.y}, {self.z})"

# 테스트
v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)

print("v1 =", v1)
print("v2 =", v2)
print("Magnitude of v1:", v1.magnitude())
print("Normalized v1:", v1.normalize())
print("Dot product of v1 and v2:", v1.dot_product(v2))
print("Cross product of v1 and v2:", v1.cross_product(v2))
print("v1 + v2 =", v1 + v2)
print("v1 - v2 =", v1 - v2)
print("v1 * 2 =", v1 * 2)
