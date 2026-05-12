# Type 3 — Multiple Inheritance
# One child, multiple parents. Python allows this — most other languages don't. This is where MRO becomes critical

class FrontendDev(Employee):
    def __init__(self, name, employee_id, salary):
        super().__init__(name, employee_id, salary)
        self.skills = ["React", "CSS", "JavaScript"]

    def build_ui(self):
        return f"{self.name} is building a beautiful UI"

    def work(self):
        return f"{self.name} is working on the frontend"


class BackendDev(Employee):
    def __init__(self, name, employee_id, salary):
        super().__init__(name, employee_id, salary)
        self.skills = ["Django", "PostgreSQL", "Redis"]

    def build_api(self):
        return f"{self.name} is building REST APIs"

    def work(self):
        return f"{self.name} is working on the backend"


# FullStackDev inherits from BOTH FrontendDev and BackendDev
class FullStackDev(FrontendDev, BackendDev):
    def __init__(self, name, employee_id, salary):
        super().__init__(name, employee_id, salary)

    def work(self):
        # Explicitly calling both parents' work methods
        fe = FrontendDev.work(self)
        be = BackendDev.work(self)
        return f"{fe} AND {be}"


fs = FullStackDev("Affu", "FS001", 120000)
print(fs.work())
# Affu is working on the frontend AND Affu is working on the backend

print(fs.build_ui())    # Inherited from FrontendDev
print(fs.build_api())   # Inherited from BackendDev



# Always check MRO with __mro__ or mro()
print(FullStackDev.__mro__)
# (<class 'FullStackDev'>, <class 'FrontendDev'>,
#  <class 'BackendDev'>, <class 'Employee'>, <class 'object'>)



# The classic diamond problem — and how Python solves it:

#        A
#       / \
#      B   C
#       \ /
#        D

class A:
    def greet(self):
        return "A"

class B(A):
    def greet(self):
        return f"B → {super().greet()}"

class C(A):
    def greet(self):
        return f"C → {super().greet()}"

class D(B, C):
    def greet(self):
        return f"D → {super().greet()}"

d = D()
print(d.greet())   # D → B → C → A

# MRO: D → B → C → A → object
# super() in D calls B, super() in B calls C (not A!),
# super() in C calls A
# This ensures A's __init__ is only called ONCE — the diamond problem solved
print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)