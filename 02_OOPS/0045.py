# Polymorphism vs Inheritance — critical distinction

# Polymorphism THROUGH inheritance — most common
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self): pass

class Circle(Shape):
    def area(self): return 3.14 * self.radius ** 2

class Square(Shape):
    def area(self): return self.side ** 2

# Same method, different behaviour — polymorphism via inheritance


# Polymorphism WITHOUT inheritance — duck typing
class PDFReport:
    def generate(self): print("Generating PDF...")

class ExcelReport:
    def generate(self): print("Generating Excel spreadsheet...")

class HTMLReport:
    def generate(self): print("Generating HTML page...")

# No shared parent — but this still works perfectly
def run_reports(reports: list):
    for report in reports:
        report.generate()   # Duck typing — just needs generate() to exist

run_reports([PDFReport(), ExcelReport(), HTMLReport()])