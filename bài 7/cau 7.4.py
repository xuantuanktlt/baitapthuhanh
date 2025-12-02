# Tên file cần đọc
filename = "sample.txt"

# Nhập số dòng muốn đọc
n = int(input("Nhập số dòng cần đọc: "))

# Mở file và đọc n dòng đầu
with open(filename, "r") as file:
    for i in range(n):
        line = file.readline()
        if not line:   # nếu file hết dòng trước khi đủ n dòng
            break
        print(line.strip())  # in ra, loại bỏ ký tự xuống dòng
