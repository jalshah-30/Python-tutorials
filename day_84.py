# '''Time Module in Python'''

import time

# def while_loop():
#     i=0
#     while i<50000:
#         i+=1

# def for_loop():
#     for i in range(50000):
#         pass

# a=time.time()
# while_loop()
# b=time.time()
# print("Time for implementing while loop:",b-a)

# x1=time.time()
# for_loop()
# x2=time.time()
# print("Time for For Loop:",x2-x1)


# #time gap/sleep
# print(20)
# time.sleep(5)
# print("5 seconds skipped")

#Local time
t=time.localtime()
formatted_time= time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formatted_time)