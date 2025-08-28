'''Multiple Inheritance'''

class Student:
    def __init__(self,name):
        self.name = name

    def display(self):
        print(f"The name of Student is {self.name}")

class Player:
    def __init__(self,game):
        self.game=game

    def display(self):
        print(f"The Student plays {self.game}")

#     Priority  1      2
class Stuply(Student,Player):
    def __init__(self, name,game):
        self.name=name
        self.game=game

s1=Stuply("Jal","Cricket")
print(s1.name)
print(s1.game)
s1.display()