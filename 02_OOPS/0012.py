'''
Build a Patient class for a hospital system:

name and age should be public
_medical_history should be protected — a list that stores conditions like "Diabetes", "Hypertension"
__blood_pressure should be private — stored as a tuple like (120, 80)
Use @property and @setter for blood_pressure — the setter should reject values where systolic is below 60 or above 200
A method add_condition(condition) that appends to _medical_history
A method get_report() that prints all details including a safely formatted blood pressure reading

Test the validation by trying to set an invalid blood pressure and catching the error.
'''

class Patient:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self._medical_history = []
        self.__blood_pressure = (120, 80)  # Default normal BP

    @property
    def blood_pressure(self):
        """Return blood pressure in a readable format."""
        systolic, diastolic = self.__blood_pressure
        return f"{systolic}/{diastolic} mmHg"

    @blood_pressure.setter
    def blood_pressure(self, value):
        systolic, diastolic = value
        if not (60 <= systolic <= 200):
            raise ValueError("Systolic blood pressure must be between 60 and 200.")
        self.__blood_pressure = (systolic, diastolic)

    def add_condition(self, condition: str):
        self._medical_history.append(condition) 
    
    def get_report(self):
        conditions = ", ".join(self._medical_history) if self._medical_history else "None"
        return (
            f"Patient Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Blood Pressure: {self.blood_pressure}\n"
            f"Medical History: {conditions}"
        )
    
# Testing the Patient class
patient = Patient("John Doe", 45)
print(patient.get_report())
patient.add_condition("Diabetes")
patient.add_condition("Hypertension")
print(patient.get_report())
# Testing invalid blood pressure
try:
    patient.blood_pressure = (50, 30)  # Invalid systolic
except ValueError as e:
    print(f"Error: {e}")
try:   
    patient.blood_pressure = (210, 100)  # Invalid systolic
except ValueError as e:
    print(f"Error: {e}")    