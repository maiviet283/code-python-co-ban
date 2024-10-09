import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Đọc dữ liệu từ file CSV
df = pd.read_csv('data.csv')

# Lấy 10 giá trị cuối cùng của cột Duration và Pulse
x = np.array(df["Duration"].tail(10))
y = np.array(df["Pulse"].tail(10))

# Thiết lập font chữ cho tiêu đề và nhãn trục
font1 = {'color':'brown','size':21}
font2 = {'color':'black','size':17}

# Tạo biểu đồ đường ở subplot thứ nhất
plt.subplot(1, 2, 1)
plt.xlabel("Duration", fontdict=font2)
plt.ylabel("Pulse", fontdict=font2)
plt.grid(color="red")
plt.plot(x, y, c='blue', mec='red', mfc='green', ms=20, marker='o', lw=3, ls=':')

# Tạo biểu đồ cột ở subplot thứ hai
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 12, 9]

plt.subplot(1, 2, 2)
plt.xlabel("Duration", fontdict=font2)
plt.ylabel("Pulse", fontdict=font2)
plt.grid(color="yellow")
plt.bar(x, y, color='blue', edgecolor='red')

# Thiết lập tiêu đề chung cho cả hai biểu đồ
plt.suptitle("Read Data from csv file")
plt.show()
