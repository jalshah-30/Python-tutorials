'''Decorators in Python'''

def decorators(fx):
    def hello(*args,**kwargs):
        print("Function Starts")
        fx(*args,**kwargs)
        print("Function Ends")
    return hello

@decorators
def main():
    print("Main function")

def add(a,b):
    print(a+b)

decorators(add)(1,2)
main()
# add(10,10)