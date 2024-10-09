import pandas as pd
f = "C:/Users/TechCare/Documents/HTML/PYTHON_CODE/GaLaiLapTrinh/Learn/sinhvien.txt"
sv = pd.read_csv(f,sep="\t",names=["Ma SV","Ten SV","Lop","Que"])
print(sv)

 # sắp xếp theo lớp
print("-"*30)
dssv_lop = sv.sort_values(["Lop"])
print(dssv_lop)

 # trích rút data : thuộc lớp 12b1, quê hà tĩnh
print("-"*30)
sva1 = sv.query('Lop == "12b1" or Que == "hatinh"')
print(sva1)
