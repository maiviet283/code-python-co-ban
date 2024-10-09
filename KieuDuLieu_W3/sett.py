s = {1,2,3,4,5,6,7,7,7}
s2 = {8}
a = set(s)
a2 = set(s2)
a.add(9)
a.update(a2)
print(7 in a)
a.remove(7)
print(a)