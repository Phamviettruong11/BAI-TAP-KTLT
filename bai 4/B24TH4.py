print ("Sinh vien:PHAM VIET TRUONG MSV:235752021610101")
# Nhập câu từ người dùng
câu = input("Nhập một câu: ")

# Khởi tạo biến đếm
số_chữ_in_hoa = 0
số_chữ_thường = 0

# Duyệt qua từng ký tự trong câu
for char in câu:
    if char.isupper():  # Kiểm tra nếu là chữ hoa
       số_chữ_in_hoa  += 1
    elif char.islower():  # Kiểm tra nếu là chữ thường
       số_chữ_thường  += 1

# In kết quả
print("Số chữ hoa:", số_chữ_in_hoa)
print("Số chữ thường:", số_chữ_thường)
