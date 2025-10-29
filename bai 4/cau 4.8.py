
ds = input('Nhap day cac tu: ').split()
max_len = max(len(tu) for tu in ds)
print('Cac tu dai nhat la:')
for tu in ds:
    if len(tu) == max_len:
        print(tu)
