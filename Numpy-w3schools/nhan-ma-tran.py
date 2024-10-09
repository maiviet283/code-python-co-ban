import numpy as np
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Nhân hai ma trận
matrix_product = np.dot(matrix1, matrix2)
# Kết quả: [[19, 22], [43, 50]]

# Tính tích vô hướng của hai vector
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])
dot_product = np.dot(vector1, vector2)
# Kết quả: 32

print(matrix_product)
print(dot_product)