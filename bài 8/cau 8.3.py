import turtle

# Tạo cửa sổ
wn = turtle.Screen()
wn.bgcolor("white")

# Tạo bút
pen = turtle.Turtle()
pen.pensize(2)

# Danh sách màu lặp lại
colors = ["red", "green", "blue"]

# Vẽ 10 hình tròn xoay quanh tâm
for i in range(10):
    pen.pencolor(colors[i % 3])   # Lấy màu theo chu kỳ 3 màu
    pen.circle(100)               # Vẽ hình tròn bán kính 100
    pen.left(36)                  # Xoay 36 độ (360/10)

# Giữ cửa sổ không tắt
turtle.done()
