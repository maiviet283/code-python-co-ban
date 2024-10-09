from abc import ABC,abstractmethod

class Sach(ABC):
    def __init__(self,masach,tieude,tacgia,nxb):
        self.__masach = masach
        self.__tieude =tieude
        self.__tacgia = tacgia
        self.__nxb = nxb

    @property
    def masach(self):
        return self.__masach
    
    @masach.setter
    def masach(self,masach):
        self.__masach = masach

    @property
    def tieude(self):
        return self.__tieude
    
    @tieude.setter
    def tieude(self,tieude):
        self.__tieude = tieude

    @property
    def tacgia(self):
        return self.__tacgia
    
    @tacgia.setter
    def tacgia(self,tacgia):
        self.__tacgia = tacgia

    @property
    def nxb(self):
        return self.__nxb
    
    @nxb.setter
    def nxb(self,nxb):
        self.__nxb = nxb

    @abstractmethod
    def thanhTien(self):
        pass

    def __str__(self):
        return f"Ma Sach : {self.__masach} - Tieu De : {self.__tieude} - Tac Gia : {self.__tacgia} - NXB : {self.__nxb}"
    
class SachGiaoKhoa(Sach):
    def __init__(self, masach, tieude, tacgia, nxb, sotrang, phuthu):
        super().__init__(masach, tieude, tacgia, nxb)
        self.__sotrang = sotrang
        self.__phuthu = phuthu

    @property
    def sotrang(self):
        return self.__sotrang
    
    @sotrang.setter
    def sotrang(self, sotrang):
        self.__sotrang = sotrang

    @property
    def phuthu(self):
        return self.__phuthu
    
    @phuthu.setter
    def phuthu(self, phuthu):
        self.__phuthu = phuthu
    
    def thanhTien(self):
        return self.__sotrang*200 + self.__phuthu
    
    def __str__(self):
        return super().__str__() + f" - So Trang : {self.__sotrang} - Phu Thu : {self.__phuthu} => Tien : {self.thanhTien()} VND"
    
class SachTieuThuyet(Sach):
    def __init__(self, masach, tieude, tacgia, nxb, sotrang, theloai, rating):
        super().__init__(masach, tieude, tacgia, nxb)
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
        return super().__str__() + f" - So Trang : {self.__sotrang} - The Loai : {self.__theloai} - RaTing : {self.__rating} => Tien : {self.thanhTien()} VND"
    
class QuanLyQuanSach:
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
    
sach1 = SachGiaoKhoa(1,"Dac Nhan Tam","Viet Mau","Kim Dong",1000,5000)
sach2 = SachGiaoKhoa(2,"Nha Gia Kim","Binh Cot","Chiu",500,3000)
sach3 = SachTieuThuyet(3,"Doraemon","Fukada","KD",1200,"Anime",4)
sach4 = SachTieuThuyet(4,"Conan","Eimil","KD",400,"Anime",10)

quanly = QuanLyQuanSach()
quanly.themSach(sach1)
quanly.themSach(sach3)
quanly.themSach(sach4)
quanly.themSach(sach2)
quanly.hienThiSach()
print(f"Tong Tien = {quanly.tongGiaSach()} VND")