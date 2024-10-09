import numpy as np
ar = np.zeros((8,8))
for column in range(ar.shape[1]):
    if column %2 !=0:
        ar[0:7,column] = 1
    else:
        ar[7,column] = 1
print(ar)