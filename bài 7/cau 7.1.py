# Đọc file
with open("sample.txt", "r") as file:
    lines = file.readlines()  # đọc tất cả các dòng vào danh sách

# Xóa ký tự xuống dòng ở cuối mỗi dòng
lines = [line.strip() for line in lines]

# Đảo ngược danh sách
lines_reversed = lines[::-1]

# In kết quả
print("Nội dung file đảo ngược:")
for line in lines_reversed:
    print(line)
