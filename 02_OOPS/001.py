class Employee:
    
    MIN_SALARY = 15_000
    MAX_SALARY = 500_000

    def __init__(self, name: str, salary: float, ssn: str):
        self.name = name              # Public — fine to access directly
        self._department = "General"  # Protected — subclasses can use this
        self.__salary = salary        # Private — only this class manages salary
        self.__ssn = ssn              # Private — sensitive data, never expose directly

        # Validate on creation itself
        if not self.__is_valid_salary(salary):
            raise ValueError(f"Salary must be between {self.MIN_SALARY} and {self.MAX_SALARY}")

    # ── GETTER — read private data in a controlled way ──
    def get_salary(self):
        return self.__salary

    # ── SETTER — write private data with validation ──
    def set_salary(self, new_salary: float):
        if not self.__is_valid_salary(new_salary):
            raise ValueError(f"Invalid salary: {new_salary}")
        self.__salary = new_salary
        print(f"Salary updated to ₹{self.__salary:,}")

    # Private helper — only used internally, never exposed
    def __is_valid_salary(self, salary: float) -> bool:
        return self.MIN_SALARY <= salary <= self.MAX_SALARY

    def get_masked_ssn(self):
        """Never expose the full SSN — only show last 4 digits."""
        return f"XXXX-XXXX-{self.__ssn[-4:]}"

    def get_details(self):
        return (
            f"Name: {self.name} | "
            f"Dept: {self._department} | "
            f"Salary: ₹{self.__salary:,} | "
            f"SSN: {self.get_masked_ssn()}"
        )


e = Employee("Affu", 75000, "1234-5678-9012")

# ✅ Correct way — use the methods the class provides
print(e.get_salary())        # 75000
e.set_salary(90000)          # Salary updated to ₹90,000
print(e.get_masked_ssn())    # XXXX-XXXX-9012
print(e.get_details())

# ❌ This would raise an AttributeError — good, that's the protection working
# print(e.__salary)

# Python's name mangling — technically accessible but you should NEVER do this
# print(e._Employee__salary)   # 90000 — works, but breaks encapsulation intentionally