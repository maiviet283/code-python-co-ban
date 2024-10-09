from abc import ABC,abstractmethod

class Sach(ABC):
    def __init__(self,masach,tieude,tacgia,namxuatban):
        self.__masach = masach
        self.__tieude = tieude
        self.__tacgia = tacgia
        self.__namxuatban = namxuatban

    @property
    def masach(self):
        return self.__masach

    @property
    def tieude(self):
        return self.__tieude
    
    @property
    def tacgia(self):
        return self.__tacgia
    
    @property
    def namxuatban(self):
        return self.__namxuatban
    
    @masach.setter
    def masach(self,masach):
        self.__masach = masach

    @tieude.setter
    def tieude(self,tieude):
        self.__tieude = tieude
    
    @tacgia.setter
    def tacgia(self,tacgia):
        self.__tacgia = tacgia

    @namxuatban.setter
    def namxuatban(self,namxuatban):
        self.__namxuatban = namxuatban

    @abstractmethod
    def thanhTien(self):
        pass

    def __str__(self):
        return f"MaSach:{self.__masach}-TieuDe:{self.__tieude}-TacGia:{self.__tacgia}-NXB:{self.__namxuatban}"
    
class SachGiaoKhoa(Sach):
    def __init__(self, masach, tieude, tacgia, namxuatban, sotrang, phuthu):
        super().__init__(masach, tieude, tacgia, namxuatban)
        self.__sotrang = sotrang
        self.__phuthu = phuthu

    @property
    def sotrang(self):
        return self.__sotrang
    
    @property 
    def phuthu(self):
        return self.__phuthu
    
    @sotrang.setter
    def sotrang(self, sotrang):
        self.__sotrang = sotrang

    @phuthu.setter
    def phuthu(self, phuthu):
        self.__phuthu = phuthu

    def thanhTien(self):
        return self.__sotrang*200 + self.__phuthu

    def __str__(self):
        return super().__str__() + f"SoTrang:{self.__sotrang}-PhuThu:{self.__phuthu} => Tien : {self.thanhTien()}"

class SachTieuThuyet(Sach):
    def __init__(self, masach, tieude, tacgia, namxuatban, sotrang, theloai, rating):
        super().__init__(masach, tieude, tacgia, namxuatban)
        if rating < 1 or rating > 5:
            rating = 1
        self.__sotrang = sotrang
        self.__theloai = theloai
        self.__rating = rating

    @property
    def sotrang(self):
        return self.__sotrang
    
    @property
    def theloai(self):
        return self.__theloai
    
    @property
    def rating(self):
        return self.__rating
    
    @sotrang.setter
    def sotrang(self, sotrang):
        self.__sotrang = sotrang

    @theloai.setter
    def theloai(self, theloai):
        self.__theloai = theloai

    @rating.setter
    def rating(self, rating):
        self.__rating = rating

    def thanhTien(self):
        return self.__sotrang*500 + 0.01*self.__rating*(self.__sotrang*500)

    def __str__(self):
        return super().__str__() + f"SoTrang:{self.__sotrang}-TheLoai:{self.__theloai}-Rating:{self.__rating} => Tien : {self.thanhTien()}"
    
class QuanLyQuanSach():
    def __init__(self):
        self.ds_sach = []
    
    def themsach(self,sach:Sach):
        self.ds_sach.append(sach)

    def hienThiSach(self):
        for sach in self.ds_sach:
            print(sach)
    
    def tongGiaSach(self):
        tong = 0
        for sach in self.ds_sach:
            tong += sach.thanhTien()
        return tong

sach1 = SachGiaoKhoa(1,"Đắc Nhân Tâm","Không Biết",2000,1000,5000)
sach2 = SachGiaoKhoa(2,"Nhà Giả Trân","Chịu",2000,1000,2000)
sach3 = SachTieuThuyet(3,"Doraemon","KaKa",2123,755,"Anime",3)
sach4 = SachTieuThuyet(4,"Connan","KaKa",2123,755,"Anime",7)

quanly = QuanLyQuanSach()

quanly.themsach(sach1)
quanly.themsach(sach2)
quanly.themsach(sach3)

quanly.hienThiSach()
print(f"Tổng Tiền = {quanly.tongGiaSach()}")