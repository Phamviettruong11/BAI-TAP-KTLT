print("PHAM VIET TRUONG MSV:235752021610101")
import search_module  # Import module chứa hàm binary_search

# Nhập số lượng phần tử của danh sách
n = int(input("Nhập số lượng phần tử trong danh sách: "))

# Nhập các phần tử vào danh sách
dlist = []
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i+1}: "))
    dlist.append(value)

# Sắp xếp danh sách trước khi tìm kiếm
dlist.sort()

# Nhập phần tử cần tìm
item = int(input("Nhập phần tử cần tìm: "))

# Gọi hàm binary_search từ module để tìm phần tử
found = search_module.binary_search(dlist, item)

# In kết quả
if found:
    print(f"Phần tử {item} được tìm thấy trong danh sách.")
else:
    print(f"Phần tử {item} không được tìm thấy trong danh sách.")
