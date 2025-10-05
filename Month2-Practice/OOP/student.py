class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def student_info(self):
        return f"Name = {self.name} and Age = {self.age}"

student1 = Student("Kay", "Ambere")

print(student1.student_info())
