#list methods
lis1=[20,25,10,4,2]
print(lis1)
# lis1.append(19) #use to add in list
# lis1.append("Jal")
# lis1.sort() ascending order
# lis1.sort(reverse=True) #descending order
# print(lis1.index(10))

# lis=lis1
#changes the lis1 as well as lis
# lis=lis1.copy() #only changes in lis will be made and no effect on lis1
# lis[0]=69

lis1.insert(1,19)

l=[19,20]
lis1.extend(l)
l.extend(lis1)
k=l+lis1
print(k)
print(lis1)
