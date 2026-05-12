'''  
Create a class called Student that represents a university student. Without using __init__ yet, 
manually set these attributes on two separate student objects: name, roll_number, cgpa. 
Then write a method is_distinction() that returns True if cgpa >= 9.0.
Create two student objects and test the method on both.

'''

class Students:
    def set_attributes(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def is_distinction(self):
        if self.cgpa >= 9.0:
            return True
        return False
    
student1 = Students()
student1.set_attributes("Alice", 101, 9.5)
student2 = Students()
student2.set_attributes("Bob", 102, 8.5)

print(student1.is_distinction())  # True
print(student2.is_distinction())  # False