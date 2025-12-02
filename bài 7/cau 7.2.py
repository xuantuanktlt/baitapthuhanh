# File cần đọc
filename = "sample.txt"

# Khởi tạo bộ đếm
num_chars = 0
num_words = 0
num_lines = 0

# Đọc file
with open(filename, "r") as file:
    for line in file:
        num_lines += 1
        num_chars += len(line)             # tính tất cả ký tự, bao gồm khoảng trắng và \n
        num_words += len(line.split())     # tách từ theo khoảng trắng

# In kết quả
print(f"Số dòng: {num_lines}")
print(f"Số từ: {num_words}")
print(f"Số ký tự: {num_chars}")
