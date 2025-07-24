'''Read(), Readlines() and other methods'''

# f=open('myfile.txt','r')
# i=0
# while True:
#     i=i+1
#     line =f.readline()
#     if not line:
#         break
#     m1=line.split(",")[0]
#     m2=line.split(",")[1]
#     m3=line.split(",")[2]    #use implicit function if any maths is used
#     print(f"Marks of {i} in S1:{m1}")
#     print(f"Marks of {i} in S2:{m2}")
#     print(f"Marks of {i} in S3:{m3}")
#     print(line)

f=open('myfile.txt','w')
lines=["Jal\n","Tejaskumar\n","Shah\n"]
f.writelines(lines)
f.close()