class Employee:
    def __init__(self, name: str, employee_id: str, salary: float):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def work(self):
        return f"{self.name} is working"

    def get_details(self):
        return f"[{self.employee_id}] {self.name} — ₹{self.salary:,}"


class Developer(Employee):
    def __init__(self, name: str, employee_id: str, salary: float, tech_stack: list):
        # super() calls the parent's __init__ — never rewrite what the parent already does
        super().__init__(name, employee_id, salary)
        self.tech_stack = tech_stack   # Developer-specific attribute

    # Overriding the parent's work() method with specialised behaviour
    def work(self):
        return f"{self.name} is writing code in {', '.join(self.tech_stack)}"

    def code_review(self):
        return f"{self.name} is reviewing a pull request"


dev = Developer("Affu", "D001", 85000, ["Python", "LangChain", "FastAPI"])
print(dev.work())          # Affu is writing code in Python, LangChain, FastAPI
print(dev.get_details())   # [D001] Affu — ₹85,000  ← inherited from Employee
print(dev.code_review())   # Affu is reviewing a pull request