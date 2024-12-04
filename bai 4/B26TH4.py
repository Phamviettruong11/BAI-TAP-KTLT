print ("Sinh vien:PHAM VIET TRUONG MSV:235752021610101")
# Khởi tạo số dư ban đầu là 0
so_du = 0

print("Nhập nhật ký giao dịch (theo định dạng 'D 100' hoặc 'W 50'). Nhập 'thoát' để kết thúc:")

while True:
    # Nhập giao dịch từ người dùng
    giao_dich = input()

    # Thoát khỏi vòng lặp nếu người dùng nhập 'thoát'
    if giao_dich.lower() == 'thoát':
        break

    # Tách giao dịch thành loại và số tiền
    try:
        loai_giao_dich, so_tien = giao_dich.split()
        so_tien = int(so_tien)

        # Kiểm tra loại giao dịch và cập nhật số dư
        if loai_giao_dich == 'D':  
            so_du += so_tien
        elif loai_giao_dich == 'W':
            so_du -= so_tien
        else:
            print("Giao dịch không hợp lệ. Vui lòng nhập lại.")

    except ValueError:
        print("Lỗi nhập liệu. Vui lòng nhập theo định dạng 'D 100' hoặc 'W 50'.")

# In số dư cuối cùng
print("Số tiền thực trong tài khoản:", so_du)

