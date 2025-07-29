'''Map,Filter and Reduce in Python'''

#map
# def square(x):
#     return x*x

l=[1,3,4,5,7]
'''newl=[]
for lists in list:
    newl.append(square(lists))'''

newl=list(map(lambda x:x*x,l))

print(newl)

#filter
# def filter_func(a):
#     return a<4
new2=list(filter(lambda x:x>4,l))
print(new2)