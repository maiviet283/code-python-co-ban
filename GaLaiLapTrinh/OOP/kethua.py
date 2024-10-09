class Item():
    def __init__(self, name:str, price:float, quantity:int = 0):
        self.name = name
        self.price = price
        self.quantity = quantity

        # kiem tra dieu kien thuoc tinh
        assert price >= 0
        assert quantity >= 0

    def Tong_Gia(self):
        return self.price * self.quantity

    # phuong thuc tinh staticmethod
    @staticmethod
    def Check_gia(gia):
        if gia <= 500:
            return 'Cheap, Tang 1'
        else:
            return 'Expensive, Tang 2'

# khoi tao class con
class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int = 0, loai:str = '4G'):
        super().__init__(name, price, quantity)
        self.loai = loai

item1 = Item("Laptop", 15000, 2)
item2 = Item("Phone", 20000, 3)

phone1 = Phone('Samsung', 1200, 5, '5G')
phone2 = Phone('Iphone', 3200, 4, '4G')

