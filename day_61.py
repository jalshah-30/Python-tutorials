'''Inheritance in  PYTHON'''

class Student:
    def __init__(self,name ,roll_no):
        self.Name=name
        self.Roll_no=roll_no

    def display(self):
        print(f"Name of student:{self.Name}\nEnrollment Number:{self.Roll_no}")

class monitor(Student):  #syntax of inheritance
    def appointed(self):
        print(f"{self.Name} is appointed as the monitor of the class")

student1=Student('Jal Shah',20)
student1.display()

student2=monitor('Mayank Desai',10)   
student2.display()
student2.appointed()

        