import os

def file_read_from_tail(fname, lines):
    bufsize = 8192
    fsize = os.stat(fname).st_size
    iter = 0
    data = []

    with open(fname, "r", encoding="utf-8") as f:
        if bufsize > fsize:
            bufsize = fsize - 1

        while True:
            iter += 1
            seek_pos = fsize - bufsize * iter
            if seek_pos < 0:
                seek_pos = 0

            f.seek(seek_pos)
            data = f.readlines()

            # Nếu đã đủ dòng hoặc đã về đầu file
            if len(data) >= lines or seek_pos == 0:
                print(''.join(data[-lines:]))
                break


# Gọi hàm
file_read_from_tail('test.txt', 2)
