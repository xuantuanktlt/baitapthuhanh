
s = input('Nhap chuoi: ')
kq = ''
for ch in s:
    if not ch.isdigit():
        kq += ch
print('Chuoi sau khi loai bo chu so:', kq)
