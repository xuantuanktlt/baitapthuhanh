import math
def Tinh(R):
    if R <= 0:
        print("Giá trị bán kính không hợp lệ! (phải lớn hơn 0)")
        return
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R ** 2
    print(f"Với bán kính R = {R}:")
    print(f" → Chu vi hình tròn = {chu_vi:.2f}")
    print(f" → Diện tích hình tròn = {dien_tich:.2f}")
try:
    R = float(input("Nhập bán kính hình tròn: "))
    Tinh(R)
except ValueError:
    print("Vui lòng nhập một số hợp lệ!")
