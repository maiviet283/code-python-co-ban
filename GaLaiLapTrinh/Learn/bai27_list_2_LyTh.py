lst = [1,5,7]

chieudai = len(lst)
min_lst = min(lst)
max_lst = max(lst)

# thêm phần tử vào cuối list
print("-"*33)
print("sau khi thêm phần tử vào cuối")
lst.append(200)
lst.append(10)
lst.append("a")
print(lst)

# đếm phần tử trong list
print("-"*33)
dem = lst.count(1)
print("so 1 trong list la : ",dem)

# đảo ngược list
print("-"*33)
print("trước khi đảo list : ",lst)
lst.reverse() # nó sẽ tự đảo rồi đè vào list cũ luôn
print("sau khi đảo list : ",lst)

# chèn vào
print("-"*33)
print("trước khi chèn",lst)
lst.insert(2, 666)
print("sau khi chèn",lst)

# tìm kiếm xem dữ liệu nằm ở vị trí mô
# tìm ở vị trí đầu tiên thôi
print("-"*33)
a = lst.index(666)
print("vị trí của số 666 trong lst là :",lst.index(666))

# thêm list khác nối vào list ban đầu
print("-"*33)
print("sau khi nối list")
lst2 = ["a","b","c","cmm"]
lst.extend(lst2)
print(lst) # thành 1 list thống nhất

# sắp xếp lại 
print("-"*33)
print("sau khi sắp xếp lại list :")
lst = [1,5,4,2,6]
lst.sort() # tự sắp xếp rồi đè vô list ban đầu luôn
print(lst)

# tạo ra một list mới giống như lst nhưng được sắp xếp
print("-"*33)
print("tạo list 2 được sắp xếp")
lst = [1,6,7,4,2]
lst2 = sorted(lst)
print(lst2)

# reset list , đưa về list rỗng
lst.clear()
print("sau khi xóa list : ",lst)