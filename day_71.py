'''dir, __dict__ and help method in Python'''

list=[1,2,3]
print(dir(list))
print(list.__add__)

tuple=(1,2,3)
print(dir(tuple))
print(tuple.__add__)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p= Person("Jal",18)
print(p.__dict__)

print(help(Person))