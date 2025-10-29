
n = int(input("Nhap so nguyen duong n: "))

print(f"Cac so nho hon {n} co tong cac uoc so lon hon chinh no la:")

for i in range(1, n):
    tong_uoc = 0
    for j in range(1, i):
        if i % j == 0:
            tong_uoc += j
    if tong_uoc > i:
        print(i)
