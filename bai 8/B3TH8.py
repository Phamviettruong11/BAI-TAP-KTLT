print("PHAM VIET TRUONG MSV:235752021610101")
import turtle

# Thiết lập màn hình và bút vẽ
screen = turtle.Screen()
screen.bgcolor("white")
pen = turtle.Turtle()
pen.speed(0)  # Tăng tốc độ vẽ
pen.width(2)

# Danh sách màu sắc sử dụng
colors = ["red", "blue", "green"]

# Hàm vẽ hình tròn
def draw_circle():
    for i in range(36):  # 36 lần xoay, mỗi lần xoay 10 độ
        pen.color(colors[i % len(colors)])  # Đổi màu theo thứ tự
        pen.circle(100)  # Vẽ hình tròn bán kính 100
        pen.right(10)    # Xoay phải 10 độ

# Vẽ hình tròn lồng ghép
draw_circle()

# Hoàn tất
pen.hideturtle()
screen.mainloop()
