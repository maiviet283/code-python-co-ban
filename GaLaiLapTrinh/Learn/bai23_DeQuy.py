def GiaiThua(n):
    if n>0 : 
        return n*GiaiThua(n-1)
    else : return 1

print(GiaiThua(8))