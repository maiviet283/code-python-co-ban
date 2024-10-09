chuoi = "      hello "
a = chuoi.strip() # xóa khoảng trắng ở đầu câu và cuối câu
print(len(a))
chuoi2 = "**chuoi */**"
a2 = chuoi2.strip("*") # xóa * ở đầu và đuôi thôi
print(a2)
string1 = "galailaptrinh"
print(string1.count("l")) # đếm xem trong chuỗi xuất hiện bao nhiêu lần "l"
print(string1.count("l",0,5)) # đếm từ 0 đến sát 5 
string2 = string1.capitalize() # viết hoa kí tự đầu tiên
print(string2)
new = string1.replace("a","j")# thay ký tự a thành kí tự j
new2 = string1.replace("a","j",1) # thay ký tự a thành kí tự j 1 lần duy nhất
print(new)
print(new2)
print(new2.find("j")) # tìm ký tự j trong chuỗi new 2 , in ra vị trí đầutiên thôi
s = "mai quoc viet"
print(s.replace("i", "j"))
print(s.strip())
