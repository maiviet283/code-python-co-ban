class sinhvien():
    def __init__(self,hoten,maSinhVien,queQuan):
        self.hoten = hoten
        self.maSinhVien = maSinhVien
        self.queQuan = queQuan

sv1 = sinhvien("Mai Quoc Viet",123,"Quang ich")
sv2 = sinhvien("Tran Thi Hoai Nam",123,"Ky Dong")
sv3 = sinhvien("Nguyen Tuan Anh",456,"Ky Tay")
sv4 = sinhvien("Vo Thi Kim Anh",789,"Son Hai")

print(f"sv1 ho ten = {sv1.hoten} - que quan = {sv1.queQuan}")