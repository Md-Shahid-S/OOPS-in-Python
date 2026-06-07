class Multiplier:
    """An object you can call like a function — common in ML pipelines."""

    def __init__(self, factor: float):
        self.factor = factor

    def __call__(self, value: float) -> float:
        return value * self.factor

    def __repr__(self):
        return f"Multiplier(factor={self.factor})"


double = Multiplier(2)
triple = Multiplier(3)

print(double(50))    # 100 — called like a function, but it's an object
print(triple(50))    # 150

# Common in ML — transform pipelines, decorators, custom activation functions
data = [10, 20, 30, 40]
scaled = list(map(double, data))   # object used like a function
print(scaled)   # [20, 40, 60, 80]