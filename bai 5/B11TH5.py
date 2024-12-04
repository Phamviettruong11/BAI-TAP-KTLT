print("PHAM VIET TRUONG MSV:235752021610101")
import numpy as np

# Định nghĩa kiểu dữ liệu cấu trúc
data_type = [('name', 'S15'), ('class', int), ('height', float)]

# Dữ liệu sinh viên
students_details = [('James', 5, 48.5), ('Nail', 6, 52.5),
                    ('Paul', 5, 42.1), ('Pit', 5, 40.11)]

# Tạo mảng có cấu trúc
students = np.array(students_details, dtype=data_type)

# In ra mảng ban đầu
print("Mảng ban đầu:")
print(students)

# Sắp xếp theo lớp, sau đó theo chiều cao nếu lớp giống nhau
sorted_students = np.sort(students, order=['class', 'height'])

# In ra mảng đã sắp xếp
print("\nMảng sau khi sắp xếp:")
print(sorted_students)
