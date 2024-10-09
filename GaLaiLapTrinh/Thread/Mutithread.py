import threading
import time

# Hàm sẽ thực hiện trong luồng 1
def count_numbers_one():
    for i in range(1, 6):
        print("Thread 1:", i)
        time.sleep(1)  # Chờ 1 giây giữa mỗi số

# Hàm sẽ thực hiện trong luồng 2
def count_numbers_two():
    for i in range(6, 11):
        print("Thread 2:", i)
        time.sleep(1)  # Chờ 1 giây giữa mỗi số

# Tạo hai luồng
thread_one = threading.Thread(target=count_numbers_one)
thread_two = threading.Thread(target=count_numbers_two)

# Bắt đầu thực thi các luồng
thread_one.start()
thread_two.start()

# Chờ cho cả hai luồng kết thúc
thread_one.join()
thread_two.join()

print("All threads have finished.")
