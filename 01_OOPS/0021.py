'''
Mini challenge for you
Take your Student class from Topic 1 and rewrite it properly using __init__. It should:

Accept name, roll_number, and cgpa at the time of object creation
Set a courses_enrolled attribute to an empty list by default
Have a method enroll(course_name) that appends to that list
Have is_distinction() return True if cgpa >= 9.0

Create two students, enroll them in different courses, and print a summary for each.
'''

class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa
        self.courses_enrolled = []

    def enroll(self, course_name):
        self.courses_enrolled.append(course_name)

    def is_distinction(self):
        return self.cgpa >= 9.0
    
student1 = Student("Alice", 101, 9.5)
student2 = Student("Bob", 102, 8.5)

student1.enroll("Math")
student1.enroll("Physics")
student2.enroll("Chemistry")
student2.enroll("Biology")
print(f"{student1.name} (Roll No: {student1.roll_number}) - CGPA: {student1.cgpa}, Courses: {student1.courses_enrolled}, Distinction: {student1.is_distinction()}")
print(f"{student2.name} (Roll No: {student2.roll_number}) - CGPA: {student2.cgpa}, Courses: {student2.courses_enrolled}, Distinction: {student2.is_distinction()}")