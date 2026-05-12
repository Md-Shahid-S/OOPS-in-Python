'''
Mini challenge for you
Build an Employee class where:

company_name and employee_count are class variables
Each employee has their own name, department, and salary as instance variables
Every time an Employee object is created, employee_count goes up by 1
A method give_raise(percent) increases that employee's salary by the given percentage
A class method get_headcount() returns the total number of employees created so far 
(we'll formally cover @classmethod in Topic 4 — for now just use ClassName.variable inside a regular method)

Create three employees, give one a raise, and print everyone's details along with the total headcount.
'''
class Employee:
    company_name = "Tech Solutions"
    employee_count = 0

    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary
        Employee.employee_count += 1

    def give_raise(self, percent):
        self.salary += self.salary * (percent / 100)
    
    def get_details(self):
        return f"{self.name} | {self.department} | Salary: {self.salary:.2f}"
    
    def get_headcount(self):
        return Employee.employee_count
    
emp1 = Employee("Alice", "Engineering", 70000)
emp2 = Employee("Bob", "Marketing", 50000)
emp3 = Employee("Charlie", "HR", 60000)
emp4 = Employee("David", "Engineering", 75000)  

emp2.give_raise(10)  # Bob gets a 10% raise
print(emp1.get_details())  # Alice | Engineering | Salary: 70000.00
print(emp2.get_details())  # Bob | Marketing | Salary: 55000.00
print(emp3.get_details())  # Charlie | HR | Salary: 60000.00
print(emp4.get_details())  # David | Engineering | Salary: 75000.00

emp3.give_raise(5)  # Charlie gets a 5% raise
print(emp3.get_details())  # Charlie | HR | Salary: 63000.00
print(f"Total employees: {emp1.get_headcount()}")  # Total employees: 4
