print("PHAM VIET TRUONG MSV:235752021610101")
class Circle(object):
    def __init__(self, r):
        # Khởi tạo bán kính cho đối tượng Circle
        self.radius = r

    def area(self):
        # Tính diện tích hình tròn: π * r^2
        return self.radius ** 2 * 3.14

# Tạo đối tượng Circle với bán kính = 2
aCircle = Circle(2)

# In diện tích của hình tròn
print(aCircle.area())
