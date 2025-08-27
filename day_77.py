'''Operator Overloading'''

class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self,temp):
        return Vector(self.i+temp.i,self.j+temp.j,self.k+temp.k)

v1=Vector(3,4,5)
print(v1)
v2= Vector(7,8,9)
print(v2)

print(v1+v2)
print(type(v1+v2))