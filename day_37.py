#finally keyword in python

# try:
#     b=int(input("Enter a number:"))
#     print(b)
# except:
#     print("Enter a valid number")
# finally:
#     print("I am executed")
'''Finally is executed no matter if it is in try or except'''
'''It is also executed even if we use return'''

def fun():
    try:
        a=int(input("Enter a number:"))
        print(a)
        return 0
    except:
        print("Error enter a proper")
        return 1
    finally:
        print("I am executed")

x=fun()
print(x)