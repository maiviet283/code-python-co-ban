class Bank():
    def __init__(self, hoten:str, cmt:int):
        self.hoten = hoten
        self.cmt = cmt

class NhanVien(Bank):
    def __init__(self, hoten: str, cmt:int):
        super().__init__(hoten, cmt)
        self.__luong = 5000

    # code de co the truy cap voi ng cap cao
    def get_luong(self):
        return self.__luong
    
    def set_luong(self, luong_moi):
        self.__luong = luong_moi

nv1 = NhanVien('viet', 1234)
nv2 = NhanVien('an', 213)

nv2.set_luong(9999)
nv2.__luong = 20

print(nv2.get_luong())

