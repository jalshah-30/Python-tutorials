#Multithreading in Python

import threading
import time
from concurrent.futures import ThreadPoolExecutor


def func(seconds):
     print(f"Sleeping for {seconds} seconds")
     time.sleep(seconds)

# time1=time.perf_counter()
# # Normal Code
# # func(4)
# # func(3)
# # func(5)
# time2=time.perf_counter()
# print(time2-time1)

#Thread code
#  time1=time.perf_counter()
#  t1=threading.Thread(target=func,args=[4])
#  t2=threading.Thread(target=func,args=[3])
#  t3=threading.Thread(target=func,args=[5])

#   t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()

# time2=time.perf_counter()
# print("\n",time2-time1)

def PoolingDemo():
   with ThreadPoolExecutor(max_workers=1) as executor:
    # future1 = executor.submit(func,3)
    # future2 = executor.submit(func,2)
    # future3 = executor.submit(func,5)
    # print(future1.result())
    # print(future2.result())
    # print(future3.result())
    l=[10,20,30,40,50]
    results= executor.map(func,l)

    for result in results:
       print(result)

PoolingDemo()