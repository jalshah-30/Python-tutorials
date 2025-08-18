#static methods in python

'''@staticmethod'''

class Math:
    def __init__(self,n):
        self.num=n
    
    def subtract(self,x):
        self.num= self.num-x

    @staticmethod
    def sub(x,y):
        return x-y
    
m = Math(20)
print(m.num)
m.subtract(10)
print(m.num)
print(m.sub(20,10))            # Way 1 to call static func
print(Math.sub(20,10))         # Way 2 to call static func