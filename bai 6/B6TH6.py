print("PHAM VIET TRUONG MSV:235752021610101")
class StringManipulator:
    def __init__(self):
        self.user_string = ""  # Biến lưu chuỗi người dùng nhập vào

    def get_String(self):
        # Chấp nhận chuỗi từ người dùng
        self.user_string = input("Nhập một chuỗi: ")

    def print_String(self):
        # In chuỗi dưới dạng chữ in hoa
        print(self.user_string.upper())

# Sử dụng lớp StringManipulator
string_manipulator = StringManipulator()

# Lấy chuỗi từ người dùng
string_manipulator.get_String()

# In chuỗi dưới dạng chữ in hoa
string_manipulator.print_String()
