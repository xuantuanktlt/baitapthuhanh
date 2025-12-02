def copy_file(src, dest):
    with open(src, "r", encoding="utf-8") as f1:
        content = f1.read()

    with open(dest, "w", encoding="utf-8") as f2:
        f2.write(content)

# Gọi hàm
copy_file("test.txt", "copy_test.txt")
