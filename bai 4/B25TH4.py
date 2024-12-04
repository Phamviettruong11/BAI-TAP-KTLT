print ("Sinh vien:PHAM VIET TRUONG MSV:235752021610101")
# Nhập danh sách các số từ người dùng, phân tách bằng dấu cách
input_numbers = input("Nhập các số, phân tách bởi dấu cách: ")

# Chuyển chuỗi đầu vào thành danh sách các số nguyên
numbers = [int(num) for num in input_numbers.split()]

# Lọc các số lẻ từ danh sách
Số_lẻ = [num for num in numbers if num % 2 != 0]

# In danh sách các số lẻ
print("Danh sách các số lẻ:", Số_lẻ)
