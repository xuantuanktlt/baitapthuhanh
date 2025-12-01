import datetime as dt

format = '%Y-%m-%dT%H:%M:%S'

# Chuyển chuỗi thành đối tượng datetime
t1 = dt.datetime.strptime('2008-10-12T14:45:52', format)

print('Day:', t1.day)
print('Month:', t1.month)
print('Minute:', t1.minute)
print('Second:', t1.second)

# Lấy thời gian hiện tại
t2 = dt.datetime.now()

# Tính độ chênh lệch thời gian
diff = t2 - t1

print('How many days difference?', diff.days)
