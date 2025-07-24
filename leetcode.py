list1=["Jal ","Shah ","is ","boy"]
a=list1[0]+list1[1]+list1[2]+list1[3]

print("Encoding:",a)

x=len(list1[0])
y=len(list1[1])
z=len(list1[2])
x1=len(list1[3])

e1=a[0:x]
e2=a[x:x+y]
e3=a[x+y:x+y+z]
e4=a[x+y+z:x+y+z+x1]

list2=[e1,e2,e3,e4]
print(list2)