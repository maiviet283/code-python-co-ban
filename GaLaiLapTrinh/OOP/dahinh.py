class SinhVien_nuocngoai():
    def __init__(self, hoten, masv, que_quan):
        self.hoten = hoten
        self.masv = masv
        self.que_quan = que_quan

    def chao(self):
        print('hello')

class SinhVien_viet():
    def __init__(self, hoten, masv, que_quan):
        self.hoten = hoten
        self.masv = masv
        self.que_quan = que_quan

    def chao(self):
        print('xin chao')

def hi(sinhvien_viet):
    sinhvien_viet.chao()

vi1 = SinhVien_viet('viet', 123, 'hatinh')
en1 = SinhVien_nuocngoai('bro', 12, 'ar')

hi(vi1)
hi(en1)