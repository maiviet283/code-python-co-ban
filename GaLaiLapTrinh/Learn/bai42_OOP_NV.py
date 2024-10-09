class Bank():
    def __init__(self,hoten:str,cmt):
        self.hoten = hoten
        self.cmt = cmt

class NhanVien(Bank):
    def __init__(self, hoten: str, cmt):
        super().__init__(hoten, cmt)
        self.__luong = 5000 # private

    def get_luong(self):
        return self.__luong

    def set_luong(self,luong_moi):
        self.__luong = luong_moi

nv1 = NhanVien("viet",123)
print(nv1.get_luong())
nv1.set_luong(400)
print(nv1.get_luong())