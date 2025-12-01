class StringReverser:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        # Tách chuỗi thành danh sách từ
        words = self.text.split()
        # Đảo ngược danh sách từ
        reversed_words = words[::-1]
        # Nối các từ thành chuỗi mới
        return ' '.join(reversed_words)


# Test chương trình
input_text = 'hello .py'
reverser = StringReverser(input_text)
output_text = reverser.reverse_words()
print("Dữ liệu vào :", input_text)
print("Đầu ra     :", output_text)
