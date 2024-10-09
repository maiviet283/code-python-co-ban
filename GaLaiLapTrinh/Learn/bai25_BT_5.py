# b = "university of technology and educatin"
# c = len(b)
# print(c)
# for i in range(c):
#     if b[i] == "a" : print(i)

a = "English = 78 Science = 83 Math = 68 History = 65"
tach = a.split(" ")
t = 0
for i in tach:
    if i.isdigit() :
        t += int(i) 
print(t)