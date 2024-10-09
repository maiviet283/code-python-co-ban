class Item():
    def __init__(self,name:str,price:float,quantity:int=0):
        self.name = name
        self.price = price
        self.quantity = quantity

        assert price > 0
        assert quantity >= 0
    
    def Tong_Gia(self):
        return self.price * self.quantit
    
    @staticmethod
    def Check_Gia(gia):
        if gia <= 500:
            return "Cheap, dat o tang 1 "
        else:
            return "Expensive, dat o tang 2"

    def __str__(self):
        return f"name:{self.name} - price:{self.price} - quantity:{self.quantity}"
    
    def printName(self):
        print(f"Hello {self.name}")

    def myfunc(abc):
        print(f"hello, {abc.name}")



class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int = 0,loai:str = "4G"):
        super().__init__(name, price, quantity)
        self.loai = loai

item1 = Item("LapTop",150)
item2 = Item("Mobi Phone",10,33)

phone1 = Phone("Cuc Gach",17,12)
phone2 = Phone("SamSung",11,2,"5G")

print(phone1.loai + phone1.name)
print(phone2.loai + phone2.name)
print(phone1 == phone2)