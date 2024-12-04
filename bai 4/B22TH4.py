print ("Sinh vien:PHAM VIET TRUONG MSV:235752021610101")
# Danh sách để lưu các số thỏa mãn điều kiện
result = []

# Duyệt qua từng số trong đoạn từ 1000 đến 3000
for num in range(1000, 3001):
    # Chuyển số thành chuỗi để kiểm tra từng chữ số
    num_str = str(num)
    # Kiểm tra xem tất cả các chữ số có phải là số chẵn không
    if all(int(digit) % 2 == 0 for digit in num_str):
        result.append(num_str)

# In các số tìm được, phân tách bởi dấu phẩy
print(",".join(result))
