#tuples are immutable
t=(20,19,25,10,35)
print(t)
print(t[1])
print(t[-4])
print(len(t))

if 19 in t:
    print("Love is present")
else:
    print("No love")

t1=t[:2]
print(t1)