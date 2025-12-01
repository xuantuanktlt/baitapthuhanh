# main.py

import binary_module

# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử: "))

lst = []
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(value)

# Sắp xếp danh sách trước khi tìm kiếm
lst.sort()
print("Danh sách sau khi sắp xếp:", lst)

# Nhập giá trị cần tìm
value = int(input("Nhập phần tử cần tìm: "))

# Gọi hàm tìm kiếm nhị phân
found = binary_module.binary_search(lst, value)

if found:
    print("True - tìm thấy phần tử", value)
else:
    print("False - không tìm thấy phần tử", value)
