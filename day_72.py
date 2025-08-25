'''super keyword in Python'''

class ParentClass:
    def ParentClass(self):
        print("This is Parent Class")
    

class ChildClass(ParentClass):
    # def ParentClass(self):
    #     print("Jal")
    #     super().ParentClass()

    def ChildClass(self):
        print("This is base class")
        super().ParentClass()

x=ChildClass()
x.ChildClass()
x.ParentClass()

class Teacher:
    def __init__(self,name,id):
        self.name=name
        self.id=id

class Subjects(Teacher):
    def __init__(self, name, id, sub):
        self.sub=sub
        super().__init__(name, id)

Rashmika=Subjects("Rashmika",101,"DBMS")
print(Rashmika.name)
print(Rashmika.id)
print(Rashmika.sub)