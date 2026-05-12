class Vector:
    """
    Represents a mathematical vector — extremely useful in ML/AI work.
    e.g. feature vectors, embeddings, gradient vectors
    """

    def __init__(self, *components: float):
        self.components = list(components)

    # + operator: v1 + v2
    def __add__(self, other: "Vector") -> "Vector":
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions")
        result = [a + b for a, b in zip(self.components, other.components)]
        return Vector(*result)

    # - operator: v1 - v2
    def __sub__(self, other: "Vector") -> "Vector":
        result = [a - b for a, b in zip(self.components, other.components)]
        return Vector(*result)

    # * operator: v * scalar  (scalar multiplication)
    def __mul__(self, scalar: float) -> "Vector":
        result = [x * scalar for x in self.components]
        return Vector(*result)

    # == operator: v1 == v2
    def __eq__(self, other: "Vector") -> bool:
        return self.components == other.components

    # len(): len(v)
    def __len__(self) -> int:
        return len(self.components)

    # Magnitude (size) of the vector
    def magnitude(self) -> float:
        return sum(x ** 2 for x in self.components) ** 0.5

    # Dot product — critical for ML similarity calculations
    def dot(self, other: "Vector") -> float:
        return sum(a * b for a, b in zip(self.components, other.components))

    def __repr__(self):
        return f"Vector{tuple(self.components)}"


# Feature vectors from an ML model
embedding1 = Vector(0.8, 0.3, 0.5, 0.9)
embedding2 = Vector(0.2, 0.7, 0.4, 0.1)

print(embedding1 + embedding2)       # Vector(1.0, 1.0, 0.9, 1.0)
print(embedding1 - embedding2)       # Vector(0.6, -0.4, 0.1, 0.8)
print(embedding1 * 2)                # Vector(1.6, 0.6, 1.0, 1.8)
print(embedding1 == embedding2)      # False
print(len(embedding1))               # 4
print(f"Magnitude: {embedding1.magnitude():.3f}")   # 1.355
print(f"Dot product: {embedding1.dot(embedding2):.3f}")  # 0.68

# The + operator works the same way for integers, strings, and now Vectors
# Same operator symbol — three completely different behaviours → Polymorphism
print(1 + 2)           # 3        (integer addition)
print("AI" + "Eng")    # AIEng    (string concatenation)
print(embedding1 + embedding2)  # Vector addition