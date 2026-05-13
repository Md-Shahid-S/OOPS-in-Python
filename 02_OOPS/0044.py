from functools import total_ordering

@total_ordering   # generates all comparison methods from just __eq__ and __lt__
class Employee:

    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def __eq__(self, other: "Employee") -> bool:
        return self.salary == other.salary

    def __lt__(self, other: "Employee") -> bool:
        return self.salary < other.salary

    def __repr__(self):
        return f"Employee({self.name}, ₹{self.salary:,})"


employees = [
    Employee("Affu", 85000),
    Employee("Ravi", 120000),
    Employee("Sara", 95000),
]

# These all work because of __eq__ and __lt__ + @total_ordering
employees.sort()
print(employees)
print(f"Highest paid: {max(employees)}")
print(f"Lowest paid:  {min(employees)}")