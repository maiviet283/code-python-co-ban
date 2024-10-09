"""
    def name (list tham số) :
        khối lệnh thực thi
        có đối số : có return -> đẩy về giá trị nào đó
        ko có đối số : ko có return -> 
"""

def Cong(x,y):
    return x+y

def Tru(x,y):
    return x-y

def PTb1(a,b): # ax + b = 0
    if a==0 and b==0 : return "Vô số nghiệm"
    elif a==0 and b!=0 : return "Vô nghiệm"
    else : return f"x = {-(b/a)}"

def XuatChuoi(chuoi):
    print(chuoi)

def N(n):
    if n%2==0:
        for i in range(1,n+1,1):
            for j in range(1,n+1,1):
                if i==j or j==1 or j==n :
                    print("*",end=" ")
                else : print(" ",end=" ")
            print()
    else :
        for i in range(1,n+1,1):
            for j in range(1,n+1,1):
                if j==1 or j==n or j+i==n+1:
                    print("*",end=" ")
                else: print(" ",end=" ")
            print()

N(7)