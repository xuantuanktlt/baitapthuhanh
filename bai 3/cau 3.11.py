def benefit(t, n, k):
    """
    Hàm tính số tiền nhận được sau k tháng gửi tiết kiệm.
    t: lãi suất (%/tháng)
    n: số vốn ban đầu
    k: số tháng gửi
    """
    monthly_rate = t / 100
    final_amount = n * (1 + monthly_rate) ** k
    
    return final_amount
try:
    t = float(input("Nhập lãi suất tiết kiệm (%/tháng): "))
    n = float(input("Nhập số vốn ban đầu: "))
    k = int(input("Nhập số tháng gửi: "))
    
    total = benefit(t, n, k)
    print(f"Số tiền nhận được sau {k} tháng là: {total:.2f}")
except ValueError:
    print("Vui lòng nhập đúng số hợp lệ!")
