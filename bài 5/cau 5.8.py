# main.py

import search_module

# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử của danh sách: "))

dlist = []
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i+1}: "))
    dlist.append(value)

# Nhập phần tử cần tìm
item = int(input("Nhập phần tử cần tìm: "))

# Gọi hàm tìm kiếm
result, index = search_module.Sequential_Search(dlist, item)

if result:
    print(f"Tìm thấy {item} tại vị trí index = {index}")
else:
    print(f"Không tìm thấy phần tử {item} trong danh sách")
