from abc import ABC,abstractmethod

class ConNguoi(ABC):
    def __init__(self,name:str, age:int):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,value):
        if value >= 0:
            self.__age = value
        else:
            raise ValueError("Age > 0")
        
    @abstractmethod
    def TienLuong(self):
        pass

    def __str__(self):
        return f"{self.__name} - {self.__age} Tuoi"
    
class HocSinh(ConNguoi):
    count_hs = 0
    def __init__(self,name:str,age:int,lop:int):
        super().__init__(name,age)
        self.__lop = lop
        HocSinh.dem_hs()
    
    @property
    def lop(self):
        return self.__lop
    
    @lop.setter
    def lop(self,value):
        self.__lop = value

    def TienLuong(self):
        return 0
    
    @classmethod
    def dem_hs(cls):
        cls.count_hs += 1

    @staticmethod
    def thongTin():
        print("-----------"*5)
        print(f"Ten Lop : {HocSinh.__name__}")
        print(f"Lop Cha : {HocSinh.__base__}")
        print(f"Tong So Luong : {HocSinh.count_hs}")

    def __str__(self):
        return super().__str__() + f" - Lop : {self.__lop} - Luong {self.TienLuong()}"
    

class GiaoVien(ConNguoi):
    count_gv = 0
    def __init__(self,name:str,age:int,hesoluong:float):
        super().__init__(name,age)
        self.__hesoluong = hesoluong
        GiaoVien.dem_gv()

    @property
    def hesoluong(self):
        return self.__hesoluong
    
    @hesoluong.setter
    def hesoluong(self,value):
        self.__hesoluong = value

    def TienLuong(self):
        return self.__hesoluong * 1000
    
    @classmethod
    def dem_gv(cls):
        cls.count_gv += 1

    @staticmethod
    def thongTin():
        print("-----------"*5)
        print(f"Ten Lop : {GiaoVien.__name__}")
        print(f"Lop Cha : {GiaoVien.__base__}")
        print(f"Tong So Luong : {GiaoVien.count_gv}")

    def __str__(self):
        return super().__str__() + f" - He So Luong : {self.__hesoluong} -> Luong = {self.TienLuong()}"


class QuanLy():
    count_tv = 0
    def __init__(self):
        self.ds = []

    def them(self,nguoi:ConNguoi):
        self.ds.append(nguoi)
        QuanLy.dem_tv()
    
    @classmethod
    def dem_tv(cls):
        cls.count_tv += 1

    def hienThi(self):
        for conNguoi in self.ds:
            print(conNguoi)
        print(f"Tong co {QuanLy.count_tv} Thanh Vien")

hs1 = HocSinh("Viet",21,12)
hs2 = HocSinh("An",21,22)
hs3 = HocSinh("Viet",21,12)
hs4 = HocSinh("An",21,22)

gv1 = GiaoVien("An",21,50)
gv2 = GiaoVien("Ba",33,70)
gv3 = GiaoVien("Ba",33,70)
gv4 = GiaoVien("Ba",33,70)
gv5 = GiaoVien("Ba",33,70)
gv6 = GiaoVien("Ba",33,70)

quanly = QuanLy()
quanly.them(hs1)
quanly.them(hs2)
quanly.them(gv3)
quanly.them(gv4)

quanly.hienThi()
