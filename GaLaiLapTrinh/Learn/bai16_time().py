# 1/1/1970
import time
giay = time.time() #quy số giây từ năm 1970 đến nay
print(giay)
hientai = time.ctime(giay) 
print(hientai)
# delay 
print("moi nhap dan an trong 5s : ")
time.sleep(1)
print("het gio r")
# trả về năm hiện tại , tháng , ngày , giờ,phút giây ,số ngày trong tuần từ 0, ngày thứ mấy trong năm
# ngày tiết kiệm ánh sáng
tg3 = time.localtime()
print(tg3.tm_mday)
print(f"hiện tại thứ {tg3.tm_wday+2} ngày {tg3.tm_mday}/{tg3.tm_mon}/{tg3.tm_year}")
