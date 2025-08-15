'''Dictonary in python'''

'''dic={
  #key  #value
    10: 'Mayank Desai',
    19: 'Hitanshi Varma',
    20: 'Jal Shah',
    25: 'Kartikeya Dabral',
    35: 'Mayank Patel',
    39: 'Miti Patel'
}

print(dic[19])
print(dic[20])
print(dic[39])
'''

dic2={
    'name':'Jal Shah',
    'age':18,
    'gender':'Male',
    20: 'Enrollment Number'
}
print(dic2['name'])   #Gives error if dict does not contain it
print(dic2.get('name')) #Gives no error if dict does not contain it
print(dic2.keys())  #gives all keys as output

for key in dic2.keys():
    print(f"{key}:{dic2[key]}")

# for key , value in dic2.items():
#     print(f"{key}:{value}")