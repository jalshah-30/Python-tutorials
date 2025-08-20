'''Class Methods as Alternative Constructors'''

class Student:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    @classmethod
    def fromStr(cls,string):
        return cls(string.split("-")[0],int(string.split("-")[1]))

s1=Student("Jal",20)
print(s1.name)
print(s1.id)

code = "Maayank-10"
s2=Student.fromStr(code)
print(s2.name)
print(s2.id)