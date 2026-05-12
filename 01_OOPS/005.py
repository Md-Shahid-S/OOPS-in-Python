from datetime import date


class Employee:
    company_name = "TechCorp"
    employee_count = 0

    def __init__(self, name: str, department: str, salary: float, birth_year: int):
        self.name = name
        self.department = department
        self.salary = salary
        self.birth_year = birth_year
        Employee.employee_count += 1

    # ─────────────────────────────────────────────
    # 1. INSTANCE METHOD
    # Receives 'self' — works on one specific object
    # Most methods you write will be instance methods
    # ─────────────────────────────────────────────
    def give_raise(self, percent: float):
        """Gives a raise to THIS specific employee."""
        self.salary *= (1 + percent / 100)
        return self.salary

    def get_details(self):
        """Returns a summary of THIS employee."""
        return (
            f"{self.name} | {self.department} | "
            f"₹{self.salary:,.0f} | Age: {Employee.get_age(self.birth_year)}"
        )

    # ─────────────────────────────────────────────
    # 2. CLASS METHOD
    # Receives 'cls' (the class itself) instead of self
    # Used for: alternative constructors, class-level operations
    # ─────────────────────────────────────────────
    @classmethod
    def get_headcount(cls):
        """Works at the company level — not tied to any one employee."""
        return f"{cls.company_name} has {cls.employee_count} employees"

    @classmethod
    def from_dict(cls, data: dict):
        """
        Alternative constructor — creates an Employee from a dictionary.
        This is the most important real-world use of @classmethod.
        Very common when reading data from APIs or databases.
        """
        return cls(
            name=data["name"],
            department=data["department"],
            salary=data["salary"],
            birth_year=data["birth_year"]
        )

    @classmethod
    def from_csv_string(cls, csv_string: str):
        """
        Another alternative constructor — creates an Employee from a CSV row.
        e.g. "Affu,AI,75000,2001"
        """
        name, dept, salary, birth_year = csv_string.split(",")
        return cls(name, dept, float(salary), int(birth_year))

    # ─────────────────────────────────────────────
    # 3. STATIC METHOD
    # Receives neither self nor cls
    # Used for: utility/helper functions logically related to the class
    # but that don't need any object or class data
    # ─────────────────────────────────────────────
    @staticmethod
    def get_age(birth_year: int) -> int:
        """
        Calculates age from birth year.
        Doesn't need any specific employee's data.
        Doesn't need the class either.
        It's just a helper that belongs here logically.
        """
        return date.today().year - birth_year

    @staticmethod
    def is_valid_salary(salary: float) -> bool:
        """Validates a salary value — pure utility, no object needed."""
        return 10_000 <= salary <= 10_000_000


# ── Using instance methods ──
e1 = Employee("Affu", "AI Engineering", 75000, 2001)
e2 = Employee("Ravi", "Data Science", 90000, 1998)

e1.give_raise(10)
print(e1.get_details())
# Affu | AI Engineering | ₹82,500 | Age: 24

# ── Using class methods ──
print(Employee.get_headcount())
# TechCorp has 2 employees

# Alternative constructor — very common in production code
data = {"name": "Sara", "department": "MLOps", "salary": 95000, "birth_year": 1999}
e3 = Employee.from_dict(data)
print(e3.get_details())

csv_row = "Kiran,Backend,80000,2000"
e4 = Employee.from_csv_string(csv_row)
print(e4.get_details())

print(Employee.get_headcount())
# TechCorp has 4 employees

# ── Using static methods ──
print(Employee.is_valid_salary(75000))   # True
print(Employee.is_valid_salary(500))     # False
print(Employee.get_age(2001))            # 24

# Static methods can also be called on an instance, but calling on the class is cleaner
print(e1.is_valid_salary(75000))         # True — works, but Employee.is_valid_salary() is preferred