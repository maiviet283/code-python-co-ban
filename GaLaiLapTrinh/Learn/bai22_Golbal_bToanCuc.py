a = 5

def test():
    global a
    a = 200
    print(a)
    # sử dụng a trong này áp dụng lên a ở trên

test()
print(a)