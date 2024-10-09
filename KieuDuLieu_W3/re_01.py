import re
txt = "Mai Quoc Viet ai"
print(re.findall("ai",txt)) # những phần tử "ai" sẽ được lặt vô 1 arr
print(re.search("\s",txt).start()) # lấy vị trí khoảng trắng đầu tiên
print(re.search("Viet",txt)) # 9 đến sát 13
print(re.split("\s",txt)) # tách từng khoảng trắng
print(re.split("\s",txt,1)) # tách từng khoảng trắng 1 lần đầu tiên thôi
print(re.sub("\s","-",txt)) # thay dấu cách = -
print(re.sub("\s","-",txt,2)) # thay dấu cách = - 2 lần đầu tiên thôi