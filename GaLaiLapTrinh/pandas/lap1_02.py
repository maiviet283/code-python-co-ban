import pandas as pd

parth_folder = "C:/Users/TechCare/Documents/HTML/PYTHON_CODE/GaLaiLapTrinh/pandas"
name_file = "lap1_02.txt"
parth_folder_file = parth_folder + "/" + name_file
print(parth_folder_file)

file = open(parth_folder_file,"a",encoding="utf-8")
while True:
    msv = input("msv = ")
    if msv == "":
        break
    name = input("name = ")
    age = int(input("age = "))
    address = input("address = ")
    file.write("\t".join([msv,name,str(age),address]) + "\n")
file.close()

file = open(parth_folder_file,"r",encoding="utf-8")
print("\t".join(["msv","name","age","address"]))
for i in file.readlines():
    print(i.replace("\n",""))
file.close()

print("Pandas","-"*30)
friend = pd.read_csv(parth_folder_file,sep="\t",names=["msv","name","age","address"])
print(friend)

print("Pandas","-"*30)
friend_age = friend.sort_values("age")
print(friend_age)

print("Pandas","-"*30)
friend_age_20 = friend.query('age == 20')
print(friend_age_20)