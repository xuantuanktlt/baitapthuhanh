class StringProcessor:
    def __init__(self):
        self.text = ""

    def get_String(self):
        self.text = input("Nhập một chuỗi: ")

    def print_String(self):
        print(self.text.upper())


# Test chương trình
sp = StringProcessor()
sp.get_String()
sp.print_String()
