'''Function Caching in Python'''

import functools
import time

@functools.lru_cache(maxsize=None)    #makes function memoize
def fx(n):
    time.sleep(5)
    return n*5

print(fx(20))
print("done for 20")

print(fx(60))
print("done for 60")

print(fx(13))
print("done for 13")

#valid only when code is runned
#cache gets clear after the code get terminated