import time
"""
for i in range(0,7,1):
    for j in range(0,7,1):
        if i==j or (j==0) or j==6 : print("*",end=" ")
        else : print(" ",end=" ")
    print()
"""
# t = time.localtime()
# t2 = time.strftime("%Y-%m-%d")
# print(t2)

# s = "Adswerwe#Asa"
# ss = "ii"
# print(s.upper())

# a = input("string :")
# a2 = ""
# for i in a :
#     if i.islower() : i = i.upper()
#     else : i = i.lower()
#     a2+=i
# print(a2)

a = "asdf/adsf:ad:Da/d"
print(a.split(":"))
print(a.split(":")[1])
aa = a.split(":")
a2 = "=".join(aa)
print(a2)