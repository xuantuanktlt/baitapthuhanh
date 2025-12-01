class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Số dư hiện tại: {self.balance} VND")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Nạp {amount} VND thành công.")
        else:
            print("Số tiền nạp phải lớn hơn 0.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Số tiền rút phải lớn hơn 0.")
        elif amount > self.balance:
            print("Số dư không đủ để rút.")
        else:
            self.balance -= amount
            print(f"Rút {amount} VND thành công.")


# Menu chương trình
def main():
    atm = ATM(1000)  # Khởi tạo ATM với số dư ban đầu 1000 VND

    while True:
        print("\n===== ATM MENU =====")
        print("1. Kiểm tra số dư")
        print("2. Nạp tiền")
        print("3. Rút tiền")
        print("4. Thoát")

        choice = input("Chọn thao tác (1-4): ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = int(input("Nhập số tiền nạp: "))
            atm.deposit(amount)
        elif choice == '3':
            amount = int(input("Nhập số tiền rút: "))
            atm.withdraw(amount)
        elif choice == '4':
            print("Thoát chương trình. Cảm ơn bạn!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
