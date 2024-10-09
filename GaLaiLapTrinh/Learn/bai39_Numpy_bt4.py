import numpy as np
l =[[1,4,3,7],
    [2,0,1,8]]
ar = np.array(l)
ar2 = np.zeros((ar.shape[1], ar.shape[0]))
print(ar2)
dem = 0
for i in ar:
    ar2[:,dem] = i
    dem+=1
print(ar2)