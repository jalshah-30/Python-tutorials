#docstrings & PEP 8
#docstring string is always made after defining the function
def get_name(name):
    '''Takes name from the user and greets them'''
    print("Have a good day",name)

get_name("Jal")
print(get_name.__doc__)

# import this (Zen of pyhton by tim peters)