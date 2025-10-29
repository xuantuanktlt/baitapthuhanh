
s = input("Nhập dãy số (cách nhau bởi dấu phẩy): ")

ds = [int(x) for x in s.split(',')]

le = [str(x) for x in ds if x % 2 != 0]
