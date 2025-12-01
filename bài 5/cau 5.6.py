import mymodule

# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử của danh sách: "))

lst = []
for i in range(n):
    value = float(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(value)

# Sắp xếp danh sách
sorted_list = mymodule.sort_list(lst)

# Tìm max và min
max_value = mymodule.find_max(lst)
min_value = mymodule.find_min(lst)

# Tìm vị trí (index)
max_index = lst.index(max_value)  # index đầu tiên xuất hiện
min_index = lst.index(min_value)

print("Danh sách sau khi sắp xếp:", sorted_list)
print("Phần tử lớn nhất:", max_value, "ở vị trí (index):", max_index)
print("Phần tử nhỏ nhất:", min_value, "ở vị trí (index):", min_index)
