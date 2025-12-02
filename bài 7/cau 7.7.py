def count_lines(fname):
    with open(fname, "r", encoding="utf-8") as f:
        lines = f.readlines()
        return len(lines)

# Gọi hàm
print(count_lines("test.txt"))
