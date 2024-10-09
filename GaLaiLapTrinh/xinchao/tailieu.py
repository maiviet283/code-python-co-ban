from abc import ABC,abstractmethod

class TaiLieu(ABC):
    def __init__(self,maso,tieude,namxuatban,dongia):
        self.__maso = maso
        self.__tieude =tieude
        self.__namxuatban = namxuatban
        self.__dongia = dongia

    @property
    def maso(self):
        return self.__maso
    
    @maso.setter
    def maso(self, value):
        self.__maso = value

    @property
    def tieude(self):
        return self.__tieude
    
    @tieude.setter
    def tieude(self, value):
        self.__tieude = value

    @property
    def namxuatban(self):
        return self.__namxuatban
    
    @namxuatban.setter
    def namxuatban(self, value):
        self.__namxuatban = value

    @property
    def dongia(self):
        return self.__dongia
    
    @dongia.setter
    def dongia(self, value):
        self.__dongia = value

    @abstractmethod
    def thanhTien(self):
        pass

    def __str__(self):
        return f"Ma So : {self.__maso} - Tieu De : {self.__tieude} - NXB : {self.__namxuatban} - Don Gia : {self.__dongia}"
    
class Sach(TaiLieu):
    def __init__(self, maso, tieude, namxuatban, dongia, tacgia):
        super().__init__(maso, tieude, namxuatban, dongia)
        self.__tacgia = tacgia

    @property
    def tacgia(self):
        return self.__tacgia
    
    @tacgia.setter
    def tacgia(self,value):
        self.__tacgia = value

    def thanhTien(self):
        return self.dongia + self.dongia*0.1
    
    def __str__(self):
        return super().__str__() + f" - Tac Gia : {self.__tacgia} => Tien : {self.thanhTien()}"
    
class TapChi(TaiLieu):
    def __init__(self, maso, tieude, namxuatban, dongia, sophathanh):
        super().__init__(maso, tieude, namxuatban, dongia)
        self.__sophathanh = sophathanh

    @property
    def sophathanh(self):
        return self.__sophathanh
    
    @sophathanh.setter
    def sophathanh(self, value):
        self.__sophathanh = value

    def thanhTien(self):
        return self.dongia + self.dongia*0.15 # Thue 15%
    
    def __str__(self):
        return super().__str__() + f" - So Phat Hanh : {self.__sophathanh} => Tien : {self.thanhTien()}"
    
class DVD(TaiLieu):
    def __init__(self, maso, tieude, namxuatban, dongia, daodien):
        super().__init__(maso, tieude, namxuatban, dongia)
        self.__daodien = daodien

    @property
    def daodien(self):
        return self.__daodien
    
    @daodien.setter
    def daodien(self, value):
        self.__daodien = value

    def thanhTien(self):
        return self.dongia + self.dongia*0.2 #Thue 20%
    
    def __str__(self):
        return super().__str__() + f" - Dao Dien : {self.__daodien} => Tien : {self.thanhTien()}"
    
class QuanLyThuVien:
    def __init__(self):
        self.ds_tailieu = []

    def themTaiLieu(self,tailieu:TaiLieu):
        self.ds_tailieu.append(tailieu)

    def hienThiTaiLieu(self):
        for tailieu in self.ds_tailieu:
            print(tailieu)

    def tongGiaTriTaiLieu(self):
        tong = 0
        for tailieu in self.ds_tailieu:
            tong += tailieu.thanhTien()
        return tong
    
tailieu1 = Sach(1,"Sach 1",2000,3000,2)
tailieu2 = TapChi(2,'Sach 2',2003,15000,4)
tailieu3 = DVD(3,'Sach 3',2015,20000,'DORA')

quanly = QuanLyThuVien()
quanly.themTaiLieu(tailieu1)
quanly.themTaiLieu(tailieu2)
quanly.themTaiLieu(tailieu3)
quanly.hienThiTaiLieu()
print("Tong Tien = ",quanly.tongGiaTriTaiLieu())
