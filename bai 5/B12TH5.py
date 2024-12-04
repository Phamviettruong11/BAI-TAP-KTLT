print("Nguyen Xuan Vu MSV:235752021610011")
import numpy as np

# Dữ liệu đầu vào
student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
student_height = np.array([40.0, 42.0, 45.0, 41.0, 38.0, 40.0, 42.0])

# Sử dụng lexsort để sắp xếp: trước theo chiều cao, sau đó theo id
sorted_indices = np.lexsort((student_id, student_height))

# In ra chỉ số sắp xếp và dữ liệu sắp xếp
print("Chỉ số:")
print(sorted_indices)

print("\nDữ liệu sắp xếp:")
for idx in sorted_indices:
    print(student_id[idx])
    print(student_height[idx])
