'''
The shadowing trap — self.x vs ClassName.x
'''


class Student:
    university_name = "Anna University"

    def __init__(self, name):
        self.name = name

s1 = Student("Affu")

# Reading works fine through self
print(s1.university_name)   # "Anna University" — Python looks at instance first,
                             # then climbs up to the class

# But WRITING through self creates a new instance variable, it doesn't change the class variable
s1.university_name = "MIT"   # ← This creates s1's own copy, shadows the class variable

print(s1.university_name)        # "MIT"          ← s1's personal copy
print(Student.university_name)   # "Anna University" ← class variable untouched
print(Student("Ravi").university_name)  # "Anna University" ← other objects unaffected