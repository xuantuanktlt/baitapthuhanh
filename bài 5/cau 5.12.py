import numpy as np

# Dữ liệu đầu vào
student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
student_height = np.array([40., 42., 45., 41., 38., 40., 42.0])

# Sử dụng lexsort()
# Ghi nhớ: lexsort sắp xếp dựa theo thứ tự từ hàng thứ 2 trở lên.
# Vì muốn sắp xếp theo height → truyền height vào sau cùng.
sorted_index = np.lexsort((student_id, student_height))

print("Chỉ số:")
print(sorted_index)

print("\nDữ liệu sắp xếp:")
for idx in sorted_index:
    print(student_id[idx], student_height[idx])
