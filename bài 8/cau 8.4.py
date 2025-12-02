from tkinter import *

# a) Tạo cửa sổ đồ họa window form
window = Tk()
window.title("Welcome to Tkinter App")
window.geometry('350x200')
window.configure(bg="lightyellow")  # đổi màu nền cửa sổ (tùy chọn)

# Thêm một label hiển thị nội dung
lbl = Label(window, text="Hello", font=("Arial", 14), bg="lightyellow")
lbl.grid(column=0, row=0, padx=10, pady=10)

# c) Xây dựng phương thức xử lý sự kiện phím bấm
def clicked():
    lbl.configure(text="Button was clicked !!", fg="blue")

# b + d) Thêm widget Button + đổi màu nền (bg) và màu chữ (fg)
btn = Button(window, 
             text="Click Me", 
             command=clicked,
             bg="green",       # màu nền button
             fg="white",       # màu chữ button
             font=("Arial", 12),
             padx=10, pady=5)

btn.grid(column=1, row=0)

# Chạy vòng lặp giao diện
window.mainloop()
