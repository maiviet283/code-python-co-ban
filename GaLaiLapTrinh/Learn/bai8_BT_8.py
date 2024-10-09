# BT8 : 
t = int(input("thang = "))
if t  in (1,3,5,7,8,12,10) :
    print(f"thang {t} co 31 ngay")
elif t in (4,6,9,11) :
    print("thang ",t," co 30 ngay")
elif t==2:
    nam = int(input("nam = "))
    if (nam%4==0 and nam%100!=0) or nam%400==0:
        print(f"thang {t} nam {nam} co 29")
    else : print(f"thang {t} nam {nam} co 28ngay")
else : print("sai du lieu thang")