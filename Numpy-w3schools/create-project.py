import numpy as np

arr = np.array([1,2,3,4,5,6])
arr2 = np.array([[1,2,3],[1,2,3]])
arr3 = np.array([[[1,2,3],[1,2,3]],[[4,5,6],[4,5,6]]])
print(arr3)
print(arr.ndim)
print(arr2.ndim)
print(arr3.ndim)