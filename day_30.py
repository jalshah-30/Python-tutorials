#recursion

def factorial(number):
    if number==0 or number==1:
        return 1
    else:
        return number*factorial(number-1)
    
x= int(input("Enter the number to get factorial:"))
print("Factorial of the number:",factorial(x))

#swaping of two numbers
def swaping(a,b):
    temp=0
    temp=a
    a=b
    b=temp
    print(a,b)

swaping(19,20)

#fibonacci series
def fibonacci(a):
    if a<=1:
        return a
    else:
        return fibonacci(a-2)+fibonacci(a-1)
    
a=7
for i in range(a+1):
    print(fibonacci(i))
    i=i+1