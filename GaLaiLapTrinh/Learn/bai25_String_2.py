s = "AASHINA" # 7 ký tự
n = "1234567"
# chiều trái sang phải : 0 1 2 3 4 5 6
# chiều phải sang trái : -7 -6 -5 -4 -3 -2 -1
print(n[0:7:2]) # chạy từ 0 đến cận 7 (0-6), bước nhảy = 2
print(n[1:7]) # chạy từ 1 đến 7 : vị trí 1 đến 6 
print(n[1:]) # chạy từ 1 đến hết
print(n[:3]) # chạy từ 0 đến sát 3 (2)
print(n[::-1]) # đảo ngược chuỗi print(n[-1:-8:-1])
