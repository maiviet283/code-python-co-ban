class Item():
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

item1 = Item("Dien Thoai",100,20)
item2 = Item("LapTop",2000,10)
print(item1.name)