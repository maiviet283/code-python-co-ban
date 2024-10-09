dict_01 = {
    "A":1,"B":2,"C":3,"D":2,"E":1,"F":4,"G":2,
    "H":4,"I":1,"J":8,"K":5,"L":1,"M":3,"N":1,
    "O":1,"P":3,"Q":10,"R":1,"S":1,"T":1,"U":1,
    "V":4,"W":4,"X":8,"Y":4,"Z":10
}
str_1="University of Technology and Education"
print("KT = ",end=" ")
for i in dict_01:
    print(i, end=" ")
print()
print("KT = ",end=" ")
tong = 0
for i in dict_01:
    print(dict_01[i],end=" ")
    tong += dict_01[i]
print()
print("Tong = ",tong)
print(str_1.upper())
for i in str_1.upper():
    if i == " ":
        print(" ",end="")
        continue
    print(dict_01[i],end="")