def roi(doanhthu,chiphi):
    return (doanhthu-chiphi)/chiphi

def QuyetDinhDauTu(roi):
    if roi >= 0.75 : 
        return "Nên đầu tư"
    else : return "Không nên đầu tư"

print("Chương trình tính ROI")
cp = float(input("Chi phí : "))
dt = float(input("Doanh thu : "))
b = roi(dt,cp)
a = QuyetDinhDauTu(b)
print(a)
print(f"tỷ lệ ROI = {b}")