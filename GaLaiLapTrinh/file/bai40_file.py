folder_path = "C:/Users/TechCare/Documents/HTML/PYTHON_CODE/GaLaiLapTrinh/file"
# with open(f"{folder_path}/bai40_file.txt","w",encoding="utf-8") as f:
#     for i in range(10):
#         f.write(f"day la dong thu {i} \n")

f = open(f"{folder_path}/bai40_file.txt","r",encoding="utf-8")
# print(f.read()) doc toan bo
#print("-------------")
#print(f.readline()) # doc 1 dong
#print(f.readline()) # doc 2 dong
#print(f.readline()) # doc 3 dong

print(f.readlines()) # in toan bo print(f.readlines()[2]) : dong thu 2
f.close()