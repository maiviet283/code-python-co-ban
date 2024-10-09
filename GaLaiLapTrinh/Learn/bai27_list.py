list1 = [1,2,3]
list2 = ["a","b","c",6,6]
list3 = [list1,list2]
list2[1] = "hello"
print(list2)
del list2[0] # delete phần tử có index = 0
print(list2)
list2.remove(6) # xóa số 6 đầu tiên thôi
print(list2)
print(list2[0:2:1])
del list2 #xóa cả list luôn
# print(list2)