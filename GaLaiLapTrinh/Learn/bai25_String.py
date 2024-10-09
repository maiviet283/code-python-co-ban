str1 = "python1 ,"
str2 = 'python2'
str3 = """
galataxaray"""
str4 = '''
    tôi là mai quốc việt
'''
ten = "nam,anh,viet,le,loan"
for i in str1:
    print(i,end=" ") # end="\t" : 1 tab

# kiểm tra ký tự có nằm trong string không
# print("on" in str1)

t = input("tên : ")
if t in ten : print("co nha")
else : print("dell co")
print(str4.strip())