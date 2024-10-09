import numpy as np
import time

arr = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]

arr1 = np.array(arr)

t1 = time.time()
a = arr[1:-1]
b = arr[-1:-1]
c = a + b
print(c)
t2 = time.time()

t3 = time.time()
d = arr1[1:-1]
e = arr1[-1:-1]
f = d + e
print(f)
t4 = time.time()

print("binh thuong : ",t2-t1)
print("np ", t4-t3)