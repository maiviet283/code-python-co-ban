# for i in range(2,10,2):print(i)


# a = int(input("a = "))
# if a%2 == 0:
#     for i in range(1,6,1):
#         a+=i
#     print(a)
# else:print("Tau dell tính số lẻ")

sum = 0
for n in range(1,8,2):
    if n==3 : continue # bỏ qua luôn ko chạy qua 3 nữa
    sum += n
print(sum)
