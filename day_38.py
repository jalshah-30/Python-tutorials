#raising custom errors
x =int(input("Enter the value of x(1-10):"))

if(x<1 or x>10):
    raise ValueError("Please enter accordingly")

'''Raise basically ends the program and shows error according to coder'''