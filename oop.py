class Person:
    def __init__(self, name):
        self.name = name1

    def introduce(self):
        return f"I am {self.name}"
    
    
    
________________________________
class Employee(Person):
    def __init__(self, name, job_title):
        self.name = name
        self.job_title = job_title

    def describe_profession(self):
        return f"I work as a {self.job_title}"
    
e = Employee("Rebecca", "Developer")
# Can still introduce
print(e.introduce())
# But also can now describe profession
print(e.describe_profession())





class Student(Employee)
    def __init__(self, name, job_title):
        super().__init__(name, job_title)
