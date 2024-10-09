import numpy as np
# bai 1
z = np.ones((5,5))
z[0,:] = 0
z[-1,:] = 0
z[:,0] = 0
z[:,-1] = 0 
# có thể lấy :,4 nhưng lấy -1 để chắc chắn đó là dòng cuối
# [[0. 0. 0. 0. 0.]
#  [0. 1. 1. 1. 0.]
#  [0. 1. 1. 1. 0.]
#  [0. 1. 1. 1. 0.]
#  [0. 0. 0. 0. 0.]]
print(z)
z[1:-1,1:-1] = 3
print(z)