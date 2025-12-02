def list_to_file(fname, lst):
    with open(fname, "w", encoding="utf-8") as f:
        for item in lst:
            f.write(item + "\n")

# Gọi hàm
list_to_file("output.txt", colors)
