import numpy as np

# Khai báo kiểu dữ liệu có cấu trúc
data_type = [('name', 'S15'), ('class', int), ('height', float)]

# Danh sách sinh viên (tên, lớp, chiều cao)
students_details = [
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.10),
    ('Pit', 5, 40.11)
]

# Tạo mảng có cấu trúc
students = np.array(students_details, dtype=data_type)

print("Original array:")
print(students)

# Sắp xếp theo chiều cao
print("Sort by height:")
print(np.sort(students, order='height'))
