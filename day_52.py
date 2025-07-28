'''Lambda function in python'''

'''def square(a):
    return a*a'''

#instead of using function we can use lambda

def appl(fx,value):
    return 20 + fx(value)
square= lambda a: a*a
avg= lambda x,y,z:(x+y+z)/3

print(square(5))
print(avg(3,4,5))
print(appl(square,5))