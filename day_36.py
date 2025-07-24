'''Exception Handling'''

try:
    a=int(input("Enter a number:"))
    num =[19,20]
    print(num[a])
except ValueError:
    print("Please enter proper integer!!")
except IndexError:
    print("Enter a valid index for given array")    