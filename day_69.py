'''Class Methods'''

class Student:
    Class=10
    def show(self):
        print(f"{self.name} is studying in {self.Class}")

    @classmethod                    #Changes the value of class variable if changed for any instance
    def Change_class(cls,newClass):
        cls.Class=newClass

s1=Student()
s1.name="Jal"
s1.show() 
s1.Change_class(11)
s1.show()   

print(Student.Class)