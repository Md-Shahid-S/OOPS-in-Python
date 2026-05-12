# Type 2 — Multi-level Inheritance
# A chain — child inherits from parent, grandchild inherits from child. Like generations in a family.


class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def get_details(self):
        return f"[{self.employee_id}] {self.name} — ₹{self.salary:,}"


class Developer(Employee):
    def __init__(self, name, employee_id, salary, tech_stack):
        super().__init__(name, employee_id, salary)
        self.tech_stack = tech_stack

    def work(self):
        return f"{self.name} is coding in {', '.join(self.tech_stack)}"


class SeniorDeveloper(Developer):
    def __init__(self, name, employee_id, salary, tech_stack, mentees: list):
        super().__init__(name, employee_id, salary, tech_stack)
        self.mentees = mentees   # SeniorDev-specific

    # Extending the parent method — not replacing it entirely
    def work(self):
        base_work = super().work()   # Get Developer's work description
        return f"{base_work} + mentoring {len(self.mentees)} developers"

    def conduct_interview(self):
        return f"{self.name} is conducting a technical interview"


senior = SeniorDeveloper(
    "Affu", "SD001", 150000,
    ["Python", "LangGraph", "Docker"],
    mentees=["Ravi", "Sara", "Kiran"]
)

print(senior.work())
# Affu is coding in Python, LangGraph, Docker + mentoring 3 developers

print(senior.get_details())
# [SD001] Affu — ₹1,50,000   ← inherited all the way from Employee

print(senior.conduct_interview())
# Affu is conducting a technical interview

# Checking the full inheritance chain
print(isinstance(senior, SeniorDeveloper))   # True
print(isinstance(senior, Developer))          # True  ← also a Developer
print(isinstance(senior, Employee))           # True  ← also an Employee