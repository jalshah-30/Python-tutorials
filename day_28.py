# f stings in python {}
# name = "My name is {} {} {}"
            #default  0  1  2
name = "My name is {2} {0} {1}"
fname="Jal"
mname="Tejaskumar"
lname="Shah"
print(name.format(fname,mname,lname))  #sequence matters

#now using fstring
print(f"My name is {fname} {mname} {lname}")

price=2.3373
print(f"Some countries give {price:.2f} in exchange of 1 rupees")
print(f"{19*20}")

#to use general {} in f string
print(f"My name is {fname}{{}}{mname}{{}}{lname}")