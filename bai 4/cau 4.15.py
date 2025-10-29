
chuoi = input("Nhap cac tu tieng Anh: ")
ds = chuoi.split()
ds.sort()
print("Cac tu theo thu tu tu dien:")
for tu in ds:
    print(tu)
