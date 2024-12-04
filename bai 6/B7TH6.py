print("PHAM VIET TRUONG MSV:235752021610101")
import math  # Import thư viện math để sử dụng giá trị pi

class Circle:
    def __init__(self, radius):
        self.radius = radius  # Khởi tạo bán kính của hình tròn

    def area(self):
        # Tính diện tích của hình tròn
        return math.pi * (self.radius ** 2)

    def circumference(self):
        # Tính chu vi của hình tròn
        return 2 * math.pi * self.radius

# Tạo đối tượng hình tròn với bán kính 5
circle = Circle(5)

# Tính và in diện tích và chu vi
print(f"Diện tích của hình tròn là: {circle.area():.2f}")
print(f"Chu vi của hình tròn là: {circle.circumference():.2f}")
