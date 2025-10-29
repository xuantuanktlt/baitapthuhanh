
chuoi = input("Nhap cac so nhi phan (phan tach boi dau phay): ")

ds = chuoi.split(',')

ket_qua = []

for so in ds:
    thap_phan = int(so, 2)
    if thap_phan % 5 == 0:
        ket_qua.append(so)

print(",".join(ket_qua))
