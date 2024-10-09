from abc import ABC,abstractmethod

class Nguoi(ABC):
    def __init__(self,ten:str,tuoi:int):
        if tuoi <= 0:
            tuoi = 1
        self.__ten = ten
        self.__tuoi = tuoi
    
    @property
    def ten(self):
        return self.__ten
    
    @ten.setter
    def ten(self,ten):
        self.__ten = ten

    @property
    def tuoi(self):
        return self.__tuoi
    
    @tuoi.setter
    def tuoi(self,tuoi):
        if tuoi <= 0:
            tuoi = 1
        self.__tuoi = tuoi

    @abstractmethod
    def tongLuong(self):
        pass

    def __str__(self):
        return f"Ten : {self.__ten} - Tuoi : {self.__tuoi}"
    
class NhanVien(Nguoi):
    def __init__(self, ten: str, tuoi: int, hesoluong:float):
        super().__init__(ten, tuoi)
        if hesoluong <= 0:
            hesoluong = 1
        self.__hesoluong = hesoluong

    @property
    def hesoluong(self):
        return self.__hesoluong
    
    @hesoluong.setter
    def hesoluong(self, hesoluong):
        if hesoluong <= 0:
            hesoluong = 1
        self.__hesoluong = hesoluong

    def tongLuong(self):
        return self.__hesoluong * 1800000
    
    def __str__(self):
        return super().__str__() + f" - He So Luong : {self.__hesoluong} => Luong = {self.tongLuong()} VND ({NhanVien.__name__})"
    
class QuanLy(Nguoi):
    def __init__(self, ten: str, tuoi: int, hesoluong:float, phucapquanly:int):
        super().__init__(ten, tuoi)

        if hesoluong <= 0:
            hesoluong = 1
        if phucapquanly < 0:
            phucapquanly = 0

        self.__hesoluong = hesoluong
        self.__phucapquanly = phucapquanly

    @property
    def hesoluong(self):
        return self.__hesoluong
    
    @hesoluong.setter
    def hesoluong(self, hesoluong):
        if hesoluong <= 0:
            hesoluong = 1
        self.__hesoluong = hesoluong

    @property
    def phucapquanly(self):
        return self.__phucapquanly
    
    @phucapquanly.setter
    def phucapquanly(self, phucapquanly):
        if phucapquanly < 0:
            phucapquanly = 0
        self.__phucapquanly = phucapquanly

    def tongLuong(self):
        return self.__hesoluong*1800000 + self.__phucapquanly
    
    def __str__(self):
        return super().__str__() + f" - He So Luong : {self.__hesoluong} - Phu Cap : {self.__phucapquanly} => Luong = {self.tongLuong()} VND ({QuanLy.__name__})"
    
class QuanLyNhanSu():
    def __init__(self):
        self.ds_nhansu = []

    def themNhanSu(self,nhansu:Nguoi):
        self.ds_nhansu.append(nhansu)

    def hienThiNhanSu(self):
        for nhansu in self.ds_nhansu:
            print(nhansu)

    def tongLuong(self):
        tong = 0
        for nhansu in self.ds_nhansu:
            tong += nhansu.tongLuong()
        return tong
    
nhanvien1 = NhanVien("Viet",21,3)
nhanvien2 = NhanVien("Thin",30,10)
nhanvien3 = NhanVien("Yasuo",25,-9)

quanly1 = QuanLy("An",26,4.5,3000000)
quanly2 = QuanLy("Be",29,5.5,4000000)

# doi tuong quan ly nhan su
quanlynhansu = QuanLyNhanSu()
#them nhan vien
quanlynhansu.themNhanSu(nhanvien1)
quanlynhansu.themNhanSu(nhanvien3)
#them quan ly
quanlynhansu.themNhanSu(quanly2)

quanlynhansu.hienThiNhanSu()

print(f"Tong Tien = {quanlynhansu.tongLuong()} VND")