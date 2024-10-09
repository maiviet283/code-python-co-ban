def myfunc(n):
    return lambda x:x+n
s = myfunc(6)
print(s(6))