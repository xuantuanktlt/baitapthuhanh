
n = int(input("Nhap so dong n: "))

pascal = []

for i in range(n):
    row = [1] * (i + 1)
    for j in range(1, i):
        row[j] = pascal[i-1][j-1] + pascal[i-1][j]
    pascal.append(row)
for row in pascal:
    print(row)
