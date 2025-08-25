'''Method Overriding in Python'''

class Shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def area(self):
        return self.x*self.y

class circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        super().__init__(radius,radius)
    
    def area(self):
        return super().area()*3.14

rectangle=Shape(4,5)
print(rectangle.area())

c=circle(3)
print(c.area())