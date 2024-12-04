print ("Sinh vien:PHAM VIET TRUONG MSV:235752021610101")
"""Chương trình tạo một máy tính đơn giản có thể cộng, trừ, nhân và 
chia bằng các hàm""" 
# Hàm này thêm hai số
def cộng(x, y):
    return x + y 
# Hàm này trừ hai số
def trừ(x, y):
    return x - y 
# Hàm này nhân hai số
def nhân(x, y):
    return x * y
# Hàm này chia hai số
def chia(x, y):
    return x / y 
print("Chọn thao tác") 
print("1.Cộng") 
print("2.Trừ") 
print("3.Nhân") 
print("4.Chia")
# Lấy ý kiến đóng góp từ người dùng
chọn = input("Chọn(1/2/3/4):") 
x = int(input("Số thứ nhất: ")) 
y = int(input("Số thứ hai: "))
if chọn == '1':
    print(x,"+",y,"=", cộng(x,y)) 
elif chọn == '2':
    print(x,"-",y,"=", trừ(x,y)) 
elif chọn == '3':
    print(x,"*",y,"=", nhân(x,y)) 
elif chọn == '4':
    print(x,"/",y,"=", chia(x,y)) 
else:
    print("Đầu vào không hợp lệ")
