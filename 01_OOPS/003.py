class Student:
    # CLASS VARIABLES — defined directly inside the class, outside any method
    # Shared by ALL Student objects. Belongs to the class itself.
    university_name = "Anna University"
    total_students = 0

    def __init__(self, name: str, roll_number: str, cgpa: float):
        # INSTANCE VARIABLES — defined using self inside __init__
        # Each object gets its own copy. Belongs to that specific object.
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa
        self.courses_enrolled = []

        # Every time a new student is created, increment the shared counter
        Student.total_students += 1   # Notice: we use Student.total_students,
                                      # not self.total_students — intentional (explained below)

    def enroll(self, course: str):
        self.courses_enrolled.append(course)

    def is_distinction(self) -> bool:
        return self.cgpa >= 9.0

    def get_summary(self):
        return (
            f"{self.name} | {self.roll_number} | CGPA: {self.cgpa} | "
            f"University: {Student.university_name}"
        )


# Creating two students
s1 = Student("Affu", "20AI001", 9.2)
s2 = Student("Ravi", "20AI002", 8.5)

s1.enroll("Deep Learning")
s2.enroll("Data Structures")

print(s1.get_summary())
# Affu | 20AI001 | CGPA: 9.2 | University: Anna University

print(s2.get_summary())
# Ravi | 20AI002 | CGPA: 8.5 | University: Anna University

# Class variable is shared — both students reflect this
print(Student.total_students)   # 2
print(s1.total_students)        # 2  ← also works, but reading through instance
print(s2.total_students)        # 2