folder_path = "C:/Users/TechCare/Documents/HTML/PYTHON_CODE/GaLaiLapTrinh/file"
f = open(f"{folder_path}/sinhvien.txt","a",encoding="utf-8")
while True:
    maSV = input("nhap ma sinh vien = ")
    if maSV == "":
        break
    tenSV = input("ten SV = ")
    lop = input("lop = ")
    que = input("que = ")
    f.write("\t".join([maSV,tenSV,lop,que]) + "\n")
f.close()

f = open(f"{folder_path}/sinhvien.txt","r",encoding="utf-8")
print("\t".join(["masv","tensv","lop","que"]))
for sv in f.readlines():
    print(sv.replace("\n",""))
f.close()