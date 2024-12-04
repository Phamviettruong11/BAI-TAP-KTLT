print("PHAM VIET TRUONG MSV:235752021610101")
import numpy as np

# Định nghĩa kiểu dữ liệu cho mảng cấu trúc
data_type = [('name', 'S15'), ('class', int), ('height', float)]

# Dữ liệu chi tiết của sinh viên: tên, lớp và chiều cao
students_details = [('James', 5, 48.5), ('Nail', 6, 52.5),
                    ('Paul', 5, 42.10), ('Pit', 5, 40.11)]

# Tạo mảng cấu trúc từ dữ liệu sinh viên
students = np.array(students_details, dtype=data_type)

# In mảng ban đầu
print("Original array:")
print(students)

# Sắp xếp mảng theo chiều cao
print("Sort by height:")
print(np.sort(students, order='height'))
