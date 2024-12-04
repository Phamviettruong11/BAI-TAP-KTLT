print("PHAM VIET TRUONG MSV:235752021610101")
import search_module  # Import module chứa hàm Sequential_Search

# Nhập số lượng phần tử của danh sách
n = int(input("Nhập số lượng phần tử trong danh sách: "))

# Nhập các phần tử vào danh sách
dlist = []
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i+1}: "))
    dlist.append(value)

# Nhập phần tử cần tìm
item = int(input("Nhập phần tử cần tìm: "))

# Gọi hàm Sequential_Search từ module để tìm phần tử
found, index = search_module.Sequential_Search(dlist, item)

# In kết quả
if found:
    print(f"Phần tử {item} được tìm thấy tại chỉ mục {index}.")
else:
    print(f"Phần tử {item} không được tìm thấy trong danh sách.")
