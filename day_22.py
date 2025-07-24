#introduction to list

list1= [19,20,25,"Jal",False,"Kartikeya","Mayank"]

print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])

print(list1[-3])
print(list1[5-3])
print(list1[len(list1)-3])

if 19 in list1:
    print("Yes")
else:
    print("No")

print(list1)
print(list1[:])

print(list1[1:4])
print(list1[1:6:2]) #jump index

lis2=[i for i in range(5)]
print(lis2)

lis3=[i for i in range(10) if i%2==0]
print(lis3)
