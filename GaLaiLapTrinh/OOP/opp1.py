class Item():
    def __init__(self,name:str,price:float,quantity:int = 0):
        self.name = name
        self.price = price
        self.quantity = quantity

        assert price >= 0
        assert quantity >= 0

class Sinhvien():
    def __init__(self, hoten:str, masv:int, quequan:str):
        self.hoten = hoten
        self.masv = masv
        self.quequan = quequan

        assert masv >= 0

    def inTen(self):
        return f'{self.hoten} - Masv {self.masv} - QQ : {self.quequan}'

item1 = Item("Laptop", 15000, 2)
item2 = Item("Phone", 20000, 3)

sv1 = Sinhvien('Mai Quoc Viet', 21 , 'Ha tinh')
sv2 = Sinhvien('Leo Messi', 36, 'Argentina')
sv3 = Sinhvien('Cristiano Ronaldo', 39, 'Portuagal')

print(f'SV1 name : {sv1.hoten} - que quan : {sv1.quequan}')
print(f'Que Quan : sv1 {sv1.quequan} - sv2 {sv2.quequan} - sv3 {sv3.quequan}')
print(f'SV3 : {sv3.inTen()}')