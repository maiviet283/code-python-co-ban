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

item1 = Item("Laptop", -15000, 2)
item2 = Item("Phone", 20000, 3)
item3 = Item("Fax", 2000)

print(f"Gia Item 1 : {item1.price * item1.quantity}")
print(f"Gia Item 1 : {item1.Tong_Gia()}")
print(f'quantity item 3 : {item3.quantity} ')
print(item1.Check_gia(300))