'''Instance variable v/s Class variable'''

class Student:
    School_Name="GPS"    #Class variable by default to all instance
    No_of_Students=0
    def __init__(self,name):
        self.name=name
        self.grace= 0.5    #instance variable
        Student.No_of_Students+=1
    
    def show_student(self):
        print(f"The name of student is {self.name} and will get {self.grace} grace marks")
        print(f"Student from {self.School_Name}" )
        print("No.of Students:",self.No_of_Students)
x= Student("Jal")
x.grace=0.7
x.School_Name="DPS"
x.show_student()

Student.School_Name="PCPS"
print(Student.School_Name)

y=Student("Mayank")
y.School_Name="JPS"
y.show_student()


#If instance variable is given for a object then it will go for it , rather going for class
#class variable