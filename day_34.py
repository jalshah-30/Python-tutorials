#Dictionary methods

'''set are unordered while dictionaries are ordered from python 3.7 onwards'''

e1={
    19 : 'Good',
    25:'Bad',
    20:'Smartest',
    39:'Normal'
}

e2={
    30:'Normal',
    35:'Smartest',
    19:'Beautiful'
}

e1.update(e2)   #the same one will be updated from e2

'''clear() is use to empty a dictionary'''
print(e1)

# e1.pop(19)
e1.popitem()  #removes the last key

#del : deletes the whole dictionary
del e1[19]  #deletes the specific key
print(e1)