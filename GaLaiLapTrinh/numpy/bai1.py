import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,5,2,4,7])
y = np.array([4,2,1,6,4])

font1 = {'color':'blue','size':17}

plt.subplot(2,2,1)
plt.xlabel("hehe 1", fontdict=font1)
plt.ylabel("vc 1")
plt.plot(x,y,marker='o',c='black',lw=2,ls='--',mec='red',mfc='green',ms=17)

plt.subplot(2,2,2)
plt.xlabel("hehe 2")
plt.ylabel("vc 2")
plt.plot(x,y,marker='o',c='black',lw=2,ls='--',mec='red',mfc='green',ms=17)

plt.subplot(2,2,3)
plt.xlabel("hehe 3")
plt.ylabel("vc 3")
plt.grid(axis='x')
plt.plot(x,y,marker='o',c='black',lw=2,ls='--',mec='red',mfc='green',ms=17)

plt.subplot(2,2,4)
plt.xlabel("hehe 4")
plt.ylabel("vc 4")
plt.plot(x,y,marker='o',c='black',lw=2,ls='--',mec='red',mfc='green',ms=17)

plt.suptitle("Hello World")
plt.show()