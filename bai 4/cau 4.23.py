
s = input("Nhập câu: ")

chu_cai = 0
chu_so = 0

for ch in s:
    if ch.isalpha():
        chu_cai += 1
    elif ch.isdigit():
        chu_so += 1

print("Số chữ cái là:", chu_cai)
print("Số chữ số là:", chu_so)
