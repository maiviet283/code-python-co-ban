class ConNguoi():
    def __init__(self, hoten:str, tuoi:int):
        self.hoten = hoten
        self.tuoi = tuoi
        assert tuoi > 1

    def inten(self):
        return f"Ten : {self.hoten} - Tuoi : {self.tuoi}"
    
    @staticmethod
    def doan_tuoi(age):
        if age >= 0 and age <= 33:
            return "Tre"
        else:
            return "Tra"
        
class HocSinh(ConNguoi):
    def __init__(self, hoten: str, tuoi: int, lop:int = 1):
        super().__init__(hoten, tuoi)
        self.lop = lop
        self.__chieucao = 'thap'
    
    def get_chieucao(self):
        return self.__chieucao
    
    def set_chieucao(self, chieucao):
        self.__chieucao = chieucao

    def chao(self):
        print('Xin chao em la hoc sinh')

class SinhVien(ConNguoi):
    def __init__(self, hoten: str, tuoi: int, lop:int = 10):
        super().__init__(hoten, tuoi)
        self.lop = lop
        self.__chieucao = 'cao'
    
    def get_chieucao(self):
        return self.__chieucao
    
    def set_chieucao(self, chieucao):
        self.__chieucao = chieucao

    def chao(self):
        print('Xin chao to la sinh vien')


def hi(loichao):
    loichao.chao()

hs = HocSinh('Hoc Sinh', 5, 2)
sv = SinhVien('Sinh Vien', 21, 14)

hs.set_chieucao('Cao')
print(hs.get_chieucao())

print(hs.inten())
print(sv.inten())
hi(hs)
hi(sv)
print(hs.doan_tuoi(18))