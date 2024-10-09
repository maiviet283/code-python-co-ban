import pandas as pd

parth_folder = "C:/Users/TechCare/Documents/HTML/PYTHON_CODE/GaLaiLapTrinh/pandas"
file_name = "lap1_01.txt"
parth_folder_file = parth_folder + "/" + file_name
file = open(parth_folder_file,"a",encoding="utf-8")
while True:
    hoTen = input("Ho va Ten = ")
    if hoTen == "":
        break
    tuoi = int(input("Tuoi = "))
    gioiTinh = input("Gioi Tinh = ")
    queQuan = input("Que Quan = ")
    file.write("\t".join([hoTen,str(tuoi),gioiTinh,queQuan]) + "\n")
file.close()

file = open(parth_folder_file,"r",encoding="utf-8")
print("\t".join(["Ho ten","tuoi","gioi tinh","que quan"]))
for i in file.readlines():
    print(i.replace("\n",""))
file.close()

print("Pandas","-"*30)
hoiBanThan = pd.read_csv(parth_folder_file,sep="\t",names=["HoTen","Tuoi","GioiTinh","QueQuan"])
print(hoiBanThan)

print("Pandas","-"*30)
hoiBanThan_tuoi = hoiBanThan.sort_values("Tuoi")
print(hoiBanThan_tuoi)

print("Pandas","-"*30)
hoiBanThan_que = hoiBanThan.query('GioiTinh=="nu"')
print(hoiBanThan_que)