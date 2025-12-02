# Tên file cần đọc
filename = "sample.txt"

# Mở file và đọc toàn bộ nội dung
with open(filename, "r") as file:
    content = file.read()  # đọc toàn bộ nội dung file vào biến content

# In nội dung file
print("Nội dung file:")
print(content)
