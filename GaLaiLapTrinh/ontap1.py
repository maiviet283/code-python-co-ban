from abc import ABC,abstractmethod

class Sach(ABC):
    def __init__(self,masach,tieude,tacgia,namxuatban):
        super().__init__()
        self.__masach = masach
        self.__tieude = tieude
        self.__tacgia = tacgia
        self.__namxuatban = namxuatban

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
    def tacgia(self,value):
        self.__tacgia = value
    
    @property
    def namxuatban(self):
        return self.__namxuatban
    
    @namxuatban.setter
    def namxuatban(self,value):
        self.__namxuatban = value

    @abstractmethod
    def thanhTien(self):
        pass

    def __str__(self):
        return f"Ten Sach: {self.__masach} - Tieu De: {self.__tieude} - Tac Gia: {self.__tacgia} - Nam Xuat Ban: {self.__namxuatban}"

class SachGiaoKhoa(Sach):
    def __init__(self, masach, tieude, tacgia, namxuatban, sotrang, phuthu):
        super().__init__(masach, tieude, tacgia, namxuatban)
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
        return self.__sotrang * 200 + self.__phuthu
    
    def __str__(self):
        return super().__str__() + f" - So Trang: {self.__sotrang} - Phu Thu: {self.__phuthu} - Tien: {self.thanhTien()}"
    
class SachTieuThuyet(Sach):
    def __init__(self, masach, tieude, tacgia, namxuatban,sotrang,theloai,rating:int):
        super().__init__(masach, tieude, tacgia, namxuatban)
        if rating < 1 or rating > 5:
            raise ValueError("Loi du lieu")
        self.__sotrang = sotrang
        self.__theloai = theloai
        self.__rating = rating

    @property
    def sotrang(self):
        return self.__sotrang

    @sotrang.setter
    def sotrang(self,sotrang):
        self.__sotrang = sotrang

    @property
    def theloai(self):
        return self.__theloai
    
    @theloai.setter
    def theloai(self,theloai):
        self.__theloai = theloai
    
    @property 
    def rating(self):
        return self.__rating
    
    @rating.setter
    def rating(self,rating):
        self.__rating = rating
    
    def thanhTien(self):
        return self.__sotrang*500 + 0.01*self.__rating*(self.__sotrang*500)
    
    def __str__(self):
        return super().__str__() + f" - So Trang: {self.__sotrang} - The Loai: {self.__theloai} - Rating: {self.__rating} - Tien: {self.thanhTien()}"


sach1 = SachGiaoKhoa(1,"Dac Nhan Tam","viet",2003,1000,5000)
sachtt = SachTieuThuyet(2,"Dc","kaka",2003,100,"da",4)

print(sach1)
print(sachtt)