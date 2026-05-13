class Vector:
    """
    A 2D vector class — a practical example of operator overloading.
    Used in physics simulations, ML feature spaces, game engines.
    """

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    # v1 + v2  →  calls __add__
    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    # v1 - v2  →  calls __sub__
    def __sub__(self, other: "Vector") -> "Vector":
        return Vector(self.x - other.x, self.y - other.y)

    # v1 * 3  →  calls __mul__
    def __mul__(self, scalar: float) -> "Vector":
        return Vector(self.x * scalar, self.y * scalar)

    # 3 * v1  →  calls __rmul__ (reversed multiplication)
    def __rmul__(self, scalar: float) -> "Vector":
        return self.__mul__(scalar)

    # v1 == v2  →  calls __eq__
    def __eq__(self, other: "Vector") -> bool:
        return self.x == other.x and self.y == other.y

    # abs(v1)  →  calls __abs__  (magnitude of vector)
    def __abs__(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    # len(v1)  →  calls __len__
    def __len__(self) -> int:
        return 2   # a 2D vector always has 2 components

    # bool(v1)  →  calls __bool__
    def __bool__(self) -> bool:
        return self.x != 0 or self.y != 0   # zero vector is falsy

    # print(v1)  →  calls __repr__
    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"


v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1 + v2)      # Vector(4, 6)       — __add__
print(v1 - v2)      # Vector(2, 2)       — __sub__
print(v1 * 3)       # Vector(9, 12)      — __mul__
print(3 * v1)       # Vector(9, 12)      — __rmul__
print(v1 == v2)     # False              — __eq__
print(abs(v1))      # 5.0                — __abs__ (3-4-5 triangle)
print(len(v1))      # 2                  — __len__
print(bool(v1))     # True               — __bool__

# Works with Python built-ins naturally
vectors = [Vector(1,1), Vector(3,4), Vector(0,2)]
largest = max(vectors, key=abs)   # uses __abs__ for comparison
print(f"Largest magnitude: {largest}")