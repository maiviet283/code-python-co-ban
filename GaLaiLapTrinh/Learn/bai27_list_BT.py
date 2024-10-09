# nhập số lượng của list , sau đó gán dữ liệu ngầu nhiên vào từng Ptử
from random import randrange
n = int(input("so phan tu trong list la : "))
lst = []
if n<0 or n>100:
    print("chay lai chuong trinh roi nhap lai")
elif n==0:
    lst.append(randrange(1,101))
    print(lst)
else:
    for i in range(0,n):
        lst.append(randrange(0,101))
    print(lst)
