with open('Sample.txt','w') as f:
    f.write('I am good')
    f.truncate(5)  #reads upto 5 only

with open('Sample.txt','r') as z:
    print(z.read())
