import tkinter as tk

root = tk.Tk()
root.title("Indicator Radio Buttons")

v = tk.IntVar()
v.set(1)

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

# Radio button dạng button (indicatoron = 0)
for text, val in languages:
    tk.Radiobutton(root,
                   text=text,
                   indicatoron=0,   # biến radio thành button
                   width=20,
                   padx=20,
                   variable=v,
                   command=ShowChoice,
                   value=val).pack(anchor=tk.W)

root.mainloop()
