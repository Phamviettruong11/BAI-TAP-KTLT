print ("Sinh vien:PHAM VIET TRUONG MSV:235752021610101")
# Nhập câu từ người dùng
câu = input("Nhập một câu: ")

# Khởi tạo biến đếm
chữ_cái = 0
chữ_số = 0

# Duyệt qua từng ký tự trong câu
for char in câu:
    if char.isalpha():  # Kiểm tra nếu là chữ cái
        chữ_cái += 1
    elif char.isdigit():  # Kiểm tra nếu là chữ số
        chữ_số += 1

# In kết quả
print("Số chữ cái:", chữ_cái)
print("Số chữ số:", chữ_số)
