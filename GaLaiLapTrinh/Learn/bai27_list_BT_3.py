n = int(input("n = "))
list1 = []
index_list1 = []
sl = 0
if n <= 0 :
    print("chạy lại chương trình và nhập lại")
elif n==1 :
    value = int(input(f"list1[0] = "))
    list1.append(value)
    print("list 1 : ",list1)
    if value < 5 :
        print("có 1 phần tử nhỏ hơn 5")
        print("vị trí của phần tử là : 0")
else:
    for i in range(n):
        value = int(input(f"list1[{i}] = "))
        list1.append(value)
        if list1[i] < 5:
            sl += 1
            index_list1.append(i)
    print("list 1 : ",list1)
    print(f"có {sl} phần tử nhỏ hơn 5")
    for i in range(len(index_list1)):
        print(f"vị trí của các phần tử là : {index_list1[i]}")