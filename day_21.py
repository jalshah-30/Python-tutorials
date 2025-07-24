#Function arguments

def default(a=6,b=9):
    print(a,b)

def required(a,b):
    print(a,b)

def number(*numbers):
    sum=0
    for i in  numbers:
        sum=sum+i

    return sum/len(numbers)

default()
required(5,6)
a=number(3)
print(a)


