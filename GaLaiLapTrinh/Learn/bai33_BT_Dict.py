KhachHang = {
    "user" : "123",
    "vietmau" : "345",
    "yasuo" : "zed"
}
username = input("username = ")
password = input("password = ")
if username in KhachHang :
    if password in KhachHang[username]:
        print("login thanh cong")
    else : print("sai password")
else : print("username ko ton tai")