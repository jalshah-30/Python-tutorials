#Constructors in python

class Person:
    
    def __init__(self,n,a,g):
        print("Hey I am a person")
        self.name=n
        self.age=a
        self.gender=g

    name="Jal"
    age=18
    gender="Male"

    def display(self):
        print(f"{self.name} is {self.age} years old and is {self.gender}")

# a=Person() Arguments needed as no void constructor
b=Person("Kartikeya",19,"Male")
# a.display()
b.display()