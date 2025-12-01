# main.py

import bubble_module

# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử: "))

nlist = []
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i+1}: "))
    nlist.append(value)

print("Danh sách ban đầu:", nlist)

# Gọi thuật toán sắp xếp nổi bọt
sorted_list = bubble_module.bubbleSort(nlist)

print("Danh sách sau khi sắp xếp:", sorted_list)
