print("PHAM VIET TRUONG MSV:235752021610101")
import sort_module  # Import module chứa hàm bubbleSort

# Nhập số lượng phần tử trong danh sách
n = int(input("Nhập số lượng phần tử trong danh sách: "))

# Nhập các phần tử vào danh sách
nlist = []
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i+1}: "))
    nlist.append(value)

# Sắp xếp danh sách bằng thuật toán bubble sort
sorted_list = sort_module.bubbleSort(nlist)

# In kết quả
print("Danh sách sau khi sắp xếp:")
print(sorted_list)
