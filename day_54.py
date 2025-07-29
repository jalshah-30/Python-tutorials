# 'is' vs '==' in python

a=[1,3,4]
b=[1,3,4]

print(a is b)   #exact location of the object in memory
'''Gives true if the values given are immutable ex: tuples,none etc'''
print(a == b)   #values