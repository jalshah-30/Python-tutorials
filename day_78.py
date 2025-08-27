'''Single Inheritance in Python'''

class Student:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def display(self):
        print("Student class is called")

class Inherited(Student):
    def __init__(self,name,id):
        Student.__init__(self,name ,id)
    def display(self):
        print("Inherited class called")

s1=Student("Jal",20)
s1.display()

s2=Inherited("Mayank",10)
s2.display()