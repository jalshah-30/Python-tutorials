'''seek(),tell() and other function in python'''

with open('file.txt','r') as f:
    print(type(f))
    # x=f.tell()  gives 0 as output
    f.seek(10)     #10 byte gets skip/seeks
    x=f.tell()
    data =f.read(5)
    print(data)
    print(x)