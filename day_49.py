'''I/O files with python'''

# f=open('myfile.txt','w')
# f.write("My name is god")
# # print(text)

# f.close()
# o=open('myfile.txt','r')
# text=o.read()
# print(text)
# o.close()

# x=open('myfile.txt','a')
# text1=x.write(" and also I am God")
# print(text1)
# x.close()

with open('myfile.txt','a') as f:
    f.write("\n I am in with")


'''by using 'with' no need of close()'''