import numpy as np

# Khai báo kiểu dữ liệu
data_type = [('name', 'S15'), ('class', int), ('height', float)]

# Dữ liệu đầu vào
students_details = [
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.1),
    ('Pit', 5, 40.11)
]

# Tạo structured array
students = np.array(students_details, dtype=data_type)

print("Original array:")
print(students)

# Sắp xếp theo class, sau đó theo height
sorted_students = np.sort(students, order=['class', 'height'])

print("Sorted by class, then height:")
print(sorted_students)
