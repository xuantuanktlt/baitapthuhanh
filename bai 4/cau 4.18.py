
n = int(input("Nhap so nguyen n: "))
fibo = [0, 1]
while True:
    next_num = fibo[-1] + fibo[-2]
    if next_num >= n:
        break
    fibo.append(next_num)

print("Cac so Fibonacci nho hon", n, "la:")
print(fibo)
