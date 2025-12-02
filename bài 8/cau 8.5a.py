import tkinter as tk

root = tk.Tk()
root.title("Radio Button Example")

v = tk.IntVar()
v.set(1)   # giá trị mặc định

languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C", 5)
]

def ShowChoice():
    print("Bạn chọn:", v.get())

tk.Label(root,
         text="Choose your favourite programming language:",
         justify=tk.LEFT,
         padx=20).pack()

# Tạo radio button bình thường
for text, val in languages:
    tk.Radiobutton(root,
                   text=text,
                   padx=20,
                   variable=v,
                   command=ShowChoice,
                   value=val).pack(anchor=tk.W)

root.mainloop()
