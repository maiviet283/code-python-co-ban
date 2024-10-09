# BT7 : tính năm nhuận 
nam = int(input("nam = "))
if (nam%4 == 0 and nam%100!= 0) or nam%400==0 :
    print(nam," la nam nhuan")
else : print(nam, " khong phai la nam nhuan") 