print("PHAM VIET TRUONG MSV:235752021610101")
import module

# Nhập số lượng phần tử của danh sách
n = int(input("Nhập số lượng phần tử của danh sách: "))

# Nhập các giá trị vào danh sách
lst = []
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(value)

# Sử dụng hàm từ module để sắp xếp và tìm phần tử lớn nhất, nhỏ nhất
sorted_lst = mymodule.sort_list(lst)
max_value = mymodule.find_max(lst)
# Phần tử nhỏ nhất là phần tử đầu tiên của danh sách đã sắp xếp
min_value = sorted_lst[0]

# Tìm vị trí của phần tử lớn nhất và nhỏ nhất
max_index = lst.index(max_value)  # Vị trí đầu tiên của phần tử lớn nhất
min_index = lst.index(min_value)  # Vị trí đầu tiên của phần tử nhỏ nhất

# In kết quả
print("Danh sách sau khi sắp xếp:", sorted_lst)
print("Phần tử lớn nhất:", max_value, "ở vị trí:", max_index)
print("Phần tử nhỏ nhất:", min_value, "ở vị trí:", min_index)
