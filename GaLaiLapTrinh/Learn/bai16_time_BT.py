import time
ten = input("Nhập tên : ")
tuoi = int(input("Nhập tuổi : "))
htai = time.localtime()
namHienTai = htai.tm_year
namSinh = namHienTai - tuoi
nam100t = namSinh + 100
print(f"Năm sinh = {namSinh}")
print(f"Năm 100 tuổi = {nam100t}")
print(f"Sau {nam100t - namHienTai} năm bạn {ten} sẽ 100 tuổi")