class RomanConverter:
    def __init__(self):
        # Bảng tra cứu các ký tự La Mã
        self.roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def roman_to_int(self, roman):
        total = 0
        prev_value = 0
        # Duyệt từ phải sang trái
        for char in reversed(roman):
            value = self.roman_dict.get(char, 0)
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return total


# Test chương trình
converter = RomanConverter()
roman_number = "XIV"
integer_number = converter.roman_to_int(roman_number)
print(f"Số La Mã {roman_number} = {integer_number}")
