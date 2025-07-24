#Tuple method
#tuple to list
t=("Jal","Mayank","Kartikeya","Heet")
print(t)
l=list(t)
l.pop(1)
l.insert(1,"Maharshi")
t=tuple(l)
print(t)

#tuples catenation
t1=("Jal","Boy")
t2=("Nisarg","Shah")
t3 = t1+t2
print(t3)

#count()
# x=t3.count("Shah")
# print(x)
# if(x<3):
#     while(x<3):
#         temp=list(t3)
#         temp.append("Shah")
#         t3=tuple(temp)
#         x=x+1
# print(t3)

#index()
x=t3.index("Shah")
print(x)
print(t3.index("Shah",0,3))