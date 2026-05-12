class Employee:

    MIN_SALARY = 15_000
    MAX_SALARY = 500_000

    def __init__(self, name: str, salary: float):
        self.name = name
        self.__salary = salary   # still private

    # @property turns a method into a readable "attribute"
    @property
    def salary(self):
        """Called when you READ: employee.salary"""
        return self.__salary

    # @salary.setter is called when you WRITE: employee.salary = 90000
    @salary.setter
    def salary(self, new_salary: float):
        if not (self.MIN_SALARY <= new_salary <= self.MAX_SALARY):
            raise ValueError(f"Salary must be between ₹{self.MIN_SALARY} and ₹{self.MAX_SALARY}")
        print(f"Salary changed from ₹{self.__salary:,} to ₹{new_salary:,}")
        self.__salary = new_salary

    # @salary.deleter is called when you do: del employee.salary
    @salary.deleter
    def salary(self):
        print("Salary record deleted")
        del self.__salary

    # Read-only property — no setter means it cannot be assigned from outside
    @property
    def annual_salary(self):
        """Computed property — calculated on the fly, not stored."""
        return self.__salary * 12


e = Employee("Affu", 75000)

# Looks like attribute access — but validation runs behind the scenes
print(e.salary)          # 75000  ← calls the @property getter
e.salary = 90000         # ← calls the @salary.setter, validation runs
print(e.salary)          # 90000
print(e.annual_salary)   # 1080000 ← read-only computed property

# ❌ This raises AttributeError — because there's no setter for annual_salary
# e.annual_salary = 2000000

# ❌ This raises AttributeError — because __salary is private
# e.__salary = 5000
