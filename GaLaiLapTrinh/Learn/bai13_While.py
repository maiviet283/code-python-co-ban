
# n = int(input("n = "))
# while n<1 or n>99:
#     n = int(input("nhap lai n = "))
# print(f"so ban vua nhap la {n}")

while True:
    hten = input("nhap ten : ")
    mhoc = input("mon hoc : ")
    diem = float(input("diem = "))
    print(f"hoc sinh {hten} , du thi mon {mhoc} , diem : {diem}")
    if (diem >= 7): print("dat")
    else : print("khong dat") 
    hoi = input("nhap n de thoat hoac bam phim bat ky de tt : ")
    if hoi == "n" or hoi == "N": break