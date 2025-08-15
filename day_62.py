'''Access modifiers in python'''

#all variables and methods are by default public in python

#by prefixing double underscore a variable can be made private

#In python there is no concept of private and protected , the given below are just convection.

class Student:
    def __init__(self):
        self.__Name="Jal"
        self._pro="I am protected"
    
s1=Student()
# print(s1.__Name)  it will give error

'''Private variables can be accessed by using following syntax'''
print(s1._Student__Name)  #Can be accessed directly and this is called name mangling

'''Protected variables can be made by prefixing single underscore'''

class Subject(Student):
    pass

s2=Subject()
print(s2._pro)