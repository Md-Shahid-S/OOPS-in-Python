# Abstract properties — when you need subclasses to define attributes too

from abc import ABC, abstractmethod

class Shape(ABC):

    @property
    @abstractmethod
    def area(self) -> float:
        """Every shape must be able to compute its area."""
        pass

    @property
    @abstractmethod
    def perimeter(self) -> float:
        pass

    def describe(self):
        # Concrete method using abstract properties
        print(f"Area: {self.area:.2f} | Perimeter: {self.perimeter:.2f}")


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    @property
    def area(self):
        return 3.14159 * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * 3.14159 * self.radius


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @property
    def perimeter(self):
        return 2 * (self.width + self.height)


shapes = [Circle(7), Rectangle(4, 6), Circle(3)]

# Polymorphism + Abstraction working together beautifully
for shape in shapes:
    shape.describe()
# Area: 153.94 | Perimeter: 43.98
# Area: 24.00 | Perimeter: 20.00
# Area: 28.27 | Perimeter: 18.85