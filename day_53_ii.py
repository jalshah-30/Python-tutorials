'''Reduce function in python'''

from functools import reduce

num=[1,3,4,20]
#    [4,4,20]
#    [8,20]
#    [28]

sum = reduce(lambda x,y:x+y ,num)
print(sum)