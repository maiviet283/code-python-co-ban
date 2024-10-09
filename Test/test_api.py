import requests

def get_users():
    # URL của API jsonplaceholder.typicode.com để lấy thông tin người dùng
    api_url = "https://jsonplaceholder.typicode.com/users"

    # Gửi yêu cầu GET đến API
    response = requests.get(api_url)

    # Kiểm tra xem yêu cầu có thành công không (mã trạng thái 200)
    if response.status_code == 200:
        # Chuyển đổi dữ liệu JSON từ phản hồi
        users = response.json()

        # In ra danh sách người dùng
        for user in users:
            print(f"ID: {user['id']}, Name: {user['name']}, Email: {user['email']}")
    else:
        print(f"Failed to get user data. Status code: {response.status_code}")

# Gọi hàm để lấy danh sách người dùng
get_users()
