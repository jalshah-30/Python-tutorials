#set methods
s1={9,4,5,6,3,5,6,3,19}
s2={10,20,19,25,45}

# print(s1,s2)
# print(s1.union(s2))
# s1.update(s2)
# print(s1)
# s3=s1.intersection(s2)  #displays only the same elemnts in the two set
# s3=s1.symmetric_difference(s2) #emoves the same elements from the two set
# s1.intersection_update(s2)  #changes s1

#isdisjoint() set
# s3=s1.isdisjoint(s2)  #returns true if no common elements are found

#issuperset() 
# s3= s1.issuperset(s2)
# s1.difference_update(s2)

#issubset()
# s3=s1.issubset(s2)  #returns true if all elements of s2 is present in s1

#add()
s1.add("Jal")
s1.remove(6)
item=s1.pop()

# print(s3)
print(s1)
print(item)

#del: is used to delete the entire set 