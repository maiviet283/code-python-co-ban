n = int(input("n = "))
lst = [int(input(f"list[{i}] = "))for i in range(n)]
lst_1 = []
dem = 0
a = 0
print("list = ",lst)
for i in lst:
    if i < 5:
        dem += 1
        lst_1.append(a)
    a+=1
print(dem)
print(lst_1)