def file_append_and_read(fname, text):
    # Mở file ở chế độ append để nối thêm nội dung
    with open(fname, "a", encoding="utf-8") as myfile:
        myfile.write(text + "\n")

    # Đọc lại toàn bộ nội dung file
    with open(fname, "r", encoding="utf-8") as myfile:
        print(myfile.read())


# Gọi hàm
file_append_and_read("abc.txt", "Python Exercises")
file_append_and_read("abc.txt", "Java Exercises")
