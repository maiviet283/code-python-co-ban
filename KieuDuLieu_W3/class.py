class Dog:
    chan = "4 chan"
    duoi = "dai cute"
    long = "mau den"
    mat = "mau nau"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sua(self):
        print("gau gau")

    def ngu(self):
        print("8h / ngay")

choXin = Dog("LyLy",19)
choXin.sua()
print(choXin.chan)