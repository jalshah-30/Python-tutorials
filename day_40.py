#Exercise 4 : Secret code language

name =input("Enter your name:")

if len(name)>=3:
    name1 = name[1:len(name)]
    name2=name1+ name[0]
    temp ='XYZ'
    fname= temp+name2+temp
else:
    a=name[1]
    y1=name.rstrip(a)
    fname=a+y1

print("The scret code generated:",fname)

if len(name)<3:
    realf=y1+a
else:
    x1=fname.rstrip(temp)
    x2=x1.lstrip(temp)
    y=name[0]
    real=x2.rstrip(y)
    realf=name[0]+real
print("Decoding the message again:",realf)