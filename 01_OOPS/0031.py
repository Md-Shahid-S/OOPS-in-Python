'''
The dangerous gotcha — mutable class variables
This is the most common bug in all of Python OOP, and interviewers love asking about it:

'''

class Student:
    # DANGER: mutable class variable (a list)
    all_grades = []   # ← This is shared across ALL instances

    def __init__(self, name):
        self.name = name

    def add_grade(self, grade):
        self.all_grades.append(grade)   # ← Modifying the shared list!


s1 = Student("Affu")
s2 = Student("Ravi")

s1.add_grade(95)
s2.add_grade(80)

print(s1.all_grades)   # [95, 80] ← Affu sees Ravi's grade too!
print(s2.all_grades)   # [95, 80] ← Same list, shared by accident





''' 
The fix is to move mutable defaults into __init__ using self:
'''
class Student:
    def __init__(self, name):
        self.name = name
        self.all_grades = []   # ✅ Each student gets their own fresh list

    def add_grade(self, grade):
        self.all_grades.append(grade)


s1 = Student("Affu")
s2 = Student("Ravi")

s1.add_grade(95)
s2.add_grade(80)

print(s1.all_grades)   # [95]  ✅
print(s2.all_grades)   # [80]  ✅