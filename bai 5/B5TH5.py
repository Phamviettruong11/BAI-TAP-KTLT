print("PHAM VIET TRUONG MSV:235752021610101")
import mymodule  # Import module vừa tạo

# Nhập số lượng phần tử của danh sách
n = int(input("Nhập số lượng phần tử của danh sách: "))

# Nhập các giá trị vào danh sách
lst = []
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(value)

# Sử dụng hàm từ module để sắp xếp và tìm phần tử lớn nhất
sorted_lst = mymodule.sort_list(lst)
max_value = mymodule.find_max(lst)
# Phần tử nhỏ nhất là phần tử đầu tiên của danh sách đã sắp xếp
min_value = sorted_lst[0]

# In kết quả
print("Danh sách sau khi sắp xếp:", sorted_lst)
print("Phần tử lớn nhất:", max_value)
print("Phần tử nhỏ nhất:", min_value)
