import pandas as pd

parth_folder = "C:/Users/TechCare/Documents/HTML/PYTHON_CODE/GaLaiLapTrinh/pandas"
name_file = "lap1.txt"
file = open(f"{parth_folder}/{name_file}","a",encoding="utf-8")
while True:
    name = input("name = ")
    if name == "":
        break
    lop = input("lop = ")
    tuoi = int(input("tuoi = "))
    que = input("que = ")
    file.write("\t".join([name,lop,str(tuoi),que]) + "\n")
file.close()

file = open(f"{parth_folder}/{name_file}","r",encoding="utf-8")
print("\t".join(["họ tên","lớp","tuổi","quê quán"]))
for sinhVien in file.readlines():
    print(sinhVien.replace("\n",""))
file.close()

print("Pandas","-"*30)
folder_file = parth_folder + "/" + name_file
banThan = pd.read_csv(folder_file,sep="\t",names=["Ho Ten","Lop","Tuoi","QueQuan"])
print(banThan)

print("Pandas","-"*30)
banThan_Lop = banThan.sort_values("Lop")
print(banThan_Lop)

print("Pandas","-"*30)
banThan_12b1 = banThan.query('Lop == "12b1" or QueQuan == "ha tinh"')
print(banThan_12b1)