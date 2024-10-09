class ConNguoi:
    def __init__(self, hoten: str, tuoi: int):
        if tuoi <= 1:
            raise ValueError("Tuoi phai lon hon 1")
        self.hoten = hoten
        self.tuoi = tuoi

    def thong_tin(self):
        return f"Ten: {self.hoten} - Tuoi: {self.tuoi}"

    @staticmethod
    def doan_tuoi(tuoi):
        if 0 <= tuoi <= 33:
            return "Tre"
        else:
            return "Tra"



class HocSinh(ConNguoi):
    def __init__(self, hoten: str, tuoi: int, lop: int = 1):
        super().__init__(hoten, tuoi)
        self.lop = lop
        self.__chieucao = 'thap'

    @property
    def chieucao(self):
        return self.__chieucao

    @chieucao.setter
    def chieucao(self, chieucao):
        self.__chieucao = chieucao

    def chao(self):
        print('Xin chao em la hoc sinh')


class SinhVien(ConNguoi):
    def __init__(self, hoten: str, tuoi: int, lop: int = 10):
        super().__init__(hoten, tuoi)
        self.lop = lop
        self.__chieucao = 'cao'

    @property
    def chieucao(self):
        return self.__chieucao

    @chieucao.setter
    def chieucao(self, chieucao):
        self.__chieucao = chieucao

    def chao(self):
        print('Xin chao to la sinh vien')


def chao_thanh_vien(thanh_vien):
    thanh_vien.chao()


hoc_sinh = HocSinh('Hoc Sinh', 5, 2)
sinh_vien = SinhVien('Sinh Vien', 21, 14)

hoc_sinh.chieucao = 'Cao'
print(hoc_sinh.chieucao)

print(hoc_sinh.thong_tin())
print(sinh_vien.thong_tin())

chao_thanh_vien(hoc_sinh)
chao_thanh_vien(sinh_vien)

print(ConNguoi.doan_tuoi(18))
