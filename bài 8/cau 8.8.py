import tkinter as tk
from tkinter import messagebox

# --- Hàm cho yêu cầu b) ---
def on_click_me():
    """Hiển thị lựa chọn Radiobutton hiện tại."""
    # Lấy giá trị từ biến điều khiển 'radio_var'.
    # Giá trị 1, 2 hoặc 3 tùy thuộc vào nút nào được chọn.
    selected_value = radio_var.get()
    if selected_value:
        messagebox.showinfo("Thông báo", f"Bạn đã chọn số: {selected_value}")
    else:
        # Trường hợp không có gì được chọn (mặc định)
        messagebox.showwarning("Cảnh báo", "Vui lòng chọn một số.")

# --- Tạo cửa sổ chính ---
root = tk.Tk()
root.title("Bài Tập Tkinter (Phần a & b)")
root.geometry("400x500") # Điều chỉnh kích thước cửa sổ chính

# --- Yêu cầu a) Xây dựng form hiển thị thông tin cá nhân ---

frame_a = tk.LabelFrame(root, text="Thông Tin Cá Nhân", padx=10, pady=10)
frame_a.pack(fill="both", expand="yes", padx=20, pady=10)

# Tạo và đặt các Label
tk.Label(frame_a, text="Họ và tên:").grid(row=0, column=0, sticky=tk.W, pady=5)
tk.Label(frame_a, text="Ngày sinh:").grid(row=1, column=0, sticky=tk.W, pady=5)
tk.Label(frame_a, text="MSSV:").grid(row=2, column=0, sticky=tk.W, pady=5)
tk.Label(frame_a, text="Ngành học:").grid(row=3, column=0, sticky=tk.W, pady=5)

# Tạo và đặt các Entry để nhập hoặc hiển thị thông tin
# Bạn có thể điền thông tin mặc định vào đây nếu muốn
tk.Entry(frame_a, width=25).grid(row=0, column=1, pady=5, padx=10)
tk.Entry(frame_a, width=25).grid(row=1, column=1, pady=5, padx=10)
tk.Entry(frame_a, width=25).grid(row=2, column=1, pady=5, padx=10)
tk.Entry(frame_a, width=25).grid(row=3, column=1, pady=5, padx=10)


# --- Yêu cầu b) Xây dựng form với Radio buttons ---

frame_b = tk.LabelFrame(root, text="Lựa Chọn (Yêu cầu b)", padx=10, pady=10)
frame_b.pack(fill="both", expand="yes", padx=20, pady=10)

# Biến điều khiển (IntVar) để theo dõi lựa chọn của Radiobutton
radio_var = tk.IntVar()
# radio_var.set(1) # Có thể thiết lập giá trị mặc định được chọn ban đầu

# Tạo các Radiobutton
# Giá trị 'value' sẽ được gán cho 'radio_var' khi nút được chọn
R1 = tk.Radiobutton(frame_b, text="1", variable=radio_var, value=1)
R1.pack(anchor=tk.W) # Căn chỉnh về phía Tây (trái)

R2 = tk.Radiobutton(frame_b, text="2", variable=radio_var, value=2)
R2.pack(anchor=tk.W)

R3 = tk.Radiobutton(frame_b, text="3", variable=radio_var, value=3)
R3.pack(anchor=tk.W)

# Tạo nút "Click Me"
button_click = tk.Button(frame_b, text="Click Me", command=on_click_me, pady=5)
button_click.pack(pady=10)

# --- Chạy vòng lặp chính của ứng dụng ---
root.mainloop()
