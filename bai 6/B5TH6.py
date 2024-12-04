print("PHAM VIET TRUONG MSV:235752021610101")
class StringReverser:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse_words(self):
        # Tách chuỗi thành các từ và đảo ngược thứ tự các từ
        words = self.input_string.split()
        reversed_words = words[::-1]  # Đảo ngược danh sách các từ
        return ' '.join(reversed_words)  # Nối lại các từ thành chuỗi

# Sử dụng class StringReverser để đảo ngược chuỗi từ từng chữ
input_string = "hello .py"  # Dữ liệu đầu vào
reverser = StringReverser(input_string)
reversed_string = reverser.reverse_words()

print(f"Đầu vào: {input_string}")
print(f"Đầu ra: {reversed_string}")
