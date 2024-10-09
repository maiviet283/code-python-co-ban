list1 = []
n = int(input("n = "))
for i in range(n):
    k = int(input(f"list1[{i}] = "))
    list1.append(k)
print("list1 : ",list1)

list2 = []
dem = 0
for i in range(n):
    j = list1[i]*list1[i]
    if (j > 50) : dem +=1
    list2.append(j)
print("list2 : ",list2)
print(f"so phan tu lon hon 50 la : {dem}")