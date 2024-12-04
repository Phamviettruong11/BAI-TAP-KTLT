print("PHAM VIET TRUONG MSV:235752021610101")
class Hinhchunhat(object):
    def __init__(self, dai, rong):
        # Khởi tạo chiều dài và chiều rộng cho đối tượng Hinhchunhat
        self.dai = dai
        self.rong = rong

    def area(self):
        # Tính diện tích hình chữ nhật: chiều dài * chiều rộng
        return self.dai * self.rong

# Tạo đối tượng Hinhchunhat với chiều dài = 5 và chiều rộng = 3
hcn = Hinhchunhat(5, 3)

# In diện tích của hình chữ nhật
print(hcn.area())
