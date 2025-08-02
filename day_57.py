#classes and objects in python

class Person:
    name="Jal"
    age=18
    gender="Male"

    def display(self):
        print(f"{self.name} is {self.age} years old and is {self.gender}")

a=Person()
a.display()

a.name="Pavan"
a.gender="Female"
a.display()

'''Self is a reference to the current instance of the class'''