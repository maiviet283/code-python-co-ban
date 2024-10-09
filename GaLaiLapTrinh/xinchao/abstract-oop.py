from abc import ABC,abstractmethod

class Sach(ABC):
    def __init__(self,masach,tieude,tacgia,nhaxuatban):
        self.__masach = masach
        self.__tieude =tieude
        self.__tacgia = tacgia
        self.__nhaxuatban = nhaxuatban
    
    @property
    def masach(self):
        return self.__masach
    
    @masach.setter
    def masach(self, value):
        self.__masach = value

    @property
    def tieude(self):
        return self.__tieude
    
    @tieude.setter
    def tieude(self, value):
        self.__tieude = value

    @property
    def tacgia(self):
        return self.__tacgia
    
    @tacgia.setter
    def tacgia(self, value):
        self.__tacgia = value

    @property
    def nhaxuatban(self):
        return self.__nhaxuatban
    
    @nhaxuatban.setter
    def nhaxuatban(self,value):
        self.__nhaxuatban = value

    @abstractmethod
    def thanhTien(self):
        pass

    def __str__(self):
        return f"Ma Sach : {self.__masach} - Tieu De : {self.__tieude} - Tac Gia : {self.__tacgia} - NXB : {self.__nhaxuatban}"
    
class SachGiaoKhoa(Sach):
    def __init__(self, masach, tieude, tacgia, nhaxuatban, sotrang, phuthu):
        super().__init__(masach, tieude, tacgia, nhaxuatban)
        self.__sotrang = sotrang
        self.__phuthu = phuthu

    @property
    def sotrang(self):
        return self.__sotrang
    
    @sotrang.setter
    def sotrang(self, value):
        self.__sotrang = value

    @property
    def phuthu(self):
        return self.__phuthu
    
    @phuthu.setter
    def phuthu(self, value):
        self.__phuthu = value

    def thanhTien(self):
        return self.__sotrang * 200 + self.__phuthu
    
    def __str__(self):
        return super().__str__() + f" - So Trang : {self.__sotrang} - Phu Thu : {self.__phuthu} => Don Gia : {self.thanhTien()}"
    
class SachTieuThuyet(Sach):
    def __init__(self, masach, tieude, tacgia, nhaxuatban, sotrang, theloai, rating):
        super().__init__(masach, tieude, tacgia, nhaxuatban)
        if rating < 1 or rating > 5:
            rating = 1
        self.__sotrang = sotrang
        self.__theloai = theloai
        self.__rating = rating

    @property
    def sotrang(self):
        return self.__sotrang
    
    @sotrang.setter
    def sotrang(self, sotrang):
        self.__sotrang = sotrang

    @property
    def theloai(self):
        return self.__theloai
    
    @theloai.setter
    def theloai(self, theloai):
        self.__theloai = theloai

    @property
    def rating(self):
        return self.__rating
    
    @rating.setter
    def rating(self, rating):
        self.__rating = rating

    def thanhTien(self):
        return self.__sotrang*500 + 0.01*self.__rating*(self.__sotrang*500)
    
    def __str__(self):
        return super().__str__() + f" - So Trang : {self.__sotrang} - The Loai : {self.__theloai} - Rating = {self.__rating} => Don Gia : {self.thanhTien()}"
    
class QuanLyQuanSach():
    def __init__(self):
        self.ds_sach = []

    def themSach(self,sach:Sach):
        self.ds_sach.append(sach)

    def hienThiSach(self):
        for sach in self.ds_sach:
            print(sach)

    def tongGiaSach(self):
        tong = 0
        for sach in self.ds_sach:
            tong += sach.thanhTien()
        return tong
    
sach1 = SachGiaoKhoa(1,"Cat","Dog","MonKey",1000,5000)
sach2 = SachGiaoKhoa(2,"Tree","Wallet","Lazy",1000,6000)
sach3 = SachTieuThuyet(3,'House','Car','Ben',1500,'Anime',1)
sach4 = SachTieuThuyet(4,'Yasuo','Xe','Zed',1500,'Anime',2)

quanly = QuanLyQuanSach()
quanly.themSach(sach1)
quanly.themSach(sach2)
quanly.themSach(sach3)
quanly.themSach(sach4)
quanly.hienThiSach()
print(f"TONG TIEN = {quanly.tongGiaSach()}")